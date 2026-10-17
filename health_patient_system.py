# PROG211 - Object-Oriented Programming 1
# Project: Community Clinic Patient Record System
# SDG 3: Good Health and Well-Being

# TASK 1: OBJECT-ORIENTED PROGRAMMING

class Patient:
    # Class attribute
    patient_count = 0

    # Constructor
    def __init__(self, patient_id, name, age, illness):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.illness = illness

        Patient.patient_count += 1

    # Instance method
    def display_details(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Illness:", self.illness)

    # Class method
    @classmethod
    def get_patient_count(cls):
        return cls.patient_count


class Clinic:
    # Constructor
    def __init__(self, clinic_name):
        self.clinic_name = clinic_name
        self.patients = []

    # Method to register a patient
    def register_patient(self, patient):
        self.patients.append(patient)
        print(patient.name, "has been registered successfully.\n")

    # Method to display registered patients
    def display_patients(self):
        print("\n--- Patients Registered at", self.clinic_name, "---")

        if len(self.patients) == 0:
            print("No patients registered.")
        else:
            for patient in self.patients:
                patient.display_details()
                print("--------------------")


# TASK 2: PYTHON DATA STRUCTURES

# List for storing patient records
patient_records = []


# Function to add a patient to the list
def add_patient(patient_list, patient):
    patient_list.append(patient)
    print(patient.name, "added to patient records successfully.\n")


# Function to display patient records
def display_patients(patient_list):
    if len(patient_list) == 0:
        print("No patient records found.")
    else:
        print("\n--- Patient Records List ---")

        for patient in patient_list:
            patient.display_details()
            print("--------------------")


# TASK 3: CREATE OBJECTS AND TEST THE SYSTEM (USER INPUT)

print("=== Welcome to the Clinic System ===")

# Create a clinic object dynamically
clinic_name_input = input("Enter the Clinic Name: ")
clinic = Clinic(clinic_name_input)

# Dynamic loop to keep asking until the user says no
patient_counter = 1

while True:
    print(f"\n--- Enter Information for Patient {patient_counter} ---")

    # Gather inputs from the user
    p_id = input("Enter Patient ID: ")
    p_name = input("Enter Name: ")

    # Input validation for age to ensure it's a number
    while True:
        try:
            p_age = int(input("Enter Age: "))
            break
        except ValueError:
            print("Please enter a valid integer for age.")

    p_illness = input("Enter Illness: ")

    # Create the Patient object dynamically using user inputs
    new_patient = Patient(p_id, p_name, p_age, p_illness)

    # Register patients with the clinic and add to records list
    clinic.register_patient(new_patient)
    add_patient(patient_records, new_patient)

    # Ask if the user wants to record another patient
    cont = input("Do you want to record another patient? (yes/no): ").strip().lower()

    if cont not in ['yes', 'y']:
        break

    patient_counter += 1

# Display all patient records using the data structure function
display_patients(patient_records)

# Demonstrate the Clinic instance method
clinic.display_patients()

# Demonstrate the Patient class method
print("\nTotal patient objects created:", Patient.get_patient_count())