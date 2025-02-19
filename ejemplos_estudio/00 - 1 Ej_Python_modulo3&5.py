#00 - 1 Ej_Python_
# Write a function fizz_buzz_sum to find the sum of all multiples of 3 or 5 below a target value.

# For example, if the target value was 10, the multiples of 3 or 5 below 10 are 3, 5, 6, and 9.
# Because 3+5+6+9=23, 3+5+6+9=23, our function would return 23

def fizz_buzz_sum (n):
    sum = 0
    for i in range(n):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i 
            print("por ahora: ", sum)
    return sum

print(fizz_buzz_sum(10))
# Esta solucion sirve, pero a medida que aumento n, se demora mas la solución.

def sum_mult (n, x):
    #primero se debe encontrar la cantidad de numeros que son multiplos de "n" menores que "x"
    p = (x - 1 )//n
    print(f"Los multiplos de {n} menores a {x} son:", [x for x in range(n,x,n)])
    sum = n*p*(p+1)//2
    return sum

print(sum_mult(3,10)+sum_mult(5,10)-sum_mult(15,10))
#def sum_mult_2 (x):
#    return sum_mult(3,x)+sum_mult(5,x)-sum_mult(15,x)

#print(sum_mult_2(10))
