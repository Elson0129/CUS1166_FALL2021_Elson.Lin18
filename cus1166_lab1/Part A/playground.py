print("Hello World\n")

print("Practicing Variables")
myVar = 1
print(f"Variable myVar : {myVar} is an {type(myVar)}")

print("\nPracticing with Python User Input")
myName = input("What is your name? ")
print("Hello %s" % myName)

print("\nPracticing with variable initialization")
i = 120
print(f"Value of variable i: {i}")
f = 1.6180339
print(f"Variable f has a value of {f} and is of type {type(f)}")
b = True
print(f"Value of variable b: {b}")
n = None
print(f"Value of variable n: {n}")

# tuple
c = (10, 20, 10)
print(f"c[0] has a value of {c[0]} and c is of type: {type(c)}")

print("\nCollections")
# list
l = ["Anna", "Tom", "John"]
l = [10, 20, 30]
print(f"l[0] has the value of {l[0]} and l is of type {type(l)}")

# sets
s = set()
s.add(1)
s.add(4)
s.add(6)
print(s)

# dictionary
grades = {"Tom" : "A", "Mark" : "B-"}
grades["Tom"]
grades["Anna"] = "F"

#initialize dictionary
myDictionary = dict()

print("\nConditional Statements")
x = 10
if (x > 0):
    print("X is positive")
elif(x < 0):
    print("X is negative")
else:
    print("Value of X is 0")

print("\nLoops")
for i in range(5):
    print(i)

for i_idx, i_value in enumerate(range(2,10)):
    print(f"{i_idx} - {i_value}" )

print("\nFunctions")
def isEven(x):
    if(x % 2) == 0:
        return True
    else:
        return False

testNums = [11, 34, 73]
print("Sample array: ")
print(*testNums)

for i in testNums:

    if(isEven(i) == True):
        print(f"{i} is even")
    else:
        print(f"{i} is odd")

print("\nClasses")
class Book:
    def _init_(self, title="Software Engineering", isbn=""):
        self.title = title
        self.isbn = isbn

    def printBook(self):
        print(self.title + ", " + self.isbn)
