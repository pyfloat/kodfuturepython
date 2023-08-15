# numbers=[]
# for _ in range(10):
#     num =int(input())
#     numbers.append(num)
def show_info(numbers):
    print(f"Сумма:{sum(numbers)}")
    print(f"Среднее арифметическое:{sum(numbers)/len(numbers)}")
    print(f"Максимальное значение:{max(numbers)}")
    print(f"Минимальное значение:{min(numbers)}")

numbers= [int(input())for _ in range(10)]
show_info(numbers)