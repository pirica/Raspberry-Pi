import os

try:
    while True:
        tmp = os.system("sudo ufw status").read()
        if tmp == "Status: active":
            print("Firewall is acitve!")
            confirm = input("Turn off the Firewall? (y/N): ") or "N"
            if confirm == "y":
                os.system("sudo ufw disable")
                print("Firewall shut down!")
            else:
                print("Firewall protects you further!")

        else:
            print("Firewall is disabled")
            confirm == input("Turn on the Firewall? (Y/n): ") or "Y"
            if confirm == "Y":
                os.system("sudo ufw enable")
                print("The Firewall protects you now!")
            else:
                print("Firewall doesn't protects you further!")

except Exception as error:
    print(error)
