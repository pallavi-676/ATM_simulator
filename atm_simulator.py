# -------------------------------
# ATM SIMULATOR (USER INPUT BASED)
# -------------------------------

# Step 1: Create account
pin = int(input("Set your 4-digit PIN: "))
balance = int(input("Enter initial amount to deposit: "))

print("\nAccount created successfully!")

# Step 2: Login
entered_pin = int(input("\nEnter your PIN to login: "))

if entered_pin == pin:
    print("Login Successful!")

    while True:
        print("\n1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        # Check balance
        if choice == 1:
            print("Your balance is:", balance)

        # Withdraw
        elif choice == 2:
            amt = int(input("Enter amount to withdraw: "))
            if amt <= balance:
                balance -= amt
                print("Withdrawal successful!")
                print("Updated balance:", balance)
            else:
                print("Insufficient balance!")

        # Deposit
        elif choice == 3:
            amt = int(input("Enter amount to deposit: "))
            balance += amt
            print("Deposit successful!")
            print("Updated balance:", balance)

        # Exit
        elif choice == 4:
            print("Thank you for using the ATM.")
            break

        else:
            print("Invalid choice!")

else:
    print("Wrong PIN! Access denied.")
