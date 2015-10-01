import os, sys

def search(path):
  for dirfile in os.listdir(path):
    print "Checking %s ..."% dirfile
    if dirfile == test:
      print "FOUND"
    else:
      if os.path.isdir(path+"/"+dirfile):
        search(path+"/"+dirfile)
    

test="ha"
startpath = "/root"

#dirs = os.listdir(path)
#for file in dirs:
#   print file

search(startpath)