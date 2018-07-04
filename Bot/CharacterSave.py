"""

Author : Robin Phoeng
Date : 4/07/2018
"""



from Character import *

def save(c):
    """
    saves a character
    :param c: character to save
    """
    assert isinstance(c, Character)

    # generate string to write
    lines = []
    lines.append("%s %d" %(c.get_name(),c.get_fate()))
    for a in c.aspects:
        lines.append("aspect %s" % str(a))

    for s in c.skills:
        lines.append("skill %s" % str(s))

    for b in c.bars.values():
        lines.append("bar %s" % str(b))

    lines.append("con_bar %s" % str(c.consequence_bar))

    for con in c.consequences:
        lines.append("con %s" % str(con))

    print(lines)

    # save name and fate points first
    with open("Game/%s.txt" %c.get_name(),"w") as file:
        file.write("\n".join(lines))


def load(filename):
    """
    loads a character
    :param filename: the name of the file to open
    :return: A character
    """

    with open("Game/%s.txt" % filename,"r") as file:
        title = file.readline().split(" ")
        cha = Character(title[0])
        cha.change_fate(int(title[1])) # assume is digits

        for line in file:
            args = line.rstrip("\n").split(" ")
            if args[0] == "aspect":
                cha.add_aspect(" ".join(args[1:]))
            elif args[0] == "bar":
                b = Bar(args[1])
                for box in args[2:]:
                    if box[0] == "~":
                        used_box = Box(int(box[3]))
                        used_box.spend()
                        b.add_box(used_box)
                    else:
                        b.add_box(Box(int(box[1])))
                cha.add_bar(b)
            elif args[0] == "skill":
                cha.add_skill(int(args[1]),args[2])
            elif args[0] == "con_bar":
                for box in args[2:]:
                    b = cha.consequence_bar
                    if box[0] == "~":
                        b.add_box(Box(int(box[3])))
                    else:
                        b.add_box(Box(int(box[1])))
            elif args[0] == "con":
                # line 1
                cha.add_consequence(int(args[1]))
                consequence = cha.get_consequence(int(args[1]))
                # get next line and read all aspects
                for aspect in file.readline().rstrip("\n").split(" "):
                    consequence.add_aspect(aspect)
                consequence.set_text(file.readline().rstrip("\n")[5:])

    return cha

