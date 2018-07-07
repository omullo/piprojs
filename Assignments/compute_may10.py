# compute_may10.py
# Prof. Lee, May 10 2018

"""
Computes CS1110 weighted numerical score as of May 10, if you fill in the
dictionary called `your_scores`.

Info regarding A5 or the final are considered "unknown" as of May 10th.

Lab scores are not accounted for by this script.
"""

import sys

TO_BE_FILLED_IN_BY_YOU = None  # This is a dummy value added for readability


class Scores():
    """

    class variables:
        NAMES = ["a1", "a2", "a3", "a4", "a5", "p1", "p2", "final"]

        WEIGHTS_AND_MAXES: dictionary with keys from Scores.NAMES and values
           being lists of the form [weight, maximum score], with unknown entries
           set to None

        WEIGHT_IND and MAX_IND: where in a value in Scores. WEIGHTS_AND_MAXES one can
            find the weight and the maximum score, respectively

    Instance attribute:
        label [str]: name for this Scores object
        ledger [dict]: attributes specified in Scores.NAMES, and entries
                are either ints, floats, or None (for score not yet known)
    """

    NAMES = ["a1", "a2", "a3", "a4", "a5", "p1", "p2", "final"]

    WEIGHT_IND = 0
    MAX_IND = 1

    WEIGHTS_AND_MAXES = {
        "a1": ( 4,  10),
        "a2": ( 6,  40),
        "a3": (10, 100),
        "a4": (10, 100),
        "a5": (10, None),
        "p1": (15,  69),
        "p2": (15,  52),
        "final": (30, None)
    }

    def __init__(self,
                 label='',
                 a1=TO_BE_FILLED_IN_BY_YOU,
                 a2=TO_BE_FILLED_IN_BY_YOU,
                 a3=TO_BE_FILLED_IN_BY_YOU,
                 a4=TO_BE_FILLED_IN_BY_YOU,
                 p1=TO_BE_FILLED_IN_BY_YOU,
                 p2=TO_BE_FILLED_IN_BY_YOU,
                 a5=None,
                 final=None):
            self.label = label

            # Make a distionary with keys being Scores.Names and corresponding
            # values being the scores given as arguments to __init__
            self.ledger = dict(zip(Scores.NAMES,
                                   [a1, a2, a3, a4, a5, p1, p2, final]))

            # Check that valid values were entered
            for classwork in Scores.NAMES:
                classwork_score = self.ledger[classwork]
                assert type(classwork_score) in [float, int, type(None)]
                if classwork_score is not None:
                    max_score = Scores.WEIGHTS_AND_MAXES[classwork][Scores.MAX_IND]
                    assert classwork_score <= max_score, \
                           "score " + str(classwork_score) + " for " + classwork + \
                           " is bigger than the maximum possible"

    def __str__(self):
        """Return string with the label and the scores represented by this
        Scores object.

        Label and each piece of coursework and are on a separate line.
        """
        outstring = self.label + '\n'
        for classwork in Scores.NAMES:
            classwork_score = self.ledger[classwork]
            outstring += (classwork + ": " + str(classwork_score) + "\n")
        return outstring

    def report(self, verbose=True):
        """Print out the weighted score.

        If bool `verbose` is True, also print out which classwork items were
        incorporated and which weren't.  No extra printed info if `verbose` is
        False.
        """
        print("\nReporting for \'" + self.label + "\'.")
        weighted_score = 0
        max_possible = 0

        for classwork in Scores.NAMES:
            # Local variable to make lines shorter
            classwork_score = self.ledger[classwork]
            weight_and_max = Scores.WEIGHTS_AND_MAXES[classwork]

            if weight_and_max[Scores.MAX_IND] is not None:

                # Stop execution with error message if a score is missing
                try:
                    assert classwork_score is not None, \
                           "You didn't initialize the score for " + classwork
                except AssertionError as ae:
                    print('**** ' + ae.args[0] + '; Quitting now!   ****')
                    sys.exit()

                # Local variables to make lines shorter
                cw_weight = weight_and_max[Scores.WEIGHT_IND]
                cw_max = weight_and_max[Scores.MAX_IND]

                if verbose:
                    print("Incorporating " + classwork +
                          ", score of " + str(classwork_score) +
                          " out of " + str(cw_max))

                weighted_score += cw_weight*classwork_score/cw_max
                max_possible += cw_weight
            elif verbose:
                print("Ignoring " + classwork)

        print("The weighted score is: " + str(round(weighted_score, 2)) +
              " (The maximum possible now is " + str(max_possible) + ")")


def make_label(letter_grade):
    """Create useful string for labeling some calibration Scores"""
    outstring = "values around this score are roughly " + letter_grade + "'s"
    outstring += " (probably neither the top nor the bottom " + letter_grade + ')'
    return outstring

if __name__ == '__main__':

    # Make sure I don't have a typo in the basic setup
    assert set(Scores.NAMES) == set(Scores.WEIGHTS_AND_MAXES.keys()), \
           "mismatch in Scores class attributes"


    a = Scores(label=make_label('A'), a1=10, a2=40, a3=85, a4=90, p1=61, p2=46)
    b = Scores(label=make_label('B'), a1=10, a2=36, a3=70, a4=63, p1=49, p2=38)
    c = Scores(label=make_label('C'), a1=10, a2=30, a3=50, a4=40, p1=40, p2=31)


    a.report(False)
    b.report(False)
    c.report(False)

    # STUDENTS: fill the missing values. You can use a, b, and c above as examples.
    your_scores = Scores(label="You!",
                         a1=8,
                         a2=36,
                         a3=89,
                         a4=67,
                         p1=65,
                         p2=47)
    your_scores.report(True)

