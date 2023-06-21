# Opening file
f = open("FitnessFirst.py", "w")

# Write 1000 lines of code
# Imports 
import math
import os

#Function to calculate BMI 
def calcBMI(height, weight):
    bmi = (weight / math.pow(height, 2)) 
    return bmi

#Function to calculate BMR 
def calcBMR(gender, weight, height, age):
    if gender == 'male':
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else: 
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161
    return bmr

#Function to calculate calories burned during exercise
def calcCalBurned(exercise, weight, duration):
    if exercise == 'running':
        calBurned = 0.75 * weight * duration
    elif exercise == 'cycling':
        calBurned = 0.6 * weight * duration
    elif exercise == 'swimming':
        calBurned = 0.45 * weight * duration
    elif exercise == 'walking':
        calBurned = 0.27 * weight * duration
    return calBurned

#Function to calculate daily calorie intake
def calcCalIntake(gender, weight, height, age, bmi):
    if gender == 'male' and bmi >= 18.5 and bmi <= 25:
        calIntake = (10 * weight) + (6.25 * height) - (5 * age) + 5
    elif gender == 'female' and bmi >= 18.5 and bmi <= 25:
        calIntake = (10 * weight) + (6.25 * height) - (5 * age) - 161
    elif bmi < 18.5:
        calIntake = (10 * weight) + (6.25 * height) - (5 * age) + 5 - 1000
    elif bmi > 25:
        calIntake = (10 * weight) + (6.25 * height) - (5 * age) + 5 + 1000
    return calIntake

#Function to calculate weekly calorie expenditure
def calcCalExpenditure(calBurned, calIntake):
    calExpenditure = calBurned + calIntake 
    return calExpenditure

#Function to calculate calories to burn to reach target weight
def calcTargetWeight(target, current, bmr):
    caloriesToBurn = (target * bmr - current * bmr) / bmr
    return caloriesToBurn 

#Function to calculate calories to eat to reach target weight 
def calcTargetCalories(target, current):
    caloriesToEat = (target * current - target * current) / current
    return caloriesToEat

#Function to calculate calories per day to reach target weight
def calcDailyTarget(caloriesToEat, caloriesToBurn):
    caloriesPerDay = caloriesToEat + caloriesToBurn
    return caloriesPerDay

#Execution
if __name__ == '__main__':
    print("Welcome to Fitness First, where we help you reach your health and fitness goals!")
    gender = input("What is your gender? (male/female): ")
    weight = float(input("What is your body weight (kg)?: "))
    height = float(input("What is your height (m)?: "))
    age = int(input("What is your age?: "))
    exercise = input("What type of exercise are you doing today (running/cycling/swimming/walking)?: ")
    duration = float(input("How long will you be doing this exercise today (hours)?: "))
    calBurned = calcCalBurned(exercise, weight, duration)
    print("You'll be burning roughly", calBurned, "calories today.")
    bmi = calcBMI(height, weight)
    print("Your BMI is", bmi)
    bmr = calcBMR(gender, weight, height, age)
    print("Your BMR is", bmr)
    calIntake = calcCalIntake(gender, weight, height, age, bmi)
    print("Your recommended daily calorie intake is", calIntake)
    calExpenditure = calcCalExpenditure(calBurned, calIntake)
    print("Your total daily calorie expenditure is", calExpenditure)
    target = float(input("What is your target weight (kg)?: "))
    current = float(input("What is your current weight (kg)?: "))
    caloriesToBurn = calcTargetWeight(target, current, bmr)
    print("You need to burn", caloriesToBurn, "calories to reach your target weight.")
    caloriesToEat = calcTargetCalories(target, current)
    print("You need to eat", caloriesToEat, "calories to reach your target weight.")
    caloriesPerDay = calcDailyTarget(caloriesToEat, caloriesToBurn)
    print("You need to aim for a total daily calorie expenditure of", caloriesPerDay, "to reach your target weight.")
    print("Thanks for using Fitness First! See you next time!")

# Close file
f.close()