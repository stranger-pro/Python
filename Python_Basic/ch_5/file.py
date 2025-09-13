import json

def load():
    try:
        with open("file.txt","r") as file:
            return json.load(file)
    except:
        return []

def push(detail):
    data= load()
    data.append(detail)
    with open("file.txt","w") as file:
        json.dump(data,file)

def input_d():
    name = input("Enter Name : ")
    village = input("Enter Village : ")
    detail = {"name":name,"village":village}
    push(detail)

def output():
    details = load()
    print("\n")
    if not details:
        print("Empty !")
    else:
        for i ,d in enumerate(details):
            print(f"{i} : [ {d["name"]} : {d["village"]} ]")
        print("\n") 

def delete(num):
    data=load()
    data.remove(data[num])
    with open("file.txt","w") as file:
        json.dump(data,file)


while(True):
    print("1 For input ")
    print("2 For output ")
    print("3 For delete")

    num = int(input("Choose A Number : "))

    match num:
        case 1:
            input_d()
        case 2:
            output()
        case 3:
            num = int(input("Enter Index : "))
            delete(num)
        case _:
            break