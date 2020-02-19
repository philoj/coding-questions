# Write your code inside this function.
# DO NOT modify the method signature
# DO NOT modify/remove any system generated code/comments


def DoWork(n, input):
    return "Hello " + input


# DO NOT remove/modify the below line
# PLCHLDR_TSTCASES#
ERROR_CLASSES_TO_SUPPRESS = set()


def run_single_test_case(method, kwargs, actual_result, failure_message):
    try:
        result = method(**kwargs)
        if result != actual_result:
            print(f"\t\t <fail>{failure_message}</fail>")
    except Exception as e:
        print(f"\t\t <fail>{failure_message}</fail>")
        if type(e) not in ERROR_CLASSES_TO_SUPPRESS:
            raise


def run_test_case():
    for case in TEST_CASES:
        failure_message = case.pop('failure_message')
        actual_result = case.pop('actual_result')
        run_single_test_case(DoWork, case, actual_result, failure_message)


TEST_CASES = ({
                  'n': 4,
                  'input': [4, 5, 1, 8],
                  'actual_result': -1,
                  'failure_message': 'Test failed for input without equilibrium position'
              }, {
                  'n': 5,
                  'input': [4, 5, 1, 8, 1],
                  'actual_result': 2,
                  'failure_message': 'Test failed to find equilibrium position.'
              }, {
                  'n': 7,
                  'input': [15, 10, 5, 4, 2, 1, 3],
                  'actual_result': 1,
                  'failure_message': 'Test failed for input with an early equilibrium position.'
              })
n_ = 7
input_ = [1, 2, 3, 4, 5, 6, 7]
result_ = DoWork(n_, input_)
print(f"Result: {result_}")

run_test_case()

# DO NOT remove/modify the below line
# PLCHLDR_TSTCASE_EXE#
