n = int(input("Enter A Number : "))

# for i in range(n):
#     for j in range((n-1)-(i),0,-1):
#         print(" ",end="")
#     for j in range(0,2*i+1):
#         print("*",end="")
#     print("\n")

for i in range(n):
    print(" "*(n-i+1),end="")
    print("*"*(2*i+1),end="")
    print("")