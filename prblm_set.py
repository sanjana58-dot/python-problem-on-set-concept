#you are given a list of subjects for students . Assume one classroom is required for 1 subject . How many classrooms are required by all students

#"python", "java","C++","python","javascript","java","pyhton","java","C++","C"


L = ["python", "java","C++","python","javascript","java","pyhton","java","C++","C"]  #given list
subjects = {"python", "java","C++","python","javascript","java","pyhton","java","C++","C"}  #copy elemnets to dictionary coz dictionary ignores repetition
no_stu = len(subjects)  #calculated length of dictionary
print("Number of classrooms needed by all students :",no_stu)
