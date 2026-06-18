from patient import Patient
from doctor import Doctor

patient_list = []
doctor_list = []

while True:

    print("\n==== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Register Patient")
    print("2. Register Doctor")
    print("3. View Patients")
    print("4. View Doctors")
    print("5. Exit")

    user_choice = input("Enter choice: ")

    if user_choice == "1":

        full_name = input("Patient Name: ")
        age = int(input("Age: "))
        illness = input("Illness: ")

        new_patient = Patient(full_name, age, illness)
        patient_list.append(new_patient)

        print("Patient successfully registered!")
