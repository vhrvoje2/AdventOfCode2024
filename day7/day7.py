from itertools import product


class Day7:
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

    def parse_equations(self, equations):
        ret = []

        for line in equations:
            eq = []
            result, nums = line.split(":")
            nums = nums.strip().split(" ")
            eq.append(result)
            eq.append(nums)
            ret.append(eq)

        return ret

    def evaluate_expression(self, exp):
        operation_count = len(exp) // 2
        while operation_count > 0:
            if exp[1] == "||":
                result = int(f"{exp[0]}{exp[2]}")
            else:
                operation = "".join(exp[:3])
                result = eval(operation)
            exp = exp[3:]
            exp.insert(0, f"{result}")
            operation_count -= 1

        return result

    def solve_part_1(self, input):
        solution = 0
        operators = ["+", "*"]
        results_set = set()

        equations = self.parse_equations(input)
        for eq in equations:
            result = int(eq[0])
            nums = eq[1]
            operators_count = len(nums) - 1
            operators_permutations = set(
                list(product(operators, repeat=operators_count))
            )

            for operator_list in operators_permutations:
                expression = []
                total_count = len(nums) + len(operator_list)
                num_idx = 0
                operator_idx = 0
                while total_count > 0:
                    if total_count % 2 != 0:
                        expression.append(nums[num_idx])
                        num_idx += 1
                    else:
                        expression.append(operator_list[operator_idx])
                        operator_idx += 1
                    total_count -= 1

                expression_result = self.evaluate_expression(expression)
                if result == expression_result:
                    results_set.add(result)

        solution += sum(list(results_set))
        return solution

    def solve_part_2(self, input):
        solution = 0
        operators = ["+", "*", "||"]
        results_set = set()

        equations = self.parse_equations(input)
        for eq in equations:
            result = int(eq[0])
            nums = eq[1]
            operators_count = len(nums) - 1
            operators_permutations = set(
                list(product(operators, repeat=operators_count))
            )

            for operator_list in operators_permutations:
                expression = []
                total_count = len(nums) + len(operator_list)
                num_idx = 0
                operator_idx = 0
                while total_count > 0:
                    if total_count % 2 != 0:
                        expression.append(nums[num_idx])
                        num_idx += 1
                    else:
                        expression.append(operator_list[operator_idx])
                        operator_idx += 1
                    total_count -= 1

                expression_result = self.evaluate_expression(expression)
                if result == expression_result:
                    results_set.add(result)

        solution += sum(list(results_set))
        return solution


if __name__ == "__main__":
    day1 = Day7()
    day1.solve_day()
