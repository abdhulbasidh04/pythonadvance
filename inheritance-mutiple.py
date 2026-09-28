# class Hospital:
#     def __init__(self):
#         self.hospital_name=input("Enter hospital name: ")
#         self.hospital_location=input("Enter hospital location: ")
#         self.phone=int(input("Enter the phone number: "))
#     def display(self):
#         print("Hospital name:",self.hospital_name)
#         print("Hospital Location:",self.hospital_location)
#         print("Hospital number:",self.phone)
# class Department:
#     def __init__(self):
#         self.department_name=input("Enter the department name: ")
#         self.doctor_name=input("Enter the doctor name: ")
#     def display_department(self):
#         print("Department:",self.department_name)
#         print("Doctor name:",self.doctor_name)
# class Patient(Hospital,Department):
#     def __init__(self):
#         Hospital.__init__(self)
#         Department.__init__(self)
#         self.patient_name=input("Enter the patient name: ")
#         self.age=int(input("Enter the patient age: "))
#         self.gender=input("Enter the Gender: ")
#         self.phone_no=int(input("Enter the patient number: "))
#         self.admission_date=input("Enter the admission date: ")
#         self.bed_no=int(input("Enter the bed number: "))
#         self.discharge_date=""
#     def set_discharge(self):
#         self.discharge_date=input("Enter the discharge date: ")
#     def full_summery(self):
#         Hospital.display(self)
#         Department.display_department(self)
#         print("Patient name:",self.patient_name)
#         print("patient age:",self.age)
#         print("gender:",self.gender)
#         print("patient number:",self.phone_no)
#         print("Admission date:",self.admission_date)
#         print("Bed no:",self.bed_no)
#         if (self.discharge_date==""):
#             print("Not yet discharged")
#         else:
#             print("Discharge date:",self.discharge_date)
# p=Patient()
# p.full_summery()
# p.set_discharge()
# p.full_summery()

class A:
    def f(self):
        print("in first function f")
    def f(self,a):
        print("In second function f")
    def f(self,a,b):
        print("in third function f")
a=A()
# a.f()
# a.f(10)
a.f(10,20)