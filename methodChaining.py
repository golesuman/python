class Car:
    def car(self):
        print('This is the car')
        return self
    def start(self):
        print('Start the car')
        return self

    def brake(self):
        print('Hey use the brake')
        return self

    def stop(self):
        print('Stop the car')
        return self

redCar=Car()
redCar.start().brake().stop()