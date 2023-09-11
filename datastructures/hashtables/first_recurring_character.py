# Given an array = [2,5,1,2,3,5,1,2,4] it should return 2
# Given an array = [2,3,4,5] it should return None

class FirstRecurringCharacter:
    def solution(self, array):
        existing_numbers = {}
        for number in array:
            if number in existing_numbers:
                return number
            existing_numbers[number] = True
        return None


solution = FirstRecurringCharacter()
print(solution.solution([2, 5, 1, 2, 3, 5, 1, 2, 4]))
print(solution.solution([2, 3, 4, 5]))
