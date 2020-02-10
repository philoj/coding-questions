Run the script by:
`(venv)$ python cli_script.py`
and follow instructions.

Exercises:
1. #Sum of pairs:
    - Given an array of size n, find the unique pairs of elements whose sum will be equal to given value K. An element can occur in only one pair. Print “None” if there is no pair whose sum is equal to K.
    - Samples:
        1. 
            - Enter target sum, K: 10
            - Enter array elements: 3, 1, 7, 9, 8
            - Pairs whose sum is K: (3, 7), (1,9)
        2. 
            - Enter target sum, K: 10
            - Enter array elements: 3, 4, 7, 3, 7
            - Pairs whose sum is K: (3, 7)
        3. 
            - Enter target sum, K: 10
            - Enter array elements: 3, 4, 7, 5, 7, 23
            - Pairs whose sum is K: (3, 7)
2. #Equilibrium Position:
    - Given an array of N elements, find the equilibrium position of the array. Equilibrium position in an array is the index of the element in the array such that the sum of elements before it is equal to the sum of elements after it. If there is no equilibrium position, print -1
    - Samples:
        1.
            - Enter elements: 4, 5, 1, 8 
            - Equilibrium position: -1
        2.
            - Enter elements: 4, 5, 1, 8, 1
            - Equilibrium position: 2
        3.
            - Enter elements: 15, 10, 5, 4, 2, 1, 3
            - Equilibrium position: 1
3. #Special Substring:
    - A string is said to be a special string if either of two conditions is met:
        1. All of the characters are the same, e.g. aaa.
        2. All characters except the middle one are the same, e.g. aadaa.
    - A special substring is any substring of a string which meets one of those criteria. Given a string, determine how many special substrings can be formed from it.
    - Samples:
        1.
            - Enter the string: asasd
            - Count of special substrings: 5
            - 'd', 's', 'sas', 'asa', 'a'
        2.
            - Enter the string: abcbaba
            - Count of special substrings: 6
            - 'aba', 'bcb', 'bab', 'b', 'a', 'c'
        3. 
            - Enter the string: aaacaaa
            - Count of special substrings: 7
            - 'a', 'aacaa', 'aaacaaa', 'aaa', 'aa', 'aca', 'c'