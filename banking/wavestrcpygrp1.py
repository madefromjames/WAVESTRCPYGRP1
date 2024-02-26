import random

def main():
    print("Welcome, what would you like to do?")

    while True:
        print("1. Open account")
        print("2. Transfer")
        print("3. Airtime")
        print("4. Internet")
        print("5. Balance")
        print("6. Bills & Utilities")
        print("7. Quit")

        choice = input("\nEnter your choice: ")

        if choice == '1' or choice == 'Open account':
            open_account()
        elif choice == '2' or choice == 'Transfer':
            transfer()
        elif choice == '3' or choice == 'Airtime':
            airtime()
        elif choice == '4' or choice == 'Internet':
            internet()
        elif choice == '5' or choice == 'Balance':
            # Write your code here
            print("Your balance is $0.00")
        elif choice == '6' or choice == 'Bills & Utilities':
            # Write your code here
            bills_util()
        elif choice == '7' or choice == 'Quit':
            print("👍 Exit successful\n")
            break
        else:
            print("\n❌ Invalid choice - Enter a number from 1 - 7\n")

def open_account():
    print(f"you've selected to open an account")
    print("Kindly fill your details below!!!")
    firstname = str(input("\nInput your First_Name Here >> ")).title()
    lastname = str(input("Input your Last_Name Here >> ")).title()
    othername = str(input("Input your Other_Name Here >> ")).title()
    email = str(input("Input your Email Here >> "))
    Address = str(input("Input your Address Here >> "))

    accountnum = random.randrange(0000000000,9999999999)

    print(f"\nDear {firstname} {lastname} {othername}, your account has been successfully created, \nYour account number is {accountnum} \nThanks for joining the family")


def transfer():
    while True:
        print("RECIPIENT ACCOUNT")
        acc = input("Enter 10 digit number: ")
        if len(acc) != 10:
            print("\n❌ Number must be exactly 10 digit\n")
            continue
        
        bank = input("Bank name: ")
        while True:
            amount = input("Amount: ")
            if not amount.isdigit():
                print("❌ Amount must be a digit")
                continue
            print(f"\n$✅ {amount} Sent successful\n")
            break
        break

def airtime():
    while True:
        print("ENTER PHONE NUMBER")
        phone = input("Phone: ")
        if len(phone) != 10:
            print("\n❌ Phone number must be exactly 10 digit\n")
            continue
        amount = input("Amount: ")
        if not amount.isdigit():
            print("\n❌ Amount must be numbers\n")
        else:
            print(f"\n✅ Recharge of ${amount} successful\n")

def internet():
    while True:
        print("MOBILE DATA\nENTER A SINGLE DATA FROM 1 - 50")
        price = 1000
        data = input("Data: ")
        if data.isdigit() and 1 <= int(data) <= 50:
            price = int(data) * price
        else:
            print("Enter a digit from 1 - 50")
            continue
        print(f"Your data amount is ${price}\n")
        user = input("⚠️  Enter 1 to PAY or 0 to CANCEL: ")
        if user == '1':
            print(f"\n✅ {data}GB of ${price} was recharged successful\n")
        else:
            print("\n❌ Transaction cancelled\n")
        break

def balance():
    ...

def bills_util():
    print(f"\nyou've selected utilities and Bill, Kindly select your utility type ")
    print("1. Cable")
    print("2. PHCN")
    typeofpayment = int(input("\nEnter your choice >> "))
    list = [" ", "Cable", "PHCN"]
    num = [1,2]
    for i in num :
        y = i
        # print(y)
        if typeofpayment <= 0 or typeofpayment >=3:
            print("\nInvalid input")
        else:
            print(f"\nYou've selected {typeofpayment} for {list[typeofpayment]} payment, Kindly select Decoder type ")
        break
    if typeofpayment ==1:
        print("1. GoTV")
        print("2. DSTV")
        print("3. Startimes")
        print("4. Box office")
        print("5. Showmax")
        cabletype = int(input("\nEnter your choice >> "))
        list2 = [" ", "GoTV", "DSTV", "Startimes", "Box office", "Showmax"]
        num = [1,2,3,4,5]
        for i in num :
            y = i
            # print(y)
            if cabletype <= 0 or cabletype >=6:
                print("\nInvalid input")
            else:
                print(f"\nYou've selected {cabletype} for {list2[cabletype]} payment")
                decodernum = int(input("\nKindly enter decoder's number >> "))
                subamount = int(input("\nKindly enter subscription amount >> "))
                print(f"\nKindly confirm you want to subscribe N{subamount} for {list2[cabletype]} with smartcard number: {decodernum}")
                iagree = str(input("Press \"Y\" for Yes to Send or Press \"N\" for No to Cancel >> ")).lower()
                if iagree == "y" or iagree == "yes":
                    print("\nYour subscription is successful!")
                elif iagree == "n" or iagree == "no":
                    print("\nYour subscription is canceled!")
                else: print("\nInvalid input")
            break
    elif typeofpayment ==2:
        print("\nKindly select electricity branch or city")
        print("1. Ikeja Electric")
        print("2. Abuja Electric")
        print("3. Eko Electric")
        print("4. Jos Electric")
        print("5. Kogi Electric")
        electriclocation = int(input("\nEnter your choice >> "))
        list3 = [" ", "Ikeja Electric", "Abuja Electric", "Eko Electric", "Jos Electric", "Kogi Electric"]
        num = [1,2,3,4,5]
        for i in num :
            y = i
            # print(y)
            if electriclocation <= 0 or electriclocation >=6:
                print("\nInvalid input")
            else:
                print(f"\nYou've selected {list3[electriclocation]} for Bill payment, Kindly select meter type ")
                print("1. Prepaid")
                print("2. Postpaid")
                electricitem = int(input("\nEnter your choice >> "))
                list2 = [" ", "Prepaid", "Postpaid"]
                num = [1,2]
                for i in num :
                            y = i
                            if electricitem <= 0 or electricitem >=3:
                                print("\nInvalid input")
                            else:
                                print(f"\nYou've selected {list2[electricitem]} for Bill payment")
                                meternum = str(input("\nKindly enter meter number >> "))
                                nepabill = int(input("\nKindly enter bill or unit amount >> "))
                                if len(meternum) >12:
                                    print("\nInvalid input, kindly ensure the number is between 7-12 combinations")
                                elif len(meternum)<=12:
                                    print(f"\nKindly confirm you want to buy electric unit worth N{nepabill} for {list2[electricitem]} meter with ID: {meternum} at {list3[electriclocation]} branch")
                                    iagree = str(input("Press \"Y\" for Yes to Send or Press \"N\" for No to Cancel >> ")).lower()
                                    if iagree == "y" or iagree == "yes":
                                        print(f"\nYour {list2[electricitem]} is successfully recharged!")
                                    elif iagree == "n" or iagree == "no":
                                        print("\nYour bill payment is canceled!")
                                else: print("\nInvalid input")
                            break    
            break          
    else:
        print("\nInvalid Selection")


if __name__ == "__main__":
    main()
    
