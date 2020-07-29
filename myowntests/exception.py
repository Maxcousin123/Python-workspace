try:
    pw=input('plz Enter the password')
    assert len(pw)>8, 'the password is too short'
except AssertionError as e:
    print(e)
else:
    print('password saved')
