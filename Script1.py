try:
    true: bool = True
    while true:
        print('Введите "+" для добавления данных и "-" для завершения')
        check: str = input()
        if check == '-':
            print("Пока")
            raise SystemExit
        elif check == '+':
            print('Введите фамилию, имя, отчество (если нету отчества то "-") и год рождения:')
            surname, name, patronymic, year = map(str, input().split())
            if name.isdigit() != true:
                if surname.isdigit() != true:
                    if (patronymic.isdigit() != true) or (patronymic == '-'):
                        if (year.isdigit() == true) and (len(year) == 4):
                            with open('test.txt', 'a') as file:
                                file.write(f'\n{surname}'f'   {name}'f'   {patronymic}'f'   {year}')
                            print('Данные записаны')
                        else:
                            print("Неверный ввод года рождения")
                    else:
                        print("Неверный ввод отчества")
                else:
                    print("Неверный ввод фамилии")
            else:
                print("Неверный ввод имени")
        else:
            print("Неверный ввод")
except ValueError:
    print("Неверный ввод данных")
except PermissionError:
    print("Не хватает прав доступа")
except Exception:
    print("Что-то пошло не так...")
except KeyboardInterrupt:
    print("Что-то пошло не так...")