directions = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
    (1, 1),
    (1, -1),
    (-1, 1),
    (-1, -1),
]


class Day4:
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

    def solve_part_1(self, input):
        solution = 0

        for y, line in enumerate(input):
            for x, letter in enumerate(line):
                if letter == "X":
                    for direction in directions:
                        l = []
                        l.append(input[y][x])
                        dx = x + direction[0]
                        dy = y + direction[1]
                        for _ in range(3):
                            if 0 <= dx < len(line) and 0 <= dy < len(input):
                                l.append(input[dy][dx])
                            else:
                                break
                            dx += direction[0]
                            dy += direction[1]
                        if "".join(l) == "XMAS":
                            solution += 1

        return solution

    def solve_part_2(self, input):
        solution = 0

        for y, line in enumerate(input):
            for x, letter in enumerate(line):
                if letter == "A":
                    # check top left bottom right
                    tl_y = y - 1
                    tl_x = x - 1
                    br_y = y + 1
                    br_x = x + 1
                    if (
                        0 <= tl_y < len(input)
                        and 0 <= tl_x < len(line)
                        and 0 <= br_y < len(input)
                        and 0 <= br_x < len(line)
                    ):
                        tl_c = input[tl_y][tl_x]
                        br_c = input[br_y][br_x]
                    else:
                        continue

                    # check top right bottom left
                    tr_y = y - 1
                    tr_x = x + 1
                    bl_y = y + 1
                    bl_x = x - 1
                    if (
                        0 <= tr_y < len(input)
                        and 0 <= tr_x < len(line)
                        and 0 <= bl_y < len(input)
                        and 0 <= bl_x < len(line)
                    ):
                        tr_c = input[tr_y][tr_x]
                        bl_c = input[bl_y][bl_x]
                    else:
                        continue

                    chars = [tl_c, tr_c, br_c, bl_c]

                    if (
                        not all(char in ["M", "S"] for char in chars)
                        or not "M" in chars
                        or not "S" in chars
                    ):
                        continue

                    if (tl_c == tr_c and bl_c == br_c) or (
                        tl_c == bl_c and tr_c == br_c
                    ):
                        assert chars.count("M") == 2
                        assert chars.count("S") == 2
                        solution += 1

        return solution


if __name__ == "__main__":
    day1 = Day4()
    day1.solve_day()
