import os

cmd1 = "help"
cmd2 = "del"
usr = input("Enter a command: ")
if usr == cmd1:
    print("help - Shows a list of commands")
else:
    if usr == cmd2:
        delete_file = input("Enter the name of the file that you want to delete")
        os.remove(delete_file)
