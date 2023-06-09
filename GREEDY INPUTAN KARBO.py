def insertion_sort(food_list):
    for i in range(1, len(food_list)):
        key = food_list[i]
        j = i - 1
        while j >= 0 and food_list[j][2] > key[2]:
            food_list[j + 1] = food_list[j]
            j -= 1
        food_list[j + 1] = key


def greedy_cat_feeding(food_list, desired_protein):
    insertion_sort(food_list)  # Mengurutkan daftar makanan berdasarkan kandungan karbohidrat menggunakan metode insertion sort

    best_combination = []
    total_protein = 0
    total_carbohydrates = 0

    for food in food_list:
        if total_protein + food[1] > desired_protein:
            break

        combination = best_combination + [food]
        total_protein = total_protein + food[1]
        total_carbohydrates = total_carbohydrates + food[2]

        if total_protein >= desired_protein:
            if total_carbohydrates < desired_protein:
                best_combination = combination
                break
        else:
            best_combination = combination

    return best_combination



# Input food items
food_list = []
num_food_items = int(input("Enter the number of food items: "))

for i in range(num_food_items):
    name = input("Enter the name of food item {}: ".format(i + 1))
    protein = int(input("Enter the protein content of food item {}: ".format(i + 1)))
    carbohydrates = int(input("Enter the carbohydrate content of food item {}: ".format(i + 1)))
    food_list.append((name, protein, carbohydrates))

desired_protein = int(input("Enter the desired protein content: "))

best_combination = greedy_cat_feeding(food_list, desired_protein)

if best_combination:
    print("Best combination:")
    for food in best_combination:
        print(food[0])
else:
    print("No combination found.")