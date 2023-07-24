#This is enviroment
#This will run basic loops.
def run():
  print("Environment is running, no errors found.")
  
  
def find_errors():
  import subprocess
  process = subprocess.Popen(['pyflakes', './CatOS_package.py', './dev_debug.py', './flop_pak.py', './user_system.py'], stdout=subprocess.PIPE)
  output, _ = process.communicate()
  if output:
      print(output.decode())

if __name__ == '__main__':
    find_errors()