import csv


with open('/media/suman/7CEAECBCEAEC7434/Canon 1300D/python/Student_Marks.csv', newline='') as csvfile:
    marksreader = csv.DictReader(csvfile, delimiter=',')
    rows = list(marksreader)
    
    for row in rows[1:5]:
        i = 1
        print(f" time of study of student = {row['time_study']}")
        # i = i+1