import os

notesnames = []
notesvalues = []

def newnote():
  name1 = input("Enter name/path: ")
  content = input("Content: ")
  f_new = open(name1 + ".txt", "w")
  f_new.write(content)


def read():
  name2 = input("Enter Name/Path: ")
  f_read = open(name2, "r")
  print(f_read.read())