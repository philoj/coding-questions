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


def run_tests(method, test_cases):
    for case in test_cases:
        failure_message = case.pop('failure_message')
        actual_result = case.pop('actual_result')
        run_single_test_case(method, case, actual_result, failure_message)
