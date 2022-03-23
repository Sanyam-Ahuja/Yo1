marks = [82,6,4,5]

lowest_marks = 0
for i in marks:
    if i > lowest_marks:
        lowest_marks= i
for n in marks:
    if lowest_marks>n:
        lowest_marks = n
# # print(lowest_marks)
# subjects = ["Sanyam", "Gaurav"]
# print(len(subjects)-1)
new_marks = marks.remove(lowest_marks)