import os

cmd1 = "flop help"
cmd1alt = "flop list"
cmd2 = "flop del"
usr = input("Enter a command: ")
if usr == cmd1:
    print("help/list - Shows a list of commands")
else:
  if usr == cmd1alt:
    print("help/list- Shows a list of commands")
  else:
    delete_file = input("Enter the path of the file that you want to delete: ")
    os.remove(delete_file)
