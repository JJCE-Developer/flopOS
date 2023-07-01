print("Importing packages")
import requests
import sys
import os 
#import apps.flop_pak.py
os.system("clear")

cmd1 = "flop shutdown"
cmd2 = "flop help"
cmd2alt = "flop list"
cmd3 = "flop del"
#cmd4 = "flop flop-pak"

while 1 < 2:
  usr = input("Enter a command: ")
  if usr == cmd1:
    confirm = input("Are you sure you want to Shutdown (y/n)")
    
  elif usr == cmd2:
      print("help/list - Shows a list of commands/n/del - Removes a file ")
  elif usr == cmd2alt:
    print("help/list- Shows a list of commands\n\ndel - Removes a file")
  elif usr == "cmd3":
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

    
