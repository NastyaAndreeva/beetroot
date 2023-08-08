class Patient:
    def __init__(self,name,age,gender,medical_history):
        self.name=name
        self.age=age
        self.gender=gender
        self.__medical_history=medical_history
        self.appointments=[]
    
    def return_med_history(self):
        return self.__medical_history
    
    def add_new_appointment(self,appointment):
        self.appointments.append(appointment)

    def remove_appointment(self,appointment):
        self.appointments.remove(appointment)

    def print_appointment(self):
        print(self.appointments)

    def __repr__(self):
        return f"Patient (\'{self.name}\', \'{self.age})\',\'{self.gender}\', \'{self.return_med_history()}\'"
    

class MedicalSystem:
    def __init__(self):
        self.patients=[]

    def add_new_patient(self,patient):
        self.patients.append(patient)

    def print_info(self):
        for patient in self.patients:
            print(f"name ='{patient.name}',age = '{patient.age}', gender='{patient.gender}',medical history='{patient.return_med_history()}' ")
    def find_patients_by_condition(self,condition):
        filtered_patients=[]
        for patient in self.patients:
            if condition==patient.name:
                filtered_patients.append(patient)
        print(repr(filtered_patients))
                


patient_1=Patient("Alina",19,"female",["corona","cold"])
med_system=MedicalSystem()
med_system.add_new_patient(patient_1)
med_system.print_info()
patient_1.add_new_appointment("17:30")
patient_1.print_appointment()
med_system.find_patients_by_condition("Alina")



    
        

