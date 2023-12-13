class Workout:
    def __init__(self, date, steps, calories_burned):
        self.date = date
        self.steps = steps
        self.calories_burned = calories_burned

class FitnessTracker:
    def __init__(self):
        self.workouts = []

    def add_workout(self, date, steps, calories_burned):
        workout = Workout(date, steps, calories_burned)
        self.workouts.append(workout)

    def view_workouts(self):
        if not self.workouts:
            print("No workouts recorded yet.")
            return

        for workout in self.workouts:
            print(f"Date: {workout.date}")
            print(f"Steps: {workout.steps}")
            print(f"Calories Burned: {workout.calories_burned}")
            print("\n")

def main():
    fitness_tracker = FitnessTracker()

    while True:
        print("Options:")
        print("1. Add a new workout")
        print("2. View recorded workouts")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Date (YYYY-MM-DD): ")
            steps = int(input("Number of steps: "))
            calories_burned = float(input("Calories burned: "))
            fitness_tracker.add_workout(date, steps, calories_burned)
            print("Workout added successfully.")
        elif choice == "2":
            fitness_tracker.view_workouts()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
