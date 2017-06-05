import os
frage = raw_input("Wirklich aktualisieren? (Y/n): ") or "Y"
print
if frage == 'Y':
        os.system("sudo apt-get update && sudo apt-get upgrade && sudo apt-get autoremove && sudo apt-get autoclean")
elif frage == 'n':
        print("Abbrechen...")

###
