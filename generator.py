
import random
import time

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

while 1:
    password_len = int(input("Code length: "))
    password_count = int(input("Code Volume: "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password      = password + password_char
        print("Here is your password : ", password )
    
        print("Code Generated")
    break
