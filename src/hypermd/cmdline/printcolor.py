class PrintStyle:

    # SPEC
    SPEC_normal    = 0
    SPEC_underline = 4
    SPEC_flashing  = 5

    # FONT
    FONT_black     = 30
    FONT_red       = 31
    FONT_green     = 32
    FONT_yellow    = 33
    FONT_blue      = 34
    FONT_pink      = 35
    FONT_cyan      = 36
    FONT_white     = 37

    # BACK
    BACK_black     = 40
    BACK_red       = 41
    BACK_green     = 42
    BACK_yellow    = 43
    BACK_blue      = 44
    BACK_pink      = 45
    BACK_cyan      = 46
    BACK_white     = 47

def printc( string , font="", back="", spec="", end="\n"):
    # print( "[%s;%s;%sm" % (spec,font,back) )
    print( f"\x1b[{spec};{font};{back}m{string}\x1b[0m" , end=end )