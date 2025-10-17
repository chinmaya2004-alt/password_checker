def password():
    password = input("Enter a password: ")
    length = len(password)

    upper = False
    lower = False
    number = False
    special = "!@#$%^&*()_+"
    spl_char = False

    if length < 8:
        print("Invalid password!! (must be at least 8 characters)")
        return

    for i in password:
        if i.isupper():
            upper = True
        elif i.islower():
            lower = True
        elif i.isdigit():
            number = True
        elif i in special:
            spl_char = True

    if upper and lower and number and spl_char:
        print("Your password is valid ✅")
    else:
        print("Your password is invalid ❌")


# Call the function
password()
