import os
import time


def smoke() -> None:

    print('Hello welcome to SMOKE.')
    time.sleep(3)
    print('Would you like to see what we can do together\n'
          'If so please sign up below or login.')


def user():

    user_list = []
    pass_list = []

    while True:
        y: str = input('Would like to join? y/n: ')
        if y == 'y':
            username = input('Enter new username: ')
            password = input('Enter new password: ')
            user_list.append(username)
            pass_list.append(password)
            return False
        elif y == 'n':
            print('Okay maybe next.')
            return False
        else:
            if y == 'q':
                k: str = input('Would you like to exit? ')
                if k == 'y':
                    print('Goodbye')
                    exit()


if __name__ == "__main__":
    smoke()
    user()

    print('We can Search through your Directory, Create Files,'
          ' Delete Files, ADD/DELETE Folders.')
    time.sleep(4)

    abc_choice = ['1: Search Directory ', '2: Create File ',
                  '3: Delete File ', '4: ADD/DELETE Folders ', '5: Quit ']

    for abc in abc_choice:
        print(abc, end=' ')
        print("\b\b", end=" ")
        print('')
        time.sleep(1)

    x: str = input('Which would like to execute: ')

    while True:
        if x == '1':
            print(os.listdir())
            break
        if x == '2':
            print('hi')
            break
        if x == '3':
            print('hello')
            break
        if x == '4':
            print('finally')
            break
        if x == '5':
            exit()
            break
