import json
from exception import Lab5Exception
from student import Student

student = []

class StudentBuilder:
    r"""
        You are expected to define a static method
        by the name build_student_object. It should take in 
        path to a json file and read the contents of the file.

        You are also expected to validate the contents read from 
        the JSON file and raise Exception accordingly
    """

    @staticmethod
    def build_student_object(json_file_path):
        data = list()
        with open(json_file_path, 'r') as f:
            data = json.load(f)

        if(data["age"] < 0 or data["age"] > 35):
            raise Lab5Exception("Invalid Age")

        if(data["cgpa"] < 0 or data["cgpa"] > 10):
            raise Lab5Exception("Invalid CGPA")

        if(data["name"] != '' and all(chr.isalpha() or chr.isspace() for chr in data["name"])):
            pass
        else:
            raise Lab5Exception("Name is not valid")

        if(data["gender"] == "male" or data["gender"] == "female" or data["gender"] == "Non-Binary" or data["gender"] == "Prefer Not To Say"):
            pass
        else:
            raise Lab5Exception("Not a valid gender")

        if(data["home_town"] != '' and all(chr.isalpha() or chr.isspace() for chr in data["home_town"])):
            pass
        else:
            raise Lab5Exception("Hometown is not valid")
        
        for i in student:
            if (i.name == data["name"] and i.age == data["age"] and i.cgpa == data["cgpa"] and i.home_town == data["home_town"] and i.gender == data["gender"]):
                return i
        newstudent = Student(data["name"],data["age"],data["cgpa"],data["gender"],data["home_town"])
        student.append(newstudent)
        return newstudent