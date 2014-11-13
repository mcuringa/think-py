# mark.py
# by:mxc
"""
Convert an rst chapter in Think Python to Mardkown.
"""

import sys
import traceback

def skip_index(i, lines):
    i += 1
    line = lines[i]
    while line.startswith(" "):
        i += 1
        line = lines[i]

    return i

def parse_image(i, lines):
    tmpl = "![{}]({})\\"
    img = lines[i]
    img.replace(".. image:: illustrations", "figs")
    i += 1
    print("--> " + img)
    if ":alt" in lines[i]:
        alt = lines[i].replace(":alt: ", "")
        i += 1
    else:
        alt = ""

    return i, tmpl.format(alt,img)

def parse(lines):

    out = ""
    n = len(lines)
    i = 0
    try:
        while i in range(n):
            line = lines[i]
            if ".. sourcecode:: python3" in line:
                i,code = parse_code(i,lines)
                out += code
            elif ".. index::" in line:
                i = skip_index(i, lines)
            elif ".. image::" in line:
                i, code = parse_image(i,lines)
                out += code
            else:
                out += line
                i += 1
    except Exception as ex:
        print("parsing failed on line", i)
        raise ex
        # a,b,c = sys.exc_info()
        # traceback.print_exception(a,b,c)
    
    return out

def parse_code(i,lines):
    tmpl = """
~~~~~~~~~~~~~~~~~~~~~~~~~~~~{{.python{}}}
{}
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
    i += 1
    numbers = ""
    if ":linenos:" in lines[i]:
        numbers = " .numberLines"
        i += 1

    code = ""
    i += 1
    line = lines[i]

    while line[0] == " " or len(line.strip()) == 0:
        code += lines[i]
        i += 1
        line = lines[i]

    code = code.replace(" " * 8, "")

    return i, tmpl.format(numbers, code)

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


convert("casestudy_fileindexer")
#convert("dictionaries")
