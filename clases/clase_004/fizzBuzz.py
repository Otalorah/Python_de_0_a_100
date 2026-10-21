n = int(input("Digite un numero: "))
if n == 0:
    print("digite un numero mayor a 0")
else:
    a = 0
    b = 1
    print("los primeros ", n, " numeros de fibonacci son")
    for _ in range(n):
        print(a)

        suma = a + b
        a = b
        b = suma


n = int(input("Ingrese el número de términos de la serie Fibonacci: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
