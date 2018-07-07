# a3.py
# STUDENTS: update the next three lines and then delete this one
# Frank and Andrew
# None
# PUT DATE YOU COMPLETED THIS HERE
# Skeleton by Lillian Lee (LJL2) and Victoria Litvinova (VL242), Mar 22 2018

from tkinter import filedialog  # Get visual request for file selection
import urllib.request  # Get vocabulary from a webpage
import string  # Get some useful string built-in values
import os
import sys

from sources import econ_terms# BEGIN REMOVE
ECON_DATA_FNAME = os.path.join('econ_terms_scratch', 'econ_vocab_data.txt')
ECON_VOCAB = econ_terms.ECON_VOCAB

#  STUDENTS: this function has been completed for you.
def get_content_lines(fname=None):
    """Given filename fname, return a list of normalized lines in the file,
    except that lines that are 'commented out', in the sense of the first
    non-whitespace character being a '#', are not included.

    EXCEPTION: if no argument is given, the "fname=None" in the function header
    sets fname to None (the actual value, NOT the string "None"), which,
    in the code below, causes the filename to be retrieved from the user via a
    visual file-open dialog.

    The normalization is almost exactly as described in Section 13.3 "Word histogram" in the
    text, and in particular the function process_line: hyphens are replaced
    with spaces (so "highly-flammable programs" would become three words);
    punctuation at the beginning and ends of words is removed (so that "Really?",
    "Really!" and "Really" are all treated as the same word), and all words are
    lower-cased (so that "CS1110" and "cs1110" are treated as the same word.)
    Leading or trailing whitespace is removed, and all line-internal whitespace
    is replaced by a single space.
    However, a "\n" is added to the end of every line.

    Precondition: fname is the name of a plain-text file, OR it is not given by
    the caller (in which case Python will set parameter fname to None).
    """
    output = []  # Initialize our accumulator

    # This is how to check if something is None (Pythonistas don't use == here.)
    if fname is None:
        # Fill in fname using a visual dialog window
        fname = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")],
                                           title="Choose an input file")

    # About open(), see section 9.1 "Reading word lists" of the text.
    # "with" makes sure file opening and closing is cleanly done.
    # The 'r' means can only read the file, not change it
    with open(fname, mode='r', encoding='utf-8') as fp:

        # See Section 13.3 "Word histogram" on looping through a file's lines
        for line in fp:
            left_justified_line = line.lstrip()  # Remove leading whitespace
            if len(left_justified_line) == 0 or left_justified_line[0] != '#':
                # Either line was empty or it wasn't a comment.
                line = line.replace('-', ' ')
                words_in_line = line.split()
                for ind in range(len(words_in_line)):
                    word = words_in_line[ind].strip()
                    word = word.strip(string.punctuation + string.whitespace)
                    word = word.lower()
                    words_in_line[ind] = word  # Replace with normalized version
                output.append(' '.join(words_in_line) + '\n')
    return output


def convert_lines_to_string(linelist):
    """ Returns: a single string that is the concatenation of every non-empty
    line in linelist except each such line has been stripped of leading and
    trailing whitespace (including newlines), and there is a single space
    between what used to be adjacent lines (ignoring lines that were originally
    empty strings before the stripping of whitespace).

    Example input and output:
        ["hi\n", "there"] -> "hi there"
        ["    hola    ", "   salut \n  howdy  "] -> "hola salut \n  howdy"
        ["so", "la", "", "do"] -> "so la do"
        ["so", "\n", "la", "", "", "do"] -> "so  la do"
           ** note the two spaces between "so" and "la"

    Precondition: linelist is a (possibly empty) list of strings.
    """
    # STUDENTS: Complete this implementation so that it satisfies its
    # specification, with the following constraints.
    # You MUST make effective use a for-loop whose header is
    #   for line in linelist:
    # (We are testing whether you can work with loops directly over items in
    # a given list.)
    #
    # Hint: dealing with lines that are empty string can be tricky; watch out
    # that you don't get extra spaces.
    #
    # Hint: our solution uses the fact that you can give more than one
    # argument to range().  For example, list(range(2, 6)) is [2, 3, 4, 5]
    # (Don't put a colon in the call to range the way I did at first,
    # costing me an embarrassing amount of time wondering why my code wasn't
    # syntactically correct ...)

    newlist=[]
    for line in linelist:
        if len(list)==0:
            newlist.append(line)
        else:
            newlist.append(line.strip()+' ')
    return ''.join(newlist)


def convert_lines_to_string2(linelist):
    """Same specification as convert_lines_to_string()"""

    # STUDENTS: Complete this implementation so that it satisfies its
    # specification, with the following constraints, which DIFFER from
    #
    # You MUST make effective use a for-loop whose header is either
    #   for ind in range(len(linelist)):
    # or
    #   for ind in list(range(len(linelist))):
    # (We are testing whether you can work with loops over the indices of
    # a given list.)
    # Implementations that just use the join() string method and/or `map`
    # will not receive credit.
    #
    # The same hint as for convert_lines_to_string applies.

    newlist=[]
    for ind in range(len(linelist)):
        if linelist[ind]=='':
            newlist.append(linelist[ind])
        else:
            newlist.append(linelist[ind].strip()+' ')
            
        


