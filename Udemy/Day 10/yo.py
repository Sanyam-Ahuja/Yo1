def my_function():
    result = 3*2
    return result

r = my_function()
print(r)

def format_name(f_name , l_name):
    return f_name.title() + " " + l_name.title()
final_name = format_name("SAnyam", "AhuJa")
print(final_name)


def Title_case(strings):
    lengh = len(strings)
    print(lengh,strings)
    x = strings.split(" ")
    for i in x:
        letter =i[0]
        letter_2 = i[1:]
        n_letter_2 = letter_2.lower()
        n_letter = letter.upper()
        print(n_letter +n_letter_2)
out = Title_case("hELlo MY NAME iS sanYam AHUJA")
a = 0
def count(string):
    """Counts the No. of Letters and spaces"""
    a = 0
    for i in string:
        a = a + 1
    print(a)   

count("sam a")
