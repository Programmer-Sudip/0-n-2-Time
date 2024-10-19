def ONSquareTime(n):
    iterations = 0
    for i in range(0,n):
        for j in range(0,n):
            print("*", end ="")
            iterations += 1
        print("")
    print("\nWhen n is ",n," Iterations",iterations,"\n")

ONSquareTime(5)
ONSquareTime(4)
ONSquareTime(3)

print("\nWith every ',n', the time taken equals  n^2")
print("0(n^2)")