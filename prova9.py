l=[1, 2, [2,3], "hola"]
lf = ["a", 2, [2,3], "hola"]
l[3] = "hala"
#print(l[::-1])
for e in l:
    print(e)
for i in range(l):
    print(e)
for i, e in enumerate(l):
    print("la posicio {} te el valor {}".format(i, e))
    if e == 1 or e == "1":
        l[1] = "a"
for e in l:
    print(e)

