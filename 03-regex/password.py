import re

def main():
    username = input("Username: ")
    password = input("Password: ")
    


    result = bool(re.match("(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[a-zA-Z\d]{8,}",password))

    if result:
        print("succesfully registered")
    else:
        print("""
            -At least 8 characters
            -At least one upercese letter
            -At least one lowercase letter
            -At least one digit
        """)