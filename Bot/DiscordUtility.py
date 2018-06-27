"""

Author : Robin Phoeng
Date : 27/06/2018
"""

import random

"""
Random assortment of functions
"""
def fudgeRoll():
    d1 = random.randrange(-1, 2, 1)
    d2 = random.randrange(-1, 2, 1)
    d3 = random.randrange(-1, 2, 1)
    d4 = random.randrange(-1, 2, 1)

    return [d1,d2,d3,d4, d1+d2+d3+d4]



def valid_id(mention):
    """
    returns the valid id from a mention string
    :param mention: the mention
    :return: string of id if valid, None otherwise
    """
    if mention is None:
        return None
    if mention[0:2] == "<@" and mention[len(mention)-1] == ">":
        id = mention[2:len(mention)-1]
        if id.isdigit():
            return id
        else:
            return None
    return None

def valid_role(role):
    """
    returns the valid role from a role mention
    :param role: role to validate
    :return: role of id, None otherwise
    """
    if role is None:
        return None
    if role[0:3] == "<@&" and role[len(role)-1] == ">":
        id = role[3:len(role)-1]
        if id.isdigit():
            return id
        else:
            return None
    return None

def is_role(role,roles):
    if role is None:
        return False
    elif role in roles:
        return True
    else:
        return False