#Q.1- Name and handle the exception occured in the following program:

a=3
try:
    if a<4:
        a=a/(a-3)
except ZeroDivisionError :
    print("divide by zero error")
else:
     print(a)


#Q.2- Name and handle the exception occurred in the following program:
#            l=[1,2,3]
#            print(l[3])

l = [1,2,3]
try:
    print(l[3])
except IndexError:
    print("index is out of range nothing to do with it")


#Q.3- What will be the output of the following code:

try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print ("An exception")


#Q.4- What will be the output of the following code:

 # Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)

#output>>>>>>>>>>>>>>
#-5.0
#a/b result in 0


#Q.5- Write a program to show and handle following exceptions:
#1. Import Error
#2. Value Error
#3. Index Error




list1 = list(range(0,6))

try:
    import  cfgh
    inp = int(input("Enter Value :"))
    print(list1[5])
except ImportError:
    print(" not detected")
except ValueError:
    print("Only Integers")
except IndexError:
    print("out of range ")
except a:
    print(a)
else:
    print(" cfgh is completed!")



#Q6.  Q.6- Create a user-defined exception
#  AgeTooSmallError() that warns the user
# when they have entered age less than 18.
#  The code must keep taking input till
# the user enters the appropriate.




class AgeError(ValueError):
    pass


def inputHandling():
    while True:
        try:
            age = int(input("Enter Your Age:"))
            if age<18:
                raise  AgeError
            else:
                print("Auth To Vote")
                break
        except AgeError:
            print("Age is Too Small to Vote")

inputHandling()
