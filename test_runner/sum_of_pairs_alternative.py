"""
Note: This alternate script for sum_of_pairs.py is sensitive to the repetitions
of the same pair in the test case answer, even though it is not required by the problem definition.

Problem 1: Sum of pairs

Given an array of size n, find the unique pairs of elements whose sum will be equal to given value K.
An element can occur in only one pair. Print “None” if there is no pair whose sum is equal to K.

"""
from typing import List, Tuple


# Write your code inside this function.
# DO NOT modify the method signature
# DO NOT modify/remove any system generated code/comments

def DoWork(n, K, input):
    # n is the number of elements, an integer
    # K is the target sum, again an integer
    # input is the list of integers.
    # Expected return value is a list of two-tuples.

    # sum pairs for the given example [1, 2, 3, 4, 5, 6, 7] and sum 10:
    return [(3, 7), (4, 6)]


# DO NOT remove/modify the below line
# PLCHLDR_TSTCASES#
def remove_duplicate_pairs(pairs):
    # sort each of the 2-tuples to remove reversed pairs, which are duplicates
    return set(tuple(sorted(pair)) for pair in pairs)


def run_single_test_case(method, kwargs, actual_result, success_message):
    # In cases of a 'None' result, empty lists are used instead for simplicity.
    actual_result = actual_result or []
    try:
        result: 'List[Tuple[int, int]]' = method(**kwargs) or []
    except Exception as e:
        print(f"\t\t <fail>Exception raised during execution {type(e).__name__}: {e.__str__()}</fail>")
    else:
        # In order to make sure pair order doesn't affect the answer,
        # the pairs are sorted before checking for inclusion, so that (3,7) and (7,3) are treated the same.
        result = [tuple(sorted(pair)) for pair in result]
        actual_result = [tuple(sorted(pair)) for pair in actual_result]
        actual_result_copy = actual_result.copy()

        for pair in actual_result:
            if pair in result:
                # pair has been found. Clear from both lists.
                result.remove(pair)
                actual_result_copy.remove(pair)
            else:
                # failed to find a pair
                print(f"\t\t <fail>Failed to find all the pairs.</fail>")
                return

        # result_copy must be empty by now
        if result:
            # this means invalid pairs are present in the result
            print(f"\t\t <fail>Invalid pairs are found in the result.</fail>")

        # actual_result_copy must be empty by now.
        elif actual_result_copy:
            # this means all pairs are not found
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
                  'actual_result': [(1, 9), (3, 7)],
                  'success_message': 'Test succeeded.',
              }, {
                  'n': 5,
                  'K': 10,
                  'input': [3, 4, 7, 3, 7],
                  'actual_result': [(3, 7), (3, 7)],
                  'success_message': 'Test succeeded.',
              }, {
                  'n': 6,
                  'K': 10,
                  'input': [3, 4, 7, 5, 7, 23],
                  'actual_result': [(3, 7)],
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
