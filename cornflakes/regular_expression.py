def adding_ing(result: str):
    if len(result) >= 3 and result.endswith(r'ing'):
        value = result + "ly"
    elif len(result) >= 3 and not result.endswith(r'ing'):
        value = result + "ing"
    else:
        value = result
    return value
