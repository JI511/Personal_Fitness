# Personal_Fitness
Personal Python project to improve skills and explore different libraries. Also using a local database with sqlite3 to learn SQL.

How to run: Personally, I prefer the windows command prompt to execute any python scripts so that is what I will cover here. 
Navigate to Personal_Fitness directory wherever you checked out the project. Note - this is the project level that the database will output to. 
Next cd into the src folder. Once here type, 'python Personal_Fitness.py' This should launch the script!

Current Progress:
There are currently 4 procedures: Body Weight, Weight Lifting, Nutrition, and Morning Lifts.

All database items have a unique identifier and the current datetime appended to them.

Body Weight:
Can add a new entry to the database for the day.
Can view a data plot of all entries.
Dump existing data to a csv file.

Weight Lifting:
This procedure is based around compound lifts, those being: bench press, squats, shoulder press, and deadlifts.
All of these items are setup to have 6 possible sets. The weight and rep amount can be input by the user.
Can update max lift values into a separate table.
Can add a new entry for chosen compound lists (Currently dummy values).
Dump existing data to a csv file.

Nutrition:
Can add new entry to a text file.

Morning Lifts:
Dump existing data to a csv file.
