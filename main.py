print("Importing packages")
import sys
import os
os.system("clear")

#cmd1 = "flop shutdown"
#cmd2 = "flop help"
#cmd2alt = "flop list"
#cmd3 = "flop del"
#cmd4 = "flop flop-pak"

while 1 < 2:
  usr = input("Enter a command: ")
  if usr == "flop shutdown":
    confirm = input("Are you sure you want to Shutdown (y/n) ")
    if confirm == "y":
      sys.exit()
    
  elif usr == "flop help":
      print("help/list - Shows a list of commands/n/del - Removes a file ")
  elif usr == "flop list":
    print("help/list- Shows a list of commands\n\ndel - Removes a file")
  elif usr == "flop del":
    delete_file = input("Path: ")
    os.remove(delete_file)
  elif usr == "help": 
    print("help - show all commands\ncatos - run catos package\n terminal - run catos terminal for one command\n toggleterminal - toggle catos terminal.")
  elif usr == "catos":
    sys.path.append("apps")
    import apps.CatOS_package
    apps.CatOS_package.run()
  elif usr == "terminal":
    os.system('clear')
    print("[CatOS terminal is running...]")
    cmdinput = input("[]catos_command: ")
    apps.CatOS_package.terminal(cmdinput)
  elif usr == "toggleterminal":
    os.system('clear')
    print("[CatOS terminnal is toggled...]")
    while 1 < 2:
      catoscmd = input("command: ")
      apps.CatOS_package.terminal(catoscmd)

    
