import json

with open('/media/suman/7CEAECBCEAEC7434/Canon 1300D/python/example_2.json', mode='r') as jsonfile:
    example = json.load(jsonfile)
    quiz = example['quiz']
    question_1 = quiz['sport']
    print(question_1['q1']['question'])



