class Person:

    def __init__(self,name,gender):
        self.name = name
        self.gender = gender
p1 = Person('Qudsia','female')
p2 = Person('Muqadsa','female')
p3 = Person('ALi','male')

#list

list1 = [p1,p2,p3]#if you do this the adress will be stored
print(list1)

list2 = [p1.name,p2.name,p3.name]
print(list2)

list3 = [p1.gender,p2.gender,p3.gender]
print(list3)


#ab agar lsit ha to list wlay function bhi laga sakty ah

for i in list1:
    print(i.name,i.gender)

#dictionary

dict = {'p1':p1,'p2':p2,'p3':p3}#if you do this the adress will be stored
print(dict)

for i in dict:
    print(i)

for i in dict:
  print(dict[i].name)
