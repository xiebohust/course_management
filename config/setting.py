import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ADMIN_DB = os.path.join(BASE_DIR,'db','admin')
SCHOOL_DB = os.path.join(BASE_DIR,'db','school')
TEACHER_DB = os.path.join(BASE_DIR,'db','teacher')
COURSE_TO_TEACHER_DB = os.path.join(BASE_DIR,'db','course_to_teacher')
COURSE_DB = os.path.join(BASE_DIR,'db','course')
CLASSES_DB = os.path.join(BASE_DIR,'db','classes')
STUDENT_DB = os.path.join(BASE_DIR,'db','student')
SCORE_DB = os.path.join(BASE_DIR,'db','score')






if __name__ == "__main__":
    print(BASE_DIR)
    print(db_path)