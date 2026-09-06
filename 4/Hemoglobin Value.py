gender = input("Enter biological gender (female/male): ").strip().lower()
hemo = float(input("Enter hemoglobin value (g/l): "))

if gender == "female":
    if hemo < 117:
        print("Hemoglobin value is low.")
    elif hemo <= 155:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
elif gender == "male":
    if hemo < 134:
        print("Hemoglobin value is low.")
    elif hemo <= 167:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
else:
    print("Invalid gender entered.")