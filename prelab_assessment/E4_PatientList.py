#you have a patient list (name, id)
#use append to add patients to an empty list in the form [name, id], and show how you would print the patient ID of Bob Boyles

header = ["Name", "Patient ID"]
patient_list = []
patient_list.append(["Ann Ables", 12])
patient_list.append(["Bob Boyles", 25])
patient_list.append(["Chris Chou", 43])

print(patient_list[1][1]) #print Bob's patient ID (double index)


#OR, since this is a person with a specific associated #, dictionary also seems helpful if the list changes order
patient_dict = {
    "Ann Ables" : 12,
    "Bob Boyles" : 25,
    "Chris Chou" : 43
}

print(patient_dict["Bob Boyles"]) #print Bob's patient ID using dictionary