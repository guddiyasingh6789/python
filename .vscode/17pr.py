letter = '''Dear <|NAME|>,
Greeting coding  abc house i am happy to tell you  about your selsction
you are selected!
have a greet day ahead
thanks and regards,
Billo
            Date: <|DATE|>
 '''
name =  input("Enter your name\n")
date =  input("Enter Date\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)