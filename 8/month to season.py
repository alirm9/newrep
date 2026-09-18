seasons = ("winter", "spring", "summer", "autumn")

month = int(input("Enter the number of the month (1-12): "))

# December (12), January (1), February (2) belong to winter
if month in [12, 1, 2]:
    season = seasons[0]
elif 3 <= month <= 5:
    season = seasons[1]
elif 6 <= month <= 8:
    season = seasons[2]
elif 9 <= month <= 11:
    season = seasons[3]
else:
    season = "Invalid month"

print(f"The season is: {season}")