
print ('Введите три числа типа int')
a = int(input('Первое число: '))
b = int(input('Второе число: '))
c = int(input('Третье число: '))

if a and b and c !=0:
    print('Нет нулевых значений!!!')

if a != 0:
    print (a)
elif b != 0:
    print (b)
elif c != 0:
    print (c)
else:
    print ("Ненулевых значений нет!")

if a > (b+c):
    print(a - b - c)
elif a < (b+c):
    print(b + c - a)

if a > 50 and (b > a or c > a):
    print('Вася')

if a > 5 or (b == 7 and c == 7):
    print('Петя')



#Калькулятор BMI fdff

name = str(input('Введите имя:'))
age = int(input('Введите возраст:'))
height = float(input('Введите рост в метрах:'))
weight = float(input('Введите вес в кг:'))

#Рассчет BMI

bmi = round(weight / height**2, 1)

#Вывод
print('Уважаемая(й) {}'. format(name),'\n','Ваш возраст: {}'. format(age),'\n', \
    'Ваш рост: {}'.format(height),'\n','Ваш вес: {}'. format(weight),'\n','Ваш BMI: {}'. format(bmi))

if bmi <= 17.5:
    print('Анорексия. Риск для здоровья выскоий. Рекомендуется повышение веса.')
    print(bmi,'____17.5__________________________________40')
elif bmi >= 17.6 and bmi <= 25.9:
    print('Норма. Риска для здоровья нет.')
    print('17.5_____',bmi,'_____________________________40')
elif bmi >= 26 and bmi <= 27.9:
    print('Избыток веса. Риск для здоровья повышенный. Рекомендуется похудение.')
    print('17.5____________',bmi,'______________________40')
elif bmi >= 28 and bmi <= 30.9:
    print('Ожирение I степени. Риск для здоровья повышенный. Рекомендуется снижение массы тела.')
    print('17.5__________________',bmi,'________________40')
elif bmi >= 31 and bmi <= 35.9:
    print('Ожирение II степени. Риск для здоровья высокий. Настоятельно рекомендуется снижение массы тела.')
    print('17.5_______________________',bmi,'___________40')
elif bmi >= 36 and bmi <= 40.9:
    print('Ожирение III степени. Риск для здоровья очень выскоий. Настоятельно рекомендуется снижение массы тела.')
    print('17.5______________________________',bmi,'____40')
else:
    print('Ожирение IV степени. Риск для здоровья чрезвычайно высокий. Необходимо немедленное снижение массы тела.')
    print('17.5__________________________________40______',bmi)