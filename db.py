import random
import string
import names
import pandas as pd


def generate_students():
    students = set()
    years = ["Freshman", "Sophomore", "Junior", "Senior"]
    for i in range(100000):
        id_ = i
        name = names.get_first_name()
        year = years[random.randint(0, 3)]
        gpa = 2.3 * random.random() + 2
        student = (id_, name, year, gpa)
        students.add(student)
    return students


def genrate_courses():
    subjects = [
        "MATH", "PHYS", "CS", "ECON", "ORIE", "BIO", "ENGL", "HIST", "GERM",
        "CHEM", "GEOG", "INFO", "ART", "BCS", "ECE", "PMA", "GOVT", "HD",
        "PSYCH", "ILR", "HADM", "AEM", "MUSIC", "PE", "LAW", "PHIL", "NBA",
        "SOC"
    ]
    classes = set()
    final_classes = []
    for sub in subjects:
        for i in range(1000):
            code = random.randint(1000, 5000)
            class_ = sub + str(code)
            classes.add(class_)
    classes = list(classes)
    for i in range(len(classes)):
        id_ = i
        credits_ = random.randint(3, 5)
        final_classes.append((id_, classes[i], credits_))
    return final_classes


def generate_join_table(students, classes):
    join = set()
    for i in range(50000):
        student_id = random.randint(0, len(students) - 1)
        class_id = random.randint(0, len(classes) - 1)
        join_ = (student_id, class_id)
        join.add(join_)
    return list(join)


students = generate_students()
courses = genrate_courses()
join = generate_join_table(students, courses)
df = pd.DataFrame(students, columns=["id", "name", "year", "gpa"])
df2 = pd.DataFrame(courses, columns=["id", "class_name", "credits"])
df3 = pd.DataFrame(join, columns=["student_id", "course_id"])
df.to_csv("./data/students.csv")
df2.to_csv("./data/courses.csv")
df3.to_csv("./data/student_courses.csv")