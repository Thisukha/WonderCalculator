class WonderCalculator:
    def __init__(self):
        self.numbers = []
        self.highest_value = None
        self.lowest_value = None
        self.average = None
        self.even_numbers = []

    def enter_numbers(self):
        print("\nEnter positive Integer Numbers\n")
        num_of_numbers = int(input("How many numbers do you want to enter = "))
        while num_of_numbers > 10:
            print("Only 10 numbers are allowed")
            num_of_numbers = int(input("How many numbers do you want to enter = "))
        for _ in range(num_of_numbers):
            number = int(input("Please input a positive number = "))
            self.numbers.append(number)

    def calculate_highest_value(self):
        self.highest_value = max(self.numbers)
        print(f"The highest value is = {self.highest_value}")

    def calculate_lowest_value(self):
        self.lowest_value = min(self.numbers)
        print(f"The lowest value is = {self.lowest_value}")

    def calculate_average(self):
        self.average = sum(self.numbers) / len(self.numbers)
        print(f"Average is = {self.average}")

    def calculate_even_numbers(self):
        self.even_numbers = [number for number in self.numbers if number % 2 == 0]
        if len(self.even_numbers) == 0:
            print("There are no even numbers in the list!")
        else:
            print("Even number is", self.even_numbers)

    def main_menu(self):
        while True:
            print("\n\nWonder Calculator\n================\nMain Menu\n")
            print("1. Enter positive Integer Numbers")
            print("2. Display Highest value")
            print("3. Display Lowest value")
            print("4. Display Average value")
            print("5. Display Even Numbers")
            print("6. Exit")
            option = int(input("Please indicate your option = "))
            if option == 1:
                self.enter_numbers()
            elif option == 2:
                self.calculate_highest_value()
            elif option == 3:
                self.calculate_lowest_value()
            elif option == 4:
                self.calculate_average()
            elif option == 5:
                self.calculate_even_numbers()
            elif option == 6:
                exit()
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    calculator = WonderCalculator()
    calculator.main_menu()
