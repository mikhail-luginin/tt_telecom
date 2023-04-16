import re


def validate_serial_number(mask: str, serial_number: str) -> bool:
    """
        This method does validation for serial number.

        :param mask: mask from equipment type model for validation serial number
        :type mask: str

        :param serial_number: serial number for validate
        :type serial_number: str

        :rtype: bool
        :return: True if serial number passed validation else False
    """

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
