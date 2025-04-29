import sqlite3

conn = sqlite3.connect('periodic_table.db')

cursor = conn.cursor()


cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS periodic_table (
        Atomic_number INTEGER PRIMARY KEY,
        Element TEXT NOT NULL,
        Symbol TEXT NOT NULL,
        Atomic_mass TEXT,
        Group_number INTEGER,
        Period INTEGER,
        Block TEXT
    )
''')


def list_all_elements():
    cursor.execute('SELECT * FROM periodic_table')
    rows = cursor.fetchall()
    for row in rows:
        print('*'*125)
        print(row)
        print('*'*125)
    conn.commit()
    if not rows:
        print('*'*125)
        print('No elements found.')
        print('*'*125)

        
def add_element():
    atomic_number = int(input('Enter the atomic number: '))
    element = input('Enter the element: ')
    symbol = input('Enter the symbol: ')
    atomic_mass = input('Enter the atomic mass: ')
    group_number = int(input('Enter the group number: '))    
    period = int(input('Enter the period: '))
    block = input('Enter the block: ')
    cursor.execute('INSERT INTO periodic_table VALUES (?, ?, ?, ?, ?, ?, ?)', (atomic_number, element, symbol, atomic_mass, group_number, period, block))
    conn.commit()
    print('Element added successfully.')
    list_all_elements()

def search_element():
    element = input('Enter the element: ')
    cursor.execute('select * from periodic_table where element = ?', (element,))
    row = cursor.fetchone()
    if row:
        print(row)
    else:
        print('Element not found.')
    conn.commit()    
    print('Element searched successfully.')
    

def update_element():
    atomic_number = int(input('Enter the atomic number: '))
    element = input('Enter the element: ')
    symbol = input('Enter the symbol: ')
    atomic_mass = input('Enter the atomic mass: ')
    group_number = int(input('Enter the group number: '))    
    period = int(input('Enter the period: '))
    block = input('Enter the block: ')    
    cursor.execute('update periodic_table set element = ?, symbol = ?, atomic mass = ?, group number = ?, period = ?, block = ? where atomic number = ?', (element, symbol, atomic_mass, group_number, period, block, atomic_number))
    conn.commit()

def delete_element():
    atomic_number = int(input('Enter the atomic number: '))
    cursor.execute('delete from periodic_table where atomic number = ?', (atomic_number,))
    conn.commit()

def main():
    while True:
        print('1. list all elements.')
        print('2. add an element.')
        print('3. search for an element.')
        print('4. update an element.')
        print('5. delete an element.')
        print('6. exit.')
        
        choice = input('Enter your choice: ')
        
        match choice:
            case '1':
                list_all_elements()
            case '2':
                add_element()
            case '3':
                list_all_elements()
                search_element()
            case '4':
                list_all_elements()
                update_element()
            case '5':
                list_all_elements()
                delete_element()
            case '6':
                break
            case _:
                print('Invalid choice. Please try again.')
                
    conn.close()
                
if __name__ == '__main__':
    main()