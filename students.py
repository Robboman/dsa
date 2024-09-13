seating_chart = [
    ["Adam", "Ben", "Charlie", "Daniel"],
    ["Eric", "Frank", "Gerry", "Henry"],
    ["Isaac", "John", "Ken", "Luke"],
    ["Manny", "Nick", "Oscar", "Pete"]
]

#print(seating_chart[2][1])
student_name = input("Student name: ")
print("The students are seated as follows:\n")
for row, seats in enumerate(seating_chart):
    for seat, name in enumerate(seats):
        #print(f"{name} is sitting in seat number {seat+1}, row {row+1}.")
        if student_name == name:
            print(f"Student {name} found! He is sitting in row {row+1} and seat {seat+1}.")
        else:
            print(f"No student by the name of {student_name} found!")