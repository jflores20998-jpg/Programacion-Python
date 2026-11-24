x = input("intro la paraula")
sum_a=0
for c in x:
    if c=="a":
        sum_a=sum_a+1
    elif c=="m":
        sum_m=sum_m+1
    else:
        sum_altres=sum_altres+1
    print("la paraula {} te {} as {} ms i {} d altres caracteres".format(x, str(sum_a), str(sum_m), str(sum_altres)))
