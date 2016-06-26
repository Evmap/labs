from zope import interface, component
import unittest
from Student import Student
from IStudents import IStudents, Students

component.provideUtility(Students())
maths = component.getUtility(IStudents)

class TestStudent(unittest.TestCase):

    def setUp(self):
        self.St1 = Student("Dima", "IMEI", 1)
        self.St2 = Student("Vasya", "Physics", 3)
        
    def test_init(self):
        self.assertEqual((self.St1.name, self.St1.faculty, self.St1.course), ("Dima", "IMEI", 1))
        self.assertEqual((self.St2.name, self.St2.faculty, self.St2.course), ("Vasya", "Physics", 3))

    def test_Add(self):
        self.assertTrue(maths.add("Dima", "IMEI", 1))
        self.assertEqual(maths.slist[0].name, "Dima")

    def test_Delete(self):
        self.assertTrue(maths.delete("Dima"))
        self.assertEqual(maths.slist, [])        
            
if __name__ == '__main__':
    unittest.main()
