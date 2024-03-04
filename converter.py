def get_ID_and_pref():
    preferences = open('preferences.txt', 'r', encoding="utf-8")
    n_students = 0
    student_wants_arr = []
    while True:
        content = preferences.readline()
        if not content:
            break
        n_students += 1
        content = content.split("\t")
        content[-1] = content[-1][:-1]
        del content[0]
        del content[0]
        del content[0]
        if len(content) > 0:
            content = content[0].split(", ")
            content = list(map(int, content))
        student_wants_arr.append(content)
    preferences.close()
    return n_students, student_wants_arr


def get_pref():
    preferences = open('preferences.txt', 'r', encoding="utf-8")
    preferences.readline()
    n_students = 0
    student_wants_arr = []
    while True:
        content = preferences.readline()
        if not content:
            break
        n_students += 1
        content = content.split("\t")
        content[-1] = content[-1][:-1]
        if len(content) > 0:
            del content[0]
        # if len(content) > 0:
        #     del content[0]
        if len(content) > 0:
            del content[0]
        del content[-1]
        # del content[0]
        if len(content) > 0:
            try:
                content = list(map(int, content))
            except:
                pass

        # print(content)
        student_wants_arr.append((content[::2], content[1::2]))
    preferences.close()
    return n_students, student_wants_arr


def get_topics_for_IDs(preferences):
    topics = open('topics.txt', 'r', encoding="utf-8")
    id_to_name = {-1: "custom"}
    while True:
        content = topics.readline()
        if not content:
            break
        content = content.split("\t")
        content[-1] = content[-1][:-1]
        if len(content)==2:
            id_to_name[int(content[0])] = content[1]
    topics.close()

    for pref in preferences:
        print(pref, id_to_name[pref], sep="; ")
    return


def printer(student_size, topic_size, single_topics_ids, student_wants_arr):
    print("n_students =", student_size, end=";\n")
    print("n_topics =", topic_size, end=";\n")

    print("single_topics_ids = {", end="")
    for i, pref in enumerate(single_topics_ids):
        print(pref, end="")

        if i < len(single_topics_ids) - 1:
            print(",", end="")
    print("};")

    print("student_wants_list = [", end="")
    for student in range(student_size):
        print("{", end="")
        for i, pref in enumerate(student_wants_arr[student]):
            print(pref, end="")

            if i < len(student_wants_arr[student]) - 1:
                print(",", end="")

        if student < student_size - 1:
            print("},", end="")
        else:
            print("}", end="")
    print("];")


def printer_pref(student_size, topic_size, single_topics_ids, students_preferences):
    print("n_students =", student_size, end=";\n")
    print("n_topics =", topic_size, end=";\n")

    print("single_topics_ids = {", end="")
    for i, pref in enumerate(single_topics_ids):
        print(pref, end="")

        if i < len(single_topics_ids) - 1:
            print(",", end="")
    print("};")

    print("student_weights = array2d(Student, Preference, [", end="")
    for student in range(student_size):
        for pref in range(1, 7):
            if students_preferences[student][0][pref] == "":
                print(0, end=", ")
            else:
                print(students_preferences[student][0][pref], end=", ")
            if pref == 6:
                print()
    print("]);")

    print("student_preferences = array2d(Student, Preference, [", end="")
    for student in range(student_size):
        for pref in range(6):
            if students_preferences[student][1][pref] == "":
                print(0, end=", ")
            else:
                print(students_preferences[student][1][pref], end=", ")
            if pref == 5:
                print()
    print("]);")


    print("topics_fixed = [", end="")
    for student in range(student_size):
        if students_preferences[student][0][0]!="":
            print(students_preferences[student][1][0], end="")
        else:
            print(0, end="")

        if student < student_size - 1:
            print(", ", end="")
    print("];")


def printer_pref_to_file(student_size, topic_size, single_topics_ids, students_preferences, file_name):
    print("n_students =", student_size, end=";\n", file=open(file_name, 'w'))
    print("n_topics =", topic_size, end=";\n", file=open(file_name, 'a'))

    print("single_topics_ids = {", end="", file=open(file_name, 'a'))
    for i, pref in enumerate(single_topics_ids):
        print(pref, end="", file=open(file_name, 'a'))

        if i < len(single_topics_ids) - 1:
            print(",", end="", file=open(file_name, 'a'))
    print("};", file=open(file_name, 'a'))

    print("student_weights = array2d(Student, Preference, [", end="", file=open(file_name, 'a'))
    for student in range(student_size):
        for pref in range(1, 7):
            if students_preferences[student][0][pref] == "":
                print(0, end=", ", file=open(file_name, 'a'))
            else:
                print(students_preferences[student][0][pref], end=", ", file=open(file_name, 'a'))
            if pref == 6:
                print("", file=open(file_name, 'a'))
    print("]);", file=open(file_name, 'a'))

    print("student_preferences = array2d(Student, Preference, [", end="", file=open(file_name, 'a'))
    for student in range(student_size):
        for pref in range(6):
            if students_preferences[student][1][pref] == "":
                print(0, end=", ", file=open(file_name, 'a'))
            else:
                print(students_preferences[student][1][pref], end=", ", file=open(file_name, 'a'))
            if pref == 5:
                print("", file=open(file_name, 'a'))
    print("]);", file=open(file_name, 'a'))

    print("topics_fixed = [", end="", file=open(file_name, 'a'))
    for student in range(student_size):
        if students_preferences[student][0][0] != "":
            print(students_preferences[student][1][0], end="", file=open(file_name, 'a'))
        else:
            print(0, end="", file=open(file_name, 'a'))

        if student < student_size - 1:
            print(", ", end="", file=open(file_name, 'a'))
    print("];", file=open(file_name, 'a'))

def printer_to_file(student_size, topic_size, single_topics_ids, student_wants_arr, file_name):
    print("n_students =", student_size, end=";\n", file=open(file_name, 'w'))
    print("n_topics =", topic_size, end=";\n", file=open(file_name, 'a'))

    print("single_topics_ids = {", end="", file=open(file_name, 'a'))
    for i, pref in enumerate(single_topics_ids):
        print(pref, end="", file=open(file_name, 'a'))

        if i < len(single_topics_ids) - 1:
            print(",", end="", file=open(file_name, 'a'))
    print("};", file=open(file_name, 'a'))

    print("student_wants_list = [", end="", file=open(file_name, 'a'))
    for student in range(student_size):
        print("{", end="", file=open(file_name, 'a'))
        for i, pref in enumerate(student_wants_arr[student]):
            print(pref, end="", file=open(file_name, 'a'))

            if i < len(student_wants_arr[student]) - 1:
                print(",", end="", file=open(file_name, 'a'))

        if student < student_size - 1:
            print("},", end="", file=open(file_name, 'a'))
        else:
            print("}", end="", file=open(file_name, 'a'))
    print("];", file=open(file_name, 'a'))


if __name__ == '__main__':
    # topic_size = 80
    # single_topics_ids = [1, 3]
    topic_size = 82
    single_topics_ids = [1, 3, 30, 31, 42]
    #
    # student_size, student_wants_arr = get_ID_and_pref()
    # printer(student_size, topic_size, single_topics_ids, student_wants_arr)
    student_size, students_preferences = get_pref()
    # print(students_preferences)
    # printer_pref(student_size, topic_size, single_topics_ids, students_preferences)
    # printer_pref_to_file(student_size, topic_size, single_topics_ids, students_preferences, "input_w_pref.dzn")

    get_topics_for_IDs([1, 5, 1, 2, 3, 3, 5, 4, 6])
