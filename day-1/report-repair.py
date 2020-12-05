# PART ONE #

with open('report.txt') as report_file:
    report_lines = [report_line.rstrip() for report_line in report_file]

report_lines = [int(report_line) for report_line in report_lines]

for line_1 in report_lines:
    for line_2 in report_lines:
        if line_1 + line_2 == 2020:
            print(line_1 * line_2)

# PART TWO #

for line_1 in report_lines:
    for line_2 in report_lines:
        for line_3 in report_lines:
            if line_1 + line_2 + line_3 == 2020:
                print(line_1 * line_2 * line_3)
