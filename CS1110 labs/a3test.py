# a3test.py
# STUDENTS: update the next three lines and then delete this one
# PUT YOUR NAME(S) AND NETID(S) HERE
# Sources/people consulted: FILL IN OR WRITE "NONE"
# PUT DATE YOU COMPLETED THIS HERE
# Skeleton by Lillian Lee (LJL2) and Victoria Litvinova, Mar 22 2018

""" Test functions for a3.py.

    STUDENTS:
    WARNING: WE HAVE PURPOSELY PLANTED ONE INCORRECT TEST CASES IN
    EACH OF THE FUNCTIONS TESTING THE CODE YOU WRITE. You need to correct them,
    and comment those changes with
    '# ... STUDENT-FIXED ERROR ...'
    so the graders can easily find what you did.
    You do NOT have to check for problems with testers of a3 functions that
    we wrote for you.

    Run this script with "python a3test.py quiet" if you want less
    diagnostic output and no visual file dialogs.

    Assumes the existence of a subdirectory `sources` in the same
    directory that contains the files distributed with CS1110 2018SP. """

import a3
import cornellasserts as ca  # Abbreviation
import sys  # For getting command-line arguments
import os  # For dealing with differences in operating systems (Windows, OSX)
import inspect  # Used to get function names automatically:
                # inspect.stack()[0] is the "highest" frame on the call stack


def add_sources_to_fname(fname):
    """Make the name for a file named fname in the subdirectory sources
    as appropriate for the caller's operating system. ("sources" is a hardcoded
    name.)"""
    return os.path.join('sources', fname)


def test_get_content_lines(verbose):
    """Test a3.get_content_lines()"""

    # A generic line that can be pasted into any function;
    # retrieves the name of current function from its frame on the stack.
    # Each item in the list returned by inspect.stack() is a call frame.
    # You can print out the frame at the top of the stack by:
    #     print(str(inspect.stack()[0])
    tester_name = inspect.stack()[0][3]
    print("Running " + tester_name + "()")

    test_cases = {
        # Different operating systems have different ways of dealing with
        # subdirectories, which is what os.path.join helps us deal with.
        #  See section 14.4 "Filenames and paths" of the text.
        add_sources_to_fname('shortest.txt'):  ["abc abcabc natural language processing\n",
                                                "3 o'clock bc!d\n"],
        add_sources_to_fname('short.txt'):
           ["here is a small piece of text a small piece of text a small piece of text here is a small piece of text at nine o'clock in the morning\n"],
        add_sources_to_fname('shortest_commented.txt'): ["abc abcabc natural language processing\n",
                                                         "bc!d bc!d\n"],
    }

    for test_input in test_cases:
        if verbose:
            print("\tTesting " + str(test_input))
        expected = test_cases[test_input]
        ca.assert_equals(expected, a3.get_content_lines(test_input))

    # For longer files, rough check that we get the right number of lines
    test_cases = {
        add_sources_to_fname('imbeciles.txt'): 33-6,
        add_sources_to_fname('lonely_as_a_cloud.txt'): 29-2,
        add_sources_to_fname('2013_obama.txt'): 184,
    }
    for test_input in test_cases:
        if verbose:
            print("\tTesting " + str(test_input))
        expected = test_cases[test_input]
        ca.assert_equals(expected, len(a3.get_content_lines(test_input)))


