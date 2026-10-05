# This module contains functions to lazily generate student data.

def student_generator(student_list, major):
    """
    Generate student records filtered by major lazily for memory efficiency
    using a Python generator.
    """
    # Parentheses (not brackets) create a generator expression: students are
    # yielded one at a time on demand instead of building a full list.
    return (
        student for student in student_list
        if student[2].casefold() == major.casefold()
    )
