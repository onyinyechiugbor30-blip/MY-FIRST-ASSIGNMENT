'''Question 2:
Store your date of birth as a tuple(day, month, year).Calculate: how many days old you are, what day of the week
you were born(using Zeller's formula _- no imports allowed), and how many days until your next birthday.
Print a formatted report.'''
#storing date of birth as a tuple(day, month and year)
date_of_birth = (10, 3, 2005)
#Store today's date as a tuple(day, month, year)
present_date = (15, "June", 2026)
#number of days in each month of a normal year. As usual in python,the count or indexing starts from zero.
#so January is indexed 0, February is indexed 1, etc
days_in_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
#count how many leap year occured betwee 2005 and 2026
count = 0
#go through each year from 2005 - 2026
for leap_year in range(2005, 2027):
#leap year occur every four years. So If a year eg 2008 divisible by 4, increase the number of leap years found by 1.
    if (leap_year % 4 == 0):
        count += 1
 #store total leap years found   
leap_year = count
#my birth year
birth_year = 2005
#current year
present_year = 2026
#years between birth year and current year excluding both years(current and birth)
years_in_between = (present_year - birth_year -1)
#days remaining in march after the 10th, march has 31 days. its the third month and is indexed 2
days_remaining_in_birth_month = days_in_month [2] - 10 
#number of days in a year
days_in_a_year = 365
#calculate the remaining days in the birth year from April which is indexed 3 till december, then add the remaining days in
#march
days_in_birth_year = sum(days_in_month[3:]) + days_remaining_in_birth_month
#calculate the days passed in present year. [:5] means from January to May. Then add the 15 days of June
days_in_present_year = sum(days_in_month[:5]) + 15
#calculate the total days in all the years between birth year and present year and add the extra days from the leap year
#the * is to multiply the number of years in between by the number of days in a year which is 365
days_in_years_in_between = (years_in_between * days_in_a_year) + leap_year
#total age in days
how_many_days_old_i_am = (days_in_birth_year + days_in_present_year + days_in_years_in_between)
print(f' I am {how_many_days_old_i_am} days old')

#ZELLER'S FORMULA
#date of birth
q = 10
#month of birth
m= 3
#birth year
year = 2005
#the modulus of the birth year by 100. that means, 2005 % 100 will give five, because 2005/100 = 20 remaining 5
#the remainder is our modulus
K = year % 100
# the floor division of the birth year by 100, so, 2005/ 100 gives 20 remaining 5. but we go wit only the whole
#because we are using the floor division
J = year // 100
#apply zeller's formula
h = (q+(13*(m+1))//5+K+(K//4)+(J//4)+(5*J))%7
#zeller's formula returns the days indexed from zero. for instance, Sat is indexed 0, Sunday is indexed 1, etc
days = ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print(f'I was born on the day: {days[h]}')

#DAYS UNTIL NEXT BIRTHDAY
#Days remaining in June after 15th
days_in_present_month = days_in_month[4] - 15
#days remaining from July till december in addition to days remaining in June after June 
days_left_in_present_year = sum(days_in_month[6:]) + days_in_present_month
#days left in present year added to January to March 10 of next year
total_days_till_next_birthday = (days_left_in_present_year + sum(days_in_month[:2]) + 10 - 1)
print(f'I have {total_days_till_next_birthday} days till my next birhday')





                 
