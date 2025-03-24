import accountcreation as AC


password = "my_secure_password"
hashed_pw = AC.hash_password(password)
print(hashed_pw)