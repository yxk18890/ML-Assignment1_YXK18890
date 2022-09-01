if __name__ == "__main__":
    dog = dict()
    dog["name"] = "Spike"
    dog["color"] = "White"
    dog["breed"] = "German"
    dog["legs"] = 4
    dog["breed"] = "pure"
    print(dog)
    student = {"first_name": "Yesh", "last_name": "Yesh", "gender": "Male", "age": 22, "marital_status": "Single",
               "skills": ["Coding"], "country": "USA", "city": "Missouri", "address": "ABCD"}
    print("Length of student: " + str(len(student)))
    print("Type of skills: " + str(type(student["skills"])))
    student["skills"].append("Gaming")
    student["skills"].append("Music")
    print("Keys: "+str(student.keys()))
    print("Values: " + str(student.values()))