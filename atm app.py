print("*********************************************")
print("**********************ATM********************")
print("*********************************************")
amount = 30000
list1 = {'2000': 10, '500': 20, '100': 30}
pin1 = "123"

def adminfun():
    global list1
    print("1.load")
    print("2.check")
    print("3.exit")
    x = int(input())
    if x == 1:
        l = list1['2000'] + int(input("enter number of 2000:"))
        m = list1['500'] + int(input("enter number of 500:"))
        n = list1['100'] + int(input("enter number of 100:"))
        list1.update({'2000': l, '500': m, '100': n})
        for i, j in list1.items():
            print("number of", i, "notes:", j)
        total = list1['2000'] * 2000 + list1['500'] * 500 + list1['100'] * 100
        print("total:", total)
    elif x == 2:
        for i, j in list1.items():
            print("number of", i, "notes in ATM:", j)
        total = list1['2000'] * 2000 + list1['500'] * 500 + list1['100'] * 100
        print("total amount in ATM:", total)
    print("1.continue or 2.exit")
    y = int(input())
    if y == 1:
        adminfun()
    else:
        print("*******THANK YOU******")
        atm()


def admin(a):
    count = 1
    admin1 = "qwerty"
    password1 = "123"
    admin2 = "siva"
    password2 = "000"
    admin3 = "deva"
    password3 = "111"
    while (count < 4):
        x = input("Enter your name:")
        y = input("Enter your password:")
        count += 1
        if (x == admin1 and y == password1) or (x == admin2 and y == password2) or (x == admin3 and y == password3):
            print("welcome", x)
            adminfun()
            break
        else:
            print("Invalid Admin login")
    else:
        print("try after 24 hrs")


def userfun():
    global amount
    global pin1
    print("1.deposit")
    print("2.withdrawal")
    print("3.Balance")
    print("4.change password")
    z = int(input())
    if z == 1:
        l = int(input("enter number of 2000:"))
        m = int(input("enter number of 500:"))
        n = int(input("enter number of 100:"))
        money = 2000 * l + 500 * m + 100 * n
        print("deposit amount:", money)
        amount = amount + money
        print("total:", amount)
        l = list1['2000'] + l
        m = list1['500'] + m
        n = list1['100'] + n
        list1.update({'2000': l, '500': m, '100': n})
    elif z == 2:
        amt = int(input("Enter the amount in whole numbers:"))
        a = amt // 2000
        print('Number of 2000 rupees note:', a)
        b = (amt - 2000 * a) // 500
        print('Number of 500 rupees note:', b)
        c = (amt - (2000 * a + 500 * b)) // 100
        print('Number of 100 rupees note:', c)
        print('Total amount withdrawal:', amt)
        amount = amount - amt
        l = list1['2000'] - a
        m = list1['500'] - b
        n = list1['100'] - c
        list1.update({'2000': l, '500': m, '100': n})
    elif z == 3:
        print('Your Current Balance amount:', amount)
    elif z==4:
        str=input("enter the new pin:")
        pin1=str
        print("Your password is successfully changed")

    print("1.continue or 2.exit")
    y = int(input())
    if y == 1:
        userfun()
    else:
        print("***********THANK YOU************")
        atm()


def user(a):
    global list1
    global pin1
    count = 1
    atm1 = "123456"
    while(count < 4):
        x = input("Enter the atm number:")
        y = input("Enter the pin:")
        count += 1
        if x == atm1 and y == pin1:
            userfun()
            break
        else:
            print("invalid number")
    else:
        print(" Your account is temporarily blocked .Try after 24 hrs")


def atm():
    print("1.admin")
    print("2.user")
    print("3.exit")
    a = int(input())
    if a == 1:
        admin(a)
    elif a == 2:
        user(a)
    elif a == 3:
        print("*********************THANK YOU**********************")


atm()
