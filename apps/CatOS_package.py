def run():
  print("Importing catos package.")
  import os
  import sys
  os.system('clear')

def terminal(cmd):
  print("importing...")
  import os
  import sys
  os.system("clear")
  if cmd == "help":
    print("[CatOS says]\nhelp - show all terminal commands.\ncls - clear screen\nshutdown - shut programm down\ncatos help - show catos help\nnote: this is catos terminal running in other program. ")
  elif cmd == "cls":
    os.system("clear")
  elif cmd == "shutdown":
    sys.exit()
  elif cmd == "catos help":
    print("Try to load the newest catos package.")
  else: 
    print("[CatOS says] This is not catos command. For help type catos help.")