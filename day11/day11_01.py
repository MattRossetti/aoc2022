class Monkey:
    def __init__(self, id, starting_items, operation, test):
        self.id = id
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.inspection_count = 0

    def incremenct_inspection(self):
        self.inspection_count += 1

    def add_item(self, item):
        self.items.append(item)

    def __repr__(self):
        repr_str = f"""Monkey with the following Attributes:
Items: {self.items}
Operation: {self.operation}
Test: {self.test}"""
        return repr_str


def monkey_from_buffer(monkey_buffer):
    id = monkey_buffer[0][-2]
    starting_items = monkey_buffer[1].replace(",", "").split()[2:]
    # operation structure: tuple(operation, value)
    operation = tuple(monkey_buffer[2].split()[-2:])
    # test structure: tuple(divisible by value, if true id, if monkey id)
    test_value = int(monkey_buffer[3].split()[-1])
    test_true = int(monkey_buffer[4].split()[-1])
    test_false = int(monkey_buffer[5].split()[-1])
    test = tuple([test_value, test_true, test_false])
    return Monkey(id, starting_items, operation, test)


with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    monkeys = []
    monkey_buffer = []
    for line in lines:
        if line == "":
            monkeys.append(monkey_from_buffer(monkey_buffer))
            monkey_buffer = []
            continue
        monkey_buffer.append(line)
    monkeys.append(monkey_from_buffer(monkey_buffer))
    monkey_buffer = []

rounds = 20
for _ in range(rounds):
    for monkey in monkeys:
        remove_list = []
        for item in monkey.items:
            monkey.incremenct_inspection()
            worry_level = int(item)
            if monkey.operation[1] == "old":
                worry_level = pow(worry_level, 2)
            else:
                operator = monkey.operation[0]
                if operator == "*":
                    worry_level = worry_level * int(monkey.operation[1])
                if operator == "+":
                    worry_level = worry_level + int(monkey.operation[1])
            worry_level = worry_level // 3
            if worry_level % monkey.test[0] == 0:
                monkeys[monkey.test[1]].items.append(worry_level)
            else:
                monkeys[monkey.test[2]].items.append(worry_level)
            remove_list.append(item)
        for item in remove_list:
            monkey.items.remove(item)

inspection_counts = []
for monkey in monkeys:
    inspection_counts.append(monkey.inspection_count)

inspection_counts.sort()
top_two = inspection_counts[-2:]
answer = top_two[0] * top_two[1]
print("answer: ", answer)
