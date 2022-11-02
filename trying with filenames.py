

name = 'padf'

def test_or_prod(filename):
    if filename[0] == 'p':
        number = 5
        print ("production certificate")

    elif filename[0] == 't':
        number = 9
        print("testing certificate")
    else:
        print("Incorrect file.")
    return number
