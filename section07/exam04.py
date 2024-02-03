exam = [99, 78, 100, 91, 81, 85, 54, 100, 71, 50]
score = []
for num in exam:
    num += 5
    if num > 100: num = 100
    score.append(num)
print(score)