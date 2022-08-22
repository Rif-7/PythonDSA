class Tree: 
    
    class Position:
        
        def element(self):
            raise NotImplementedError("Must Be Implemented By Subclass")

        def __eq__(self, other):
            raise NotImplementedError("Must Be Implemented By Subclass")

        def __ne__(self, other):
            return self != other

    def root(self):
        raise NotImplementedError("Must Be Implemented By Subclass")
    
    def parent(self, p):
        raise NotImplementedError("Must Be Implemented By Subclass")

    def num_of_children(self, p):
        raise NotImplementedError("Must Be Implemented By Subclass")

    def children(self, p):
        raise NotImplementedError("Must Be Implemented By Subclass")
    
    def __len__(self):
        raise NotImplementedError("Must Be Implemented By Subclass")

    def is_root(self, p):
        return self.root() == p
    
    def is_leaf(self, p):
        return self.num_of_children(p) == 0
    
    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.root() == p:
            return 0
        return 1 + self.depth(self.parent(p))

    def height(self, p):
        if self.is_leaf(p):
            return 0
        return 1 + max(self.height(child) for child in self.children(p))