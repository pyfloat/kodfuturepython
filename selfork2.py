# file =open('file.txt', 'w', encoding='utf-8')
# for i in range (1,21):
#     file.write(f'{i}\n')
# file.close()
# file =open('file.txt', 'w+', encoding='utf-8')
# file.seek(10)
# for i in file:
#     print(i)
# file.close()
secret_number = 4  
user_number = int(input("Угадай число от 1 до 10: "))  

if user_number == secret_number:
    print("Ты отгадал!")
elif user_number < secret_number:
    print("Мое число больше!")
else:
    print("Мое число меньше!")
