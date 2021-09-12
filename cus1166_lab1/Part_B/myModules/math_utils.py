def average_grade(roster):
    total = 0

    for student in roster:
        total += student.get_grade()

    return total/len(roster)
