import math


def sum_nathurale(n):
    sum = 0
    for i in range(0, n, 1):
        if i % 5 == 0 or i % 3 == 0:
            sum += i
    return sum


def palindrom_cheak(string):
    i = 0
    verdikt = 0
    while i < (len(string) / 2):
        if (string[i] == string[-(i + 1)]):

            verdikt = 1
        else:
            verdikt = 0
            break
        i = i + 1
    return verdikt


# print("palindrom_cheak "+str(palindrom_cheak(str(990025))))


def palindrom_search(num_1, num_2):
    value1 = num_1
    value2 = num_1
    value0 = 0
    flag = 0
    i = 0
    palindrom = 0
    while value1 != num_2:
        value2 = num_1
        while value2 != num_2:
            value0 = value1 * value2
            if palindrom_cheak(str(value0)) == 1 and value0 > palindrom:
                palindrom = value0
            value2 = value2 + 1
        value1 = value1 + 1

    print(value1)
    print(value2)
    print(palindrom)
    return str(palindrom)


# print(palindrom_search(100,999))


def series_Fibonachi(numberelement):
    i = 2
    a1 = 1
    a2 = 2
    a3 = 0
    while i < numberelement:
        a3 = a1 + a2
        a1 = a2
        a2 = a3
        i = i + 1
    return a3


# print(problem_nomber7(10001))

def problems_seven(numbers):
    i = 12
    mas_num = [2, 3, 5, 7, 11]
    while len(mas_num) < numbers:
        j = 0
        i += 1
        # print(i)
        flag = True
        while j < len(mas_num):
            if i % mas_num[j] == 0:
                flag = False
            j += 1
        if flag == True:
            mas_num.extend([i])
            print("element nomer# " + str(len(mas_num)) + "i=" + str(i))


def problems_sevens(numbers):
    i = 5
    num = 12
    mas_num = [2, 3, 5, 7, 11]
    while i < numbers:
        j = 0
        num += 1
        # print(i)
        flag = True
        if i < int(numbers / 10):
            while j < len(mas_num):
                if num % mas_num[j] == 0:
                    flag = False
                j += 1
            if flag == True:
                mas_num.extend([i])
                print("element nomer# " + str(len(mas_num)) + "i=" + str(i))
                i += 1
        else:
            flag = True
            while j < len(mas_num):
                if num % mas_num[j] == 0:
                    flag = False
                j += 1
            if flag == True:
                i += 1
                print("element nomer# " + str(i) + "i=" + str(num))


# problems_sevens(10001)



def PifagorTripel(number):
    a = 0
    while a < number:
        a = a + 1
        b = 0
        while b < number:
            b = b + 1
            c = a ** 2 + b ** 2
            c = math.sqrt(c)
            if c - int(c) == 0:
                if a + b + c == 1000:
                    print(a, b, c)
                    print(a * b * c)


# PifagorTripel(1000)

