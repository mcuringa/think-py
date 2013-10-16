


def read(inFile):
    f = open(inFile)
    text = f.read()
    return text


def parse(text):

    out = ""
    code = ""
    inCode = False
    for line in text:
        if line.startswith("    .. sourcecode:: python3"):
            inCode = True
            code += "~~~~~~~~~~~~~~~~~~~~~~~~~~~~{.python"

        if inCode:
            if line.
