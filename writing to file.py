with open ("shopping.txt", "r") as file:
    content = file.read()
    print(content)
with open ("shopping.txt", "r") as file:
    all_lines = file.readlines()
    print(f"Items in the shopping list: {len(all_lines)}")
    for line in all_lines:
        print(line.strip())


import json

name = ["Alice", "Bob", "Charlie"]
grade = {
    "name": "Alice",
    "grade": "5"
}
with open("names.text", "r") as file:
    grades_from_file = file.read()
    data = json.loads(grades_from_file)
    print(data)