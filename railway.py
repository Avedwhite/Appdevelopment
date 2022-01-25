use1="qwerty"
password1="123"
use2="siva"
password2="000"
seats=10
stops=5
n=1
list=["1.Coimbatore","2.Tirupur","3.Erode","4.Salem","5.Chennai"]
seatarray=[[0 for j in range(stops)]for i in range(seats)]
print("***********************RAILWAY ONLINE BOOKING******************")
while(n<=1):
    def booking():
        global seatarray
        global list
        print(*list)
        n=int(input("Enter the number of bookings:"))
        for pas in range(n):
            st,ed=map(int,input("Enter the starting,ending point:").split(","))
            for i in range(seats):
                if sum(seatarray[i][st-1:ed-1])==0:
                    print("Seat allocated is",i+1)
                    for j in range(st-1,ed):
                        seatarray[i][j]=pas+1
                    break
            else:
                print("Seat not Available")
        userfun()


    def cancelling():
        global seatarray
        n = int(input("Enter the number of bookings to be cancelled:"))
        for pas in range(1,n+1):
            st, ed = map(int, input("Enter the starting,ending point:").split(","))
            for i in range(seats):
                if sum(seatarray[i][st - 1:ed - 1]) != 0:
                    print("Seat is cancelled")
                    for j in range(st - 1, ed):
                        seatarray[i][j] -= pas
                    break
        userfun()

    def userfun():
        print("1.Booking tickets\n2.cancelling tickets\n3.exit")
        z = int(input())
        if z == 1:
            booking()
        elif z == 2:
            cancelling()
        else:
            print("*******Thank you for booking*******")
            pass


    def user():
        global use1,use2
        global password1,password2
        print("WELCOME TRAVELER ")
        x=input("Enter your name:")
        y=input("Enter your password:")
        if(x==use1 and y==password1)or(x==use2 and y==password2):
            print("***** WELCOME " + x + "******")
            userfun()
        else:
            print("invalid password")
            user()


    user()