




password = "1234"
attempt = 4
while attempt>0:
    user = input("Enter your password\n:")
    if user == password:
        print("YES U R CORRECT")
        print("YOUR WELCOME")
        break
    else:
        attempt-=1
        print("INCORRECT PASSWORD")
    if attempt>0:
        print(f"YOU HAVE ONLY {attempt} ATTEMPTS LEFT")
    else:
        print("NO MORE ATTEMPTS LEFT ACCOUNT IS LOKED")

