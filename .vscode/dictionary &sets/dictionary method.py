myDict = {
    "Fast": "In a Quick manner",
    "Harry": "A Coder",
    "Marks": [1, 2, 3, 4],
    "anotherDict": {'Harry': 'player'},
    1:3
}
# PRINTS THE KEYS OF DICTIONARY
# DICTIONARY METHOD

# print(myDict.keys())
# print(type(myDict.keys()))
print(list(myDict.keys()))
print(list(myDict.values()))
print(list(myDict.items()))#print the (key ,value) for all contents of dictionary
print(myDict)#if we want to update "myDict", we can use this method
updateDict = {
     "Lovish": "Friend",
     "Shubhm": "Friend",
     "Divya": "Friend",
     "Harry": "Dancer"
}
myDict.update(updateDict)#updates the dictonary by adding with key value value pairs from updateDict
print(myDict)
print(myDict.get("Harry"))# print value associated with key "Harry"
print(myDict["Harry"])# print value associated with key "Harry"

# The differnce between .get and [] syntax in Dictionaries?

print(myDict.get("Harry2"))#retruns none  as Harry2 is not present Dictionary
print(myDict["Harry2"])#throwns an error as Harry2 is not present Dictionary