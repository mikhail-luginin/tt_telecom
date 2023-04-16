import re


def validate_serial_number(mask, serial_number):
    if len(serial_number) > 10:
        return False
    pattern = ""
    for char in mask:
        match char:
            case "N":
                pattern += "\d"
            case "A":
                pattern += "[A-Za-z]"
            case "a":
                pattern += "[a-z]"
            case "X":
                pattern += "[A-Za-z0-9]"
            case "Z":
                pattern += "[-_@]"
            case _:
                pattern += re.escape(char)
    return bool(re.match(pattern, serial_number))
