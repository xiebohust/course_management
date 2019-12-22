

"""
创建北京、上海 2 所学校
创建linux , python , go 3个课程，linux py在北京开， go 在上海开
课程包含，周期，价格，通过学校创建课程
通过学校创建班级，班级关联课程、讲师
创建学员时，选择学校，关联班级
创建讲师角色时要关联学校，
提供两个角色接口
7.1. 学员视图，可以注册，交学费，选择班级，
7.2. 讲师视图，讲师可管理自己的班级，上课时选择班级，查看班级学员列表，修改所管理的学员的成绩
7.3. 管理视图，创建讲师，创建班级，创建课程
上面的操作产生的数据都通过pickle序列化保存到文件里
"""

import pickle
import os
from config import setting
from src import identifier


class BaseModel:
    db_path = ''

    def save(self):
        nid = str(self.nid)
        path = os.path.join(self.db_path, nid)
        f = open(path,'wb')
        pickle.dump(self,f)


    @classmethod
    def get_all(cls):
        l = []
        for item in os.listdir(cls.db_path):
            f = open(os.path.join(cls.db_path,item),'rb')
            obj = pickle.load(f)
            l.append(obj)
        return l

    def __str__(self):
        return self.name

    def login(self):
        pass


class Admin(BaseModel):
    db_path = setting.ADMIN_DB

    def __init__(self,user,password):
        self.user = user
        self.password = password
        self.nid = identifier.AdminNid(Admin.db_path)

    @staticmethod
    def login(user,pwd):
        pass


class School(BaseModel):
    db_path = setting.SCHOOL_DB

    def __init__(self,name):
        self.name = name
        self.income = 0
        self.nid = identifier.SchoolNid(School.db_path)




class Teacher(BaseModel):
    db_path = setting.TEACHER_DB

    def __init__(self,name,level):
        self.name = name
        self.level = level
        self.nid = identifier.TeacherNid(Teacher.db_path)


class Course(BaseModel):
    db_path = setting.COURSE_DB

    def __init__(self,name,price,period,school_id):
        self.name = name
        self.price = price
        self.period = period
        self.school_id = school_id
        self.nid = identifier.CourseNid(Course.db_path)


class CourseToTeacher(BaseModel):
    db_path = setting.COURSE_TO_TEACHER_DB

    def __init__(self,course_id,teacher_id):
        self.course_id = course_id
        self.teacher_id = teacher_id
        self.nid = identifier.CourseToTeacherNid(CourseToTeacher.db_path)


class Classes(BaseModel):
    db_path = setting.CLASSES_DB

    def __init__(self,name,tuition,school_id,course_to_teacher_list):
        self.name = name
        self.tuition = tuition
        self.course_to_teacher_list = course_to_teacher_list
        self.school_id = school_id
        self.nid = identifier.ClassesNid(Classes.db_path)

class Score:
    def __init__(self,student_id):
        self.student_id = student_id
        self.score_dict = {}

    def set(self,course_to_teacher_nid, number):
        self.score_dict[course_to_teacher_nid] = number

    def get(self,course_to_teacher_nid):
        return self.score_dict.get(course_to_teacher_nid, None)
        # return self.score_dict[course_to_teacher_nid]

class Student(BaseModel):
    db_path = setting.STUDENT_DB

    def __init__(self, name, age, classes_id):
        self.name = name
        self.age = age
        self.classes_id = classes_id
        self.nid = identifier.StudentNid(Student.db_path)
        self.score = Score(self.nid)








if __name__ == '__main__':
    for i in School.get_all():
        print(str(i))