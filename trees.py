# ===================================================================================
# General Trees
# =================================================================================


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.child.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = '    ' * self.get_level()
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if len(self.child) > 0:
            for c in self.child:
                c.print_tree()


def build_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


# root = build_tree()
# root.print_tree()


# ===================================================================================
# Binary Trees
# ===================================================================================


class BinaryTrees:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data is self.data:
            return
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTrees(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTrees(data)

    def print_tree(self):
        elements = []

        if self.left:
            elements += self.left.print_tree()

        else:
            if self.right:
                elements += self.right.print_tree()

        elements.append(self.data)

        return elements

def build_tree(elements):
    root = BinaryTrees(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

        return root


numbers = [100, 20, 3, 4, 40, 50, 20, 77, 82]
numbers_tree = build_tree(numbers)
print(numbers_tree.print_tree())