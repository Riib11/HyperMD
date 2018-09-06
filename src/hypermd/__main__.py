import hypermd.cmdline.logger as logger
import hypermd.cmdline.titler as titler

from hypermd.parsing.lexer      import lex
from hypermd.parsing.parser     import parse
from hypermd.compiling.compiler import compile

import argparse
import sys
import subprocess

#
#
#
def main():

    # argument parser
    argparser = argparse.ArgumentParser()
    
    # arguments: positional
    argparser.add_argument("input", nargs="*", help="input file")

    # argument: optional
    argparser.add_argument("-o","--output"  , help="name for the output file")
    argparser.add_argument("-v","--version" , help="version", action="store_true")
    argparser.add_argument("-d","--debug"   , help="print debug logs", action="store_true")

    # parse arguments
    args = argparser.parse_args()
    # logger.log( "log" , args )

    if not args.input:
        titler.print_title()
        quit()

    if args.version:
        titler.print_title()
        quit()

    #
    # compile
    #
    for filename in args.input:
        if not filename.endswith(".hmd"):
            logger.log( "error" , "please provide only .hmd files" )
            quit()

        with open(filename, "r+") as file:
            # lex
            lexed = lex( file )
            # logger.log( "log" , lexed )
            # parse
            parsed = parse(lexed)
            # logger.log( "log" , str(parsed) )
            # compile
            compile( parsed , filename[:-4]+".html" )

#
#
#
main()
