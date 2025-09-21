#Prompt the user to insert the minutes spent on each previous topic task. 
# Calculate the sum and the average. 
# Display those in the example program run format(Note! precision). 
# Make sure to calculate the required average for two decimal digits and later integer as rounded integer (precision 0 + type conversion).

#Example program run:

#Program starting.
print("Program starting.")
#Estimate how many minutes you spent on programming...
print("Estimate how many minutes you spent on programming...\n")
#A1_T1: 3
#A1_T2: 7
#A1_T3: 9
#A1_T4: 8
#A1_T5: 13
#A1_T6: 14
#A1_T7: 21
t1 = int(input("A1_T1: "))
t2 = int(input("A1_T2: "))
t3 = int(input("A1_T3: "))
t4 = int(input("A1_T4: "))
t5 = int(input("A1_T5: "))
t6 = int(input("A1_T6: "))
t7 = int(input("A1_T7: "))
#In total you spent 75 minutes on programming.
total = t1+t2+t3+t4+t5+t6+t7
#tähän voisi laskea: 
#average = float(total / 7), printissä sitten {round(average,2)} ja {round(average)}
print(f"\nIn total you spent {total} minutes on programming.")
#Average per task was 10.71 min and same rounded to the nearest integer 11 min.
print(f"Average per task was {round(float(total/7),2)} min and same rounded to the nearest integer {round(total/7)} min.")
#Program ending.
print("\nProgram ending.")
