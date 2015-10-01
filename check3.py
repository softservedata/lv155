import unittest
import os
from sys import argv

class Check(unittest.TestCase):
  # Test Data
  parentDir="root"
  checkDir=[]

  @staticmethod
  def setUpClass():
    #i=1
    #while i<len(argv)
    print "In setUpClass()"

  def setUp(self):
    #
    # Precondition. Goto to self.parentDir folder
    os.chdir("/"+self.parentDir)
    print "  setUp"

  def tearDown(self):
    print "  tearDown"

  def test_allExistDir(self):
    #
    if len(self.checkDir)>0:
      for dir in self.checkDir:
        print "CHECKING... %s"% dir
        self.check_allExistDir(dir)
    else:
      print "[WARNING] checkDir is Empty"
      self.assertTrue(False)

  def check_allExistDir(self,dir):
    #
    # if exist
    result = os.path.exists("./"+dir)
    print "if exist: result value %s"% result
    self.assertTrue(result)
    #
    # access
    ret = os.access(dir, os.X_OK)
    print "F_OK - return value %s"% ret
    self.assertTrue(ret)
    #
    # if directory
    result=os.path.isdir("./"+dir)
    print "if directory: result value %s"% result
    self.assertTrue(result)

if __name__ == '__main__':
  print "Len= %s"% len(argv)
  while len(argv)>1:
    Check.checkDir = Check.checkDir + [argv.pop()]
  unittest.main()
