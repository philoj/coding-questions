def validate_integer(value):
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        return False
