# file= open("file.txt")
# data=file.read()
# print(data)
# file.close()

# file= open("file.txt", encoding="utf-8")
# data=file.readlines()
# print(data)
# file.close()

# file= open("file.txt", encoding="utf-8")
# lst=[]
# for line in file:
#     lst.append(int(line))
#     print(summ(lst))

# file= open("file.txt", "w", encoding="utf-8")
# file.write("Hello, world!")
# file.close()
# import json
# a={"x":123}
# file= open("file.txt", "w", encoding="utf-8")
# a= json.load(file)
# print(a)
# file.close()

# file= open("file.txt", "a", encoding="utf-8")
# file.write("\nHello, world!")
# file.close()

# Открываем файл для записи
file = open("nums.txt", "w")

# Записываем целые числа от 1 до 20
for num in range(1, 21):
    file.write(str(num) + "\n")

# Закрываем файл
file.close()
