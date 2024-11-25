class SuperCls:
    def __init__(self):
        self.members = 0
        self.cost = 0
        self.total = 0
        self.theater_name = ""
        self.movie_name = ""
        self.money = 0
        self.change = 0

    def bill(self):
        self.members = int(input("Enter the number of members: "))
        self.total = self.members * self.cost
        print(f"Total amount is: {self.total}")
        self.money = int(input("Enter the amount: "))
        if self.money < self.total:
            print("Insufficient amount")
        else:
            self.change = self.money - self.total
            print("******* Bill Details ********")
            print(f"Theater Name: {self.theater_name}")
            print(f"Movie Name: {self.movie_name}")
            print(f"Members: {self.members}")
            print(f"Cost per Ticket: {self.cost}")
            print(f"Total Cost: {self.total}")
            print(f"Remaining Change: {self.change}")
            print("______ Thank You! Visit Again! ______")


class SubCls(SuperCls):
    def hanuman(self):
        print("Click 1 for Mamatha Theater")
        print("Click 2 for Prathima Multiplex")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            self.theater_name = "Mamatha Theater"
            self.movie_name = "Hanuman"
            self.cost = 250
            self.bill()
        elif choice == 2:
            self.theater_name = "Prathima Multiplex"
            self.movie_name = "Hanuman"
            self.cost = 200
            self.bill()
        else:
            print("Choose the correct number")


class DerivedCls(SubCls):
    def salaar(self):
        print("Click 1 for Asian Srinivasa")
        print("Click 2 for Asian Shiva")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            self.theater_name = "Asian Srinivasa"
            self.movie_name = "Salaar"
            self.cost = 350
            self.bill()
        elif choice == 2:
            self.theater_name = "Asian Shiva"
            self.movie_name = "Salaar"
            self.cost = 250
            self.bill()
        else:
            print("Choose the correct number")


class DriverCls:
    @staticmethod
    def main():
        print("Welcome")
        print("Click 1 for Hanuman")
        print("Click 2 for Salaar")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("You have chosen Hanuman")
            sub_cls = SubCls()
            sub_cls.hanuman()
        elif choice == 2:
            print("You have chosen Salaar")
            derived_cls = DerivedCls()
            derived_cls.salaar()
        else:
            print("Choose the correct option")


# Running the main method
if __name__ == "__main__":
    DriverCls.main()
