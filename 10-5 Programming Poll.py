#10-5 Programming Poll:

filename = 'programming_poll.txt'

while True:
    reason = input("Why do you like programming? Enter 'end' to end prorgram \n")
    if reason == 'end':
        break
    else:
        with open(filename,'a') as file_object:
            file_object.write(reason + '\n')