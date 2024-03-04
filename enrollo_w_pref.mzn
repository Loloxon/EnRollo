% Parameters
int: n_students;
int: n_topics;

set of int: Student = 1..n_students;
set of int: Topic = 1..n_topics;
set of int: Preference = 1..6;
set of int: Weight = 0..10;

% array[Student, Topic] of 0..1: student_wants;
array[Student, Preference] of -1..n_topics: student_preferences;
array[Student, Preference] of Weight: student_weights;
array[Student] of -1..n_topics: topics_fixed;
set of Topic: single_topics_ids;

array[Student] of var Weight: how_happy;
% array[Student, Topic] of var 0..1: student_has;
array[Student] of var -1..n_topics: student_gets;
array[Topic] of var 0..2: topic_assignees;


constraint forall(S in Student)(if topics_fixed[S]!=0 then student_gets[S] = topics_fixed[S] else student_gets[S]>0 endif);

% constraint forall(S in Student)(sum(T in Topic)(student_has[S, T])=1);
constraint forall(T in Topic)(topic_assignees[T] = count(S in Student)(student_gets[S] = T));

constraint forall(T in single_topics_ids)(topic_assignees[T] <= 1);

constraint forall(S in Student)(how_happy[S] = sum([if student_gets[S]==student_preferences[S, P] then student_weights[S, P] else 0 endif | P in Preference]));

% constraint forall(S in Student)(how_happy[S] = if student_preferences[S, 1] == -1 then 10 else 0 endif);

var 0..n_students*10: score = sum(S in Student)(how_happy[S]);

solve maximize score;

output ["Students score: " ++ show(score)]
        ++ ["\n"] ++ ["student;   topic;\n"] ++
        [join(";\n", [ show(S) ++ ";         " ++ show(student_gets[S])| S in Student]) ++ ";"]
%         ++ ["\n"] ++
%         [join("\n", [ "student" ++ show(S) ++ ": " ++ join(",", [show(if student_gets[S]=T then 8 else 0 endif) | T in Topic]) | S in Student])] 
%         ++ ["\n"] ++
%         ["            " ++  join(",", [show(topic_assignees[T]) | T in Topic])]

