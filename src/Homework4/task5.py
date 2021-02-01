number_of_students = int(input())
one_student_language = set()
all_student_language = set()
common_student_language = set()
for students in range(number_of_students):
    number_of_languages = int(input())
    student_languages = {input() for _ in range(number_of_languages)}
    all_student_language.update(student_languages)
    if not students:
        common_student_language |= student_languages
        one_student_language |= student_languages
    else:
        common_student_language &= student_languages
        one_student_language ^= student_languages
one_student_language = one_student_language - common_student_language
print(common_student_language)
print(one_student_language)
