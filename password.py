import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    if length_error:
        return "Weak (Minimum 8 characters required)"
    if digit_error:
        return "Weak (Add at least one number)"
    if uppercase_error:
        return "Weak (Add at least one uppercase letter)"
    if lowercase_error:
        return "Weak (Add at least one lowercase letter)"
    if special_char_error:
        return "Weak (Add at least one special character)"

    return "Strong Password"

print("---- Password Strength Checker ----")

password = input("Enter your password: ")
result = check_password_strength(password)

print("Result:", result)
