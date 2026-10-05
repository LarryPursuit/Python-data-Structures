# This module contains operations related to sets.

def unique_majors(student_list):
    """
    Return a set of unique student majors using set comprehension.
    Extract the major field from each student record.
    """
    # A set automatically discards duplicate majors.
    return {major for _, _, major in student_list}
