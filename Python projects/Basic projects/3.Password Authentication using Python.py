import getpass

username = input("Enter a username:")
database = {"Manoj.kumar" : "123456", "kumar.manoj" : "654321"}

if username in database:
    attempts = 3
    while attempts > 0:
        password = getpass.getpass("Enter a password:")
        if password == database[username]:
            print("✅ Verified!")
            break
        else:
            attempts -= 1
        print(f"❌ Wrong password. Attempts left: {attempts}")

    if attempts == 0:
        print("🚫 Too many failed attempts. Access denied.")
else:
    print("⚠️ Invalid Username. Please try again.")