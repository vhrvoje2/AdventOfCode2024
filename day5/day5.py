class Day5:
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

    def parse_pages(self, pages):
        parsed_pages = []

        for page in pages:
            nums = list(map(int, page.split(",")))
            parsed_pages.append(nums)

        return parsed_pages

    def validate_pages(self, pages, rules):
        valid_pages = []

        for page in pages:
            page_valid = True
            for rule in rules:
                rule1, rule2 = list(map(int, rule.split("|")))
                if rule1 in page and rule2 in page:
                    rule1_idx = page.index(rule1)
                    rule2_idx = page.index(rule2)
                    if rule1_idx > rule2_idx:
                        page_valid = False
                        break
            if page_valid:
                valid_pages.append(page)

        return valid_pages

    def solve_part_1(self, input):
        solution = 0

        separator = input.index("")
        rules = input[:separator]
        pages = input[separator + 1 :]
        pages = self.parse_pages(pages)

        valid_pages = self.validate_pages(pages, rules)

        for page in valid_pages:
            solution += page[len(page) // 2]

        return solution

    def solve_part_2(self, input):
        solution = 0

        separator = input.index("")
        rules = input[:separator]
        pages = input[separator + 1 :]
        pages = self.parse_pages(pages)

        valid_pages = self.validate_pages(pages, rules)
        invalid_pages = [page for page in pages if page not in valid_pages]

        for page in invalid_pages:
            apply_rules = True
            while apply_rules:
                count = 0
                for rule in rules:
                    rule1, rule2 = list(map(int, rule.split("|")))
                    if rule1 in page and rule2 in page:
                        rule1_idx = page.index(rule1)
                        rule2_idx = page.index(rule2)
                        if rule1_idx > rule2_idx:
                            tmp = page[rule2_idx]
                            page[rule2_idx] = page[rule1_idx]
                            page[rule1_idx] = tmp
                            count += 1

                apply_rules = count > 0

        for page in invalid_pages:
            solution += page[len(page) // 2]

        return solution


if __name__ == "__main__":
    day1 = Day5()
    day1.solve_day()