def test_convert_lines_to_string(verbose):
    """Test a3.test_convert_lines_to_string() and
       a3.test_convert_lines_to_string2() """

    # A generic line that can be pasted into any function;
    # retrieves the name of current function from its frame on the stack.
    # Each item in the list returned by inspect.stack() is a call frame.
    # You can print out the frame at the top of the stack by:
    #     print(str(inspect.stack()[0])
    tester_name = inspect.stack()[0][3]
    print("Running " + tester_name + "()")



    # Have to store lists as tuples in order to have them be dict. keys.
    test_cases = {
        ("hi\n", "there"): "hi there",
        ("hi\n", "there\n"):  "hi there",
        ("    hola    ", "   salut \n  howdy  "): "hola salut \n  howdy",
        ("so", "la", "", "do"): "so la do",
        ("so", "\n", "la", "", "", "do"): "so  la do",  # no extra space after la
        # STUDENTS: you should add enough test cases to make the set of test cases
        # sufficient. Put any new test cases you want in the dictionary
        # below this line, and leave the next comment line in your code so the
        # graders to easily locate it and your additions.
        # ..... STUDENT-ADDED DICT. CONVERT...STRING TEST CASES BELOW THIS LINE ....
    }

    # Yes, functions can be elements of lists, too! Note that the elements
    # are not (values returned by) function calls, but the functions themselves.
    fns_to_test = [a3.convert_lines_to_string, a3.convert_lines_to_string2]
    for ind in range(len(fns_to_test)):  # also OK to wrap "list" around range()
        convertfn = fns_to_test[ind]
        print("testing " + convertfn.__name__)
        for test_input in test_cases:
            if verbose:
                print("\tTesting " + str(test_input))
            expected = test_cases[test_input]
            ca.assert_equals(expected,
                             # Convert tuple back to list
                             convertfn(list(test_input)))

        # STUDENTS: you should add enough test cases to make the set of test cases
        # sufficient. If you have additional test cases to add that wouldn't be
        # suitable for encoding in dictionary test_cases, then place them here.
        # Make sure you call the generic alias `convertfn` so that both your
        # convert_line_to_string() and convert_line_to_string2() can be tested
        # on the same test cases.
        # Leave the following comment line in your submitted code so that the
        # graders can easily locate it and thus your additions.
        # ..... STUDENT-ADDED NON-DICT. CONVERT...STRING TEST CASES BELOW THIS LINE ....



        if ind < (len(fns_to_test)-1):  # Not the last fn to test
            # Check whether students are ready to test the next function
            ask_to_quit(verbose, fns_to_test[ind+1].__name__)


def test_convert_lines_to_paragraph(verbose):
    """Test a3.convert_lines_to_paragraphs"""
    tester_name = inspect.stack()[0][3]
    print("Running " + tester_name + "()")

    test_cases = {}  # Start with empty dictionary

    # test_file is the name of a file containing lines to
    # extract and make into a test input (i.e., a list of lines)
    # for convert_lines_to_paragraphs()
    test_file = add_sources_to_fname('short_stanzas.txt')
    expected = []
    stanza = "1st line of 1st stanza"
    expected.append(stanza)
    stanza = "1st line of 2nd stanza"
    expected.append(stanza)
    stanza = "1st line of 3rd stanza"
    stanza += " 2nd line of 3rd stanza"
    stanza += " 3rd line of 3rd stanza"
    expected.append(stanza)

    test_cases[test_file] = expected

    # We are using a list because hidden from students at submission time we
    # have multiple implementations.
    fns_to_test = [a3.convert_lines_to_paragraphs]
    for convertfn in fns_to_test:
        print("testing " + convertfn.__name__)
        for test_file in test_cases:
            if verbose:
                print("\tTesting " + str(test_file))
            expected = test_cases[test_file]
            test_input = a3.get_content_lines(test_file)
            ca.assert_equals(expected,
                             convertfn(test_input))

        test_input = []
        if verbose:
                print("\tTesting " + str(test_input))
        ca.assert_equals([], convertfn(test_input))

        test_input = ["\n", "\n"]  # all lines blank
        if verbose:
                print("\tTesting " + str(test_input))
        ca.assert_equals([], convertfn(test_input))

        # ends with multiple blank lines
        test_input = ["\n", "\n", "just one content line", "\n"]
        if verbose:
                print("\tTesting " + str(test_input))
        ca.assert_equals(["just one content line"],
                         convertfn(test_input))

        # embedded newline
        test_input = ["I'm\ntricky",
                      "and you can be too  \n",
                      "\n",
                      "stay in school"]
        if verbose:
                print("\tTesting " + str(test_input))
        ca.assert_equals(["I'm\ntricky and you can be too", "stay in school"],
                         convertfn(test_input))

        test_file = add_sources_to_fname('lonely_as_a_cloud.txt')
        if verbose:
            print("\tTesting file " + str(test_file))
        test_input = a3.get_content_lines(test_file)
        result = convertfn(test_input)
        ca.assert_equals(result[0], "i wandered lonely as a cloud that floats on high o'er vales and hills when all at once i saw a crowd a host of golden daffodils beside the lake beneath the trees fluttering and dancing in the breeze")
        ca.assert_equals(result[1], 'continuous as the stars that shine and twinkle on the milky way they stretched in never ending line along the margin of a bay ten thousand saw i at a glance tossing their heads in sprightly dance')
        ca.assert_equals(result[2], 'the waves beside them danced but they out did the sparkling waves in glee a poet could not but be gay in such a jocund company i gazed and gazed but little thought what wealth the show to me had brought')
        ca.assert_equals(result[3], 'for oft when on my couch i lie in vacant or in pensive mood they flash upon that inward eye which is the bliss of solitude and then my heart with pleasure fills and dances with the daffodils')

        # STUDENTS: you should add enough test cases to make the set of test
        # cases sufficient.
        # ... STUDENT-ADDED NON-DICT. CONVERT...PARA TEST CASES BELOW THIS LINE ....


