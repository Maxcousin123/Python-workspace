try:
    num=int(input('ENter a even number'))
    assert num%2==0,"U have entered a invalid input or odd number"
except AssertionError as obj:
    print(obj)

print('after the assertion')