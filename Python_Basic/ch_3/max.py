# list = []
max_n = float('-inf')
for i in range(4):
    number = int(input("Enter A Number : "))
    max_n = max(number, max_n)

# num = max(list)

print(f"Max Number : {max_n}")