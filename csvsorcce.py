import csv
# For the average
from statistics import mean
# Sorted Dict
from collections import OrderedDict


def calculate_averages(input_file_name, output_file_name):
    averages = OrderedDict()
    with open(input_file_name, "r") as file_1:
        file_1 = csv.reader(file_1, delimiter=',')
        for row in file_1:
            Scores = []
            for grades in range(1, len(row)):  # Because name = row[0]
                Scores.append(float(row[grades]))
            Avg = mean(Scores)
            averages[row[0]] = Avg
    with open(output_file_name, "w") as out:
        count = 0
    for name in averages:
        count += 1
        if count == 1:
            out.write(name + "," + str(averages[name]))
        else:
            out.write("\n" + name + "," + str(averages[name]))


def calculate_sorted_averages(input_file_name, output_file_name):
    averages = {}
    with open(input_file_name) as file_1:
        file_1 = csv.reader(file_1, delimiter=',')
    for row in file_1:
        Scores = []
        for grades in range(1, len(row)):
            Scores.append(float(row[grades]))
        avg = mean(Scores)
        averages[row[0]] = avg
    averages_ord = OrderedDict(
        sorted(averages.items(), key=lambda x: (x[1], x[0])))  # لامبدا تابع موقت هست و این خط از کد دیکت رو سورت میکند

    with open(output_file_name, 'w') as out:
        count = 0
        for name in averages_ord:
            count += 1
            if count == 1:
                out.write(name + "," + str(averages_ord[name]))
            else:
                out.write("\n" + name + "," + str(averages_ord[name]))


def calculate_three_best(input_file_name, output_file_name):
    averages = {}
    with open(input_file_name) as file_1:
        file_1 = csv.reader(file_1, delimiter=',')
    for row in file_1:
        Scores = []
        for grades in range(1, len(row)):
            Scores.append(float(row[grades]))
        avg = mean(Scores)
        averages[row[0]] = avg
    average_ord = OrderedDict(sorted(averages.items(), key=lambda x: (-x[1], x[0])))
    with open(output_file_name, "w") as out:
        best = []
        for row in range(3):
            best_avg = average_ord.popitem(last=False)
            best.append(best_avg)
        out.write(best[0][0] + "," + str(best[0][1]))
        out.write(best[1][0] + "," + str(best[1][1]))
        out.write(best[2][0] + "," + str(best[2][1]))


def calculate_three_worst(input_file_name, output_file_name):
    averages = {}
    with open(input_file_name) as file_1:
        file_1 = csv.reader(file_1, delimiter=',')
        for row in file_1:
            scores = []
            for i in range(1, len(row)):
                scores.append(float(row[i]))
            avg = mean(scores)
            averages[row[0]] = avg

    averages_ord = OrderedDict(sorted(averages.items(), key=lambda x: (x[1], x[0])))

    with open(output_file_name, 'w') as out:
        worst = []
        for i in range(3):
            worst_avg = averages_ord.popitem(last=False)
            worst.append(worst_avg)

        out.write(str(worst[0][1]) + "\n")
        out.write(str(worst[1][1]) + "\n")
        out.write(str(worst[2][1]))


def calculate_average_of_averages(input_file_name, output_file_name):
    averages = {}
    with open(input_file_name) as file_1:
        file_1 = csv.reader(file_1, delimiter=',')
        for row in file_1:
            scores = []
            for i in range(1, len(row)):
                scores.append(float(row[i]))
            avg = mean(scores)
            averages[row[0]] = avg

    averages_ord = OrderedDict(sorted(averages.items(), key=lambda x: (x[1], x[0])))

    SUM = 0
    count = 0
    for average in averages_ord:
        count += 1
        SUM += float(averages_ord[average])
    avg_avg = SUM / count
    with open(output_file_name, 'w') as out:
        out.write(str(avg_avg))
