class Robot:
    def __init__(self, name):
        self.name = name
        self._battery_level = 100

    @property
    def battery_level(self):
        return self._battery_level

    @battery_level.setter
    def battery_level(self, battery_level):
        if 0 <= battery_level <= 100:
            self._battery_level = battery_level

    def charge_battery(self, amount):
        if amount + self._battery_level > 100:
            return "Cant charge"
        else:
            self._battery_level = self._battery_level + amount
            return f"Battery level : {self._battery_level}"

    def work(self):
        self._battery_level = self._battery_level - 10
        return "Robot is working"


class CleaningRobot(Robot):
    def __init__(self, name, brush_type):
        super().__init__(name)
        self.brush_type = brush_type

    def work(self):
        self.battery_level -= 15
        return f"{self.name} is working with {self.brush_type}"

    def __call__(self):
        return self.work()


r1 = Robot("Alpha")
r1.work()
r1.work()
r1.work()

r2 = Robot("Beta")
r2.work()

r3 = Robot("Gamma")
robots = [r1, r2, r3]

robots.sort(key=lambda robot: robot.battery_level)
for robot in robots:
    print(f"Robot: {robot.name}\n")
