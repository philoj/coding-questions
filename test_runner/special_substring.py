from typing import Set, List


# Write your code inside this function.
# DO NOT modify the method signature
# DO NOT modify/remove any system generated code/comments


def DoWork(input: str) -> 'List[str]':
    return ["Hello ", input]


# DO NOT remove/modify the below line
# PLCHLDR_TSTCASES#
def validate_single_substring(sub_string: str, actual_result: 'Set[str]'):
    if sub_string in actual_result:
        actual_result.discard(sub_string)
        return True


def run_single_test_case(method, kwargs, actual_result: 'Set[str]', success_message):
    try:
        result: 'List[str]' = method(**kwargs)
    except Exception as e:
        print(f"\t\t <fail>Exception raised during execution {type(e).__name__}: {e.__str__()}</fail>")
    else:
        # remove duplicates
        result_set = set(result)

        if any(not validate_single_substring(sub_string, actual_result) for sub_string in result_set):
            # some sub strings were not valid
            print(f"\t\t <fail>There are invalid sub strings in the result.</fail>")

        # if all sub strings are found, actual_result would be empty by now
        elif len(actual_result) != 0:
            print(f"\t\t <fail>Failed to find all the sub strings.</fail>")
        else:
            print(f"\t\t  <success>{success_message}</success>")


def run_test_case():
    for case in TEST_CASES:
        success_message = case.pop('success_message')
        actual_result = case.pop('actual_result')
        run_single_test_case(DoWork, case, actual_result, success_message)


TEST_CASES = ({
                  'input': 'asasd',
                  'actual_result': {'a', 's', 'd', 'asa', 'sas'},
                  'success_message': 'Test succeeded.'
              }, {
                  'input': 'abcbaba',
                  'actual_result': {'a', 'b', 'c', 'bcb', 'bab', 'aba'},
                  'success_message': 'Test succeeded.',
              }, {
                  'input': 'aaacaaa',
                  'actual_result': {'a', 'c', 'aa', 'aaa', 'aca', 'aacaa', 'aaacaaa'},
                  'success_message': 'Test succeeded.',
              })
# input_ = "asasds"
# result_ = DoWork(input_)
# print(f"Result: {result_}")

run_test_case()

# DO NOT remove/modify the below line
# PLCHLDR_TSTCASE_EXE#
