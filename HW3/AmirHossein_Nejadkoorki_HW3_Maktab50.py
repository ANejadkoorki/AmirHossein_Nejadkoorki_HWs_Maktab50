password = input("please enter your password :   ")
# length of password
length = True if len(password) >= 6 else print('your password should have at least 6 characters')
# digits
countD = 0
for i in password:
    if i.isdigit():
        countD += 1
cD = print('your password should have at least 1 Digit ') if countD < 1 else False
# lower case
countL = 0
for i in password:
    if i.islower():
        countL += 1
cL = print('your password should have at least 1 lower case ') if countL < 1 else False
# upper case
countU = 0
for i in password:
    if i.isupper():
        countU += 1
cU = print('your password should have at least 1 uppercase ') if countU < 1 else False
# special characters
special_character = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']
countS = 0
for i in password:
    if i in special_character:
        countS += 1
cS = print('your password should have at least 1 special character ') if countS < 1 else False
# Finall check
Finall = print('your password is STRONG!!!') if len(
    password) >= 6 and countD >= 1 and countL >= 1 and countU >= 1 and countS >= 1 else False

print('-------------------------------------------------------------------------')
print('code by AmirHossein Nejadkoorki')
