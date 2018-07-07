# a4_soln.py --- solution version
# Lillian Lee (LJL2), plus, where credited, Victoria Litvinova
# Apr 20 2018 (This version folds in updates.)

# STUDENTS:
# Instructions: implement the bodies of the predefined function headers below
# according to their specifications.
#
# Rule 1: no direct or indirect calls to positions._collect_reachable_positions()
# in any code you submit.
# (Using positions.draw() to debug is OK, but delete such calls before
# submission.)
#
# Rule 2: No strategies that essentially "flatten" an org chart into a
# non-nested list (of strings,  Positions, whatever) and then operate on that.
# Rule 1 is actually a consequence of rule 2.
#
# (We want to see you directly implement recursion in two different settings,
# even though a valid alternate approach in real life is to collect up all
# reachable positions in a flat list, and then for each of the two problems
# below you just iterate over that, doing different things for in the iteration.)
#
# Rule 3: implementations must make effective use of recursion. It's OK to
# include for-loops or anything else, too.


def posns_above(root):
    """Returns: list of Positions that supervise Position `root`, or supervise
    `root`'s supervisors, ... and so on up.

    No repeats in the returned list. (OK if different Positions have the same title)
    """
    outlist = []
    for sup in root.sups:
        if sup not in outlist:
            outlist.append(sup)
        # Get what is reachable from sup
        above_sup_list = posns_above(sup)

        # Add non-repeats to outlist
        for posn in above_sup_list:
            if posn not in outlist:
                outlist.append(posn)
    return outlist


def map_people_to_positions(root):
    """Returns: dictionary of netids of people who hold the `root` Position or
    any Position subordinate to `root`, or subordinate to a subordinate of `root`,
    and so on, all the way down.
    The value for a given netid: list of Positions held by that netid that are
    the `root` Position or any Position subordinate to the `root`, or
    subordinate to a subordinate of `root`, all the way down,
    no repeats.

    Do not include keys that are not netids in your returned Dictionary; there
    should be no key entry representing vacant or non-specified.
    """
    outdict = {}

    if isinstance(root.holder, str):
        # The holder is a netid
        outdict[root.holder] = [root]  # Put root Position into the dictionary
    for sub in root.subs:
        sub_dict = map_people_to_positions(sub)


        # STUDENTS: the dictionary method() probably does not do what
        # you want, because it does not *combine: values, but overwrites them,
        # >>> d1 = {"LJL2": ["co-instructor"]}
        # >>> d2 = {"LJL2": ["janitor"]}
        # >>> d1.update(d2)
        # >>> d1
        # {'LJL2': ['janitor']}
        #
        # You need to be able to loop and work directly with dictionaries
        # for prelim 2.

        # Load sub_dict info into outdict
        for netid in sub_dict:
            subplist = sub_dict[netid]  # List of Positions learned from sub
            if netid not in outdict:
                # Make a new entry in outdict
                outdict[netid] = subplist
            else:
                # Have to add to existing outdict entry, avoiding repeats
                oldplist = outdict[netid]  # Make local variable for convenience
                for posn in subplist:
                    if posn not in oldplist:
                        oldplist.append(posn)
    return outdict


def map_people_to_positions2(root):
    ## Version of above with fewer local variables

    outdict = {}
    if isinstance(root.holder, str):
        outdict[root.holder] = [root]
    for sub in root.subs:
        sub_dict = map_people_to_positions2(sub)
        # Load sub_dict info into outdict
        for netid in sub_dict:
            if netid not in outdict:
                # Make a new entry in outdict
                outdict[netid] = sub_dict[netid]
            else:
                # Have to add to existing outdict entry, avoiding repeats
                for posn in sub_dict[netid]:
                    if posn not in outdict[netid]:
                        outdict[netid].append(posn)
    return outdict


def map_people_to_positions3(root):
    ## Alternate solution by Victoria Litvinova, with edits by LL.
    ## Difference: does checking for repeats OUTSIDE the main for-loop.
    outdict = {}

    if root.holder is not None and root.holder != 0:
    # Having the first clause be "root.holder != None" is OK, but dis-preferred
        outdict = {root.holder: [root]}
    for sub in root.subs:
        sub_dict = map_people_to_positions3(sub)
        for netid in sub_dict:
            subplist = sub_dict[netid]
            if netid not in outdict:
                outdict[netid] = subplist
            else:
                # This could add repeats, but we'll remove them later
                outdict[netid] += subplist

    for netid in outdict:
        deduplicated = []
        for p in outdict[netid]:
            if p not in deduplicated:
                deduplicated.append(p)
        outdict[netid] = deduplicated
    return outdict


def map_people_to_positions4(root):
    ## Alternate solution by Victoria Litvinova, with edits by LL.
    ## Difference: does checking for repeats OUTSIDE the main for-loop,
    ## but where we use set() and list() to remove repeats.
    ## We didn't cover set() in class and you don't need to know it
    ## for prelim 2, but it's useful in real life.
    outdict = {}

    if root.holder is not None and root.holder != 0:
    # Having the first clause be "root.holder != None" is OK, but dis-preferred
        outdict = {root.holder: [root]}
    for sub in root.subs:
        sub_dict = map_people_to_positions4(sub)
        for netid in sub_dict:
            subplist = sub_dict[netid]
            if netid not in outdict:
                outdict[netid] = subplist
            else:
                # This could add repeats, but we'll remove them later
                outdict[netid] += subplist

    for netid in outdict:
        # This is an idiom for removing duplicates from a list:
        # convert the list to a set (which can't have repeats by definition)
        # and then convert back to a list
        outdict[netid] = list(set(outdict[netid]))
    return outdict


def map_people_to_positions5(root):
    ## Alternate solution by Victoria Litvinova, with edits by LL.
    ## Difference: does checking for repeats OUTSIDE the main for-loop.
    ## And, uses the dictionary items() method, which yields tuples,
    ## plus the fact that you can assign to tuples in one line.
    ## We didn't cover this in class and you don't need to know if
    ## for prelim 2, but it's useful in real life.
    outdict = {}
    if isinstance(root.holder, str):
        outdict = {root.holder: [root]}
    for sub in root.subs:
        for (netid, poslist) in map_people_to_positions5(sub).items():
            if netid not in outdict:
                outdict[netid] = poslist
            else:
                outdict[netid] += poslist  # Will discard repeats later

    for netid in outdict:
        outdict[netid] = list(set(outdict[netid]))
    return outdict
