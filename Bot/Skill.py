"""

Author : Robin Phoeng
Date : 22/06/2018
"""

class SkillContainer:
    """
    A container of skills, ordered by highest
    """
    def __init__(self):
        self.skills = []
        self.sorted = True

    def add(self,level,name):
        """
        Add a new skill
        Non-case sensitive, does not allow for duplicates
        :param level: the level of the skill
        :param name: the name of the skill
        :return: True if added
        """
        search = name.lower()
        for skill in self.skills:
            if skill.text == search:
                return False
        self.skills.append(Skill(level,name.lower()))
        self.sorted = False
        return True

    def remove(self,name):
        """
        Removes a skill
        Non-case sensitive, assumes no duplicates
        :param name: the name of the skill
        :return: the skill that is removed, None otherwise
        """
        search = name.lower()
        for skill in self.skills:
            if skill.text == search:
                self.skills.remove(skill)
                return skill
        return None

    def get_level(self, name):
        """
        Get a skill, non case sensitive
        All skills are stored in lower case.
        :param name: the name of the skill
        :return: the level of the skill, none otherwise
        """
        search = name.lower()
        for skill in self.skills:
            if skill.text == search:
                return skill.level
        return None

    def __str__(self):
        """
        Display skills, with highest ones first
        :return: A string of highest skills first
        """
        if len(self.skills) == 0:
            return ""
        # sort skills
        if not self.sorted:
            self.skills.sort(key=lambda a:a.level,reverse= True) # reverse true to sort descending
        output = ""
        for skill in self.skills:
            output += "| " + str(skill) + " "
        output += "|" # add the last |

        return output


class Skill:
    """
    A representation of a skill in Fate SRD
    """
    def __init__(self, level, text):
        self.level = level
        self.text = text

    def __str__(self):
        return "%d %s" % (self.level, self.text)


