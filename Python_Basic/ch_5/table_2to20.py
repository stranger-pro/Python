def table(n):
    table=""
    for i in range(1,11):
        table += f"{i} * {n} = {i*n} \n"
    with open(f"tables/table_{n}.txt","w") as a:
        a.write(table)

for i in range(2,21):
    table(i)