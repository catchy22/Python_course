
def number_1(string):
    s=''    #создание пустой строковой переменной
    return len(string)  #возврат результата вычисления длины строки

print(number_1('this is a test string'))  #печать результата вычисления длины строки

def number_2(list_1,list_2):
    if len(list_1)>len(list_2):
        return(len(list_1))
    elif len(list_1)<len(list_2):
        return(len(list_2))
    else:
        return('самого длинного списка нет')

print(number_2([0,1,3,1,22,'m'],[1,1,1,1,1,1,1]))
print(number_2([0,1,3,1,22,'m',7],[1,1,1,1,1,1,1]))



def number_3(list,value):
    list.append(value)
    return(list)

print(number_3([0,1,1,1,0,0,1],1))
print(number_3(['hell'],'o'))


def number_4(value):
    if value>100 or value<-100:
        print('-')
    else:
        print('+')

number_4(40)
number_4(400)
number_4(-400)



def number_5():
    str_1 = 'test'
    str_2 = 'test1'
    if str_1 in str_2:
        print('ДА')
    else:
        print('НЕТ')

number_5()


def number_6(list):
    positive_value=[]
    for value in list:
        if value >= 0:
            positive_value.append(value)
    print(len(positive_value))

number_6([1,-3,4,-10,-5])
number_6([11,-33,-14,10,25])


def number_7(year,month):
    if month <=12:
        print(year*12*29+month*29)
    else:
        print('error')

number_7(0,1)
number_7(0,2)
number_7(1,14)
number_7(1,10)



def number_8(string):
    string_new=''
    try:
        string_old=string.split(' ')
        for word in string_old:
          string_new+=word[0]
        print(string_new)
    except AttributeError:
        print('wrong data type')

number_8('wake up grab a brush and put a little makeup')
number_8(816)


def number_9(value):
    factorial = 1
    while value > 1:
        factorial *= value
        value -= 1
    return factorial

print(number_9(2))
print(number_9(5))
print(number_9(10))
