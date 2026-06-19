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

    elif user_choice == "2":

        full_name = input("Doctor Name: ")
        age = int(input("Age: "))
        specialization = input("Specialization: ")

        new_doctor = Doctor(full_name, age, specialization)
        doctor_list.append(new_doctor)

        print("Doctor successfully registered!")

    elif user_choice == "3":

        if len(patient_list) == 0:
            print("No patients found.")
        else:
            for patient in patient_list:
                patient.display_information()

    elif user_choice == "4":

        if len(doctor_list) == 0:
            print("No doctors found.")
        else:
            for doctor in doctor_list:
                doctor.display_information()

    elif user_choice == "5":
        print("Exiting system... Goodbye!")
        break

    else:
        print("Invalid choice!")
