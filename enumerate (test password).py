passwords = ["123456", "ali2024", "SecurePass1", "abc111111", "Pa$$word123"]

for index, password in enumerate(passwords, start=1):
    has_digit = False
    has_upper = False

    if len(password) >= 8:
        for char in password:
            if char.isdigit():
                has_digit = True
            if char.isupper():
                has_upper = True

        if has_digit and has_upper:
            print(f"User {index}: ✅ Strong password ({password})")
        else:
            print(f"User {index}: ⚠️ Weak password ({password})")
    else:
        print(f"User {index}: ❌ Too short ({password})")
