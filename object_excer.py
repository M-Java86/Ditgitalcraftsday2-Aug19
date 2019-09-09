class Person:
    def __init__(self, name, email, phone, friends):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = friends

def greet(self, other_person):
    return 'Hello {}, I am {}!'.format(other_person.name, self.name)

sonny = Person ('Sonny','sonny@hotmail.com','483-485-4948',[])
jordan = Person ('Jordan','jordan@aol.com','495-586-3456',[])

#Adding
print(sonny.greet(jordan))