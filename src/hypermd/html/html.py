class Element:
    def __init__(self, name, single):
        self.name = name
        self.single = single
        self.attrs = {}
        self.content = ""

    def set_attr(self, k, v): self.attrs[k] = v
    def get_attr(self, v): return self.attrs[k]

    def tohtml(self):
        attrs = (" " + " ".join([ f"{k}=\"{v}\""
            for k,v in self.attrs.items() ])
            if len(self.attrs) > 0
            else "")
        if self.single:
            s = f"<{self.name}{attrs}>"
            return s
        else:
            s = f"<{self.name}{attrs}>"
            s += self.content
            s += f"</{self.name}>"
            return s
    __str__ = tohtml; __repr__ = tohtml