import utils.utils as utils


answers = utils.open_file('answers.txt')

# PART ONE #
already_answered = []
questions_count = 0

for answer in answers:
    if not answer:
        questions_count += len(already_answered)
        already_answered = []
        continue

    for question in answer:
        if question not in already_answered:
            already_answered.append(question)

print(questions_count)

# PART TWO #
questions_count = 0
people_in_group_count = 0
questions_answered = {}

for answer in answers:
    if not answer:
        for question_answered in questions_answered:
            if questions_answered[question_answered] == people_in_group_count:
                questions_count += 1
        people_in_group_count = 0
        questions_answered = {}
        continue

    people_in_group_count += 1

    for question in answer:
        if question not in questions_answered:
            questions_answered[question] = 0
        questions_answered[question] += 1

print(questions_count)
