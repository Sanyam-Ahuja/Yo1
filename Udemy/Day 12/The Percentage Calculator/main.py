print("Welcome To The Percentage Calculator")
s_m = {}
more = True
def get_marks():
    global s_m
    global more
    while more:
        l = input("What is Your Subject.")
        g = int(input("What Marks Did You Recieve."))
        s_m[l] = g
        if input("Are There More Subjects y for yes and n for no") == "n":
            more = False
get_marks()
marks = list(s_m.values())
subjects = list(s_m.keys())
def get_key(val):
    for key, value in s_m.items():
         if val == value:
             return key
 
    return "key doesn't exist"
no_s = 0
for i in s_m:
    no_s = no_s+1
t_m = sum(marks)
totl = int(input("What was The Total marks in Each Subject"))

percentage = round((t_m/(totl*no_s)) *100, 2)
print(f"Your Percentage in All The Subjects is {percentage}%")

no_b = len(subjects)-1

lowest_marks = 0
for i in marks:
    if i > lowest_marks:
        lowest_marks= i
for n in marks:
    if lowest_marks>n:
        lowest_marks = n

# subject_with_lowest_marks = s_m.index
subject_with_lowest_marks = get_key(lowest_marks)
best_5 = input(f"Do You Only Want To claculate The top highest Marks Percentage. This Means the lowest marks Would Be removed from Your Percentage, In Your Cas Which is {lowest_marks} in {subject_with_lowest_marks} So The Best {no_b} percentage Would Be Calculated")

if best_5 == "y":
    marks.remove(lowest_marks)
    new_subjects = subjects.remove(subject_with_lowest_marks)
    new_percentage = ((sum(marks))/((no_b *totl))) *100
    print(f"So Your Best {no_b} is {new_percentage}%")
else:
    print("Thanks For Using The Percentage calculator, Com back again.")