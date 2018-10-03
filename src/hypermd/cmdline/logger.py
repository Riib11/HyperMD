from hypermd.cmdline.printcolor import *

def log( tag , msg ):

    def check(s): return s == tag

    def print_tag(tag_sym, color):
        printc( "["+tag_sym+"]"
            , font=color
            , back=PrintStyle.BACK_black
            , end="")

    if check( "msg" ):
        print_tag( "#" , PrintStyle.FONT_green )
    elif check( "error" ):
        print_tag( "!" , PrintStyle.FONT_red )
    elif check( "log" ):
        print_tag( ">" , PrintStyle.FONT_cyan )
    else:
        print_tag( "%" , PrintStyle.FONT_red )

    print(" "+str(msg))
