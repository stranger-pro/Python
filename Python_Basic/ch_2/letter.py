letter = '''Dear <Name>
You Are Selected
<Date> '''

name = input("Enter Name : ")
date = input("Enter Date : ")


new_letter = letter.replace("<Date>",date)
org_letter = new_letter.replace("<Name>",name)

print(org_letter)