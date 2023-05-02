select t.full_name, avg(assignments_grades.grade) as avg_grade
from assignments_grades
inner join assignments a on a.assisgnment_id = assignments_grades.assisgnment_id
inner join teachers t on t.teacher_id = a.teacher_id
group by a.teacher_id
order by avg_grade
limit 1