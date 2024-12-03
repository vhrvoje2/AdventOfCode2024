import re
import enum


class Day2:
    def __init__(self):
        self.test_1 = self.read_file("test_1.txt")
        self.test_2 = self.read_file("test_2.txt")
        self.input = self.read_file("input.txt")

    def solve_day(self):
        print("Part 1 test:\t", self.solve_part_1(self.test_1))
        print("Part 1 input:\t", self.solve_part_1(self.input))
        print("Part 2 test:\t", self.solve_part_2(self.test_2))
        print("Part 2 input:\t", self.solve_part_2(self.input))

    def read_file(self, filename):
        content = []

        with open(filename, "r") as file:
            for line in file:
                print(line)
                content.append(line.strip())

        return content

    def parse_instructions(self, line):
        result = 0

        instructions = re.findall("mul\(\d*,\d*\)", line)
        for instruction in instructions:
            values = list(map(int, instruction[4:-1].split(",")))
            result += int(values[0]) * int(values[1])

        return result

    def solve_part_1(self, input):
        solution = 0

        for line in input:
            solution += self.parse_instructions(line)

        return solution

    def solve_part_2(self, input):
        solution = 0

        line = "".join(input)
        instruction_groups = []

        end_idx = line.index("don't()")
        instruction_groups.append("do()" + line[:end_idx])
        line = line[end_idx + 7 :]

        while end_idx != -1:
            start_idx = line.index("do()") if "do()" in line else -1
            try:
                end_idx = (
                    line[start_idx:].index("don't()") + start_idx
                    if "don't()" in line
                    else -1
                )
            except:
                end_idx = -1
            if end_idx > start_idx:
                instruction_groups.append(line[start_idx:end_idx])
            else:
                instruction_groups.append(line[start_idx:])
            line = line[end_idx:]

        solution += sum(map(self.parse_instructions, instruction_groups))

        return solution


if __name__ == "__main__":
    day1 = Day2()
    day1.solve_day()
