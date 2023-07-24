url1 = "FloppaGcdn.github.io/flop_pak/CatOS_package.py"
filename1 = "CatOS_package.py"

#def install():
#    import requests
     
#    usr = input("App ID: ")
#    if usr == "cl:cat-os-lite":
#       rq = requests.get(url1)
#       with open(filename1, "wb"):

def run():
  import call
  print("Notes: Use . instead of / and dont use file extensions\n\n All files must be in the apps dir")
  run_path = input("Path: ")
  open_py_file = call({"python", run_path})
  open_py_file


  
