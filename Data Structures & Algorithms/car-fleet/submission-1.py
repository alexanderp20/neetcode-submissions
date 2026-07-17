class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_array = [[]] * len(position)
        fleet_stack = []

        for i in range(len(position)):
            car_array[i] = [position[i], speed[i]]
        car_array.sort(reverse=True)

        for car in car_array:
            time = (target - car[0]) / car[1]
            if fleet_stack and time <= fleet_stack[-1]:
                continue
            else:
                fleet_stack.append(time)

        return len(fleet_stack)