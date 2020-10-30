n=1
suma_p=0
suma_n=0
nr_p=0
nr_n=0
while n<=12:
    t=eval(input("Dati temperaturile "))
    if t>=0:
        suma_p+=t
        nr_p+=1
    if t<0:
        suma_n+=t
        nr_n+=1
    n+=1
suma_med_p=suma_p/nr_p
print('Media anuala a temperaturilor pozitive =',suma_med_p)
suma_med_n=suma_n/nr_n
print('Media anuala a temperaturilor negative =',suma_med_n)