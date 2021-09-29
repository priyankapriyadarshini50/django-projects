# d is the dictionary for address
d = {'adya': 'Ormond Kinder', 'priyanka': '2 Ulupna Road', 'umesh': 'TCS st Kilda office'}
print("The adress of Adya's school is %s" % d['adya'])
print("The address of Priyanka's house is %s" % d['priyanka'])
print("The address of Umesh's office is %s" % d['umesh'])
# add a new address to the address book
d['devasmita'] = 'WhydhamVale, Voctoria'
print("The length of the dictionary is %d" % len(d))
# delete one address from address book
del d['devasmita']
print("The number of contacts in the address book is %s " % len(d))
# shows the key/value pairs as tuples in a list
MyList = d.items()
print(MyList)
thisdict = {'Brand': 'Ford', 'Model': 'Mustang', 'Year': 2020, 'Year': 1986}
print(thisdict)
# add a list value to the above dictionary
thisdict['Electric'] = False
thisdict['Colours'] = ['red', 'blue', 'white']
print("The updated dictionary after adding a new key/value pair is %s" % thisdict)
# delete the key 'model' from the dictionary
del thisdict['Model']
print("The updated dictionary after deleting the key 'model' is %s" % thisdict)
# type() returns the class of dictionary
print(type(thisdict))
print(type(thisdict['Electric']))
print(type(thisdict['Colours']))
# accessing the values of key/value pairs using get()
x = thisdict.get('Year')
a = thisdict['Brand']
print("The values of the key 'Year' and 'Brand' are %d %s respectively." % (x, a))
# accessing all the keys in a dictionary using keys() method
y = thisdict.keys()
print("All the keys available in the dictionary thisdict are %s" % y)
# accessing all the values in a dictionary using values()
z = thisdict.values()
print("All the values in the dictionary thisdict are %s" % z)
# now electric cars are available in Ford brand (change one value)
thisdict['Electric'] = True
print("The updated dictionary is %s" % thisdict)
# Dictionary looping, returns the keys of the dictionary
for b in thisdict:
    print("The key in the dictionary is %s" % b)
# print all the values of the dictionary
for c in thisdict:
    print("The value in the dictionary is %s" % thisdict[c])


# This function finds the values in a dictionary
def find_french_word():
    dictionary = {'cat': 'chat',
                  'dog': 'chien',
                  'horse': 'cheval'
                  }
    words = ['cat', 'lion', 'horse']
    for word in words:
        if word in dictionary:
            print(dictionary[word])
        else:
            print("Not in the dictionary")


find_french_word()


# this program creates students average scores

student_dictionary = {}
while True:
    name = input("Enter student's name:")
    if name == '':
        break
    score = int(input("Enter student's score (1-10):"))
    if score < 1 or score > 10:
        break

    if name in student_dictionary:
        student_dictionary[name] += [score]
    else:
        student_dictionary[name] = [score]
print(student_dictionary)

for name in sorted(student_dictionary.keys()):
    sum = 0
    counter = 0
    for score in student_dictionary[name]:
        sum += score
        counter += 1
    print(sum, counter)
    average = sum / counter
    print(name, "average score:", average)

d1 = {'Adam Smith': 'A', 'Judy Paxton': 'B+'}
d2 = {'Mary Louis': 'A', 'Patrick White': 'C'}
d3 = {}

d3.update(d1)
d3.update(d2)

print(d3)
    

