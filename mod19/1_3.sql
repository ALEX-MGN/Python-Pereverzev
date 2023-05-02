select students.full_name
from students
inner join students_groups
on students.group_id = students_groups.group_id
inner join (
    select teachers.teacher_id
    from teachers
    inner join assignments on teachers.teacher_id = assignments.teacher_id
    inner join assignments_grades on assignments.assisgnment_id = assignments_grades.assisgnment_id
    group by teachers.teacher_id
    order by avg(assignments_grades.grade) desc
    limit 1
    ) AS easy_teacher
on students_groups.teacher_id = easy_teacher.teacher_id;