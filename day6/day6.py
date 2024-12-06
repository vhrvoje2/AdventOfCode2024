directions = {"UP": (-1, 0), "DOWN": (1, 0), "LEFT": (0, -1), "RIGHT": (0, 1)}
next_directions = {"UP": "RIGHT", "RIGHT": "DOWN", "DOWN": "LEFT", "LEFT": "UP"}


class Day6:
    def __init__(self):
        self.test = self.read_file("test.txt")
        self.input = self.read_file("input.txt")

    def solve_day(self):
        print("Part 1 test:\t", self.solve_part_1(self.test))
        print("Part 1 input:\t", self.solve_part_1(self.input))
        # print("Part 2 test:\t", self.solve_part_2(self.test))
        # print("Part 2 input:\t", self.solve_part_2(self.input))

    def read_file(self, filename):
        content = []

        with open(filename, "r") as file:
            for line in file:
                content.append(line.strip())

        return content

    def get_start_position(self, map):
        start = None

        for y, line in enumerate(map):
            for x, char in enumerate(line):
                if char == "^":
                    start = (y, x)
                    break

            if start != None:
                break

        return start

    def visualize(self, map, y, x, visited):
        for _y, line in enumerate(map):
            for _x, _ in enumerate(line):
                if (_y, _x) == (y, x) or (_y, _x) in visited:
                    print("X", end="")
                else:
                    print(map[_y][_x], end="")
            print()

        print()

    def solve_part_1(self, input):
        solution = 0

        visited = set()
        start_pos = self.get_start_position(input)
        y, x = start_pos

        curr_dir = "UP"

        while True:
            visited.add((y, x))
            new_y = y + directions[curr_dir][0]
            new_x = x + directions[curr_dir][1]
            # self.visualize(input, y, x, visited)

            if new_y < 0 or new_y >= len(input) or new_x < 0 or new_x >= len(input[y]):
                break

            if input[new_y][new_x] == "#":
                curr_dir = next_directions[curr_dir]
                continue

            y = new_y
            x = new_x

        solution += len(visited)
        return solution

    def solve_part_2(self, input):
        solution = 0

        return solution


if __name__ == "__main__":
    day1 = Day6()
    day1.solve_day()
