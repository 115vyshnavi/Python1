username = "asha99"
password = "secret123"
is_admin = False
access = (username != "" and len(password) >= 8) or is_admin
print(access)