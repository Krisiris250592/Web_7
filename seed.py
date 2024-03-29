from datetime import date, datetime, timedelta
from random import randint, choice
import faker
from sqlalchemy import select

from db.models import Teacher, Student, Discipline, Grade, Group
from db.db import session


def date_range(start: date, end: date) -> list:
    result = []
    current_date = start
    while current_date <= end:
        if current_date.isoweekday() < 6:
            result.append(current_date)
        current_date += timedelta(1)
    return result

def fill_data():
    disciplines = [
        'Python',
        'SQL',
        'Dart',
        'JAVA',
        'C++',
        'C#',
        'Swift'
    ]

    groups = ['A-1', 'B-2', 'C-3']

    fake = faker.Faker('uk_UA')
    number_of_teachers = 5
    number_of_students = 50

    def seed_teachers():
        for _ in range(number_of_teachers):
            teacher = Teacher(first_name=fake.first_name(), last_name=fake.last_name())
            session.add(teacher)
        session.commit()

    def seed_disciplines():
        teacher_ids = session.scalars(select(Teacher.id)).all()
        for discipline in disciplines:
            session.add(Discipline(name=discipline, teacher_id=choice(teacher_ids)))
        session.commit()

    def seed_groups():
        for group in groups:
            session.add(Group(name=group))
        session.commit()

    def seed_students():
        group_ids = session.scalars(select(Group.id)).all()
        for _ in range(number_of_students):
            student = Student(first_name=fake.name(), group_id=choice(group_ids))
            session.add(student)
        session.commit()

    def seed_grades():
        start_date = datetime.strptime("2024-01-02", "%Y-%m-%d")
        end_date = datetime.strptime("2024-02-20", "%Y-%m-%d")
        d_range = date_range(start=start_date, end=end_date)
        discipline_ids = session.scalars(select(Discipline.id)).all()
        student_ids = session.scalars(select(Student.id)).all()

        for d in d_range:
            random_id_discipline = choice(discipline_ids)
            random_ids_student = [choice(student_ids) for _ in range(5)]
            for student_id in random_ids_student:
                grade = Grade(
                    grade=randint(1, 12),
                    date_of=d,
                    student_id=student_id,
                    discipline_id=random_id_discipline,
                )
                session.add(grade)
        session.commit()

    seed_teachers()
    seed_disciplines()
    seed_groups()
    seed_students()
    seed_grades()


if __name__ == "__main__":
    fill_data()
