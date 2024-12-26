class Teacher:
    def __init__(self, first_name: str, last_name: str, age: int, email:str, assigned_subjects: set[str]):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.assigned_subjects = assigned_subjects

def create_schedule(subjects, teachers):
    uncovered_elements = subjects.copy()

    result = []

    while uncovered_elements:
        current_subj_len = 0
        current_age = 0
        current_subset = []
        current_teacher = None
        for teacher in teachers:
            teachers_list = Teacher(*teacher)
            if current_subj_len == 0:
                current_subj_len = len(set(subjects) - set(teachers_list.assigned_subjects))
                current_age = teachers_list.age
                current_subset = teachers_list.assigned_subjects
                current_teacher = teacher
            if 0 < len(set(subjects) - set(teachers_list.assigned_subjects)) < current_subj_len:
                current_subj_len = len(teachers_list.assigned_subjects)
                current_age = teachers_list.age
                current_subset = teachers_list.assigned_subjects
                current_teacher = teacher
            elif (len(set(subjects) - set(teachers_list.assigned_subjects)) > 0 and
                  len(set(subjects) - set(teachers_list.assigned_subjects)) == current_subj_len):
                if teachers_list.age < current_age:
                    current_subj_len = len(teachers_list.assigned_subjects)
                    current_age = teachers_list.age
                    current_subset = teachers_list.assigned_subjects
                    current_teacher = teacher

        if current_teacher != () and current_teacher is not None:
            teachers.remove(current_teacher)
            uncovered_elements -= current_subset
            result.append(Teacher(*current_teacher))

    return result



if __name__ == '__main__':
    # Множина предметів
    subjects = {'Математика', 'Фізика', 'Хімія', 'Інформатика', 'Біологія'}
    # Створення списку викладачів
    teachers = [('Олександр', 'Іваненко', 45, 'o.ivanenko@example.com', {'Математика', 'Фізика'}),
                ('Марія', 'Петренко', 38, 'm.petrenko@example.com', {'Хімія'}),
                ('Сергій', 'Коваленко', 50, 's.kovalenko@example.com', {'Інформатика', 'Математика'}),
                ('Наталія', 'Шевченко', 29, 'n.shevchenko@example.com', {'Біологія', 'Хімія'}),
                ('Дмитро', 'Бондаренко', 35, 'd.bondarenko@example.com', {'Фізика', 'Інформатика'}),
                ('Олена', 'Гриценко', 42, 'o.grytsenko@example.com', {'Біологія'})
                ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}")
            print(f"   Викладає предмети: {', '.join(teacher.assigned_subjects)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
