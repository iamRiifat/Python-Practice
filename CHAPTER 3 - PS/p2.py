#Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
name=input()
date=input()
print(letter.replace("<|Name|>",name).replace("<|Date|>",date))