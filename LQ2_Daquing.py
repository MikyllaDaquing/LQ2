def quizTwo(name):
    students ={
        "studentName" : name,
        "classMate" : "Beverly Sumao-i"
    }

    # Store the length of the studentName and classMate in a List
    lengths = [len(students["studentName"]), len(students["classMate"])]
    print(lengths)
    
    classNumbers = [1, 2, 3]
    # IF...ELIF...ELSE condition from Q2 Original Source Code
    if classNumbers[0] > classNumbers[1] and classNumbers[0] > classNumbers[2]:
        print("Class 1 is the highest")
    elif classNumbers[1] > classNumbers[0] and classNumbers[1] > classNumbers[2]:
        print("Class 2 is the highest")
    else:
        print("Class 3 is the highest")

    # Reverse the sort() of the classNumbers List
    classNumbers.sort(reverse=True)

# Call the quizTwo function with the user's name as a parameter
quizTwo(name = input("Enter your name: "))