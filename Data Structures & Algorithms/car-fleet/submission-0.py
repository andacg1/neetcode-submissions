class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # calculate what time they will arrive at the finish line by
        # if a car that is behind another will finish before the car in front, merge those two
        cars = list(zip(position, speed))
        cars = list(map(lambda car: (car[0], car[1], (target - car[0]) / car[1]), cars))
        cars.sort()
        # print(cars)
        fleets = len(position)
        right = len(position) - 2
        curr_car = cars[-1]
        while right >= 0:
            prev_car = cars[right]
            if prev_car[2] <= curr_car[2]:
                # single fleet
                fleets -= 1
            else:
                # separate fleets
                curr_car = prev_car
            right -= 1
        return fleets