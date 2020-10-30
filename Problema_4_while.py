  
a=eval(input("Introduceti un nr "))
x=1
suma=0
p=1
while x<=a:
    p*=x
    suma+=x
    x+=1

print("Suma nr este ", suma )
print("Produsul nr este ", p)
print("Media aritmetica a nr este ",suma/a)