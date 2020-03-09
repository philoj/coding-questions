"""
Problem 3: Special Substring

A string is said to be a special string if either of two conditions is met:
    - All of the characters are the same, e.g. aaa.

    - All characters except the middle one are the same, e.g. aadaa.

A special substring is any substring of a string which meets one of those criteria.
Given a string, determine how many special substrings can be formed from it.
For example, given the string s = mnonopoo , we have the following special substrings:
    {m, n, o, n, o, p, o ,o, non, ono, opo, oo}
Write a program to accept a string, and print out the count of special substrings along with the special substrings.
"""
from typing import Set, List


# Write your code inside this function.
# DO NOT modify the method signature
# DO NOT modify/remove any system generated code/comments


def DoWork(input):
    # input is a string
    # Expected return value is the list of all special substrings

    # special substrings for the given example 'asasds':
    return ['asa', 'd', 'sds', 's', 'sas', 'a']


# DO NOT remove/modify the below line
# PLCHLDR_TSTCASES#

def run_single_test_case(method, kwargs, actual_result: 'Set[str]', failure_message, success_message):
    try:
        result: 'List[str]' = method(**kwargs)
    except Exception as e:
        print(f"\t\t <fail>Exception raised during execution {type(e).__name__}: {e.__str__()}</fail>")
    else:
        # remove duplicates
        result_set = set(result)
        if actual_result != result_set:
            print(f"\t\t <fail>{failure_message}</fail>")
        else:
            print(f"\t\t  <success>{success_message}</success>")


def run_test_case():
    for case in TEST_CASES:
        success_message = case.pop('success_message')
        failure_message = case.pop('failure_message')
        actual_result = case.pop('actual_result')
        run_single_test_case(DoWork, case, actual_result, failure_message, success_message)


TEST_CASES = ({
                  'input': 'asasd',
                  'actual_result': {'a', 's', 'd', 'asa', 'sas'},
                  'success_message': 'Test succeeded.',
                  'failure_message': 'Failed to find all the sub strings.'
              }, {
                  'input': 'abcbaba',
                  'actual_result': {'a', 'b', 'c', 'bcb', 'bab', 'aba'},
                  'success_message': 'Test succeeded.',
                  'failure_message': 'Failed to find all the sub strings.'
              }, {
                  'input': 'aaacaaa',
                  'actual_result': {'a', 'c', 'aa', 'aaa', 'aca', 'aacaa', 'aaacaaa'},
                  'success_message': 'Test succeeded.',
                  'failure_message': 'Failed to find all the sub strings.'
              })
# input_ = "asasds"
# result_ = DoWork(input_)
# print(f"Result: {result_}")

run_test_case()

# DO NOT remove/modify the below line
# PLCHLDR_TSTCASE_EXE#
