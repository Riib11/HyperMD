####################################################
# Block
########################
blocks_head = []

class Block:
    name = "Block"
    tag = "div"
    content_seperator = ""
    allows_nesting = True
    def __init__(self, parent):
        self.parent = parent
        self.parent.add(self) if parent else None
        self.content = []

    def add(self, x): self.content.append(x)

    def get_parent(self):
        return self.parent if self.parent else self

    def __getitem__(self, i): return self.content[i]
    def __iter__(self): return iter(self.content)

    def tostring(self): 
        s = f"({self.name})["
        s += self.content_seperator.join(map(str,self.content))
        s += "]"
        return s
    __str__ = tostring; __repr__ = tostring

####################################################
# Body
########################
class Body(Block):
    name = "Body"
    content_seperator = "\n"
    def __init__(self):
        super().__init__(None)

#
class Paragraph(Block):
    name = "Paragraph"

####################################################
# Inline
########################
blocks_inline = []

class Inline(Block):
    start, end = "", ""
    
    @classmethod
    def is_start(cls, c): return c == cls.start
    @classmethod
    def is_end  (cls, c): return c == cls.end


class Span(Inline):
    name = "span"
    tag = "span"

#
#
def make_inline(_name, _tag, _start, _end=None, _allows_nesting=True, is_head=False):
    class X(Inline):
        name, start, tag, allows_nesting = _name, _start, _tag, _allows_nesting
        end = _end if _end else _start
    blocks_inline.append(X)

    if is_head: blocks_head.append(X)

#
#
make_inline("italic"     , "span" , "_")
make_inline("bold"       , "span" , "*")
make_inline("link"       , "a"    , "@", _allows_nesting=False)
make_inline("codeinline" , "code" , "`", _allows_nesting=False)
make_inline("mathinline" , "span" , "$", _allows_nesting=False)

####################################################
# Line
########################
blocks_line = []

class Line(Block):
    start = ""
    allows_nesting = True

    def __init__(self, parent, line):
        super().__init__(parent)
        self.arg = line

    @classmethod
    def is_start(cls, line): return line.startswith(cls.start)
    @classmethod
    def remove_start(cls, line): return line[len(cls.start):].strip()

#
#
class UnorderedListItem(Line):
    name = "unorderedlistitem"
    starts = ["-", "* "]
    tag = "li"
    allows_nesting = True

    @classmethod
    def is_start(cls, line):
        return any([line.startswith(s) for s in cls.starts])
    @classmethod
    def remove_start(cls, line):
        for s in cls.starts:
            if line.startswith(s):
                return line[len(s):]

blocks_line.append(UnorderedListItem)

# this didn't work out so well...
#
# class OrderedListItem(Line):
#     name = "orderedlistitem"
#     tag = "li"
#     allows_nesting = True

#     def __init__(self, parent, line):
#         if ". " in line:
#             line = line[:line.index(". ")]
#         elif ") " in line:
#             line = line[:line.index(") ")]
#         super().__init__(parent, line)

#     @classmethod
#     def is_start(cls, line):
#         if ". " in line:
#             s = line[:line.index(". ")]
#             return s.isalnum() and len(s) <= 3
#         elif ") " in line:
#             s = line[:line.index(") ")]
#             return s.isalnum() and len(s) <= 3

#         return False

#     @classmethod
#     def remove_start(cls, line):
#         if ". " in line:
#             return line[line.index(". ")+2:]
#         elif ") " in line:
#             return line[line.index(") ")+2:]

# blocks_line.append(OrderedListItem)

#
#
def make_line(_name, _start, _tag, _allows_nesting=True, is_head=False):
    class X(Line):
        name, start, tag, allows_nesting = _name, _start, _tag, _allows_nesting
    blocks_line.append(X)

    if is_head: blocks_head.append(X)

#
#
make_line("h5", "#####" , "h5")
make_line("h4", "####"  , "h4")
make_line("h3", "###"   , "h3")
make_line("h2", "##"    , "h2")
make_line("h1", "#"     , "h1")
make_line("image", "%"  , "img")
make_line("quote", "> " , "div")
make_line("align-right", "]]]", "div")

make_line("style"  , "::style"  , "link"   , False, True)
make_line("script" , "::script" , "script" , False, True)
make_line("title"  , "::title"  , "title"  , False, True)
make_line("highlight" , "::highlight" , "link" , False, True)

####################################################
# Multiline
########################
blocks_multiline = []

class Multiline(Block):
    start, end = "", ""

    def __init__(self, parent, arg):
        super().__init__(parent)
        self.arg = arg

    @classmethod
    def is_start(cls, line): return line.startswith(cls.start)
    @classmethod
    def is_end(cls, line): return line.startswith(cls.end)
    @classmethod
    def remove_start(cls, line): return line[len(cls.start):].strip()

    def tostring(self): 
        s = f"({self.name}:{self.arg})["
        s += self.content_seperator.join(map(str,self.content))
        s += "]"
        return s
    __str__ = tostring; __repr__ = tostring

#
#
def make_multiline(_name, _start, _end, _tag, is_head=False):
    class X(Multiline):
        name, start, end, tag = _name, _start, _end, _tag
    blocks_multiline.append(X)
    
    if is_head: blocks_head.append(X)

make_multiline("codemultiline", "```"       , "```"   , "pre code")
make_multiline("mathmultiline", "$$"        , "$$"    , "p")
make_multiline("style"        , "::style{"  , "::}"   , "style", True)
make_multiline("script"       , "::script{" , "::}"   , "script", True)

#
#
#
def lex(file):

    block = Body()

    for line in file:

        if line.startswith("---"):
            continue

        elif isinstance(block, Multiline):
            # special line (inside multiline)
            
            # check if current multiline end
            if block.is_end(line):
                block = block.get_parent()
                continue

            # else, just add to multiline
            block.add(line.strip("\n"))

        else:
            # normal line
            line = line.strip()
            if line == "": continue

            # check if a new multiline start
            is_multiline = False
            for bmultiline in blocks_multiline:
                if bmultiline.is_start(line):
                    block = bmultiline(block,
                        bmultiline.remove_start(line))
                    is_multiline = True
                    break
            if is_multiline: continue

            # get line block for this line
            is_paragraph = True
            for bline in blocks_line:
                if bline.is_start(line):
                    block = bline(block, line)
                    line = bline.remove_start(line)
                    is_paragraph = False
                    break
            # if not a special block line, then paragraph
            if is_paragraph:
                block = Paragraph(block)

            # lex line for inline block
            # alows lexed nesting
            if block.allows_nesting:
                inline = Span(block)
                for c in line:
                    normal = True
                    # check for end of current inline block
                    if inline.is_end(c):
                        inline = inline.get_parent()
                        continue
                    if inline.allows_nesting:
                        # check for start of new inline block
                        for binline in blocks_inline:
                            if binline.is_start(c):
                                inline = binline(inline)
                                normal = False
                                break
                    # else, just normal add
                    if normal:
                        inline.add(c)
            # doesn't allow lexed nesting, so just
            # add line raw
            else:
                block.add(line)

            # end of line, so escape block
            block = block.get_parent()

    # escape all inlines
    while not isinstance(block, Body):
        block = block.get_parent()

    return block