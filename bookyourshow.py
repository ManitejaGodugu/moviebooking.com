import random

class SuperCls:
    def __init__(self):
        self.members = 0
        self.cost = 0
        self.total = 0
        self.theater_name = ""
        self.movie_name = ""
        self.money = 0
        self.change = 0
        self.time = ""
        self.seats = []

    def allocate_seats(self):
        # Ensure the seats are in a consecutive series
        start_seat = random.randint(1, 250 - self.members + 1)  # Random starting point
        self.seats = list(range(start_seat, start_seat + self.members))  # Consecutive seat numbers

    def bill(self):
        self.members = int(input("Enter the number of members: "))
        if self.members > 250:
            print("Seats are limited to a maximum of 250. Try again.")
            return
        self.total = self.members * self.cost
        self.allocate_seats()
        print(f"Total amount is: {self.total}")
        self.money = int(input("Enter the amount: "))
        if self.money < self.total:
            print("Insufficient amount")
        else:
            self.change = self.money - self.total
            print("******* Bill Details ********")
            print(f"Theater Name: {self.theater_name}")
            print(f"Movie Name: {self.movie_name}")
            print(f"Show Time: {self.time}")
            print(f"Members: {self.members}")
            print(f"Cost per Ticket: {self.cost}")
            print(f"Total Cost: {self.total}")
            print(f"Assigned Seats: {', '.join(map(str, self.seats))}")
            print(f"Remaining Change: {self.change}")
            print("______ Thank You! Visit Again! ______")


class SubCls(SuperCls):
    def hanuman(self):
        print("Click 1 for Mamatha Theater")
        print("Click 2 for Prathima Multiplex")
        theater_choice = int(input("Enter your choice: "))
        if theater_choice == 1:
            self.theater_name = "Mamatha Theater"
            self.movie_name = "Hanuman"
            self.cost = 250
        elif theater_choice == 2:
            self.theater_name = "Prathima Multiplex"
            self.movie_name = "Hanuman"
            self.cost = 200
        else:
            print("Choose the correct number")
            return

        print("Select show time:")
        print("1. 10:00 AM")
        print("2. 1:00 PM")
        print("3. 4:00 PM")
        print("4. 7:00 PM")
        time_choice = int(input("Enter your choice: "))
        time_options = ["10:00 AM", "1:00 PM", "4:00 PM", "7:00 PM"]
        if 1 <= time_choice <= 4:
            self.time = time_options[time_choice - 1]
        else:
            print("Invalid time selection")
            return

        self.bill()


class DerivedCls(SubCls):
    def salaar(self):
        print("Click 1 for Asian Srinivasa")
        print("Click 2 for Asian Shiva")
        theater_choice = int(input("Enter your choice: "))
        if theater_choice == 1:
            self.theater_name = "Asian Srinivasa"
            self.movie_name = "Salaar"
            self.cost = 350
        elif theater_choice == 2:
            self.theater_name = "Asian Shiva"
            self.movie_name = "Salaar"
            self.cost = 250
        else:
            print("Choose the correct number")
            return

        print("Select show time:")
        print("1. 11:00 AM")
        print("2. 2:00 PM")
        print("3. 5:00 PM")
        print("4. 8:00 PM")
        time_choice = int(input("Enter your choice: "))
        time_options = ["11:00 AM", "2:00 PM", "5:00 PM", "8:00 PM"]
        if 1 <= time_choice <= 4:
            self.time = time_options[time_choice - 1]
        else:
            print("Invalid time selection")
            return

        self.bill()


class DriverCls:
    @staticmethod
    def main():
        print("Welcome")
        print("Click 1 for Hanuman")
        print("Click 2 for Salaar")
        movie_choice = int(input("Enter your choice: "))
        if movie_choice == 1:
            print("You have chosen Hanuman")
            sub_cls = SubCls()
            sub_cls.hanuman()
        elif movie_choice == 2:
            print("You have chosen Salaar")
            derived_cls = DerivedCls()
            derived_cls.salaar()
        else:
            print("Choose the correct option")


# Running the main method
if __name__ == "__main__":
    DriverCls.main()
