class teacher:
    def __init__(self):
        self.stud_number=0
    def teach(self,mat_name,*args):
        for student_person in args:
            student_person.take(mat_name)
            self.stud_number+=1

class student:
    def __init__(self):
        knowledge = []
        self.knowledge = knowledge

    def take(self, knowledge_string):
        if knowledge_string not in self.knowledge:
            self.knowledge.append(knowledge_string)

class study_mat:
    def __init__(self, *args):
        self.materials = list(args)

    def output(self,mat_id):
        return self.materials[mat_id]

materials=study_mat('Python','Version Control Systems','Relational Databases','NoSQL databases','Message Brokers')
t1=teacher()
st1=student()
st2=student()
st3=student()
st4=student()

t1.teach(materials.output(0),st1,st3)
t1.teach(materials.output(1),st2,st4)
t1.teach(materials.output(2),st1,st3,st2)
t1.teach(materials.output(3),st3,st2)
t1.teach(materials.output(4),st1,st2,st3)

print('student 1 knows',', '.join(st1.knowledge))
print('student 2 knows',', '.join(st2.knowledge))
print('student 3 knows',', '.join(st3.knowledge))
print('student 4 knows',', '.join(st4.knowledge))
