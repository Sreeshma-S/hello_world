user_input = input("Enter your value: ")

if len(user_input) < 3:
    user_input = input("Enter your value (Atleast 3 characters): ")
    txt = "Hello {}, How are you?".format(user_input)
    print(txt)
else:
    txt = "Hello {}, How are you?".format(user_input)
    print(txt)