import typing


def sum_of_pairs(target_sum: int, elements: 'typing.List[int]') -> 'typing.List[typing.Tuple[int,int]]':
    """
    Given an array of size n, find the unique pairs of elements whose sum will be equal to given value K.
    An element can occur in only one pair. Print “None” if there is no pair whose sum is equal to K.
    :param target_sum: K
    :param elements:
    :return:
    """
    # make the input unique and sort
    sorted_elements = list(sorted(set(elements)))
    pairs = []

    # iterate until second last element in the sorted list
    for index, element in enumerate(sorted_elements[:-1], start=0):
        if element > target_sum:
            # no point in further iteration. break
            break
        else:
            # element is smaller or equal to sum

            # the required pair for this element to sum upto the target_sum:
            required_element = target_sum - element

            # (there is no need to look into already iterated elements or current element)
            if required_element in sorted_elements[index + 1:]:
                pairs.append((element, required_element))
    return pairs
