# numbers=[]
# for _ in range(10):
#     num =int(input())
#     numbers.append(num)
# def show_info(numbers):
#     print(f"Сумма:{sum(numbers)}")
#     print(f"Среднее арифметическое:{sum(numbers)/len(numbers):.2f}")
#     print(f"Максимальное значение:{max(numbers)}")
#     print(f"Минимальное значение:{min(numbers)}")

# numbers= [int(input())for _ in range(10)]
# show_info(numbers)


# def sum_of_digits(number):
#     number_str = str(number)
#     sum_digits = 0
#     for digit in number_str:
#         sum_digits += int(digit)
#     print("Сумма цифр в числе:", sum_digits)
# number = int(input("Введите натуральное число: "))
# sum_of_digits(number)
# def sum_of_digits(num):
#     s=[int(i) for i in str(num)]

# num=int(input())
# summa=sum_of_digits(num)
# print(summa)
# print("Hello, World", sep=",,,", end="!!!")

# def func(n):
#     return n if n<2 else func(n//2)+func(n%2)
# count=0
# for i in range(2**30):
#     if func(i)==27:
#         count+=1
# print(count)