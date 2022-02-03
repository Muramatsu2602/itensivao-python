qnt=0
total=0
while True:
    try:
        goesIn = input("Enter a number: ")
        if goesIn == "done":
            break
        num = float(goesIn)

        qnt+=1
        total+=num        
    except: 
        print("bad data")

avg = total/qnt
print(total, qnt, avg) #  same as in C: printf("%d %d %d",total, qnt, avg);