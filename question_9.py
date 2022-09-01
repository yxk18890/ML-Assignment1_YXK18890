if __name__ == "__main__":
    N = int(input("Enter number of students: "))
    students_weight = list()
    for i in range(N):
        students_weight.append(float(input("Enter the weight in lbs: ")))

    students_weight_in_kgs = list()
    for lbs in students_weight:
        students_weight_in_kgs.append(lbs * 0.45359237)

    print("Weights in kgs: ")
    for kgs in students_weight_in_kgs:
        print("{weight:.2f} KG".format(weight=kgs))
