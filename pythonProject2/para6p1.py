try:
    print("start code")
    print(10/0)
    print("No error")
except NameError:
    print("We have an error")
except ZeroDivisionError:
    print("We have ZDE(0)")

print("code after capsule")
