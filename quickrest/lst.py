"""Simple ReST list."""

class Lst:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return "\n".join(
            ("* " + "\n  ".join(str(item).split("\n")))
            for item in self.items)
