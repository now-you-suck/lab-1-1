def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Îøèáêà: ââåäèòå ÷èñëî")


def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Îøèáêà: äåëåíèå íà íîëü"
# Îñíîâíàÿ ïðîãðàììà
print("Óëó÷øåííûé êàëüêóëÿòîð")
print("Äîñòóïíûå îïåðàöèè: +, -, *, /, ^, sqrt")

