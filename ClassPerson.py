class Person:
    name = ''
    age = 0
    country = ''

    #construct method
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    #method
    def greet (self):
        print('hello my name is {}'.format(self.name))

    def despedir (self):
        print('bye : {}'.format(self.name))

    def buy(self, element):
        self.greet()
        print('Puedo comprar un {}'.format(element))
        self.despedir()

class Student(Person):
    colegio = ''
    def __init__(self,colegio,name,country,age):
        Person.__init__(self,name,country,age)
        self.colegio = colegio

    def get_colegio(self):
        print("mi colegio es: {}".format(self.colegio))






class University(Student):
    program = ''
    def __init__(self,colegio,name,country,age,program):
        Student.__init__(self,colegio,name,country,age)
        self.program = program

    def get_program(self):
        print('mi programa es: {}'.format(self.program))



class Cargo:
    nombreCargo = ''
    def __init__(self,nombreCargo):
        self.nombreCargo = nombreCargo

    def get_NombreCargo(self):
        print('su cargo es: {}'.format(self.nombreCargo))



class Trabajador(Person,Cargo):
    sueldo = 0

    def __init__(self,name, age, country, nombreCargo, sueldo ):
        Person.__init__(self,name, age, country)
        Cargo.__init__(self,nombreCargo)
        self.sueldo = sueldo

    def get_sueldo(self):
        print("su salario es: {}".format(self.sueldo))




santiago = Person('santiago',25,'colombia')
santiago.buy('carro')
print()


estudiante = Student('ccp','estudiante','colombia',18)
estudiante.get_colegio()
print()

cesmag = University('colegio','Santigo','Colombia',25,'sistemas')
cesmag.get_colegio()
cesmag.get_program()
print()

diana = Trabajador ('diana',28,'colombia','docente',1234)
diana.get_sueldo()
diana.get_NombreCargo()
