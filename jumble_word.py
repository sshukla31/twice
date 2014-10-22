"""
This module performs word jumble operation.
The program accepts a string as input, and then return a list of words that can be created using the submitted letters. For example, on the input "dog", the program should return a set of words including "god", "do", and "go".
"""

def permutation(word, k=0, result=None):
    """
    Perform word permutation
    Args:
        word (str): Word to perform permutation on
        k=0 (int): Start index
        result (list): List to store final result
    Returns:
        result (list): List of permuted words
    Exception:
        None
    """
    if k == len(word):
        result += ["".join(map(str, word))]
    else:
        for index in range(k, len(word)):
            word[k], word[index] = word[index], word[k]
            permutation(word, k + 1, result)
            word[k], word[index] = word[index], word[k]

    return result


def combination(k, available, used):
    """
    Perform word combination
    Args:
        k=2 (int): combinations word count
        available (str): Word to perform combination on
        used (list): List to store final result
    Returns:
        used (list): List of word combinations
    Exception:
        None
    """
    if len(used) == k:
        yield list(used)
    elif len(available) == 0:
        pass
    else:
        head = available.pop(0)
        used.append(head)
        for c in combination(k, available, used):
            yield c
        used.pop()
        for c in combination(k, available, used):
            yield c
        available.insert(0, head)


def search_file(word):
    """
    Search file for a given word
    Args:
        word(string): String to be searched in File
    Returns:
        True in case of success or False
    Exception:
        OSError and IOError
    """
    try:
        with open('en_US.dic') as inf:
            for line in inf:
                if word.lower() == line.partition("/")[0].lower():
                    return True
    except (OSError, IOError) as ex:
        raise ex

    return False


def run(query):
    """ Return result for jumbled words """
    combs = []
    result = []
    for k in range(2, len(query) + 1):
        for word in combination(k, list(query), []):
            for element in permutation(word=word, result=[]):
                if "".join(element) not in result and search_file("".join(element)):
                    result.append("".join(element))

    return sorted(result)


if __name__ == '__main__':
    query = raw_input("Input word : ").strip()
    if len(query) == 0:
        print "Please enter some value"
    else:
        print run(query)
