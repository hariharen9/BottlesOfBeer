x = input("Enter the number of bottles of beer you have \n")
x = int(x)


def beer(bob):
    if bob < 1:
        print("""No more bottles of beer on the wall. No more bottles of beer. CHEERS!!!!!!!""")
        return

    tmp = bob
    bob -= 1
    print("""{} bottles of beer on the wall.{} bottles of beer. Take one down, pass it around,{} bottles of beer on the wall.""".format(tmp, tmp, bob))
    beer(bob)


beer(x)
