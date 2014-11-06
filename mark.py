# mark.py
# by:mxc
"""
Convert an rst chapter in Think Python to Mardkown.
"""

def skip_index(i, lines):
    i += 1
    line = lines[i]
    while line.startswith(" "):
        i += 1
        line = lines[i]

    return i

def parse_image(i, lines):
    pass

def parse(lines):

    out = ""
    n = len(lines)
    i = 0
    while i in range(n):
        line = lines[i]
        if ".. sourcecode:: python3" in line:
            i,code = parse_code(i,lines)
            out += code
        elif ".. index::" in line:
            i = skip_index(i, lines)
        elif ".. image::" in line:
            parse_image(i,lines)
        else:
            out += line
            i += 1
    return out

def parse_code(i,lines):
    code = "~~~~~~~~~~~~~~~~~~~~~~~~~~~~{.python"
    i += 1
    numbers = False
    if ":linenos:" in lines[i]:
        code += " .numberLines"
        i += 1
    code += "}\n"
    i += 1
    line = lines[i]

    while line[0] == " " or len(line.strip()) == 0:
        code += lines[i]
        i += 1
        line = lines[i]

    code = code.replace(" " * 8, "")
    code += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    return i, code

def convert(f):
    lines = list(open(f + ".rst"))
    print("got the lines")
    out = parse(lines)
    print("parsed")
    f = open(f + ".md",'w')
    f.write(out)
    f.flush()
    f.close()
print("converting...")
convert("way_of_the_program")
#convert("dictionaries")
