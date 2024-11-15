favorite_food = []

print('\n-------Welcome to Favorite Food Manager--------\n')

while True:
    print("------------**------------")
    print('0. Exit')
    print('1. Add Food')
    print('2. Remove Food')
    print('3. View all favorite food')
    print("------------**------------")
    print("\n")

    option = int(input("Choose an option (0/1/2/3): "))

    if option == 0:
        print('Thank you for using Favorite Food Manager.\n') 
        break
    
    elif option == 1:
        food = input("Write your favorite food : ")
        if food not in favorite_food:
            favorite_food.append(food.strip())
            print("---- Favorite food added successfully. ----\n")
        else:
            print(food,'--------Alrady Exits------\n')
    elif option == 2:
        if not favorite_food:
            print("---- The list is empty. No food to remove. ----\n")
        else:
            food = input("Write which food you want to remove : ")
            if food in favorite_food:
                favorite_food.remove(food)
                print("---- Favorite food removed successfully. ----\n")
            else:
                print("---- Food not found in the list. ----\n")

    elif option == 3:
        if not favorite_food:
            print("---- The favorite food list is empty. ----\n")
        else:
            print("---- All favorite foods ----")
            for index, food in enumerate(favorite_food, start=1):
                print(f"{index}. {food}")
            

            print("---- End of list ----\n")

    else:
        print("Invalid option. Please choose a valid option.\n")
