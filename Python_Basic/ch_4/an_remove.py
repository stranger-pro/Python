def remov(list,word):
    l = []
    for i in list:
        if(word!=i):
            l.append(i.strip(word))
    return l


l = ["Aditya","Rahul","Ankit","Aanya","Arpit","Ankita","Ziya"]

p = remov(l,"Ziya")
print(p)