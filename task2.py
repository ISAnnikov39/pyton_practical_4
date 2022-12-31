#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


n = int (input("введите число "))

def Prime_factors(n):
    for i in range(2, n+1):
        if n%i ==0:
            n= n//i
            print(i)
            return Prime_factors(n)

Prime_factors(n)
        



