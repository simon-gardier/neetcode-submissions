class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        #
        #   x                                        |   d = speed * time -> time = (d - position) / speed
        #  x                                         |
        #    x    8s                                 |
        #x                                           |
        #      x    10s                              |
        #

        fleets = set()
        cars_data = [] # order, ideal_time

        for i in range(len(position)):
            cars_data.append([-position[i], (target - position[i]) / speed[i]])
        cars_data.sort(key=lambda x: x[0])

        fastest_allowed_fleet_time = cars_data[0][1]
        for i, (order, car_time) in enumerate(cars_data):
            fastest_allowed_fleet_time = max(fastest_allowed_fleet_time, car_time)
            fleets.add(fastest_allowed_fleet_time)

        return len(fleets)
