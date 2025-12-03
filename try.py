def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(2))

def arbol(n):
    for i in range(1,n+1):
        for j in range(i):
            print("*", end="")
        print()
arbol(5)

def ordenado(lista):
    minimo=0
    for num in lista:
        if num>=minimo:
            return "la lista esta ordenada"
        else:
            return "la lista no esta ordenada"     
print(ordenado([1,2,3]))

def producto(lista):
    total=1
    for i in lista:
        total*=i
    return total
print(producto([1,2,3]))

def mayus(lista):
    total_mayus = 0
    total_minus = 0
    for palabra in lista:
        for letra in palabra:
            if letra.isupper():
                total_mayus += 1
            elif letra.islower():
                total_minus += 1
    return total_mayus, total_minus

print(mayus(["paTATa", "Oro"]))  


    

