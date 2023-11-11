#important : this syntax will creat an dicationary and not an empty set
a={}
print(type(a))

#An empty set can be created using the below syntax
b= set()
print(type(b))

#adding the value in empty set
b.add(4)
b.add(5)
b.add(6)
# we can't add list in set
# b.add([1,2,3])
print(b)
print(len(b))# we can print length in set
# b.remove(6)
# print(b.pop())
b.clear()#clear the set b
print(b)