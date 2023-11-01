def find_ways(target):
    def backtrack(current, expression, idx):
        if idx == 9:
            if eval(expression) == target:
                results.append(expression)
            return
        for operator in "+- ":
            if operator == ' ':
                new_expression = expression + str(numbers[idx])
                backtrack(current + numbers[idx], new_expression, idx + 1)
            else:
                new_expression = expression + operator + str(numbers[idx])
                new_current = eval(str(current) + operator + str(numbers[idx]))
                backtrack(new_current, new_expression, idx + 1)

    numbers = [i for i in range(1, 10)]
    results = []
    backtrack(numbers[0], str(numbers[0]), 1)
    return results

target = int(input())
solutions = find_ways(target)
print(len(solutions))