def convert_lines_to_paragraphs(linelist):
    """ Returns: a list of the paragraph-strings corresponding to
    the paragraphs in linelist.

    Each paragraph in linelist is a maximal contiguous subsequence of lines
    in linelist such that the sequence does not contain a blank line.
    A blank line is exactly the string "\n".

    A paragraph-string is the result of running convert_lines_to_string()
    or convert_lines_to_string2 on a paragraph.

    If linelist is empty, or if all the lines in linelist are empty,
    returns the empty list.

    See the test cases in a3test.test_convert_lines_to_paragraph() for examples.

    Precondition: linelist is a (possibly empty) list of strings.
    """
    # STUDENTS: Complete this implementation so that it satisfies its
    # specification, with the following constraints.
    # You MUST make effective use a for-loop.
    # You must decide for yourself whether it is better to loop over linelist
    # or over the indices of linelist, or whether it matters.
    # (We have solutions for either strategy, but one seemed a little trickier
    # than the other.
    #
    # There are a lot of subtleties here.
    # First, take a close look at the test cases we have given you in
    # a3text.test_convert_lines_to_paragraph().
    # Notice that you need to handle cases in which there are multiple
    # consecutive blank lines.
    # Try figuring out what you as a human do to get the right answer on the
    # all of the test cases, before you try to implement your strategy in Python.
    # If you don't understand a test input or test output, ASK SOMEONE
    # BEFORE CODING!
    #
    # Suggested strategy: you know you want to build up a list that consists of
    # strings, so it seems that an accumulator variable that you add or append to
    # makes sense. But each of those strings is created by merging together a
    # set of lines.  So you might have another variable that stores the lines in
    # the current paragraph (as defined above). When the current paragraph is
    # done, run convert_lines_to_string() on that current-paragraph list, and
    # then reset that current-paragraph list to get ready for the next paragraph.

    pass  # STUDENTS: remove this `pass` statement when done






# STUDENTS: we ran this function to provide you a local version of the text
# of the relevant webpages --- to speed things up for you (you don't have
# to wait for webserver responses), and to keep the load light on the webserver
# (we don't want to have 500+ students hitting The Economist's webserver over
# and over again).
def download_econ_vocab_data(fname):
    """(over)write into file fname the concatenation of text regarding
    economics-related terminology text from
        https://www.economist.com/economics-a-to-z/a
        https://www.economist.com/economics-a-to-z/b
        ...
        https://www.economist.com/economics-a-to-z/z

    Preconditions: directory econ_dict exists in the same directory as this file.
    """
    with open(fname, mode='a+', encoding='utf-8') as fp:

        # Isn't it handy to be able to loop through strings?
        for letter in string.ascii_lowercase:
            # You can check that this is like what we did in A1, file
            # get_status_from_webpage.py
            data_name = 'https://www.economist.com/economics-a-to-z/'
            try:
                data_source = urllib.request.urlopen(data_name + letter)
                fp.write(data_source.read().decode('utf-8'))
                fp.write('\n\n')  # have a separator between webpages
            except ValueError:
                print("Something is wrong with the web address or webpage.")
                sys.exit()


def get_econ_vocab_helper(vlist_to_add_to, work_text):
    """Extends vlist_to_add_to with the list of the vocabulary items,
    lower-cased, in work_text, assumed to be well-formatted html"""

    # Add each <h2>...</h2> term or phrase to vlist_to_add_to, separating out
    # comma-separated phrases.

    i_start = work_text.find('<h2>')
    if i_start == -1:
        # No more <h2> tags, all done
        return
    else:
        work_text = work_text[i_start + len('<h2>'):]
        try:
            i_end = work_text.index('</h2>')  # If no matching </h2>,
                                              # quit because the data is corrupt
        except:
            print('ˆData has a <h2> without matching </h2>.')
            sys.exit()
        # Deal with "G7, G8, G20"
        term_list = work_text[:i_end].split(',')
        for term in term_list:
            vlist_to_add_to.append(term.lower().strip())
        work_text = work_text[i_end + len('</h2>') + 1:]

        # Recursive call!
        get_econ_vocab_helper(vlist_to_add_to, work_text)


def get_econ_vocab(fname):
    """Returns a list of the vocabulary items in fname, lower-cased."""
    with open(fname, mode='r', encoding='utf-8') as fp:
        outlist = []
        get_econ_vocab_helper(outlist, fp.read())
        return outlist

