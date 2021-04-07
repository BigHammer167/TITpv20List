spisok=[] #пустой список
numbers=[1,2,3,4,5]
abc=["Abc","B","C"]
slovo="Programmeerimine" #текст
slovo_list=list(slovo.lower()) #проеобразовал все буквы в маленькими
slovo.split()
print(slovo)
print(slovo_list)
while True:
    print("1-добавить букву в список")
    print("2-склеить списки\n3-добавить бкуву на i - позиция")
    print("4-удалить элемент\n5-удалить элемент указав его порядковый номер")
    print("6-удалить  позицию элемента\n7-перевернуть список")
    valik=int(input())
    if valik==1:
        a=input("Введи букву")
        slovo_list.append(a) # - Добавляет элемент в конец списка 
        print(f"Добавили {a} новый список",slovo_list)
        a="".join(slovo_list)
        print(a.replace("eerimine","mnoe obespesenie")) # Функция меняет "eerimine" на "mnoe obespesenie" в итого получается совсем другое слово
    elif valik==2:
        slovo_list.extend(abc) # - Расширяет список list, добавляя в конец все элементы списка abc
        print(slovo_list)
    elif valik==3:
        a=input("Введите букву, которую хочешь добавить")
        i=int(input("Введите номер позиции, куда хочешь добавить букву"))
        slovo_list.insert(i-1,a) #0,1,2... list.insert(i-1,a) - Вставляет на i-ый элемент значение a
        print(slovo_list)
        print("Слово состоит из букв" if a.isalpha() else "Слово не состоит из букв")   # Проверяет состоит ли слово из букв
        print("Слово начинается с большой буквы" if a.istitle() else "Слово не начинается с большой буквы") # Проверяет не начинается ли слово с большой буквы
        print("Все буквы в нижнем регистре" if a.islower() else "Одна из букв в верхнем регистре")   # Проверяет состоит ли все буквы в верхнем регистре
        print("Все буквы в верхнем регистре" if a.isupper() else "Одна из букв в нижнем регистре")   # Проверяет состоит ли все буквы в нижнем регистре
        print("Строка не состоит из неотображаемых символов" if a.isspace() else "Строка состоит из неотрображаемых символов")   #Проверяет состоит ли строка из неотображаемых символов
    elif valik==4:
        a=input("Введите букву, которую хочешь удалить")
        n=slovo_list.count(a)
        print(ord(a[0])) # Выдает код первой буквы со строки
        if n>0:
            for i in range(n):
                slovo_list.remove(a) # - Удаляет первый элемент в списке, имеющий значение a
        else:
            print("Искомой буквы нет")
            print(slovo_list)
    elif valik==5:
        i=int(input("Введите номер позиции элемента для удаления"))
        n=len(slovo_list) #n=10,i=9
        if i<n:
            slovo_list.pop(i) # - Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент
            print(slovo_list)
            a="".join(slovo_list) 
        else:
            print("Букв меньше, чем указаная позиция")
    elif valik==6:
        a=input("Введи букву,позицию которую хочешь узнать")
        i=slovo_list.index(a) #проверка если буквы нет
        print(f"Элемент {a} стоит на {i+1}-ом месте ")
        print(" _ ".join(slovo_list)) # Добавляет между буквами  нижнее подчёркивание
    elif valik==7:
        slovo_list.reverse() # - Разворачивает список 
        print(slovo_list)
        
       
        

