from PyInquirer import prompt

from sample_solutions.solutions.equilibrium_position import equilibrium_position
from sample_solutions.input_validation import validate_integer
from sample_solutions.solutions.special_substring import special_substring
from sample_solutions.solutions.sum_of_pairs import sum_of_pairs

SUM_OF_PAIRS = 'Sum of pairs'
EQUILIBRIUM_POSITION = 'Equilibrium Position'
SPECIAL_SUBSTRING = 'Special Substring'

QUESTIONS = (SUM_OF_PAIRS, EQUILIBRIUM_POSITION, SPECIAL_SUBSTRING)
cli_questions = [
    {
        'type': 'list',
        'name': 'question',
        'message': 'Choose an exercise to run:',
        'choices': [
            SUM_OF_PAIRS,
            EQUILIBRIUM_POSITION,
            SPECIAL_SUBSTRING,
        ]
    },
    {
        'when': lambda ans: ans['question'] == SUM_OF_PAIRS,
        'type': 'input',
        'name': 'sum',
        'message': 'Enter target sum, K:',
        'validate': lambda val: validate_integer(val) or 'Please enter integers only.',
        'filter': int,
    },
    {
        'when': lambda ans: ans['question'] in {SUM_OF_PAIRS, EQUILIBRIUM_POSITION},
        'type': 'input',
        'name': 'elements',
        'message': 'Enter the array of integers separated by comma:',
        'validate': lambda val: not any(
            not validate_integer(v) for v in val.strip(',').split(',')
        ) or 'Please enter integers only.',
        'filter': lambda val: [int(v) for v in val.strip(',').split(',')]
    },
    {
        'when': lambda ans: ans['question'] == SPECIAL_SUBSTRING,
        'type': 'input',
        'name': 'full_string',
        'message': 'Enter the string:'
    }
]

if __name__ == '__main__':
    answers = prompt(cli_questions)

    if answers['question'] == SUM_OF_PAIRS:
        pairs = sum_of_pairs(answers['sum'], answers['elements'])
        print('Unique pairs: ', end='')
        print(' '.join(f"({pair[0]}, {pair[1]})" for pair in pairs) if pairs else None)
    elif answers['question'] == EQUILIBRIUM_POSITION:
        print(f"Equilibrium position: {equilibrium_position(answers['elements'])}")
    elif answers['question'] == SPECIAL_SUBSTRING:
        matches = special_substring(answers['full_string'])
        if matches:
            print(f"Count of special substrings: {len(matches)}")
            print(', '.join(f"'{sub}'" for sub in matches))
        else:
            print('No matching special substrings.')
