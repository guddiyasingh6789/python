myDict={
    
    "pankha":"fan",
    "vathu":"item",
    "klm":"pen"
}
print("options are",myDict.keys())
a = input("enter the hindi word\n")
# print("the meaning of your word is:",myDict[a])

#Below line will not throw an error if the key is not present in the dictionary 
print("the meaning of your word is:",myDict.get(a))
