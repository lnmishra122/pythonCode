from datetime import date
class person:
    def __init__(self,name,age):
        self.name= name
        self.age= age

    @classmethod

    def fromBirthyear(cls,name,year):
        return cls(name,date.today().year-year)

    @staticmethod

    def isAdult(age):
        return age>18
person1=person('rahul',25)
person2=person.fromBirthyear('anton',1995)

print person1.age
print person2.age

print person.isAdult(17)
