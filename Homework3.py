# Dima Pilipenka
# Date: 12/10/2024
# Description: Homework 3
# Grodno IT Academy Python 3.10

#1
    # Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
    #Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
    #Входные данные - строка из чисел, разделенная пробелами.
    #Выходные данные - количество пар.
    #Важно: `1 1 1` - это 3 пары, `1 1 1 1` - это 6 пар.
    
def pairs(numbers_string):
    # Преобразуем строку в список чисел
    numbers = list(map(int, numbers_string.split()))
    
    # Создаем словарь для подсчета вхождений каждого числа
    count = {}
    for number in numbers:
        if number in count:
            count[number] += 1
        else:
            count[number] = 1
    
    # Считаем количество пар
    total_pairs = 0
    for num, cnt in count.items():
        if cnt > 1:
            total_pairs += cnt * (cnt - 1) // 2  # Формула для сочетаний C(n, 2)
    
    return total_pairs

# Пример использования
input_string = "1 1 1 1"
print(pairs(input_string))  # Вывод: 6

    

#2
def uniques(array):
    #Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
    #Элементы нужно выводить в том порядке, в котором они встречаются в списке.
    return uniques

def uniques(array):
    # Создаем словарь для подсчета вхождений элементов
    count = {}
    
    # Подсчитываем количество вхождений каждого элемента
    for item in array:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
            
    # Извлекаем элементы, которые встречаются только один раз
    result = [item for item in array if count[item] == 1]
    
    return result

# Пример использования
my_list = [1, 2, 2, 3, 4, 4, 5]
print(uniques(my_list))  # Вывод: [1, 3, 5]



#3
def ordered_list(array):
    # Дан список целых чисел. Требуется переместить все ненулевые элементы в левую часть списка,
    # не меняя их порядок, а все нули - в правую часть. Порядок ненулевых элементов изменять нельзя,
    # дополнительный список использовать нельзя, задачу нужно выполнить за один проход по списку.
    # Верните полученный список.
    return array



def ordered_list(array):
    # Указатель на позицию для ненулевого элемента
    non_zero_index = 0
    
    # Проходим по всем элементам списка
    for i in range(len(array)):
        if array[i] != 0:
            # Если элемент ненулевой, перемещаем его в позицию non_zero_index
            array[non_zero_index] = array[i]
            non_zero_index += 1
            
    # Заполняем оставшуюся часть списка нулями
    for i in range(non_zero_index, len(array)):
        array[i] = 0
    
    return array

# Пример использования
my_list = [0, 1, 0, 3, 12]
print(ordered_list(my_list))  # Вывод: [1, 3, 12, 0, 0]



#4
    #Возмите кортеж `('a', 'b', 'c')`, И сделайте из него список.

def tuple_to_list(in_tuple):
    # Преобразуем кортеж в список
    lst = list(in_tuple)
    return lst

# Пример использования
my_tuple = ('a', 'b', 'c')
print(tuple_to_list(my_tuple))  # Вывод: ['a', 'b', 'c']


#4/1
def euclid(a,b):
    #Даны два натуральных числа. Вычислите их наибольший общий делитель при помощи алгоритма Евклида (мы не знаем функции и рекурсию). can't call itself
    return ...

def euclid(a, b):
    while b != 0:
        a, b = b, a % b  # Обмен значениями: b становится a % b, а a становится b
    return a

# Пример использования
num1 = 48
num2 = 18
print(euclid(num1, num2))  # Вывод: 6


#5
#Dictionaries
def cities(input_string):
    #Дан список стран и городов каждой страны. Затем даны названия городов. Для каждого города укажите, в какой стране он находится.
    #Учтите, что бывают ситуации когда город с таким называнием бывает в разных странах (Брест есть в Беларуси и Франции).
    #Входные данные
    #Программа получает на вход количество стран N. Далее идет N строк, каждая строка начинается с названия страны, затем идут названия городов этой страны.
    #В следующей строке записано число M, далее идут M запросов — названия каких-то M городов, перечисленных выше.
    #Выходные данные
    #Для каждого из запроса выведите название страны, в котором находится данный город.
    #Пример данных:
    #Входные данные
    #2
    #Russia Moscow Petersburg Novgorod Kaluga
    #Ukraine Kiev Lvov Odessa
    #3
    #Odessa
    #Moscow
    #Novgorod
    #Выходные данные
    #Ukraine
    #Russia
    #Russia
    #input_string = "2\nRussia Moscow Petersburg Novgorod Kaluga\nUkraine Kiev Lvov Odessa\n3\nOdessa\nMoscow\nNovgorod"
    #output_string = 'Ukraine\nRussia\nRussia'
    #country_map={}

    return input_string

def cities(input_string):
    # Разделяем входные данные на строки
    lines = input_string.strip().split('\n')
    
    # Читаем количество стран
    n = int(lines[0])
    
                
