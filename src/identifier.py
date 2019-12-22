import os
from lib import commons
import pickle

class Nid:
    def __init__(self,role,db_path):
        role_list = [
            'admin','school','teacher','course','classes',
            'student','course_to_teacher'
        ]
        if role not in role_list:
            print('wrong')
        else:
            self.role = role
            self.uuid = commons.create_uuid()
            self.db_path = db_path

    def __str__(self):
        return self.uuid

    def get_obj_by_uuid(self):
        for name in os.listdir(os.path.join(self.db_path)):
            if name == self.uuid:
                return pickle.load(open(os.path.join(self.db_path,self.uuid),'rb'))


class AdminNid(Nid):
    def __init__(self, db_path):
        super(AdminNid, self).__init__('admin',db_path)


class SchoolNid(Nid):
    def __init__(self, db_path):
        super(SchoolNid, self).__init__('school',db_path)

class TeacherNid(Nid):
    def __init__(self, db_path):
        super(TeacherNid, self).__init__('teacher', db_path)


class CourseNid(Nid):
    def __init__(self, db_path):
        super(CourseNid, self).__init__('course', db_path)

class CourseToTeacherNid(Nid):
    def __init__(self, db_path):
        super(CourseToTeacherNid, self).__init__('course_to_teacher', db_path)



class ClassesNid(Nid):
    def __init__(self, db_path):
        super(ClassesNid, self).__init__('classes', db_path)



class StudentNid(Nid):
    def __init__(self, db_path):
        super(StudentNid, self).__init__('student', db_path)


if __name__ == '__main__':
    a = Nid('admin','aa')
    print(str(a))