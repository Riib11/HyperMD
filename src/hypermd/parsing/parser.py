import hypermd.parsing.lexer as lexer

####################################################
# Document
########################
class Document:
    def __init__(self):
        self.content = {
            "body" : [],
            "head" : []
        }

    def add(self, kind, x):
        self.content[kind].append(x)

    def tostring(self):
        s  = "\n---------------------\n"
        s += "head:"
        s += "\n* " + "\n* ".join(map(str,self.content["head"]))
        s += "\n---------------------\n"
        s += "body:"
        s += "\n* " + "\n* ".join(map(str,self.content["body"]))
        return s
    __str__ = tostring; __repr__ = tostring

#
#
#
def parse(lexed):

    doc = Document()
    
    for x in lexed:

        if any([ type(x).name == C.name for C in lexer.blocks_head ]):
            doc.add("head", x)
        else:
            doc.add("body", x)

    return doc