class Day2:
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

    def validate_levels(self, levels):
        is_valid = False

        is_sorted = sorted(levels) == levels or sorted(levels, reverse=True) == levels

        in_range = True
        for i in range(len(levels) - 1):
            diff = abs(levels[i] - levels[i + 1])
            if diff < 1 or diff > 3:
                in_range = False
                break

        if is_sorted and in_range:
            is_valid = True

        return is_valid

    def solve_part_1(self, input):
        solution = 0

        for line in input:
            levels = list(map(int, line.split(" ")))
            if self.validate_levels(levels):
                solution += 1

        return solution

    def solve_part_2(self, input):
        solution = 0

        for line in input:
            levels = list(map(int, line.split(" ")))
            if self.validate_levels(levels):
                solution += 1
            else:
                for i in range(len(levels)):
                    modified_levels = levels[:i] + levels[i + 1 :]

                    if self.validate_levels(modified_levels):
                        solution += 1
                        break

        return solution


if __name__ == "__main__":
    day1 = Day2()
    day1.solve_day()
