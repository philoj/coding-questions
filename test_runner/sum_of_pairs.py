from typing import List, Set, Tuple


# Write your code inside this function.
# DO NOT modify the method signature
# DO NOT modify/remove any system generated code/comments

def DoWork(n: int, K: int, input: 'List[int]') -> 'List[Tuple[int, int]]':
    return []


# DO NOT remove/modify the below line
# PLCHLDR_TSTCASES#


def validate_pair_found(pair_found: 'Tuple[int, int]', actual_result: 'Set[Tuple[int,int]]'):
    # verify the length, make sure either the given tuple or its reversed version is part of the solution
    if len(pair_found) == 2:

        # handle reversed pairs also. For ex., (3,7) and (7,3) are equally valid.
        reversed_pair = pair_found[::-1]
        if pair_found in actual_result or reversed_pair in actual_result:
            actual_result.discard(pair_found)
            actual_result.discard(reversed_pair)
            return True


def run_single_test_case(method, kwargs, actual_result, success_message):
    try:
        result: 'List[Tuple[int, int]]' = method(**kwargs)
    except Exception as e:
        print(f"\t\t <fail>Exception raised during execution {type(e).__name__}: {e.__str__()}</fail>")
    else:
        # remove duplicates
        result_set = set(result)

        if any(not validate_pair_found(pair, actual_result) for pair in result_set):
            # some pairs were not valid
            print(f"\t\t <fail>There are invalid pairs in the result.</fail>")
        # if all pairs are found, actual_result would be empty by now
        elif len(actual_result) != 0:
            print(f"\t\t <fail>Failed to find all the pairs.</fail>")
        else:
            print(f"\t\t  <success>{success_message}</success>")


def run_test_case():
    for case in TEST_CASES:
        success_message = case.pop('success_message')
        actual_result = case.pop('actual_result')
        run_single_test_case(DoWork, case, actual_result, success_message)


TEST_CASES = ({
                  'n': 5,
                  'K': 10,
                  'input': [3, 1, 7, 9, 8],
                  'actual_result': {(1, 9), (3, 7)},
                  'success_message': 'Test succeeded.'
              }, {
                  'n': 5,
                  'K': 10,
                  'input': [3, 4, 7, 3, 7],
                  'actual_result': {(3, 7)},
                  'success_message': 'Test succeeded.',
              }, {
                  'n': 6,
                  'K': 10,
                  'input': [3, 4, 7, 5, 7, 23],
                  'actual_result': {(3, 7)},
                  'success_message': 'Test succeeded.',
              })
# n_ = 7
# input_ = [1, 2, 3, 4, 5, 6, 7]
# K_ = 10
# result_ = DoWork(n_, K_, input_)
# print(f"Result: {result_}")

run_test_case()

# DO NOT remove/modify the below line
# PLCHLDR_TSTCASE_EXE#
