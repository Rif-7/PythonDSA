from Tree import Tree


class BinaryTree(Tree):
    """Abstract Base Class Representing a Binary Tree Structure"""

    def left(self, p):
        raise NotImplementedError("Must Be Implemented By Subclass")

    def right(self, p):
        raise NotImplementedError("Must Be Implemented By Subclass")

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            # p must be root 
            return None

        if self.left(parent) == p:
            return self.right(parent)
        else:
            return self.left(parent)
    
    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        elif self.right(p) is not None:
            yield self.right(p)
        

        

