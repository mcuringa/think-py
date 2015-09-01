# mark.py
# by:mxc
"""
Convert an rst chapter in Think Python to Mardkown.
"""

import sys
import traceback

def skip_index(lines):
    line = lines.pop(0)
    while line.startswith(" "):
        line = lines.pop(0)

    return

def parse_image(lines):
    tmpl = "![{}]({})"
    img = lines.pop(0)
    img.replace(".. image:: illustrations", "figs")
    print("--> " + img)
    if ":alt" in lines[0]:
        alt = lines.pop(0).replace(":alt: ", "")
    else:
        alt = ""

    return tmpl.format(alt,img)

def parse(lines, out=""):
    if len(lines) == 0:
        return out

    line = lines[0]
    if ".. sourcecode:: python3" or ".. sourcecode:: python" in line:
        lines.pop(0)
        code = parse_code(lines)
        out += code
    elif ".. index::" in line:
        skip_index(lines)
    elif ".. image::" in line:
        code = parse_image(i,lines)
        out += code
    else:
        out += lines.pop(0)
    
    return parse(lines, out)

def parse_code(lines):
    tmpl = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~{{.python{}}}
{}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
    line = lines.pop(0)
    print(line)
    numbers = ""
    if ":linenos:" in line:
        numbers = " .numberLines"

    code = ""
    line = lines.pop(0)

    while line.startswith(" "):
        code += line
        line = lines.pop(0)
    
    code = code.replace(" " * 8, "")

    return tmpl.format(numbers, code)

def convert(f):
    lines = list(open(f + ".rst"))
    out = parse(lines)
    f = open(f + ".md",'w')
    f.write(out)
    f.flush()
    f.close()


def main(rst):
    if rst.endswith(".rst"):
        rst = rst[:-4]
    print(rst)
    print("Converting {}.rst to {}.md".format(rst,rst))
    print("The following images were found while converting:")
    convert(rst)


if __name__ == "__main__":
    main(sys.argv[1])

