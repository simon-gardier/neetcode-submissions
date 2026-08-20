class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        #
        #   x                                        |   d = speed * time -> time = (d - position) / speed
        #  x                                         |
        #    x                                       |
        #x                                           |
        #      x                                     |
        #

        fleets = set()
        cars_data = []

        for i in range(len(position)):
            cars_data.append([-position[i], (target - position[i]) / speed[i]])
        cars_data.sort(key=lambda x: x[0])

        slowest_fleet_time = None
        for i, (negative_position, car_time) in enumerate(cars_data):
            if slowest_fleet_time is None:
                slowest_fleet_time = car_time
            fleets.add(max(slowest_fleet_time, car_time))
            slowest_fleet_time = max(slowest_fleet_time, car_time)

        return len(fleets)
