li = [input() for _ in range(3)]

FizzBuzz = ["Fizz", "Buzz", "FizzBuzz"]
for idx, item in enumerate(li):
    if item not in FizzBuzz:
        target = int(item) + 3 - idx

if target % 3 == 0 and target % 5 == 0:
    answer = FizzBuzz[2]
elif target % 3 == 0:
    answer = FizzBuzz[0]
elif target % 5 == 0:
    answer = FizzBuzz[1]
else:
    answer = target

print(answer)
