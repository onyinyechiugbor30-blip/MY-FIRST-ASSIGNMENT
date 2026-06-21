'''Question 6: Create a set of all students in your class(at least 10 names). Then create seperate set for students
who attended Monday, Tuesday, Wednesday. Use set operations to find who attended all three days, who missed at least once, 
who only came once and who never attended at all'''

#A set of all the students in the class
students_in_my_class = {'Onyinyechi', 'Austin', 'Chisom', 'Increase', 'Wisdom', 'Chidi', 'Sarah', 'Glory', 
                        'Anointing', 'Collins'}
#students who attended on Monday
Monday_attendees = {'Onyinyechi', 'Wisdom', 'Sarah', 'Glory', 'Anointing', 'Collins'}
#students who attended on Tuesday
Tuesday_attendees = {'Onyinyechi', 'Wisdom', 'Anointing', 'Chisom'}
#students who attended on Wednesday
Wednesday_attendees = {'Onyinyechi', 'Wisdom', 'Sarah', 'Collins', 'Increase'}

#STUDENTS WHO ATTENDED ALL THREE DAYS
# & means intersection. It will give only the students common to all three sets

attended_all_three_days= Monday_attendees & Tuesday_attendees & Wednesday_attendees
print("attended all three days: ", attended_all_three_days)

#STUDENTS WHO MISSED AT LEAST ONE DAY
#"-" means difference or subtract. so it removes students who attended all three days
missed_at_least_one = students_in_my_class- attended_all_three_days
print("missed at least once: ", missed_at_least_one)

#STUDENTS WHO ATTENDED ONLY ONE DAY
only_once  = set()
#loop through every student in the class
for student in students_in_my_class:
    #start counting attendance for each student
    count = 0
    #check if student attended on Monday
    if student in Monday_attendees:
        #keeps adding until the count is exhausted
        count +=1
        #check if student attended on Tuesday
    if student in Tuesday_attendees:
        count +=1
        #check if student attended on wednesday
    if student in Wednesday_attendees:
        count +=1
        # if student attended only one day
    if count==1:
        only_once.add(student)
print("attended only once:", only_once)

#ATTENDED AT LEAST ONE DAY
# "|"" means union and it combines all student from all days, not just students common to all days
attended_at_least_one = Monday_attendees|Tuesday_attendees|Wednesday_attendees

# STUDENTS WHO NEVER ATTENDED
#students in my class attendance but never attended any class
never_attended = students_in_my_class - attended_at_least_one
print("Never attended: ", never_attended)



