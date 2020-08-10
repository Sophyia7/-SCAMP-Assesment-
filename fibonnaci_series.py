while True:
    print()
    fib=int(input("Enter the number:"))
    n1=0
    n2=1
    count=0
    while(count<fib):
            print(n1, end=",")
            nth=n1+n2
            n1=n2
            n2=nth
            count+=1

           
