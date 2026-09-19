# i will  revise of strings function , then  i will do some project on conditional statment 
 
#1 INDEXING[this is your to get the position of the character ]
name=str(input("enter your name "))
character= name[4]
print("4th position character= ",character) # indexing always count from 0.

#2 slicing[its basically cut the string and we can get the desired code ]
dna=str(input("write the sequence of dna,i will cut from 1-6 position"))
code=dna[0:6]
print("this is a slice of string",code)

#3 len[to get the length of string]
name=str(input("Enter your first name "))
a=len(name)
print("The lenght of name is",a) 


#4 now we will do project using conditional statement 
colour=str(input("Enter the colour of traffic light= "))
if (colour=="red"):
    print("STOP the vehical")

elif (colour=="yellow"):
    print("wait for green signal to go")

elif(colour=="green"):
    print("GO you can run your vehical")

else:
    print("the light is broken")


 #5WAP to check if a no. entered by the user is odd or even.
numb=int(input("enter the number- "))
if numb%2==0:
    print("this is even number ",numb)
else:
    print("this is odd number ",numb)

#6 WAP to find the greatest of 3 no. netered by the user .
a= int(input('enter 1 no.-'))
b= int(input("enter 2 no.-"))
c= int(input("enter 3 no.-"))

if a>=b and a>=c:
 if b>=c:
     print(a,b,c)
 else:
    print(a,c,b)

elif b>a>c:
   if a>c:
    print(b,a,c)
   else:
     print(b,c,a)

else:
  if c>a>b:
    print(c,a,b)
  else:
   print(c,b,a)

# 7 WAP to check is a number is a multiple of 7 or not.
a = int(input("write a number so that i will search it is divisible by 7 or not-"))
if a%7==0:
    print(a,"-this is divisible  by 7")

else:
    print(a,"-not divisible by 7")


