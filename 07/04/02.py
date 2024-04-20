def check_password(password, chars="$%!?@#"):
    res = False
    for i in password:
        if i in chars and len(password) >= 8:
            res = True
            break
    return res
