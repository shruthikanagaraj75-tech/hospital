appointments = []

name = input("Enter Patient Name: ")
doctor = input("Enter Doctor Name: ")

appointments.append([name, doctor])

print("\nAppointment Details")
print("Patient:", appointments[0][0])
print("Doctor :", appointments[0][1])
print("Appointment Booked Successfully!")