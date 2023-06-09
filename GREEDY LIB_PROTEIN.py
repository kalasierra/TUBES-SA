import tkinter as tk
import time

def insertion_sort(food_list):
    for i in range(1, len(food_list)):
        key = food_list[i]
        j = i - 1
        while j >= 0 and food_list[j][1] > key[1]:
            food_list[j + 1] = food_list[j]
            j -= 1
        food_list[j + 1] = key


def greedy_cat_feeding(food_list, desired_protein):
    insertion_sort(food_list)  # Sort food list by carbohydrate content using insertion sort

    best_combination = []
    total_protein = 0
    total_carbohydrates = 0

    for food in food_list:
        if total_protein >= desired_protein:
            break

        combination = best_combination + [food]
        new_protein = total_protein + food[1]
        new_carbohydrates = total_carbohydrates + food[2]

        if new_protein > desired_protein:
            if new_carbohydrates < total_carbohydrates:
                best_combination = combination
                total_protein = new_protein
                total_carbohydrates = new_carbohydrates
        else:
            best_combination = combination
            total_protein = new_protein
            total_carbohydrates = new_carbohydrates

    return best_combination


def find_best_combination():
    food_list = []
    desired_protein = 0
    
    start_time = time.time()  # Ambil waktu awal eksekusi

    # Get values from input fields
    for entry in food_entries:
        name = entry[0].get()
        protein = float(entry[1].get())
        carbohydrates = float(entry[2].get())
        food_list.append((name, protein, carbohydrates))

    desired_protein = float(desired_protein_entry.get())

    best_combination = greedy_cat_feeding(food_list, desired_protein)

    if best_combination:
        result_text.set("Best combination:\n" + "\n".join([food[0] for food in best_combination]))
    else:
        result_text.set("No combination found.")
        
    end_time = time.time()  # Ambil waktu akhir eksekusi
    execution_time = end_time - start_time  # Hitung waktu eksekusi
    
    execution_time_label.config(text="Execution Time: {:.4f} seconds".format(execution_time))

# Create the main window
window = tk.Tk()
window.configure(bg="light blue")
window.title("Greedy Cat Feeding")

# Create the food list section
food_list_frame = tk.Frame(window)
food_list_frame.configure(bg="light blue")
food_list_frame.pack()

food_entries = []
num_foods = tk.IntVar()
num_foods.set(3)

#Label dan Entry untuk jumlah makanan kucing
num_foods_label = tk.Label(food_list_frame, text="Number of Foods:")
num_foods_label.configure(bg="light blue")
num_foods_label.grid(row=0, column=0, sticky="e")

num_foods_entry = tk.Entry(food_list_frame, textvariable=num_foods)
num_foods_entry.grid(row=0, column=1, padx=5, pady=5)

def update_food_entries():
    count = num_foods.get()
    for entry in food_entries:
        entry[0].destroy()
        entry[1].destroy()
        entry[2].destroy()
    food_entries.clear()
    for i in range(count):
        food_name_label = tk.Label(food_list_frame, text="Food {}: ".format(i + 1))
        food_name_label.configure(bg="light blue")
        food_name_label.grid(row=i + 1, column=0, sticky="e")

        food_name_entry = tk.Entry(food_list_frame)
        food_name_entry.grid(row=i + 1, column=1)

        protein_label = tk.Label(food_list_frame, text="Protein: ")
        protein_label.configure(bg="light blue")
        protein_label.grid(row=i + 1, column=2, sticky="e")

        protein_entry = tk.Entry(food_list_frame)
        protein_entry.grid(row=i + 1, column=3)

        carbohydrates_label = tk.Label(food_list_frame, text="Carbohydrates: ")
        carbohydrates_label.configure(bg="light blue")
        carbohydrates_label.grid(row=i + 1, column=4, sticky="e")

        carbohydrates_entry = tk.Entry(food_list_frame)
        carbohydrates_entry.grid(row=i + 1, column=5)

        food_entries.append((food_name_entry, protein_entry, carbohydrates_entry))

update_button = tk.Button(food_list_frame, text="Update", command=update_food_entries)
update_button.grid(row=0, column=2, padx=5, pady=5)

update_food_entries()

# Create the desired protein section
desired_protein_frame = tk.Frame(window)
desired_protein_frame.configure(bg="light blue")
desired_protein_frame.pack(pady=10)

desired_protein_label = tk.Label(desired_protein_frame, text="Desired Protein:")
desired_protein_label.configure(bg="light blue")
desired_protein_label.grid(row=0, column=0, sticky="e")

desired_protein_entry = tk.Entry(desired_protein_frame)
desired_protein_entry.grid(row=0, column=1, padx=5, pady=5)

# Create the result section
result_frame = tk.Frame(window)
result_frame.configure(bg="light blue")
result_frame.pack()

result_text = tk.StringVar()
result_label = tk.Label(result_frame, textvariable=result_text)
result_label.configure(bg="light blue")
result_label.pack()

execution_time_label = tk.Label(result_frame)
execution_time_label.configure(bg="light blue")
execution_time_label.pack()

find_combination_button = tk.Button(result_frame, text="Find Best Combination", command=find_best_combination)
find_combination_button.pack(pady=10)

window.mainloop()
