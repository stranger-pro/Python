import random as rd
import string as s

letters_num = rd.randint(4,6)
name = ""
for i in range(letters_num):
    l =  rd.choice(['a','e','g','h','i','l','n','o','p','r','s','u'])
    name += l

name = name.capitalize()

print(name)