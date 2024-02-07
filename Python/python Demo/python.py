#Hello World:

print("Hello World")
print("Welcome To Prasanth")
a=55
b=50
d=a+b
print(d)

#Operators:

a=int(input("Enter Value A :"))
b=int(input("Enter Value B :"))
c=int(input("Enter Value C :"))
print("Your Value A Is     :",a)
print("Your Value B Is     :",b)
print("Your Value C Is     :",c)
print("Your Answer Is      :",a+b-c)

#If In Condition Using:

if a>b :
    print("A greter Than B")
else :
    print("B greter Than A")

#If Shoutcut Usings:

print("A greter Than B") if a>b else print("B greter Than A")

print("A greter Than B") if a>b else print("A And B Is Equal") if a==b else print("B greter Than A")

#If AND OR Condition Using:

if a>b and c>d :
    print("Both Condition Same")
if a>b or c>d :
    print("Any Condtion is True")


#Concatinate:
First_name=input("Enter Your First_name :")
Last_name=input("Enter Your Last_name   :")
print("Your First_name :",First_name)
print("Your Last_name  :",Last_name)
print(First_name + " " + Last_name)

#Tesing Usge String:
print(First_name.strip())
print(First_name.upper())
print(Last_name.lower())
print(First_name.title())
print(First_name.replace("S","p"))

#format string:
name = "Saranya"
product = "Smart watch"
cost = 1500
myorder ="Hey {} your order {} purchase and pay the {}."
print(myorder.format(name,product,cost))

