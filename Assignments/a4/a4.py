# a4.py
# Andrew Nkubito (an328) and Frank Omullo (foo6)
# Sources/people consulted:None  STUDENTS: None
# 04/18/2018
# Skeleton by Lillian Lee (LJL2)
# Apr 12 2018

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
#
# Rule 3: implementations must make effective use of recursion. It's OK to
# include for-loops or anything else, too.

def posns_above(root):
    """Returns: list of Positions that supervise Position `root`, or supervise
    `root`'s supervisors, ... and so on up.

    No repeats in the returned list. (OK if different Positions have the same title)
    """
    admin=[] # the administrators/supervisors
    for sup in root.sups:
        if sup not in admin:
            admin.append(sup)
        admin2=posns_above(sup)
        for sup in admin2:
            if sup not in admin:
                admin.append(sup)
    return admin

def map_people_to_positions(root):
    """Returns: dictionary of netids of people who hold the `root` Position or
    any Position subordinate to `root`, or subordinate to a subordinate of `root`,
    and so on, all the way down.
    The value for a given netid: list of Positions held by that netid, no repeats
    """
  
    staff={} #a dictionary of the staff and postions of root and the surbodinates
    staff[str(root.holder)]=[root]
    for sub in root.subs:
        staff[str(sub.holder)]=[sub]
        staff2=map_people_to_positions(sub) # staff2 contains the surbodinates of the surbodinates of root
        for x in staff2:
            if x not in staff:
                staff[x]=staff2[x]
            else:
                for person in staff2[x]:
                    if person not in staff[x]:
                        staff[x].append(person)
                
    return staff