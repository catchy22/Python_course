#####task 1

import numpy as np
import re

a=sorted(np.random.random(10))

print('\n',a,'\n')


#####task 2

a=np.array([[1,0],[0,1]])
b=np.tile(a,(4,4))

print('\n',b,'\n')


#####task 3

a=np.full((8,4),2)
b=np.full((4,2),5)

print('\nresult:\n',np.matmul(a,b))


#####task 4

a=(np.random.random(10))

print('\n',a,'\n')

#####task 5

def task5(a):

    fac_list=[]
    x=0
    for i in range(2,a):
        if a%i==0:
            fac_list.append([i,int(a/i)])
    l=len(fac_list)
    if l!=0:
        print(f'множители:{fac_list}')
        for i in range(0, l):
            print(f'\nматрица {i+1}:\n')
            print(np.random.randint(0,100,(fac_list[i][0],fac_list[i][1])))
            # print(fac_list[1])
    else:
        print('число нельзя разбить на множители без остатка')

task5(20)

#####task 6
class analysis:

    def __init__(self,file_path):
        self.file_path=file_path
        self.file_array=None

    def read_file(self):
        self.file_array=np.genfromtxt(self.file_path,delimiter=';',dtype=str)
        return self.file_array

    def file_search(self,pattern):
        r=re.findall(rf'\{pattern}',str(self.file_array))
        print('\n',r)


a=analysis('conn_names5.csv')
a.read_file()
a.file_search('d{5}')
a.file_search('d{2}\w{5}')


#####task 7

def task7(a,s,last=False):
    b=np.random.randint(1,20,(s,a.size))
    global c
    c=np.matmul(b,a)

    if last==False:
        res=np.sin(c)
    else:
        res = np.maximum(0,c)
    print('\n\nрандомная матрица:\n\n',b)
    print('\n\nрезультирующий массив\n\n',res)
    return (c)

c=None
x=5
a=np.random.randint(1,20,(x,1))
#i
task7(a,10)

#ii
task7(c,10)

#iii
task7(c,5,True)