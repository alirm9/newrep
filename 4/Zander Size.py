length = float(input("Enter the length of the zander in centimeters: "))
size_limit = 42

if length < size_limit:
    difference = size_limit - length
    print(
        f"Release the fish back into the lake. It is {difference:.1f} cm below the size limit."
    )
else:
    print("The zander meets the size limit.")