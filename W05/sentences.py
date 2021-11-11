import random

def get_determiner(grammatical_number):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If grammatical_number == 1, this function will return
    either "the" or "one". Otherwise this function will
    return either "some" or "many".

    Parameter
        grammatical_number: an integer.
            If grammatical_number == 1, this function will return
            a determiner for a single noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if grammatical_number == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(grammatical_number):
    """Return a randomly chosen noun.
    If grammatical_number == 1, this function will
    return one of these ten single nouns:
        "adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"
    Otherwise, this function will return one of these
    ten plural nouns:
        "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"

    Parameter
        grammatical_number: an integer that determines
            if the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if grammatical_number == 1:
        nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    else:
        nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    # Randomly choose and return a determiner
    noun = random.choice(nouns)
    return noun

def get_verb(grammatical_number, tense):
    """Return a randomly chosen verb. If tense is "past", this
    function will return one of these ten verbs:
        "drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and grammatical_number is 1, this
    function will return one of these ten verbs:
        "drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and grammatical_number is NOT 1,
    this function will return one of these ten verbs:
        "drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
        "will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"

    Parameter
        grammatical_number: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought",
            "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if grammatical_number == 1:
            verbs = ["drinks", "eats", "grows", "laughs", "thinks",
                "runs", "sleeps", "talks", "walks", "writes"]
        else:
            verbs = ["drink", "eat", "grow", "laugh", "think",
                "run", "sleep", "talk", "walk", "write"]
    else:
        verbs = ["will drink", "will eat", "will grow", "will laugh",
            "will think", "will run", "will sleep", "will talk",
            "will walk", "will write"]
    verb = random.choice(verbs)
    return verb

def create_sentence(grammatical_number, tense):
    determiner = get_determiner(grammatical_number)
    noun = get_noun(grammatical_number)
    verb = get_verb(grammatical_number, tense)
    return (f"{determiner} {noun} {verb}")

def main():
    # single past
    single_past = create_sentence(1, "past")
    print(single_past)
    # plural past
    plural_past = create_sentence(2, "past")
    print(plural_past)
    # single present
    single_present = create_sentence(1, "present")
    print(single_present)
    # plural present
    plural_present = create_sentence(2, "present")
    print(plural_present)
    # single future
    single_future = create_sentence(1, "future")
    print(single_future)
    # plural future
    plural_future = create_sentence(2, "future")
    print(plural_future)

main()
