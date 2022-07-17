more_than_8_letters = False
capital = False
symbol = False
number = False

password_strong = False

lowercase = False 

while password_strong == False :
    

    password = input("Type your password, use minimum 8 letters, capital , numbers,and symbols:")

    #checking valid length
    if len(password) < 8:
        print("The password should be at least 8 letters")
        continue
    else:
        more_than_8_letters = True

    for index in password:
        if index.isupper(): 
                capital = True
        elif index in "0123456789":
            number = True
        elif index.islower():
            lowercase = True
        else: # index not in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            symbol = True
    
    if number and capital and symbol and more_than_8_letters:
        print(f"The password {password} is strong enough!")
        password_strong = True
    else:
        if not number:
            print("Your password has no number")
            
        
        if not capital:
            print("your password has no capital letter")
            

        if not symbol:
            print("yor password has no symbol")

        print("Give new password")
            
