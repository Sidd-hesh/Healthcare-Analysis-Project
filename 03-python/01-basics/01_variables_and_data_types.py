# PYTHON BASICS: VARIABLES AND DATA TYPES
# For absolute beginners!

# ============================================
# 1. WHAT IS A VARIABLE?
# ============================================
# A variable is like a box that holds information
# Variable name = Value you want to store

# Let's create our first variable!
patient_name = "John Smith"
print(patient_name)  # This prints the value to screen

patient_age = 45
print(patient_age)

# ============================================
# 2. DATA TYPES
# ============================================

# STRING - Text (enclosed in quotes)
doctor_name = "Dr. Sarah Johnson"
hospital_name = 'City Medical Center'  # Single or double quotes both work
print(doctor_name)
print(type(doctor_name))  # Check the data type

# INTEGER - Whole numbers (no decimal point)
patient_id = 12345
bed_number = 42
admissions_count = 5
print(patient_id)
print(type(patient_id))

# FLOAT - Decimal numbers
patient_height = 5.9  # in feet
patient_weight = 165.5  # in pounds
temperature = 98.6  # Fahrenheit
print(patient_height)
print(type(patient_height))

# BOOLEAN - True or False (yes/no answers)
is_admitted = True
has_insurance = False
requires_surgery = True
print(is_admitted)
print(type(is_admitted))


# ============================================
# 3. VARIABLE NAMING RULES
# ============================================

# ✓ GOOD NAMES (clear and descriptive)
patient_id = 101
patient_first_name = "John"
appointment_date = "2024-09-15"
is_emergency_case = True

# ✗ AVOID (unclear or wrong)
# x = 101  # Too vague
# PatientID = 101  # Wrong style (Python uses snake_case)
# 123patient = 101  # Can't start with number
# patient-id = 101  # Can't use hyphens

# Note: Python is case-sensitive!
patient_name = "John"
Patient_Name = "Jane"
PATIENT_NAME = "Bob"
print(patient_name)  # prints "John"
print(Patient_Name)  # prints "Jane"


# ============================================
# 4. VARIABLE OPERATIONS
# ============================================

# Math operations
age = 45
years_worked = 20
total = age + years_worked
print(f"Total: {total}")  # Using f-string to combine text and variables

# String operations (concatenation)
first_name = "John"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name)

# Better way using f-strings
full_name_v2 = f"{first_name} {last_name}"
print(full_name_v2)

# Boolean operations
is_patient_critical = True
is_doctor_available = False
can_proceed = is_patient_critical and is_doctor_available
print(can_proceed)  # False, because both need to be True


# ============================================
# 5. CHANGING VARIABLE VALUES
# ============================================

patient_temperature = 98.6
print(f"Temperature: {patient_temperature}")

patient_temperature = 102.3  # Temperature increased!
print(f"Temperature: {patient_temperature}")

# Update using the variable's current value
patient_age = 45
patient_age = patient_age + 1  # Add 1 year
print(f"New age: {patient_age}")  # prints 46

# Shorter way
patient_age += 1  # Same as patient_age = patient_age + 1
print(f"New age: {patient_age}")  # prints 47


# ============================================
# 6. GETTING USER INPUT
# ============================================

# This asks the user to type something
# (Uncomment to try - it will wait for input!)
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")

# Input is always a STRING, even if you type a number!
# patient_id_input = input("Enter patient ID: ")
# print(type(patient_id_input))  # This will be <class 'str'>

# To convert to a number, use int() or float()
# patient_id_input = int(input("Enter patient ID: "))
# print(type(patient_id_input))  # Now it's <class 'int'>


# ============================================
# 7. PRACTICE EXERCISE
# ============================================

# Exercise 1: Create variables for a patient record
# Create the following variables:
# - patient_name (string)
# - patient_age (integer)
# - patient_weight (float)
# - is_hospitalized (boolean)

# Your code here:
# patient_name = ?
# patient_age = ?
# patient_weight = ?
# is_hospitalized = ?


# Exercise 2: Print all variables
# print(patient_name)
# print(patient_age)
# print(patient_weight)
# print(is_hospitalized)


# Exercise 3: Calculate BMI (Body Mass Index)
# Formula: BMI = weight (pounds) / (height (inches))^2 * 703
# Create variables for weight and height, then calculate BMI
# Your code here:


print("\n--- Practice Exercises Above (uncomment to test) ---")
