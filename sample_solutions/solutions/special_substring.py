import re
import typing

SPECIAL_STRING_REGEX = r'((\w)\2*)(?:\w\1)?'


def special_substring(full_string) -> 'typing.List[str]':
    matches = set()
    string_to_match = full_string
    while string_to_match:
        match = re.match(SPECIAL_STRING_REGEX, string_to_match)
        if match:
            match_start = match.start()
            matches.add(string_to_match[match_start: match.end()])

            # restart the search from next character
            # so that overlapping matches are also found.
            string_to_match = string_to_match[match_start + 1:]
        else:
            # no more matches
            break
    return [m for m in matches]
