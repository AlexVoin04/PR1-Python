try:
    with open('test.txt', 'r') as file:
        print('Фамилия   Имя   Отчество   Дата рождения')
        while True:
            line = file.readline()
            if not line:
                break
            print(line.strip())
except Exception:
    print("Что-то пошло не так...")