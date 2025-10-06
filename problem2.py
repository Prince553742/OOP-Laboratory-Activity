class StudentGradingSystem:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 100: self.grades.append(grade)
        else: print("Invalid grade. Ignored.")

    def compute_average(self):
        if not self.grades: return 0
        return sum(self.grades) / len(self.grades)

    def compute_point_grade(self, average):
        return ((100 - average) + 10) / 10

    def get_remarks(self, average):
        if average < 50: return "Dropped"
        elif average < 75: return "Failed"
        elif average <= 79: return "Passed – Satisfactory"
        elif average <= 84: return "Passed – Good"
        elif average <= 89: return "Passed – Average"
        elif average <= 99: return "Passed – Very Good"
        else: return "Passed – Excellent"

    def display_results(self):
        if not self.grades:
            print("\nNo valid grades entered.")
            return

        print("\n--- Results ---")
        print("Entered Grades:", self.grades)
        avg = self.compute_average()
        point_grade = self.compute_point_grade(avg)
        remarks = self.get_remarks(avg)
        print(f"Average Grade: {avg:.2f}")
        print(f"Point Grade: {point_grade:.2f}")
        print(f"Remarks: {remarks}")


def main():
    system = StudentGradingSystem()
    print("Enter grades (0–100). Enter -1 to finish.\n")
    while True:
        try:
            grade = float(input("Enter grade: "))
            if grade == -1: break
            system.add_grade(grade)
        except ValueError: print("Please enter a valid number.")
    system.display_results()

if __name__ == "__main__":
    main()
