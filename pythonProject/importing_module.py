#  import execution_methods

#  1st way to import and call functions using dotted notation
#  import HelloWorld
#  HelloWorld.say_hi()
#  print('The version is:', HelloWorld.version)


#  2nd way to import module and call function
#  from HelloWorld import say_hi, version
#  say_hi()
#  print("version is:", version)


#  3rd way to import module and call functions
from HelloWorld import *
say_hi()
print("Version is :", version)
