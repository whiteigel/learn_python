zodiac = [
['Овен','March',21,'April',19],
['Телец','April',20,'May',20],
['Близнецы','May',21,'June',21],
['Рак','June',22,'July',22],
['Лев','July',23,'August',22],
['Дева','August',23,'September',22],
['Весы','September',23,'October',23],
['Скорпион','October',24,'November',21],
['Стрелец','November',22,'December',21],
['Козерог','December',22,'January',19],
['Водолей','January',20,'February',18],
['Рыбы','February',19,'March',20]
]

month = input('Enter birth month: ')
day = int(input('Enter birth date: '))

# comment

for sign in zodiac:
  if sign[1] == month and day >= sign[2] or sign[3] == month and day <= sign[4]:
    print('You zodiac sign is', sign[0])