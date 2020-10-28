#1 - Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
line = "www.my_site.com#about"
line = line.replace('#', '/')
print(line)

#2 - Напишите программу, которая добавляет ‘ing’ к словам
msg = "This is a test msg"
arr = msg.split(" ")
i = "ing"
arr2 = (arr[0] + i) + (arr[1] + i) + (arr[2] + i) + (arr[3] + i) + (arr[4] + i)
arr2 = arr2.replace('ng', 'ng ')
print(arr2)

#3 - В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
stroka = 'Ivan Ivanou'
stroka = stroka.split(' ')
stroka = stroka[::-1]
stroka = ' '.join(stroka)
print(stroka)

#4 - Напишите программу которая удаляет пробел в начале, в конце строки
liniya = ' probel v nachale i v konce '
liniya2 = liniya.strip()
print(liniya2)
