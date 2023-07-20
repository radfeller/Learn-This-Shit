import random
print("Привет, пользователь! Тебе необходимо угадать число, которое я загадал.")


def main():
    while True:
        random_int = random.randint(1,10)
        print("Придумал число! Угадай!")
        otv = int(input())
        if otv == random_int:
            print("Ты молодец! Возьми с полки огурец!")
            break
        else:
            print("Дебил тупой блять иди нахуй!")




if __name__ == "__main__":
    main()
else:
    print("Вы пытаетесь запустить не основной модуль")
