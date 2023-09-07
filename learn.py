                                        #Basics
print("Hello World")
                                      #Conditions


                                        #Loops

#ForEach
fruits=["apple", "apple2", "apple3"]
for fruit in fruits:
    if fruit == "apple":
        print(fruit)

for fruit in fruits:
    print(fruit)
    if fruit == "apple2":
        break 

for fruit in fruits:
    if fruit == "apple2":
        continue 
    print(fruit)

#Range    
for x in range(6):
    print(x+1)

for x in range(2,6):
    print(x+1)   

for x in range(8):
  if x == 3 or x == 2:
      continue
  print(x) 
else:
    print("Finished!")    

colours = ["red","blue","yellow"]
cars = ["nissan", "tesla", "peugot"]

for x in colours:
    for y in cars: 
        print(x,y)
#While 

i=0
while (i<5):
    print(i)
    i=i+1

#WhileElse
i=0
while (i<5):
    if i%2 == 0:
        print(i)
        i=i+1
    else:
        i=i+1

                                      #Functions 

def print_hello():
    print("Hello from here")

def print_numbers():
    print("Here are your numbers")
    for x in range(5):
        print(x)

def passingFunction(fname):
    print(fname + " Welcome to the program")
    
def passing2Function(fname, lname):
    print(fname + " " + lname + " Welcome to the program")
    
def my_names(*names):
    for name in names:
        print(name)

def my_specified_names(name1, name2, name3):
        print(name1, name2, name3)

def my_function(**kid):
  print("His last name is " + kid["lname"] + " and " + kid["fname"])

def default_names(country = "Scotland"):
    print("I am from " + country)

my_function(fname = "Tobias", lname = "Refsnes")

print_hello()

print_numbers()

passingFunction("Emily")

passing2Function("Emily","Herron")

my_names("Emily", "Hans", "John")

my_specified_names(name3 ="Emily", name2 ="Hans", name1 ="Aysha")

default_names("Sweden")

default_names("Brazil")

def pass_list(list):
    for x in list:
        print(x)

pass_list(["apple", "banana"])

def get_back(x):
    return 5 * x

print(get_back(10))

def recursion(x):
    
        if x > 5 :
            print(x)
            x = x -1
            recursion(x)
          
        else:
            print("too small")
            x = x -1
            if x > 0:
                recursion(x)

recursion(10)
    
        

