import tkinter as tk
import time

def cat_feeding_brute_force(foods, target_protein):
    kombinasi_terbaik = []
    min_karbohidrat = float('inf')
    min_protein = float('inf')

    # Semua kemungkinan kombinasi jenis makanan
    for r in range(1, len(foods) + 1):
        kombinasi = get_kombinasi(foods, r)

        # Periksa setiap kombinasi
        for combo in kombinasi:
            total_protein = sum(food[1] for food in combo)
            total_karbohidrat = sum(food[2] for food in combo)
            protein_diff = abs(total_protein - target_protein)

            # Perbarui kombinasi terbaik jika memenuhi kriteria
            if total_protein <= target_protein and protein_diff < min_protein:
                kombinasi_terbaik = [combo]
                min_protein = protein_diff
                min_karbohidrat = total_karbohidrat
            elif total_protein <= target_protein and protein_diff == min_protein:
                if total_karbohidrat < min_karbohidrat:
                    kombinasi_terbaik = [combo]
                    min_karbohidrat = total_karbohidrat
                elif total_karbohidrat == min_karbohidrat:
                    kombinasi_terbaik.append(combo)

    return kombinasi_terbaik


def get_kombinasi(list, r):
    if r == 1:
        return [[x] for x in list]
    kombinasi = []
    for i in range(len(list) - r + 1):
        sisa = get_kombinasi(list[i + 1:], r - 1)
        for combo in sisa:
            kombinasi.append([list[i]] + combo)
    return kombinasi


def find_kombinasi_terbaik():
    foods = []
    target_protein = int(protein_entry.get())

    start_time = time.time()  # Ambil waktu awal eksekusi

    # Dapatkan nilai dari kolom input
    for entry in food_entries:
        jenis_makanan = entry[0].get()
        protein = int(entry[1].get())
        karbohidrat = int(entry[2].get())
        foods.append((jenis_makanan, protein, karbohidrat))

    kombinasi_terbaik = cat_feeding_brute_force(foods, target_protein)

    if kombinasi_terbaik:
        hasil_teks.set("Best kombinasi:\n")
        for combination in kombinasi_terbaik:
            result = ", ".join(food[0] for food in combination)
            hasil_teks.set(hasil_teks.get() + result + "\n")
    else:
        hasil_teks.set("Tidak ditemukan kombinasi.")

    end_time = time.time()  # Ambil waktu akhir eksekusi
    eksekusi_waktu = end_time - start_time  # Hitung waktu eksekusi

    eksekusi_waktu_label.config(text="Execution Time: {:.4f} seconds".format(eksekusi_waktu))


# Buat GUI
window = tk.Tk()
window.configure(bg="light blue")
window.title("Cat Feeding - Brute Force")

# Buat bagian untuk daftar makanan
food_list_frame = tk.Frame(window)
food_list_frame.configure(bg="light blue")
food_list_frame.pack(pady=10)

food_entries = []
num_foods = tk.IntVar()
num_foods.set(3)

num_foods_label = tk.Label(food_list_frame, text="Banyaknya makanan:")
num_foods_label.configure(bg="light blue")
num_foods_label.grid(row=0, column=0, padx=10, sticky="e")

num_foods_entry = tk.Entry(food_list_frame, textvariable=num_foods)
num_foods_entry.grid(row=0, column=1, padx=10)


def update_food_entries():
    count = num_foods.get()
    for entry in food_entries:
        entry[0].destroy()
        entry[1].destroy()
        entry[2].destroy()
    food_entries.clear()
    for i in range(count):
        food_label = tk.Label(food_list_frame, text="Food {}: ".format(i + 1))
        food_label.configure(bg="light blue")
        food_label.grid(row=i + 1, column=0, pady=5, sticky="e")

        food_entry = tk.Entry(food_list_frame)
        food_entry.grid(row=i + 1, column=1, pady=2)

        protein_label = tk.Label(food_list_frame, text="Protein {}: ".format(i + 1))
        protein_label.configure(bg="light blue")
        protein_label.grid(row=i + 1, column=2, pady=5, sticky="e")

        protein_entry = tk.Entry(food_list_frame)
        protein_entry.grid(row=i + 1, column=3, pady=2)

        karbohidrat_label = tk.Label(food_list_frame, text="karbohidrat {}: ".format(i + 1))
        karbohidrat_label.configure(bg="light blue")
        karbohidrat_label.grid(row=i + 1, column=4, pady=5, sticky="e")

        karbohidrat_entry = tk.Entry(food_list_frame)
        karbohidrat_entry.grid(row=i + 1, column=5, pady=2)

        food_entries.append((food_entry, protein_entry, karbohidrat_entry))


update_button = tk.Button(food_list_frame, text="Update", command=update_food_entries)
update_button.grid(row=0, column=2, columnspan=2, padx=10)

# Buat bagian untuk target protein
target_frame = tk.Frame(window)
target_frame.configure(bg="light blue")
target_frame.pack(pady=10)

target_protein_label = tk.Label(target_frame, text="Target Protein:")
target_protein_label.configure(bg="light blue")
target_protein_label.pack(side="left", padx=10)

protein_entry = tk.Entry(target_frame)
protein_entry.pack(side="left")

# Buat bagian hasil
result_frame = tk.Frame(window)
result_frame.configure(bg="light blue")
result_frame.pack(pady=10)

hasil_teks = tk.StringVar()
result_label = tk.Label(result_frame, textvariable=hasil_teks)
result_label.configure(bg="light blue")
result_label.pack()

eksekusi_waktu_label = tk.Label(result_frame)
eksekusi_waktu_label.configure(bg="light blue")
eksekusi_waktu_label.pack()

find_button = tk.Button(result_frame, text="Find Best kombinasi", command=find_kombinasi_terbaik)
find_button.pack()

# Jalankan GUI
window.mainloop()
