if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    #creating two empty variables average and sum
    average = 0
    sum = 0
    #looping through the keys and values in the dictionary
    for key, value in student_marks.items():
        #checking if the key matches the query_name
        if key == query_name:
            #looping through all of the grades and summing them all up
            for v in value:
                sum += v
            #finding the average
            average = sum/len(value)
    #formating output to two decimal places
    print("{:.2f}".format(average))