def test_get_econ_vocab(verbose):
    """ Test a3.get_econ_vocab() """
    # Does just some rough checks

    tester_name = inspect.stack()[0][3]
    print("Running " + tester_name + "()")
    print("...this takes a little while")

    result = a3.get_econ_vocab()
    assert type(result) == list
    ca.assert_equals(type(result), list)
    ca.assert_true(len(result) > 20)

    # spot checks
    ca.assert_equals(672, len(result))
    some_terms = ['agency costs', 'capital gains', 'euro', 'poverty', 'third way']
    some_terms.extend(['tax base', 'volatility', 'yield', 'welfare'])
    for term in some_terms:
        ca.assert_true(term in result)
    ca.assert_false('Tariff' in result)


# helper function for more compact testing code
def round3(x):
    """Returns x rounded to 3 places as a float.  x should be a float or an int."""
    return round(float(x), 3)


def test_track_topic(verbose):
    """ Test a3.track_topic() """
    # This code presumes that a3.get_content_lines(), a3.convert_lines_to_string(),
    # and a3.convert_lines_to_paragraphs() are all implemented correctly.

    tester_name = inspect.stack()[0][3]
    print("Running " + tester_name + "()")

    # Single-document examples from specification
    test_cases = {
        # Need the comma in ("abc",) to convince Python  that "abc" is an item
        # in a one-element tuple, not a sequence to be turned into ('a', 'b', 'c')
        ("abc abcabc a   a", ("abc",)): round3(1/4),
        ("abc abcabc a   a", ("ABC", "a")): round3(2/4),
        ("ab abab a   a", ("ABC", "a", "ab", "v", "abab")): round3(4/4),
    }
    for test_input in test_cases:
        docs_list = [test_input[0]]
        vocab_list = list(test_input[1])
        if verbose:
                print("\tTesting " + str((docs_list, vocab_list)))
        ca.assert_equals([test_cases[test_input]], a3.track_topic(docs_list, vocab_list))


    # Just one document, vary the vocabulary lists
    linelist = a3.get_content_lines(add_sources_to_fname("shortest.txt"))
    docs_list = [a3.convert_lines_to_string(linelist)]
    vocab_tuples = {
        ("abc",): [round3(1/8)],  # Need the comma to convince Python "abc" is a tuple
                                  # item, not a sequence to be turned into ('a', 'b', 'c')
        ("abcab",): [round3(0)],
        ("abc", "o'clock", "bipedal", "abcabc", "natural"): [round3(5/8)],
        tuple(a3.convert_lines_to_string(linelist).split(),): [round3(1)]   # All the words
    }
    for key in vocab_tuples:
        vocab_list = list(key)
        if verbose:
                print("\tTesting " + str((docs_list, vocab_list)))
        ca.assert_equals(vocab_tuples[key], a3.track_topic(docs_list, vocab_list))

    # Several documents, each corresponding to a stanza (paragraph)
    linelist = a3.get_content_lines(add_sources_to_fname("imbeciles.txt"))
    docs_list = a3.convert_lines_to_paragraphs(linelist)
    len_list = []  # Stores the lengths of each document checked for length
    for doc in docs_list:
        len_list.append(len(doc.split()))

    vocab_tuples = {
        ("cheese", "continuous"): [round3(1/len_list[0]),
                                   round3(1/len_list[1]),
                                   0.,
                                   0.],
        # Should be case-sensitive, where these docs have been downcased
        ("cheese", "Continuous"): [round3(1/len_list[0]), 0., 0., 0.],
        # Should not pick up commented lines
        ("cheese", "Harry"): [round3(1/len_list[0]), 0., 0., 0.],
        ("cheese", "imbeciles"): [round3(2/len_list[0]),
                                  0.,
                                  0.,
                                  round3(1/len_list[3])],
        ("the",): [round3(3/len_list[0]),
                   round3(3/len_list[1]),
                   round3(3/len_list[2]),
                   round3(2/len_list[3])],
        ("the", "a", "an"): [round3((3 + 3 + 0)/len_list[0]),
                             round3((3 + 2 + 0)/len_list[1]),
                             round3((3 + 2 + 0)/len_list[2]),
                             round3((2 + 0 + 0)/len_list[3])]
    }
    for key in vocab_tuples:
        vocab_list = list(key)
        if verbose:
                print("\tTesting " + str((docs_list, vocab_list)))
        #TODO: NOTICE THE NESTED indices!! Ask the students to do?
        # Check each float in the resulting list
        result = a3.track_topic(docs_list, vocab_list)
        for ind in range(len(docs_list)):
            ca.assert_floats_equal(vocab_tuples[key][ind], result[ind])

    # STUDENTS: you should add enough test cases to make the set of test cases
    # sufficient. If you have additional test cases to add that wouldn't be
    # suitable for encoding in dictionary test_cases, then place them here.
    # Make sure you call the generic alias `convertfn` so that both your
    # convert_line_to_string() and convert_line_to_string2() can be tested
    # on the same test cases.
    # Leave the following comment line in your submitted code so that the
    # graders can easily locate it and thus your additions.
    # ..... STUDENT-ADDED NON-DICTIONARY TEST CASES BELOW THIS LINE ....








