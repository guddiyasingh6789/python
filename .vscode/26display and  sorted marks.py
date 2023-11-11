m1=input("Enter marks for student number 1: ")
m2=input("Enter marks for student number 2: ")
m3=input("Enter marks for student number 3: ")
m4=input("Enter marks for student number 4: ")
m5=input("Enter marks for student number 5: ")
m6=input("Enter marks for student number 6: ")

mylist=[m1,m2,m3,m4,m5,m6]
mylist.sort()
print(mylist)


# 2. QUESTION
# CHECK THAT A TUPLE CAN'NT BE CHANGED IN PYTHON
a=(1,2,3,4,5)
a[0]=34
print(a[0])