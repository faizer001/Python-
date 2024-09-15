num = int(input("Display multiplication table of? "))
for i in range(1, num+1):
    for j in range (1,11):
        print(i, 'x', j, '=', j*i) 
    print(" ")