# STUDENTS: don't edit this function.
def ask_to_quit(verbose, nextfn=None):
    """Ask if user wishes to test the next function nextfn;
       terminate execution if not.
    Does nothing if `verbose` is False.
    If nextfn, the name of the next function, isn't given, Python uses the
      value None"""
    if verbose:
        if nextfn is None:
            nextfn = "the next function"
        msg = 'Press q to quit, anything else to start testing/running '
        msg += nextfn + '(). '
        response = input(msg)
        if response == "q":
            sys.exit()


# See the second half of section 14.9 "Writing modules" of the text for more
# on this __name__ business. Basic idea: the indented code is only run if
# this file is run by `python a3test.py` on the command line
if __name__ == '__main__':

    verbose = True  # Default mode is to give lots of output.
                    # False means give less output

    # Handling arguments from the command line
    if len(sys.argv) > 1:
        # Was called with at least one argument
        if len(sys.argv) == 2 and sys.argv[1] in ["quiet"]:
            # called by "python a3test.py quiet"
            verbose = False
        else:
            print("Invalid argument(s), only possible argument is 'quiet'.")
            sys.exit()

    fns_to_run = [test_get_content_lines,
                  test_convert_lines_to_string,
                  test_convert_lines_to_paragraph,
                  # test_get_econ_vocab,   # commented out to speed up testing
                  test_track_topic
                  ]
    for ind in range(len(fns_to_run)):
        fn = fns_to_run[ind]
        fn(verbose)
        if ind < (len(fns_to_run)-1):  # not the last test
            ask_to_quit(verbose, nextfn=fns_to_run[ind+1].__name__)
