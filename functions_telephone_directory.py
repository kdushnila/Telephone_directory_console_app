import pandas as pd
import os


def add_note(base: pd.DataFrame):
    # need to make separate data later, it for faster work
    new_note = input('\nEnter a list element separated by ", ": ')
    new_note = new_note.split(sep=', ')
    print(f"\nYou added {new_note} to telephone directory")
    base.loc[len(base.index)] = new_note


def delete_note(base: pd.DataFrame):
    # function for delete by index. You can delete few or one data
    delete_index = (input('\nEnter index of data(if you want to delete few rows, '
                          'write it with space): ')).split(sep=' ')
    delete_index = [int(i) for i in delete_index]
    base.drop(labels=delete_index, axis=0, inplace=True)
    base.reset_index(drop=True, inplace=True)
    print(f'\nYou deleted data by {delete_index} index.')


def edit_note(base: pd.DataFrame):
    edit_index = int(input('\nWrite index of data, that you want to change: '))
    print(base.query(f'index == {edit_index}').to_string())
    edit_agree = input('\nYou want to change this data? yes/no: ')
    if edit_agree == 'yes':
        pass
    elif edit_agree == 'no':
        pass
    else:
        print('\nError! Wrong answer.')


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


def menu():
    print('\nOptions:\n'
          'print - print all data\n'
          'add - add new data\n'
          'delete - delete data\n'
          'edit - edit data\n'
          'find - find data\n'
          'cls - clear screen\n'
          'stop - stop program and save or not database\n')


def pagination(base: pd.DataFrame):
    pass


def cls():
    os.system('cls')
