from string import ascii_letters, digits


def check_email(email):
    symbols = ascii_letters + digits + '@._'
    if email.index('@') > email.index('.'):
        return False
    for i in email:
        if i not in symbols:
            return False
    return True


emails = input().split()
print(*list(filter(check_email, emails)))
