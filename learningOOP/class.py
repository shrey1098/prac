import datetime, threading, time


class Car():

    def __init__(self, type):
        self.type = type
        self.speed = 0
        self.acceleration = 0
        self.gear_num = 0
        self.distance = 0
        self.start_time = time.time()
        if self.type == "manual":
            self.manual_gear_up_logic()

    def accelerate(self, magnitude):
        if magnitude > 10:
            return Exception("Accelerate only between 0-10")
        else:
            if self.type == "automatic":
                self.acceleration = magnitude
                self.automatic_gear_logic()
                self.speed = magnitude * 10
            else:
                self.acceleration = magnitude
                self.speed = magnitude * 10
                self.manual_gear_check()

    def automatic_gear_logic(self):
        if self.acceleration <= 2:
            self.gear(1)
        elif self.acceleration <= 4:
            self.gear(2)
        elif self.acceleration <= 6:
            self.gear(3)
        elif self.acceleration <= 8:
            self.gear(4)
        elif self.acceleration <= 10:
            self.gear(5)

    def manual_gear_up_logic(self):
        input_gear = input("enter gear 1-5: ")
        if int(input_gear) > 5:
            return Exception("Gears only till 5th")
        self.gear_num = int(input_gear)
        input_accelerate = input("Accelerate between 0-10: ")
        self.accelerate(int(input_accelerate))

    def manual_gear_down_logic(self):
        gear_down = input("Reduce the gear to: ")
        self.gear(int(gear_down))

    def gear(self, gear):
        if gear >= 5:
            return Exception(f"no {gear}th gear found")
        self.gear_num = gear

    def manual_gear_check(self):
        if self.gear_num*2 != self.acceleration:
            print("Grr gRRR grrrRRR")
            print("car not in correct gear and acceleration")
            self.manual_gear_up_logic()

    def breaks(self, magnitude):
        if magnitude > 10:
            return Exception("Break only between 0-10")
        else:
            if magnitude > self.acceleration:
                magnitude = self.acceleration
                if self.type == "manual":
                    self.manual_gear_down_logic()
            else:
                magnitude = self.acceleration - magnitude
                if self.type == "manual":
                    self.manual_gear_down_logic()
            self.accelerate(magnitude)

    def dist(self):
        now_time = time.time()
        time_elapsed = now_time - self.start_time
        self.distance = self.speed * time_elapsed
        print(self.distance)
        threading.Timer(5, self.dist).start()


x = Car('manual')
print(f"speed is: {x.speed}")
print(f"gear is: {x.gear_num}")

x.breaks(2)
print(f"speed is: {x.speed}")
print(f"gear is: {x.gear_num}")