def track_topic(docs_list, vocab_list):
    """
    Returns: a list of the fraction of words in each document in docs_list that
    are in vocab_list.

    In more detail...

    Preconditions:

    * docs_list: a (possibly empty) list of nonempty strings, each of which
    contains at least one non-white-space character. We consider each item of
    docs_list to be a "document" where the "words" of the document are all the
    spans of characters that don't contain spaces. No "words" contain beginning
    or ending punctuation, although internal punctuation is OK.
    So, this document
        hey howdy          how's the weather
    has five words.
    This document
        xxx y z3!42
    has three words.
    This is NOT a legal document:
        hey howdy,     how's the weather???

    * vocab_list is a non-empty list of non-empty strings that may contain
    spaces. We consider each item of vocab_list to be a target "word". No
    target word can have beginning or ending punctuation, although internal
    punctuation is OK.

    This function returns a new list outlist such that:
        * len(outlist) == len(docs_list), and
        * for each valid index `ind` of docs_list, outlist[i] is the fraction
          of words in document docs_list[i] that are found in vocab_list.
          The fraction should be a float rounded to three digits past the
          decimal point via the round() built-in function.

    Examples:
    if doclist[0] is "abc abcabc a   a" and vocab_list is ["abc"],
        then outlist[0] should be .25 (i.e, 1/4).
    If doclist[1] is "abc abcabc a   a" and vocab_list is ["ABC", "a"],
        then outlist[1] should be .5 (i.e., 2/4)
    If doclist[2] is "ab abab a   a" and vocab_list is ["ABC", "a", "ab", "v", "abab"],
        then outlist[2] should be 1.0 (i.e., 4/4).

    The reason we disallow punctuation is to avoid having to decide whether
    a document "are you okay?" contains a word in the list ["okay"].
    """
    # STUDENTS: Complete this implementation so that it satisfies its
    # specification, with the following constraints.
    # You MUST make effective use a for-loop, and you will might need to use a
    # nested for-loop.
    #
    # Hint: If you are counting how many vocab_list words occur in a given
    # document, don't forget to reset that count every time you start with a
    # new document.
    #
    # Hint: we found the string method split() to be quite useful.  For a
    # (kind of unconventional) example of using split to get a convenient list
    # of words, see the file
    # http://www.cs.cornell.edu/courses/cs1110/2018sp/lectures/lecture12/modules/madlibs2.py

    pass  # STUDENTS: remove this `pass` statement when done

if __name__ == '__main__':
    # econ_vocab= get_econ_vocab()
    # print(econ_vocab)

    # https://www.exaptive.com/blog/topic-modeling-the-state-of-the-union
    red_topic = ['make sure', 'company', 'college', 'republican', 'parent',
                 'medicare', 'bipartisan', 'kid', 'small business', 'global']
    purple_topic = ['afghanistan', 'america', 'terror',  'troop', 'border',
                    'terrorist', 'violence', 'enemy', 'fighting', 'rule']

    sotus = []  # State of the Union addresses, 2005-2016
    for year in range(2001, 2009):
        fname = os.path.join('sources', str(year)+'_bush.txt')
        sotus.append(convert_lines_to_string(get_content_lines(fname)))
    for year in range(2009, 2017):
        fname = os.path.join('sources', str(year)+'_obama.txt')
        sotus.append(convert_lines_to_string(get_content_lines(fname)))
    for year in range(2017, 2019):
        fname = os.path.join('sources', str(year)+'_trump.txt')
        sotus.append(convert_lines_to_string(get_content_lines(fname)))

    print("Demonstration of tracing a topic through a single speech: ")
    print("How the red topic trends through Obama's 2013 SOTU. Topics typically exhibit such `bursty' behavior.")
    fname = os.path.join('sources', '2013_obama.txt')
    obama13 = convert_lines_to_paragraphs(get_content_lines(fname))
    print(track_topic(obama13, red_topic))



    red_trend = track_topic(sotus, red_topic)
    purple_trend = track_topic(sotus, purple_topic)

    import matplotlib.pyplot as plt
    plt.title("Topic trends in recent US State of the Union addresses")
    plt.ylabel("fraction of speech tokens on the topic")
    x = list(range(2001, 2019))
    plt.plot(x, track_topic(sotus, ECON_VOCAB),
             'b', marker='o', label="The Economist's economic terms")
    plt.plot(x, track_topic(sotus, red_topic),
             'r', marker='o',
             label="Evans' red topic (selections: 'college', 'parent', ...)")
    plt.plot(x, track_topic(sotus, purple_topic),
             'purple', marker='o',
             label="Evans' purple topic (selections: 'terrorist', 'enemy', ...)")
    labels = ["2001: Bush", "2005: Bush",
              "2009: Obama", "2013: Obama",
              "2017: Trump"]
    plt.xticks(range(2001, 2019, 4), labels, rotation=45, fontsize=6)
    plt.legend()
    plt.show()
    plt.close('all')


