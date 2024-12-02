class Day1:
    def __init__(self):
        self.test = self.read_file("test.txt")
        self.input = self.read_file("input.txt")

    def solve_day(self):
        print("Part 1 test:\t", self.solve_part_1(self.test))
        print("Part 1 input:\t", self.solve_part_1(self.input))
        print("Part 2 test:\t", self.solve_part_2(self.test))
        print("Part 2 input:\t", self.solve_part_2(self.input))

    def read_file(self, filename):
        content = []

        with open(filename, "r") as file:
            for line in file:
                content.append(line.strip())

        return content

    def create_lists(self, input):
        list1 = []
        list2 = []

        for pair in input:
            num1, num2 = pair.split("   ")
            list1.append(int(num1))
            list2.append(int(num2))

        list1.sort()
        list2.sort()

        return list1, list2

    def solve_part_1(self, input):
        solution = 0
        list1, list2 = self.create_lists(input)

        for nums in zip(list1, list2):
            solution += abs(nums[0] - nums[1])
        return solution

    def solve_part_2(self, input):
        solution = 0
        list1, list2 = self.create_lists(input)

        for num in list1:
            count = list2.count(num)
            solution += num * count

        return solution


if __name__ == "__main__":
    day1 = Day1()
    day1.solve_day()
