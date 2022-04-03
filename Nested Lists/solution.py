student_list = []
student_score_list = []

def takesecond(element):
    return element[1]

for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    student_list.append([name, score])
    student_score_list.append(score)

student_score_list = list(set(student_score_list))
student_score_list.sort()
#print student_score_list
lowest_second_item = student_score_list[1]

lowest_second_list = []
for i in student_list:
    if i[1] == lowest_second_item:
        lowest_second_list.append(i[0])

lowest_second_list.sort()
for item in lowest_second_list:
    print item
