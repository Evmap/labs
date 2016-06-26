from zope import interface, component
from Student import Student

class IStudents(interface.Interface):

    def add(name, faculty, course):
        """Add student to list"""

    def delete(name):
        """Delete student from list"""

class Students:
    interface.implements(IStudents)
    def __init__(self):
        self.slist = []
        
    def add(self, name, faculty, course):
        self.slist.append(Student(name, faculty, course))
        return True

    def find(self, name):
        for var in self.slist:
            if var.name == name:
                return var
            
    def delete(self, name):
        self.slist.remove(self.find(name))
        return True
