x=0
suma=0
while not((x%2!=0) and (x%3==0)):
    x=eval(input("Introduceti un nr "))
    if x%2==0:
        suma+=x

print("Suma nr este ", suma)