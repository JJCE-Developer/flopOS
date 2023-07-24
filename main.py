
def run():
  print("Importing packages")
  import os
  #import time
  import sys
  sys.path.append('apps')
  import apps.environment
  os.system("clear")
  print("Setting default variables.")
  install_prefix = "flopos.install "
  notesstatus = False
  print("Setting up user system")
  import apps
  

#cmd1 = "flop shutdown"
#cmd2 = "flop help"
#cmd2alt = "flop list"
#cmd3 = "flop del"
#cmd4 = "flop flop-pak"
  #flop_sleep = input("Time until sleep")

  print("NOTES:\n\nEvery default command starts with flop")

  while 1 < 2:

    usr = input("admin" + "@Flop-OS $ ~/ ")
    if usr == "flop shutdown":
      confirm = input("Are you sure you want to Shutdown (y/n) ")
      if confirm == "y":
        sys.exit()
    
    elif usr == "flop help":
        print("help/list - Shows a list of\n\ndel - Removes a file ")
    elif usr == "flop list":
      print("help/list- Shows a list of command\n\ndel - Removes a file")
    elif usr == "flop del":
      delete_file = input("Path: ")
      os.remove(delete_file)
    elif usr == "help": 
      print("help - show all commands\ncatos - run catos package\n|_terminal - run catos terminal for one command\n|__toggleterminal - toggle catos terminal.")
  
#  elif usr == "flop flop-pak install":
#    import apps.flop_pak 
#    apps.flop_pak.install()
    elif usr == "flop flop-pak run":
      import apps.flop_pak
      apps.flop_pak.run

    elif usr == "flop dev-panel":
      import apps.dev_debug
    elif usr == "catos":
      sys.path.append("apps")
      import apps.CatOS_package
      apps.CatOS_package.run()
    elif usr == "terminal":
      os.system('clear')
      print("[CatOS terminal is running...]")
      cmdinput = input("[]catos_command: ")
      apps.CatOS_package.terminal(cmdinput)
    elif usr == "checksystem":
      apps.environment.find_errors()
    
    elif usr == "toggleterminal":
      os.system('clear')
      print("[CatOS terminnal is toggled...]")
      while 1 < 2:
        catoscmd = input("command: ")
        apps.CatOS_package.terminal(catoscmd)
    elif usr == " ".join([install_prefix + "notes"]):
      print("Installing notes... ")
      import apps.notes
      notesstatus = True
    elif usr == "note add":
      if notesstatus == True:
         apps.notes.newnote()

    elif usr == "note read":
      if notesstatus == True:
         apps.notes.read()
    
#  time.sleep(flop_sleep)
#    os.system("clear")

run()
#last update 27/07/2023 by codelogic