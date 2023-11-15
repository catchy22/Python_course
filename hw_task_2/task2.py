def number_1(inp_string):
    stop_list=['Python','php','go','C']
    out_string=[]

    string_old = inp_string.split(' ')
    for word in string_old:
        if word not in stop_list:
            out_string.append(word)
    return ' '.join(out_string)

print(number_1('my C cat go C tastes like php Python Pepsi Cola go'))


######number_2
i=3
numbers_list=[12,7,14,9.0,6,5]

print(list(filter(lambda x:x%i==0,numbers_list)))


def number_3(*args):

    return tuple(filter(lambda x:isinstance(x,str),args))

print(number_3('a',3,True,'cat','in',67,'a hat'))


def number_4(list_1,list_2):
    result = []
    for x in list_1:
        if x in list_2:
            result.append(x)
    return result


list_1=[7,'aaa','17',2023,False,16,4,2,5]
list_2=[0,17,'aaaa',5,2,2023,True,'7',2023,False]

print(number_4(list_1,list_2))


def number_6(func):
    def find_except(*args):
        try:
           value=func(*args)
           if type(value)!=int:
               raise ValueError
        except ValueError:
            print(func.__name__,'содержит не int величину - ',value)

    return find_except


@number_6
def number_6a(a):
    return a/2

number_6a(8)

@number_6
def number_6b(a):
    return a+2

number_6b(8)


def number_7(func):
    def wrapper(*args):
        try:
            print(func(*args))
        except Exception as err:
            print(f"произошла ошибка {err}, перезапускаем")
            try:
                print(func(*args))
            except:
                print("ошибка сама по себе не исчезла")

    return wrapper

@number_7
def number_7a(*args):
    return list(map(lambda x:4/x,args))

number_7a(3,2,0,1)

@number_7
def number_7b(*args):
    return list(map(lambda x:4/x,args))

number_7b(3,22,1)


######number_8:
elements = [(2, 12, "Mg"), (1, 11, "Na"), (1, 3, "Li"), (2, 4, "Be")]

print(sorted(elements,key=lambda x:x[1]))

######number 9:

import time

def number_9(func):
    def wrapper(*args):
        start_time = time.time()
        func(*args)
        end_time=time.time()
        print(f'время выполнения декорируемой функции = {end_time-start_time} c')

    return wrapper

@number_9
def number_9a(a,b):
    sum=0
    for i in range(a**b):
        sum+=i
    print(sum)

number_9a(7,8)

@number_9
def number_9b(a,b):
    sum=0
    for i in range(b**a):
        sum+=i
    print(sum)

number_9b(5,12)

