from time import sleep
from vehicleType import VehicleType
from cabBookingSystem import CabBookingSystem
from location import Location

class Demo:
    def run(self):
        self.system = CabBookingSystem()

        # creating riders
        rider1 = self.system.createRider("John Doe", "+10738731098")
        rider2 = self.system.createRider("Gyan Singh", "+19826789740")

        # creating vehicles
        vehicle1 = self.system.createVehicle("TG 2378", VehicleType.MINI)
        vehicle2 = self.system.createVehicle("TG 2784", VehicleType.SEDAN)
        vehicle3 = self.system.createVehicle("TG 2063", VehicleType.MINI)
        vehicle4 = self.system.createVehicle("TG 2977", VehicleType.MINI)

        # creating drivers
        driver1 = self.system.createDriver("Rakesh Kumar", "+2987986336", vehicle1.id)
        driver2 = self.system.createDriver("Panna Lal", "+2128674487", vehicle2.id)
        driver3 = self.system.createDriver("Ram Lal", "+2129768756", vehicle3.id)
        driver4 = self.system.createDriver("Shyam Prakash", "+2878685443", vehicle4.id)
        driver1.online()
        driver2.online()
        driver3.online()
        driver4.online()

        # creating ride req
        fromLocation = Location("Rampur", 20, 50)
        toLocation = Location("Ghatshila", -10, 30)
        ride1 = self.system.getFareEstimate(rider1.id, fromLocation, toLocation, VehicleType.MINI)

        # ops
        driver = self.system.requestRide(ride1.id)
        if driver is None:
            print("Sorry. No drivers available.")
        else:
            print("Driver found.")
            sleep(2)
            self.system.pickupRider(ride1.id)
            print("Pickup done.")
            sleep(5)
            self.system.completeRide(ride1.id)
            print("Ride completed.")

        print("Success")

if __name__ == "__main__":
    Demo().run()