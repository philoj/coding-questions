from PyInquirer import prompt

from input_validation import validate_integer
from sum_of_pairs import sum_of_pairs

QUESTION_1 = '1: Sum of pairs'
QUESTION_2 = '2: Equilibrium Position'
QUESTION_3 = '3: Special Substring'
QUESTIONS = (QUESTION_1, QUESTION_2, QUESTION_3)
cli_choose_question = [{
    'type': 'list',
    'name': 'question',
    'message': 'Choose an exercise to run:',
    'choices': [
        {
            'name': QUESTION_1
        },
        {
            'name': QUESTION_2
        },
        {
            'name': QUESTION_3
        },
    ],
    'default': 0
}]

if __name__ == '__main__':
    answers = prompt(cli_choose_question)
    question = answers['question']
    if question == QUESTION_1:
        sum_of_pairs_questions = [
            {
                'type': 'input',
                'name': 'sum',
                'message': 'Enter target sum, K:',
                'validate': lambda val: validate_integer(val) or 'Please enter integers only.'
            },
            {
                'type': 'input',
                'name': 'elements',
                'message': 'Enter array elements separated by comma:',
                'validate': lambda val: not any(
                    not validate_integer(v) for v in val.split(',')
                ) or 'Please enter integers only.'
            }
        ]
        answers = prompt(sum_of_pairs_questions)
        target_sum = int(answers['sum'])
        elements = [int(val) for val in answers['elements'].split(',')]
        print(sum_of_pairs(target_sum, elements))

    elif question == QUESTION_2:
        pass
    elif question == QUESTION_3:
        pass
