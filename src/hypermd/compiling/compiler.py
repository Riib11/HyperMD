import hypermd.parsing.parser as parser
import hypermd.parsing.lexer  as lexer

from hypermd.html.html import *

#
#
#

html_start = """
<!DOCTYPE html>
<html>
"""

html_end = """
</html>
"""

mathjax = """
<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.3/latest.js?config=TeX-MML-AM_CHTML" async></script>"""

highlight = """
<script type="text/javascript" src="highlight/highlight.pack.js">
</script><script type="text/javascript">hljs.initHighlightingOnLoad()</script>"""



#
#
#

def compile(parsed, target):
    parsed.add("head", mathjax)
    parsed.add("head", highlight)

    with open(target, "w+") as file:
        file.write(html_start)

        def tohtml(x):
            s = ""
            if isinstance(x, parser.Document):
                # body
                s += "\n<body>"
                s += "\n<div id=\"container\">"
                s += tohtml(x.content["body"])
                s += "</div>"
                s += "</body>"
                # head
                s += "\n\n<head>"
                s += tohtml(x.content["head"])
                s += "</head>\n"
            elif isinstance(x, lexer.Inline):
                content = tohtml(x.content).strip()
                
                if x.name == "link":
                    content = content.split(" ")
                    e = Element(x.tag, False)
                    e.set_attr("href", content[0])
                    e.set_attr("class", x.name)
                    e.content = content[0]
                    if len(content) > 1:
                        e.content = content[1]
                    s = e.tohtml()

                elif x.name == "mathinline":
                    e = Element(x.tag, False)
                    e.set_attr("class", x.name)
                    e.content = "\\(" + content + "\\)"
                    s = e.tohtml()
                
                else:
                    e = Element(x.tag, False)
                    e.set_attr("class", x.name)
                    e.content = content
                    s = e.tohtml()
            elif isinstance(x, lexer.Line):
                content = tohtml(x.content).strip()
                
                if x.name == "image":
                    e = Element(x.tag, True)
                    e.set_attr("class","image")
                    e.set_attr("src", content)
                    s = e.tohtml()

                elif x.name == "style":
                    e = Element(x.tag, True)
                    e.set_attr("rel"  , "stylesheet")
                    e.set_attr("type" , "text/css")
                    e.set_attr("href" , content)
                    s = e.tohtml()

                elif x.name == "script":
                    e = Element(x.tag, False)
                    e.set_attr("type" , "text/javascript")
                    e.set_attr("src"  , content)
                    s = e.tohtml()

                elif x.name == "highlight":
                    e = Element(x.tag, True)
                    e.set_attr("rel"  , "stylesheet")
                    e.set_attr("type" , "text/css")
                    e.set_attr("href" , "highlight/styles/"+content+".css")
                    s = e.tohtml()

                else:
                    e = Element(x.tag, False)
                    e.set_attr("class", x.name)
                    e.content = content
                    s = e.tohtml()

            elif isinstance(x, lexer.Multiline):
                content = "\n".join(x.content)

                if x.name == "codemultiline":
                    e_outer = Element("pre", False)
                    e_middle = Element("code", False)
                    e = Element("pre", False)
                    e.set_attr("class", x.name + " " + x.arg)
                    e.content = content
                    e_middle.content = e.tohtml()
                    e_outer.content = e_middle.tohtml()
                    s = e_outer.tohtml()

                elif x.name == "mathmultiline":
                    e = Element(x.tag, False)
                    e.set_attr("class", x.name)
                    e.content = "$$\n" + content + "\n$$"
                    s = e.tohtml()

                else:
                    e = Element(x.tag, False)
                    e.set_attr("class", x.name + " " + x.arg)
                    e.content = content
                    s = e.tohtml()

            elif isinstance(x, lexer.Paragraph):
                e = Element("p", False)
                e.set_attr("class", "paragraph")
                e.content = tohtml(x.content)
                s = e.tohtml()

            elif isinstance(x, str):
                s = x
            
            elif isinstance(x, list):
                s = "".join(map(tohtml, x))

            return s



        file.write(tohtml(parsed))

        file.write(html_end)