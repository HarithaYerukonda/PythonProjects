def strength(password):
    result = {}

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False

    for i in password:
        if i.isdigit():
            digit = True

        else:
            digit = False
    result["digits"] = digit

    upper = False

    for i in password:
        if i.isupper():
            upper = True

        else:
            upper = False
    result["upper"] = upper

    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"


user_action = input("Enter the password:")
strength(user_action)
