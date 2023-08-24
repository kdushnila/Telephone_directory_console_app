# test program for telephone directory
import pandas as pd

from functions_telephone_directory import (add_note, delete_note,
                                           edit_note, menu,
                                           find_note, pagination, cls)

# new columns and dataframe for the first time, then it's no need after first save
'''
col = ['surname', 'name', 'patronymic',
       'organisation_name', 'work_phone_number', 'personal_phone_number']
db = pd.DataFrame(columns=col)
'''

# reading from csv database that was made one time higher and saved
db = pd.read_csv('test_db_csv.csv', index_col=0)

# new data for test for the first time(than i added datas with this program)
'''
db.loc[len(db.index)] = ['Kurosh', 'Danila', 'Dmitriyevich',
                         'Big Company', '84997770707', '88005553535']
# print(db.to_string())
'''
# Hello from program
print('\nHello, its telephone directory!')

# main circle with all functions from menu
# (all functions are in another file named functions_telephone_directory)
while True:
    user_input = input('\nWhat you wanna do? Write it here '
                       '(if you want look at the commands - write "menu"): ')
    if user_input == 'print':
        print(db.head().to_string())
    elif user_input == 'add':
        add_note(db)
    elif user_input == 'delete':
        delete_note(db)
    elif user_input == 'edit':
        edit_note(db)
    elif user_input == 'find':
        find_note(db)
    elif user_input == 'cls':
        cls()
    elif user_input == 'menu':
        menu()
    elif user_input == 'page':
        pagination(db)
    elif user_input == 'stop':
        decide = input('\nDo you want to save file? yes/no: ')
        if decide == 'yes':
            db.to_csv('test_db_csv.csv')
            break
        elif decide == 'no':
            break
        else:
            print('\nI dont understand you')
    else:
        print('\nI dont understand you')
