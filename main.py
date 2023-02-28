from string import ascii_lowercase
from time import sleep
import os


def clear(secs=1):
    sleep(secs)
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    is_running = True

    while is_running:
        option = input(
            'Enter \'encode\' to encrypt or \'decode\' to decrypt: ')
        message = input('Enter your message: ').lower()
        shift = int(input('Enter the shift number: '))
        new_message = cipher(option, message, shift)
        print(f'\nHere\'s the encoded result: {new_message}')
        clear(2)

        again = input('Enter \'yes\' to restart or \'no\' to quit: ').lower()
        if again == 'no':
            is_running = False
        clear()


def cipher(option, message, shift_number):
    letters = list(ascii_lowercase)
    shifted = letters[shift_number:] + letters[:shift_number]

    if option == 'encode':
        scheme = {letter: code for letter, code in zip(letters, shifted)}
    else:
        scheme = {letter: code for letter, code in zip(shifted, letters)}

    return ''.join([scheme[letter] for letter in message])


if __name__ == '__main__':
    main()
