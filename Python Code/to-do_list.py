user_input = 'List'
data = []

def show_menu():
    print('1. Add Item')
    print('2. Mark as Done')
    print('3. View to do List')
    print('4. Exit')



while user_input != '4':

    show_menu()
    user_input = input("Enter  your Choice: ")

    if user_input == '1':
        item = input('What is to be done?: ')
        data.append(item)
        print("Added Item")
    elif user_input == '2':

        item = input("What is to be marked as done: ")
        if item in data:
            data.remove(item)
            print("Item Removed", item)
        else:
            print('Item is not in the list')

    elif user_input == '3':
        for item in data:
            print(item)
            
    elif user_input == '4':
        print("Goodbye")
    else:
        print("Please enter 1, 2, 3 or 4")
