import csv
from collections import OrderedDict
from statistics import mean

averages = {}
with open("grades.csv") as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        # print(row)
        # name = row[0]
        Scores = []
        # the list will contain integer form of grades
        for grade in range(1, len(row)):
            Scores.append(float(row[grade]))
        Avg = mean(Scores)
        averages[row[0]] = Avg
    count = 0
    for name in averages:
        count += 1
        if count == 1:
            print(name + "," + str(averages[name]))
        else:
            print(name + "," + str(averages[name]))

print("//////////////////// FINISH TASK ONE /////////////////////")

averages_ord = OrderedDict(sorted(averages.items(), key=lambda x: (x[1], x[0])))  # sort by scores
for key, value in averages_ord.items():
    print(key, value)
print("//////////////////// FINISH TASK TWO /////////////////////")

averages_ord = OrderedDict(sorted(averages.items(), key=lambda x: (-x[1], x[0])))
best = []
for i in range(3):
    best_avg = averages_ord.popitem(last=False)
    best.append(best_avg)
print(best[0][0] + "," + str(best[0][1]))
print(best[1][0] + "," + str(best[1][1]))
print(best[2][0] + "," + str(best[2][1]))

print("//////////////////// FINISH TASK THREE /////////////////////")

averages_ord = OrderedDict(sorted(averages.items(), key=lambda x: (x[1], x[0])))
worst = []
for i in range(3):
    worst_avg = averages_ord.popitem(last=False)
    worst.append(worst_avg)
print(str(worst[0][1]))
print(str(worst[1][1]))
print(str(worst[2][1]))

print("//////////////////// FINISH TASK FOUR /////////////////////")

averages_ord = OrderedDict(sorted(averages.items(), key=lambda x: (x[1], x[0])))
SUM = 0
count = 0
for averages in averages_ord:
    count += 1
    SUM += float(averages_ord[averages])
avg_of_avg = SUM / count
print(str(avg_of_avg))

print("//////////////////// FINISH TASK FIVE /////////////////////")
