dic_admin = {"qwerty": "123"}
dic_vendor = {"siva": "123"}
vendor_proposal={"siva": "A"}
dic_user = {"deva": "123"}
n=1
vendor_lst={}
original_vendor=["siva"]
phone = {"realmex7": 27000, "iphone": 150000}
laptop = {"vivo book": 90000, "zenbook": 60000}
items=[phone,laptop]
while(n>=1):
    print("********************** AMAZON ******************************")
    print("1.admin\n2.vendor\n3.user")
    choice = int(input())
    def admin():
        global dic_admin
        global vendor_lst
        lst=list(vendor_lst)
        admin_name = str(input("enter the name:"))
        admin_password = str(input("enter the password:"))
        if ((admin_name, admin_password) in dic_admin.items()):
            print("*****WELCOME " + admin_name + "*****")
            print("1.accept/remove vendor\n2.exit")
            choice=int(input())
            if(choice==1):
              print("WAITING LIST:")
              count=0
              if(len(vendor_lst.items())!=0):
                for i in range(0,len(lst)):
                    count+=1
                    print(str(count)+".",lst[i])
                    print("1)accept\n2)decline")
                    choice1=int(input())
                    if(choice1==1):
                        vendor_proposal.update({lst[i] : 'A'})
                        vendor_lst.pop(lst[i])
                        original_vendor.append(lst[i])
                    else:
                        vendor_proposal.update({lst[i] : 'D'})
                        vendor_lst.pop(lst[i])
              else:
                print("No Pending")
        else:
            print("Invalid username or password")
    def vendor():
        global dic_vendor
        global vendor_lst
        print("1.new vendor\n2.existing vendor\n3.exit")
        vendor_choice = int(input())
        if (vendor_choice == 1):
            loop = True
            while (loop == True):
                vendor_name = str(input("enter the Name:"))
                vendor_password = str(input("enter the password:"))
                if ((vendor_name, vendor_password) in dic_vendor.items()):
                        print("name is already existing")
                        loop = True
                else:
                    dic_vendor.update({vendor_name : vendor_password})
                    vendor_lst.update({vendor_name : vendor_password})
                    vendor_proposal.update({vendor_name : "new"})
                    loop = False
        elif (vendor_choice == 2):
            vendor_name = str(input("enter the name:"))
            vendor_password = str(input("enter the password:"))
            if ((vendor_name, vendor_password) in dic_vendor.items()):
                if (vendor_proposal.get(vendor_name) == "A"):
                    print("***logined successfully***")
                    vendorfun()
                elif(vendor_proposal.get(vendor_name) == "D"):
                    print("your proposal is  declined")
                else:
                    print("In progress")
            else:
                print("invalid username or password")
    def user():
        global dic_user
        print("1.new user\n2.existing user\n3.exit")
        user_choice = int(input())
        if (user_choice == 1):
            loop = True
            while (loop == True):
                user_name = str(input("enter the Name:"))
                user_password = str(input("enter the password:"))
                if ((user_name, user_password) in dic_user.items()):
                    print("name is already existing")
                    loop = True
                else:
                    dic_user.update({user_name:user_password})
                    print("Your account is created successfully")
                    loop = False
        elif (user_choice == 2):
            user_name = str(input("enter the name:"))
            user_password = str(input("enter the password:"))
            if ((user_name, user_password) in dic_user.items()):
                print("*****logined successfully******")
                userfun()
            else:
                print("invalid username or password")
    def vendorfun():
        global phone,laptop
        global  items
        print("1.add or update items \n2.remove items \n3.exit")
        choice=int(input())
        if(choice==1):
            print("Category:\n1.phone\n2.laptop")
            choice=int(input())
            if(choice==1):
                item_name=str(input("Phone Name:"))
                item_value=str(input("price:"))
                phone.update({item_name : item_value})
                print("PRODUCT  PRICE")
                for i, j in phone.items():
                    print(i,j,sep=" ")
            else:
                item_name=str(input("LAPTOP Name:"))
                item_value=str(input("price:"))
                laptop.update({item_name: item_value})
                for i, j in laptop.items():
                    print(i,j,sep=" ")
            vendorfun()
        elif(choice==2):
            print("Category:\n1.phone\n2.laptop")
            choice = int(input())
            if (choice == 1):
                item_name = str(input("phone name:"))
                phone.pop(item_name)
                for i, j in phone.items():
                    print(i, j, sep=" ")
            else:
                item_name = str(input("laptop name:"))
                laptop.pop(item_name)
                for i, j in laptop.items():
                    print(i, j, sep=" ")
            vendorfun()
        else:
            pass
    def userfun():
        global phone, laptop
        global items
        print("Category:\n1.phone\n2.laptop")
        search=int(input("mention the category:"))
        if search==1:
            print("*********products*******")
            print("PRODUCT  PRICE")
            for i,j in phone.items():
                print(i,j,sep=" ")
            str=input("Name of the product:")
            if str in phone.keys():
                print("The product is added to the cart")
                x=input("Do you want to continue:")
                if x=="yes":
                    print("****The order is confirmed****\nThank you for shopping")
                else:
                    print("*****The order is cancelled****")
            else:
                print("The product is unavailable")
        elif search==2:
            print("*********products*******")
            print("PRODUCT  PRICE")
            for i,j in laptop.items():
                print(i,j,sep=" ")
            str=input("Name of the product:")
            if str in laptop.keys():
                print("The product is added to the cart")
                x = input("Do you want to continue:")
                if x == "yes":
                    print("*****The order is confirmed*****\nThank you for shopping")
                else:
                    print("********The order is cancelled******")
            else:
                print("The product is not available")

    if (choice == 1):
        admin()
    elif (choice == 2):
        vendor()
    elif (choice == 3):
        user()
