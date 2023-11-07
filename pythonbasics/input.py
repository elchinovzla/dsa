user_name = input("what is your username?")
password = input("please enter a password:")
password_lenght = len(password)
masked_password = '*' * password_lenght

print(f"hello {user_name}, your password is {masked_password} and its length is {password_lenght}")
