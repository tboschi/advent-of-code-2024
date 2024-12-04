def read(path: str) -> list[str]:
    """ Read a file into a list of lines """
    data = []
    with open(path) as file:
        for line in file:
            data.append(line.strip())
    return data


def read_test(test: str) -> list[str]:
    """ Split a test string into a list of lines """
    return test.splitlines()
