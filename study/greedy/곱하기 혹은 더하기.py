# 0또는 1이면 더하고, 0이 아니면 곱한다

numbers = list(map(int, input()))
answer = numbers[0]

for i in range(1, len(numbers)):
    if answer <= 1 or numbers[i] <= 1:
        answer += numbers[i]
    else:
        answer *= numbers[i]

print(answer)