from notery.cmdline.printcolor import *

def repeat(n,f):
    for _ in range(n): f()

def fill( n=1 ):
    repeat(n, lambda:
        printc(" ", back=PrintStyle.BACK_red, end=""))

def space( n=1 ): 
    repeat(n, lambda:
        printc(" ", back=PrintStyle.BACK_black, end=""))

def shadow_h( n=1 ):
    # repeat(n, lambda: printc("═", spec=2, back=PrintStyle.BACK_black, end=""))
    repeat(n, lambda: printc("═", spec=2, back=PrintStyle.BACK_black, end=""))

def shadow_v( n=1 ):
    repeat(n, lambda: printc("║", spec=2, back=PrintStyle.BACK_black,  end=""))

def shadow_cbl( n=1 ):
    repeat(n, lambda: printc("╝", spec=2, back=PrintStyle.BACK_black,  end=""))

def shadow_ctr( n=1 ):
    repeat(n, lambda: printc("╔", spec=2, back=PrintStyle.BACK_black,  end=""))

def shadow_ctl( n=1 ):
    repeat(n, lambda: printc("╗", spec=2, back=PrintStyle.BACK_black,  end=""))

def shadow_t( n=1 ):
    repeat(n, lambda: printc("╦", spec=2, back=PrintStyle.BACK_black,  end=""))

def shadow(): printc(" ", spec=2, back=PrintStyle.BACK_black, font=PrintStyle.FONT_white, end="")

def br( n=1 ):
    repeat(n, lambda:
        print())

"""
left bottom  : ▖

left top     : ▘

right bottom : 

right top    :




"""

def shape( ss ):
    for s in ss:
        for c in s:
            spec = 1
            back = PrintStyle.BACK_black
            font = PrintStyle.FONT_green
            if   c == "#":
                fill()
                c = ""
            elif c == "/": c = "/"
            elif c == "}": c = "\\"
            elif c == "1":
                c = "\\"
                font = PrintStyle.FONT_red
            elif c == "2":
                c = "/"
                font = PrintStyle.FONT_red
            elif c == "3":
                c = "|"
                font = PrintStyle.FONT_red
            elif c == "4":
                c = "_"
                font = PrintStyle.FONT_red
            # elif c == " ": space()
            # elif c == "-": shadow_h()
            # elif c == "|": shadow_v()
            # elif c == "/": shadow_cbl()
            # elif c == "^": shadow_ctr()
            # elif c == "]": shadow_ctl()
            # elif c == "T": shadow_t()
            printc(c, spec=spec, back=back, font=font, end="")
        br()


def print_title():

    print()
    print("version 0.0.0")

    shape([
        "               ___  __  ___               ",
        "    /  }/   / /  / /   /  /          44   ",
        "   /   /}  / /  / /   /  /  31  23  3  1  ",
        "  /___/  }/ /__/ /__ /__/   3 12 3  3   1 ",
        " /   /   / /    /   / }     3    3  3   2 ",
        "/   /   / /    /__ /   }    3    3. 3442 .",
        "                                          ",
    ])