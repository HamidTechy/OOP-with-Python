class Train:

    def __init__(self, name, seats, fare):
        self.name = name
        self.seats = seats
        self.fare = fare

    def getstatus(self):
        print(f"Name of Train is {self.name}")
        print(f"Seats available in Train is {self.seats}")

    def fareinfo(self):
        print(f"The price of ticket in  {self.name} is Rs. {self.fare}")

    def ticketbooked(self):
        if self.seats > 0:
            print("your ticket is booked")
            self.seats = self.seats - 1
        else:
            print("sorry the Train is full")

    def cancelticket(self):
        if self.seats > 0:
            print("your ticket is canceled")
            self.seats += 1


interacity = Train("Karachi Express", 300, 190)
interacity.getstatus()
interacity.fareinfo()
interacity.ticketbooked()
interacity.getstatus()
interacity.cancelticket()
interacity.getstatus()
