import random
class person:
    def __init__(self,fio,age,sex):
        self.fio=fio
        self.age=age
        self.sex=sex

    def info(self):
        print('ФИО',self.fio)
        print('возраст',self.age)
        print('пол',self.sex)


class teacher(person):
    def __init__(self,fio,age,sex):
        super().__init__(fio,age,sex)
        self.stud_number=0
    def teach(self,mat_name,*args):
        for student_person in args:
            student_person.take(mat_name)
            self.stud_number+=1

class student(person):
    def __init__(self,fio,age,sex):
        super().__init__(fio, age, sex)
        knowledge = []
        self.knowledge = knowledge

    def __len__(self):
        return len(self.knowledge)

    def take(self, knowledge_string):
        if knowledge_string not in self.knowledge:
            self.knowledge.append(knowledge_string)

    def forget(self):
        x=random.randint(0,len(self.knowledge))
        y=random.randint(0,len(self.knowledge))
        if x<y:
            del self.knowledge[x:y]
        elif x>=y:
            del self.knowledge[y:x]
        if len(self.knowledge)==0:
            self.knowledge.append('nothing')


class study_mat:
    def __init__(self, *args):
        self.materials = list(args)
    def __len__(self):
        return len((self.materials))

    def output(self,mat_id):
        return self.materials[mat_id]

materials=study_mat('Python','Version Control Systems','Relational Databases','NoSQL databases','Message Brokers')
t1=teacher('Гречкин Федор Антонович',41,'М')
st1=student('Иванов Антуан Ренатович',14,'М')
st2=student('Сидоров Петр Федорович',21,'М')
st3=student('Петрова Анна Вячеславовна',19,'М')
st4=student('Шевченко Илья Васильевич',38,'М')

t1.teach(materials.output(0),st1,st3)
t1.teach(materials.output(1),st2,st4)
t1.teach(materials.output(2),st1,st3,st2)
t1.teach(materials.output(3),st3,st2)
t1.teach(materials.output(4),st1,st2,st3)

print('student 1 knows',', '.join(st1.knowledge))
print('student 2 knows',', '.join(st2.knowledge))
print('student 3 knows',', '.join(st3.knowledge))
print('student 4 knows',', '.join(st4.knowledge))
print('\n')


t1.info()
st3.info()


print('\n')

st1.forget()
st2.forget()

print('student 1 knows',', '.join(st1.knowledge), 'after vacation')
print('student 2 knows',', '.join(st2.knowledge), 'after vacation')

print('\n')
print('кол-во знаний студента 2 -', len(st2.knowledge))
print('кол-во материалов', len(materials))
