def count_grade():
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0

    for number in range(1, 6):
        name = input("Enter student name: ")
        score = input("Enter student grade: ")
        score_lower = score.lower()

        match score_lower:
            case "a":
                count_a += 1
            case "b":
                count_b += 1
            case "c":
                count_c += 1
            case "d":
                count_d += 1
            case _:
                print("Error")

    print(f'''
The number of student that scored A is {count_a}
The number of student that scored B is {count_b}
The number of student that scored C is {count_c}
The number of student that scored D is {count_d}
    ''')





if __name__ == "__main__":
    count_grade()