# Словарь для хранения городов и соответствующих стран
    country_map = {}
    
    # Читаем данные о странах и городах
    for i in range(1, n + 1):
        parts = lines[i].split()
        country = parts[0]
        cities = parts[1:]
        
        for city in cities:
            if city not in country_map:
                country_map[city] = []
            country_map[city].append(country)
    
    # Читаем количество запросов
    m = int(lines[n + 1])
    
    # Результирующий список для хранения ответов
    result = []
    
    # Обрабатываем запросы
    for i in range(n + 2, n + 2 + m):
        city_query = lines[i].strip()
        if city_query in country_map:
            # Берем первую страну из списка (по заданию не указано, как обрабатывать несколько стран)
            result.append(country_map[city_query][0])
        else:
            result.append("Unknown")  # Если город не найден
    
    return '\n'.join(result)

# Пример 
input_string = "2\nRussia Moscow Petersburg Novgorod Kaluga\nUkraine Kiev Lvov Odessa\n3\nOdessa\nMoscow\nNovgorod"
output_string = cities(input_string)
print(output_string)  # Вывод: 'Ukraine\nRussia\nRussia'



#6

#Sets
def languages(input_string):
    #Задачи для домашней работы
    #Языки
    #Каждый из N школьников некоторой школы знает Mi языков. Определите, какие языки знают все школьники и языки, которые знает хотя бы один из школьников.
    #Входные данные
    #Первая строка входных данных содержит количество школьников N. Далее идет N чисел Mi, после каждого из чисел идет Mi строк, содержащих названия языков, которые знает i-й школьник.
    #Пример входных данных:
    #3 # N количество школьников
    #2 # M1 количество языков первого школьника
    #Russian # языки первого школьника
    #English
    #3 # M2 количество языков второго школьника
    #Russian
    #Belarusian
    #English
    #3
    #Russian
    #Italian
    #French
    #Выходные данные
    #В первой строке выведите количество языков, которые знают все школьники. Начиная со второй строки - список таких языков.
    #Затем - количество языков, которые знает хотя бы один школьник, на следующих строках - список таких языков.
    #input_string = "3\n2\nRussian\nEnglish\n3\nRussian\nBelarusian\nEnglish\n3\nRussian\nItalian\nFrench"
    #output_string = '1\nRussian\n5\nRussian\nFrench\nItalian\nEnglish\nBelarusian'

    return input_string

def languages(input_string):
    # Разбиваем входные данные на строки
    lines = input_string.strip().split('\n')
    
    # Читаем количество школьников
    n = int(lines[0])
    
    # Множество для языков, которые знают все школьники
    common_languages = None
    # Множество для языков, которые знает хотя бы один школьник
    all_languages = set()
    
    # Читаем языки для каждого школьника
    index = 1
    for _ in range(n):
        m_i = int(lines[index])  # Читаем количество языков для i-го школьника
        index += 1
        # Множество для языков текущего школьника
        student_languages = set()
        
        for _ in range(m_i):
            language = lines[index].strip()
            student_languages.add(language)
            all_languages.add(language)  # Добавляем язык в общее множество
            index += 1
        
        # Находим общие языки
        if common_languages is None:
            common_languages = student_languages
        else:
            common_languages.intersection_update(student_languages)
    
    # Подготовка к выводу
    common_languages = sorted(common_languages) if common_languages else []
    all_languages = sorted(all_languages)
    
    # Формируем результат
    result = []
    result.append(str(len(common_languages)))
    result.extend(common_languages)
    result.append(str(len(all_languages)))
    result.extend(all_languages)
    
    return '\n'.join(result)

# Пример использования
input_string = "3\n2\nRussian\nEnglish\n3\nRussian\nBelarusian\nEnglish\n3\nRussian\nItalian\nFrench"
output_string = languages(input_string)
print(output_string)  # Вывод: '1\nRussian\n5\nRussian\nBelarusian\nEnglish\nFrench\nItalian'


#7

#Generators
def list_gen(arr1, arr2):
    #Генераторы списков
    #Используйте генератор списков чтобы получить следующий: ['xy', 'xz', 'xv', 'yy', 'yz', 'yv']. из ['x','y'] & ['y','z','v']
    #пример:
    return result

def list_gen(arr1, arr2):
    # Генераторы списков
    result = [a + b for a in arr1 for b in arr2]
    return result

# Пример использования
arr1 = ['x', 'y']
arr2 = ['y', 'z', 'v']
result = list_gen(arr1, arr2)
print(result)  # Вывод: ['xy', 'xz', 'xv', 'yy', 'yz', 'yv']


#8

#Генераторы словарей
def dict_gen(N):
    #Создайте словарь с помощью генератора словарей, так чтобы его ключами были числа от 1 до N, а значениями кубы этих чисел.
    return result

def dict_gen(N):
    # Генератор словарей
    result = {i: i**3 for i in range(1, N + 1)}
    return result

# Пример использования
N = 5
result = dict_gen(N)
print(result)  # Вывод: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}


#9
#Кортежи
def multiplication_table(N):
    #Создайте генератор, который возвращает строки таблицы умножения от 0 до заданного числа.
    return table


def multiplication_table(N):
    # Создаем генератор, который возвращает строки таблицы умножения от 0 до N
    for i in range(N + 1):
        yield ' '.join(f"{i} x {j} = {i * j}" for j in range(N + 1))

# Пример использования
N = 5
for line in multiplication_table(N):
    print(line)

        