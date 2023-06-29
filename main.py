print("Importing packages")
import os
os.system("clear")

cmd1 = "flop help"
cmd1alt = "flop list"
cmd2 = "flop del"

while 1 < 2:
  usr = input("Enter a command: ")
  if usr == cmd1:
      print("help/list - Shows a list of commands/n/del - Removes a file ")
  else:
    if usr == cmd1alt:h
    print("help/list- Shows a list of commands\n\ndel - Removes a file")
else:
  if usr == cmd2:h
  delete_file = input("Enter the path of the file that you want to delete: ")
  os.remove(delete_file)
