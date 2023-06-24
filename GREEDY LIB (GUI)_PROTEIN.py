import tkinter as tk
import time

def insertion_sort(list_food):
    for i in range(1, len(list_food)):
        key = list_food[i]
        j = i - 1
        while j >= 0 and list_food[j][1] > key[1]:
            list_food[j + 1] = list_food[j]
            j -= 1
        list_food[j + 1] = key


def greedy_cat_feeding(list_food, target_protein):
    insertion_sort(list_food)  # Urutkan daftar makanan berdasarkan kandungan karbohidrat menggunakan insertion sort

    kombinasi_terbaik = []
    total_protein = 0
    total_karbohidrat = 0

    for food in list_food:
        if total_protein >= target_protein:
            break

        kombinasi = kombinasi_terbaik + [food]
        new_protein = total_protein + food[1]
        new_karbohidrat = total_karbohidrat + food[2]

        if new_protein > target_protein:
            if new_karbohidrat < total_karbohidrat:
                kombinasi_terbaik = kombinasi
                total_protein = new_protein
                total_karbohidrat = new_karbohidrat
        else:
            kombinasi_terbaik = kombinasi
            total_protein = new_protein
            total_karbohidrat = new_karbohidrat

    return kombinasi_terbaik


def find_kombinasi_terbaik():
    list_food = []
    target_protein = 0
    
    start_time = time.time()  # Ambil waktu awal eksekusi

    # Dapatkan nilai dari kolom input
    for entry in food_entries:
        jenis_makanan = entry[0].get()
        protein = float(entry[1].get())
        karbohidrat = float(entry[2].get())
        list_food.append((jenis_makanan, protein, karbohidrat))

    target_protein = float(target_protein_entry.get())

    kombinasi_terbaik = greedy_cat_feeding(list_food, target_protein)

    if kombinasi_terbaik:
        result_text.set("Best kombinasi:\n" + "\n".join([food[0] for food in kombinasi_terbaik]))
    else:
        result_text.set("Tidak ditemukan kombinasi.")
        
    end_time = time.time()  # Ambil waktu akhir eksekusi
    eksekusi_waktu = end_time - start_time  # Hitung waktu eksekusi
    
    eksekusi_waktu_label.config(text="Execution Time: {:.4f} seconds".format(eksekusi_waktu))

# Buat jendela utama
window = tk.Tk()
window.configure(bg="light blue")
window.title("Greedy Cat Feeding")

# Buat bagian daftar jenis makanan
list_food_frame = tk.Frame(window)
list_food_frame.configure(bg="light blue")
list_food_frame.pack()

food_entries = []
num_foods = tk.IntVar()
num_foods.set(3)

#Label dan Entry untuk jumlah makanan kucing
num_foods_label = tk.Label(list_food_frame, text="Banyaknya Makanan:")
num_foods_label.configure(bg="light blue")
num_foods_label.grid(row=0, column=0, sticky="e")

num_foods_entry = tk.Entry(list_food_frame, textvariable=num_foods)
num_foods_entry.grid(row=0, column=1, padx=5, pady=5)

def update_food_entries():
    count = num_foods.get()
    for entry in food_entries:
        entry[0].destroy()
        entry[1].destroy()
        entry[2].destroy()
    food_entries.clear()
    for i in range(count):
        food_jenis_makanan_label = tk.Label(list_food_frame, text="Food {}: ".format(i + 1))
        food_jenis_makanan_label.configure(bg="light blue")
        food_jenis_makanan_label.grid(row=i + 1, column=0, sticky="e")

        food_jenis_makanan_entry = tk.Entry(list_food_frame)
        food_jenis_makanan_entry.grid(row=i + 1, column=1)

        protein_label = tk.Label(list_food_frame, text="Protein: ")
        protein_label.configure(bg="light blue")
        protein_label.grid(row=i + 1, column=2, sticky="e")

        protein_entry = tk.Entry(list_food_frame)
        protein_entry.grid(row=i + 1, column=3)

        karbohidrat_label = tk.Label(list_food_frame, text="karbohidrat: ")
        karbohidrat_label.configure(bg="light blue")
        karbohidrat_label.grid(row=i + 1, column=4, sticky="e")

        karbohidrat_entry = tk.Entry(list_food_frame)
        karbohidrat_entry.grid(row=i + 1, column=5)

        food_entries.append((food_jenis_makanan_entry, protein_entry, karbohidrat_entry))

update_button = tk.Button(list_food_frame, text="Update", command=update_food_entries)
update_button.grid(row=0, column=2, padx=5, pady=5)

update_food_entries()

# Buat bagian untuk target protein 
target_protein_frame = tk.Frame(window)
target_protein_frame.configure(bg="light blue")
target_protein_frame.pack(pady=10)

target_protein_label = tk.Label(target_protein_frame, text="Target Protein:")
target_protein_label.configure(bg="light blue")
target_protein_label.grid(row=0, column=0, sticky="e")

target_protein_entry = tk.Entry(target_protein_frame)
target_protein_entry.grid(row=0, column=1, padx=5, pady=5)

# Buat bagian untuk result
result_frame = tk.Frame(window)
result_frame.configure(bg="light blue")
result_frame.pack()

result_text = tk.StringVar()
result_label = tk.Label(result_frame, textvariable=result_text)
result_label.configure(bg="light blue")
result_label.pack()

eksekusi_waktu_label = tk.Label(result_frame)
eksekusi_waktu_label.configure(bg="light blue")
eksekusi_waktu_label.pack()

find_kombinasi_button = tk.Button(result_frame, text="Find Best kombinasi", command=find_kombinasi_terbaik)
find_kombinasi_button.pack(pady=10)

window.mainloop()
