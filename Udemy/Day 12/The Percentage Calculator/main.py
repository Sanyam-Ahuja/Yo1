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
print(s_m)