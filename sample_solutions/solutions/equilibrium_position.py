import typing


def equilibrium_position(elements: 'typing.List[int]') -> int:
    total_sum = sum(elements)
    for index, element in enumerate(elements, start=0):
        one_side_sum = (total_sum - element) / 2
        if sum(elements[:index]) == one_side_sum:
            return index
    return -1
