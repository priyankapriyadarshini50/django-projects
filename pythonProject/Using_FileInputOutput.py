f = open("mytestfile.txt")  # it creates a file object, but it does not create a text file
print(f.read(5))
f.seek(0)
print(f.read())
f.seek(0)
print(f.readlines())
#f1 = open('F:\\2. Priyanka\\Python Notes\\SomePythonImportantNotes.txt', "r")
#print(f1.read())
#  to read one line of the text
#print(f1.readline())
#print(f.readline())
#print(f1.readline(5))
# to read all the lines one by one using looping
#for x in f:
 #   print(x)
#f.close()
#  Best practice to read a file as here we do not need to close the file explicitly
#with open("demofile.txt") as demo_user_file:
 #   content = demo_user_file.read()
  #  print(content)
#f = open("demofile.txt","a")
#f.write("New content is added to the file.")
#f.close()

#f = open("demofile.txt", "r")
#print(f.read())
#f.close()

#f = open("demofile.txt","w")
#f.write("Opps, I have deleted and overwritten all the contents")
#f.close()

#f = open("demofile.txt","r")
#print(f.read())
#f.close()

# To create a new file with filename mynewtest file
#  f1 = open("mynewtest.txt", "x")
#f1 = open("mynewtest.txt", "w")
#f1.write("Priyanka has created a new file and started writing in it!")
#f1.close()

#f1 = open("mynewtest.txt", "r")
#print(f1.read())
#f1.close()
# To delete a file
#import os
#os.remove("mytestfile")
