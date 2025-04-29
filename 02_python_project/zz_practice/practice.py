
import json
Fname = 'Grocery_store.txt'
def load_data():
    try:
        with open(Fname,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    

def items_helper(items):
    with open(Fname, 'w') as file:
        json.dump(items, file)
        
def list_all_items(items):
    for index, item in enumerate(items, start=1):
        print(f'{index}.')
    
def add_items(items):
    item_name = input("Enter name of item: ")
    item_price = input("Enter price of one item: ")
    items.append({'Name' : item_name, 'Price': item_price})
    items_helper(items)


def select_items(items):
    pass
    
def remove_items(items):
    pass

def total_price_items(items):
    pass

def main():
    items = load_data()

    while True:
        print('press 1, if you want to list all items.')
        print('press 2, if you want to list all items.')
        print('press 3, if you want to add items in your list.')
        print('press 4, if you want to remove items from your list.')
        print('press 5, if you want to total price of selected items of list.')
        print('press 6, if you want to Exit program.')

        choice = input("enter your choice: ")

        match choice:
            case '1':
                list_all_items(items)

            case '2':
                add_items(items)

            case '3':
                select_items(items)

            case '4':
                remove_items(items)

            case '5':
                total_price_items(items)

            case '6':
                print("Thank you to use this program.")
                break

            case _:
                print('Invalid Choice.')

if __name__ == '__main__':
    main()