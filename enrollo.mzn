% Parameters
int: n_students;
int: n_topics;

set of int: Student = 1..n_students;
set of int: Topic = 1..n_topics;

% array[Student, Topic] of 0..1: student_wants;
array[Student] of set of Topic: student_wants_list;
set of Topic: single_topics_ids;

array[Student] of var 0..1: is_happy;
% array[Student, Topic] of var 0..1: student_has;
array[Student] of var Topic: student_gets;
array[Topic] of var 0..2: topic_assignees;

% constraint forall(S in Student)(sum(T in Topic)(student_has[S, T])=1);
constraint forall(T in Topic)(topic_assignees[T] = count(S in Student)(student_gets[S] = T));

constraint forall(T in single_topics_ids)(topic_assignees[T] <= 1);

constraint forall(S in Student)(is_happy[S] = (student_gets[S] in student_wants_list[S]));


var 0..n_students: score = sum(S in Student)(is_happy[S]);

solve maximize score;

output ["Students with topic they didn't want: " ++ show(n_students-score)]
        ++ ["\n"] ++ ["student;   topic;\n"] ++
        [join(";\n", [ show(S) ++ ";         " ++ show(student_gets[S])| S in Student]) ++ ";"]
%         ++ ["\n"] ++
%         [join("\n", [ "student" ++ show(S) ++ ": " ++ join(",", [show(if student_gets[S]=T then 8 else 0 endif) | T in Topic]) | S in Student])] 
%         ++ ["\n"] ++
%         ["            " ++  join(",", [show(topic_assignees[T]) | T in Topic])]

