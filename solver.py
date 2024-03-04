from datetime import datetime

from minizinc import Instance, Model, Solver

from converter import get_topics_for_IDs, get_pref, printer_pref_to_file


def convert(file_name, topic_size, single_topics_ids):
    student_size, students_preferences = get_pref()
    printer_pref_to_file(student_size, topic_size, single_topics_ids, students_preferences, file_name)


if __name__ == '__main__':
    topic_size = 82
    single_topics_ids = [1, 3, 7, 30, 31, 38, 42, 22, 25, 39, 77]
    students_filled = 132

    file_name = "input_w_pref.dzn"
    convert(file_name, topic_size, single_topics_ids)

    model = Model("enrollo_w_pref.mzn")
    model.add_file(file_name)
    # model.add_file("input.dzn")
    solver = Solver.lookup("cbc", refresh=True)
    instance = Instance(solver, model)
    start = datetime.now()
    result = instance.solve(optimisation_level=2, intermediate_solutions=True)

    # print(result[-1].student_gets)
    get_topics_for_IDs(result[-1].student_gets)

    print("Solving time:", datetime.now() - start, "for", 100 * students_filled / 160, "|", students_filled,
          "students; avg score:", result[-1].objective / students_filled)

# Solving time: 0:00: 04.501735
# for 74.375 | 119 students; avg score: 7.65546218487395

# Solving time: 0:00:03.962111
# for 82.5 | 132 students; avg score: 7.431818181818182