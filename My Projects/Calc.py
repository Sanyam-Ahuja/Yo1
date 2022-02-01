# Calculator
# Inputs
_1a = input("Enter Your First No.")
_oa = input("Enter Your Operartion")
_2a = input("Enter Your Second No.")


# Conversion From Strings To Integers The Floats(Decimals)
# A point To be added to check wether string has . or not
_1a = float(_1a)
_2a = float(_2a)
# _2a = int(_2a)
# _1a = int(_1a)


#Managing Opertion and Printing


if (_oa == "+"):
    print(_1a +_2a)
elif (_oa == "-"):
            print(_1a -_2a)
elif (_oa == "*"):
                   print(_1a *_2a)
elif _oa == "/":
                            print(_1a /_2a)
elif _oa == "//":
    print(_1a // _2a)
elif _oa == "%":
    print(_1a % _2a)
else :
    print("Sorry Invalid Operation")