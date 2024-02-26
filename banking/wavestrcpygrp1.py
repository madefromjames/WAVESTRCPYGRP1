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
            ... 
        elif choice == '6' or choice == 'Bills & Utilities':
            # Write your code here
            ...
        elif choice == '7' or choice == 'Quit':
            print("👍 Exit successful\n")
            break
        else:
            print("\n❌ Invalid choice - Enter a number from 1 - 7\n")

def open_account():
    print("PLEASE PROVIDE YOUR INFO TO BEGIN")
    full_name = input("Full name: ")
    email = input("Email: ")
    password = input("Password: ")
    print("\n✅ Account created successful")
    print(f"{full_name}\n{email}\n")

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
                print("❌ Amount must be a number")
                continue
            print(f"\n$✅ {amount} sent successful\n")
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
    ...


if __name__ == "__main__":
    main()
    