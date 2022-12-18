# -*- coding: utf-8 -*-
"""An experiment using a screen-reader to interact with the user
clearly.  In particular, it uses punctuation correctly, inserts
new-line characters after periods or commas (to avoid awkward
mid-sentence pauses due to line-breaks) and introduces a delay after
each line to give the screen reader some processing time.
"""

# by Lawrence Perez, 2022-Dec

from time import sleep

# Global variables
slp = 2  # constant printdelay() sleep time setting
font_size = 12  # default setting

"""Notes (by Daniel for Lawrence):

I used this unused block string instead of line comments so that it
would read better. The interpreter will parse and then ignore it.

"Notes" is a nice word for constuctive critism. I mean well.

The original file had some whitespace issues.

I recommend that you install the code reformatter 'black' using

> pip install black

and invoke it with

> black <file or folder>

'Note from Lawrence: Linux needs black to be installed with sudo privileges to be found.'

Black will reformat your source code in place, fixing any whitespace
issues and anything else that doesn't meet it's uncompromising
standard. Black reformatted this file and fixed these four issues:

- Added one blank line after the import block.
- Added two blank lines before 'def' blocks.
- Added spaces before and after equals signs in assignments.
- Removed a space between the function name 'sleep' and the
  parenthesis following the name that encloses the parameter.

Black is _very_ picky. If it doesn't change anything, you did good.

I have made these changes to the source file:

Added docstrings to procedures. Style guidelines require a docstring
on any public functions (these are not public) and recommend either
a docstring or a comment to describe any private functions.

The top-level procedure of this script was split by the 'def' blocks
that it uses. While valid python, I find it confusing to have a bit
of the main routine at the top and a bit at the bottom. I have
collected the entire procedure at the bottom.

I have converted the top-level script (not including the import lines)
into a 'main' routine that returns an exit status.  The main routine
is called by a top-level script that guards against running the script
upon import and returns the exit status to the operating system.

I have renamed the routine 'load' to 'load_font_size'.

I have added a block for global variables at the top below imports.

Grouped file open read/write and close lines together.

Added function call parenthesis to one file.close() line.

Added an formatted string to say "Font Size is".

Other notes:

Function and variable names should be lowercase with an underscore
character between words.

The 'with open()' pattern may be used to simplify blocks using 'file =
open' and 'file.close()' and ensure close upon file errors (as you did
in the main routine).

"""


def load_font_size():
    """Read the font size from the file 'fontSize.var' and set the
    global setting font_size."""

    global font_size  # global font size setting

    file = open("./fontSize.var", "r")  # can use with open here
    font_size = int(file.read())
    file.close()


def load_sr_delay():
    """Read the sleep delay (in milliseconds)from the file 'srDelay.var' and set the
    global setting slp."""

    global slp  # global delay setting

    file = open("./srDelay.var", "r")  # can use with open here
    slp = int(file.read())
    slp = slp / 1000
    file.close()


def printdelay(s):
    """Print an object with a pause before and after printing."""

    global slp  # global printdelay() sleep time setting

    sleep(slp)
    print(s)
    sleep(slp)


def save_font_size():
    """Ask the user for input and save it to the font size settings file."""

    newsize = input("Type in new font size: ")

    file = open("./fontSize.var", "w")  # can use with open here
    file.write(newsize)
    file.close()

    printdelay("Saved!")


def save_sr_delay():
    """Ask the user for input and save it to the screen reader delay settings file."""

    newsleep = input("Type a new sleep delay you wish to use. ")

    file = open("./srDelay.var", "w")  # can use with open here
    file.write(newsleep)
    file.close()

    printdelay("Saved!")


def main():

    with open("fontSize.var", "w") as f:
        f.write("12")
    with open("srDelay.var", "w") as f:
        f.write("200")

    while True:
        load_sr_delay()
        load_font_size()
        printdelay(f"Font Size is {font_size}, and sleep is {slp}")
        save_font_size()
        save_sr_delay()
    # exit unreachable due to 'while True' above. Use control-C.


# Execute this script
if __name__ == "__main__":
    main()
