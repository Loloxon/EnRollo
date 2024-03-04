import random

from converter import printer

div = 10
student_size = 160 // div
topic_size = 100 // div
student_wants_arr = []
for student in range(student_size):
    pref_no = random.randint(2, 5)
    arr = []
    for pref in range(pref_no):
        arr.append(random.randint(1, topic_size))
    student_wants_arr.append(arr)

single_topics_ids = []
for topic in range(topic_size):
    if random.randint(0, 100) < 20:
        single_topics_ids.append(topic+1)

# print(student_wants_arr)
# print(single_topics_ids)

printer(student_size, topic_size, single_topics_ids, student_wants_arr)

# print("n_students =", student_size, end=";\n")
# print("n_topics =", topic_size, end=";\n")
#
#
# print("single_topics_ids = {", end="")
#
# for i, pref in enumerate(single_topics_ids):
#     print(pref, end="")
#
#     if i < len(single_topics_ids) - 1:
#         print(",", end="")
# print("};")
#
# print("student_wants_list = [", end="")
# for student in range(student_size):
#     print("{", end="")
#     for i, pref in enumerate(student_wants_arr[student]):
#         print(pref, end="")
#
#         if i < len(student_wants_arr[student]) - 1:
#             print(",", end="")
#
#     if student<student_size-1:
#         print("},", end="")
#     else:
#         print("}", end="")
# print("];")
