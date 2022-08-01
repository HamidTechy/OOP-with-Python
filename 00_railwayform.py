class RailwayForm:
    FormType = "Reservation Form"
    def printdata(self):
        print(f"passenger name is {self.name}")
        print(f"train name is {self.train}")


ticketapplication = RailwayForm()
ticketapplication.name = "Hamid"
ticketapplication.train = "Orange Train"
ticketapplication.printdata()
