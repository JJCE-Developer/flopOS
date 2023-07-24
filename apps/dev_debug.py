def panel():
  import os
  
  os.system("clear") 
  
  debug_pass = os.environ['admin_pass']

  pass_input = input("Debug password ")
  if pass_input == debug_pass:
    debug_usr = input("Debug command: ")
  elif debug_usr == "dev-info":
    print("\n\nCodeName: The Flopy Floppa\n\nBuild Number: 00001")
    
# elif debug_usr == "flop-dev delete-os":
#    os.remove(main.py)
