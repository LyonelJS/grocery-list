grocery_list = []
choice = 0
while choice != '4': 
    print('Pick between choices 1 to 4')   
    print('[1] Add an item')
    print('[2] View list')
    print('[3] Remove item')
    print('[4] Exit')
    choice = input('Enter your choice: ')

    match choice:
        case '1': 
            add_to_list = input('Enter the item to add: ')
            grocery_list.append(add_to_list)
            print(f'{add_to_list} has been added to list')
        case '2':
            if len(grocery_list) != 0:
                print('Your Grocery List:')
                for l in grocery_list:
                    print(l)
            else: 
                print('Your grocery list is empty')
        case '3':
            item_remove = input('Enter an item to remove: ')
            if item_remove in grocery_list:
                grocery_list.remove(item_remove)
                print(f'{item_remove} has been removed from the list')
            else:
                print(f'{item_remove} is not in the list')
        case '4': break
        case _: 
            print('Enter a number between 1 to 4')

print('You have exit from the list')