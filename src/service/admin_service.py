import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
)

from src import models
print(models.School.get_all())

menu = """
1.创建学校
2.查看学校
3.创建班级
4.查看班级
5.创建课程
6.查看课程
"""

def create_school():
    name = input('input school name:')
    obj_school = models.School(name)
    obj_school.save()

def get_school_list():
    for i in models.School.get_all():
        print(str(i))




def create_class():
    list_school = ''
    school_name = input('choose school name:')
    if school_name in list_school:
        school_id = str(models.School(school_name).nid)
        name = input('input class name:')
        tuition = input('tuition:')

        course_to_teacher_list = input('course_to_teacher_list')
        obj_school = models.Classes(name=name, tuition=tuition,school_id=school_id,course_to_teacher_list=course_to_teacher_list)
        obj_school.save()
    else:
        print('学校不存在')

def get_class_list():
    for obj_sch in models.Classes.get_all():
        print(str(obj_sch))


def create_course():
    name = input('input class name:')
    tuition = input('tuition:')
    school_id = input('school')
    course_to_teacher_list = input('')
    obj_school = models.Classes(name=name, tuition=tuition,school_id=school_id,course_to_teacher_list=course_to_teacher_list)
    obj_school.save()

def get_course_list():
    for obj_sch in models.Course.get_all():
        print(str(obj_sch))

action_list = {
    '1':create_school,
    '2':get_school_list,
    '3':create_class,
    '4':get_class_list,
    '5':create_course,
    '6':get_course_list
}


def main():
    while True:
        print(menu)
        action = input('choose action:')
        if action in action_list:
            action_list[action]()





if __name__ == "__main__":
    main()
