class InvalidPasswordException(Exception):

    pass



while True:

    try:

        p = input('Enter a password with of minimum length 8 characters: ')

        if len(p) < 8:

            raise InvalidPasswordException

        elif len(p) >= 8:

            print ('Your password is saved!')

            break

    except InvalidPasswordException:

        print ('Plz increase the length of your password')

print ('Password defined')