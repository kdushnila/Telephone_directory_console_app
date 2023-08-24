import pandas as pd
import os


# this function makes new row with your data
def add_note(base: pd.DataFrame):
    # need to make separate data later, it for faster work
    new_note = input('\nEnter a list element separated '
                     'by ", "\n("Surname", "Name", "Patronymic", '
                     '"Organisation name", "Work phone number", "Personal phone number"): ')
    try:
        new_note = new_note.split(sep=', ')
        print(f"\nYou added {new_note} to telephone directory")
        base.loc[len(base.index)] = new_note
    except ValueError or TypeError:
        print('Error! You entered incorrect data')


# this func deleting row by index
def delete_note(base: pd.DataFrame):
    # function for delete by index. You can delete few or one data
    delete_index = (input('\nEnter index of data(if you want to delete few rows, '
                          'write it with space): ')).split(sep=' ')
    try:
        delete_index = [int(i) for i in delete_index]
        base.drop(labels=delete_index, axis=0, inplace=True)
        base.reset_index(drop=True, inplace=True)
        print(f'\nYou deleted data by {delete_index} index.')
    except ValueError:
        print('Error! You entered incorrect data')


# this func need to edit rows, you can edit it all, it's a faster way, this data is not so big
def edit_note(base: pd.DataFrame):
    try:
        edit_index = int(input('\nWrite index of data, that you want to change: '))
        print(base.query(f'\nindex == {edit_index}').to_string())
        edit_agree = input('\nYou want to change this data? yes/no: ')

        if edit_agree == 'yes':
            new_info = input('\nEnter a list element separated '
                             'by ", "\n("Surname", "Name", "Patronymic", '
                             '"Organisation name", "Work phone number", "Personal phone number"): ')
            new_info = new_info.split(sep=', ')
            base.loc[edit_index] = new_info
        elif edit_agree == 'no':
            pass
        else:
            print('\nError! Wrong answer.')
    except ValueError or TypeError:
        print('\nError! Wrong data!')


# this func helps you find row by any parameter
def find_note(base: pd.DataFrame):
    find_criteria = input('\nSurname - 1,\nName - 2,\nPatronymic - 3,\nOrganization name - 4,\n'
                          'Work phone number - 5,\nPersonal phone number - 6\n'
                          '\nPlease, enter number, you want to find by: ')

    if find_criteria.isdigit():
        find_criteria = int(find_criteria)
        find_word = input('\nEnter word or number you want find by: ')
        find_set = {1: 'surname', 2: 'name', 3: 'patronymic',
                    4: 'organisation_name', 5: 'work_phone_number', 6: 'personal_phone_number'}

        find_df = pd.DataFrame
        if find_criteria == 5 or find_criteria == 6:
            find_df = base.query(f'{find_set[find_criteria]} == {find_word}')
            if find_df.empty:
                print('\nSorry, there is no data that you want to find :(')
            else:
                print(find_df.to_string())
        elif 5 > find_criteria > 0:
            find_df = base.query(f'{find_set[find_criteria]} == "{find_word}"')
            if find_df.empty:
                print('\nSorry, there is no data that you want to find :(')
            else:
                print(find_df.to_string())
        else:
            print('\nError! Wrong number.')
    else:
        print('\nError! Wrong number!')


# this func makes simple menu for starting message
def menu():
    print('\nOptions:\n'
          'print - print first 5 datas\n'
          'add - add new data\n'
          'delete - delete data\n'
          'edit - edit data\n'
          'find - find data\n'
          'cls - clear screen\n'
          'page - pagination mode\n'
          'stop - stop program and save or not database\n')


# this func clears console page from trash
def cls():
    os.system('cls')


# this func for simple pagination in this database, it's mode, can be turned on and off
def pagination(base: pd.DataFrame):
    print(base[:10])
    start = 0
    step = 10
    while True:
        page = input('\nEnter "go" or "back" to change page\n'
                     '(write "stop" if you want to quit pagination mode): ')

        try:
            if page == 'stop':
                break
            elif page == 'go':
                if step > base.index.max():
                    print("\nIts last page, go back!")
                    continue
                cls()
                start += 10
                step += 10
                print(base[start:step])
            elif page == 'back':
                if start == 0:
                    print('\nIts the first page! You cant go back!')
                    continue
                cls()
                start -= 10
                step -= 10
                print(base[start:step])
            else:
                print('\nError! Wrong data entered!')
        except ValueError or TypeError:
            print('\nError! Wrong data!')
