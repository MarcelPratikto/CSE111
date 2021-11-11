from sentences import get_determiner, get_noun, get_verb
import pytest

def test_get_determiner():
    # 1. Test the single determiners.
    single_determiners = ["the", "one"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.
    plural_determiners = ["some", "many"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    single_nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]

    for _ in single_nouns:
        noun = get_noun(1)
        assert noun in single_nouns

    plural_nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]

    for _ in plural_nouns:
        noun = get_noun(2)
        assert noun in plural_nouns
    
def test_get_verb():
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    for _ in past_verbs:
        verb = get_verb(1, "past")
        assert verb in past_verbs
    
    single_present_verbs = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    for _ in single_present_verbs:
        verb = get_verb(1, "present")
        assert verb in single_present_verbs
    
    plural_present_verbs = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    for _ in plural_present_verbs:
        verb = get_verb(2, "present")
        assert verb in plural_present_verbs

    future_verbs = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    for _ in future_verbs:
        verb = get_verb(1, "future")
        assert verb in future_verbs

# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", __file__])