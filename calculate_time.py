'''
    CS 5001
    Lab 1
    Exercise 4
    Name: Ruby Lo
'''

'''
Write a Python program to solve the general version of the problem below. Ask the user for the time now (in hours),
and ask for the number of hours to wait. Your program should output what the time will be on the clock when the
alarm goes off.

You look at the clock and it is exactly 11am. You set an alarm to go off in 51 hours.
At what time does the alarm go off?

You may assume military time, so 1pm is 13:00 hours. Here is some example output:

What time is it? 23
How long until your alarm expires? 4
Your alarm will expire at 3.
'''

def main():
    # Given values
    current_hour= 11
    alarm_go_off= 51 

    # Input 
    current_hour= int(input("what is the current time?"))
    alarm_go_off= int(input("how long until your alarm goes expires?"))

    # Calculate for future hour, add alarm_go_off to current_hour
    alarm_hour= (current_hour + alarm_go_off) % 24

    # Output result
    print(f"the alarm will go off at: {alarm_hour:02d}:00") 

if __name__ == '__main__':
    main()
