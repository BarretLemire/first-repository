class BinarySearchTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
    def insert(self, value) -> None:
        if value == self.value:
            return
        
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTreeNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTreeNode(value)
                
    def search(self, value) -> bool:
        if self.value == value:
            return True
                
        if value < self.value:
            if self.left:
                return self.left.search(value)
            else:
                return False
                
        if value > self.value:
            if self.right:
                return self.right.search(value)
            else:
                return False
        
    def in_order_traversal(self) -> list:
        elements = []
        
        if self.left:
            elements += self.left.in_order_traversal()
            
        elements.append(self.value)
        
        if self.right:
            elements += self.right.in_order_traversal()
            
        return elements
    
    def find_min(self) -> int:
        if self.left is None:
            return self.value
        return self.left.find_min()
    
    def find_max(self) -> int:
        if self.right is None:
            return self.value
        return self.right.find_max()
    
    def delete(self, value):
        if value < self.value:
            if self.left:
                self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min_val = self.right.find_min()
            self.value = min_val
            self.right = self.right.delete(min_val)
        
        return self
                            
    def height(self) -> int:
        return self._calculate_height(self)
    
    def _calculate_height(self, node):
        if node is None:
            return 0
        else:
            left_height = self._calculate_height(node.left)
            right_height = self._calculate_height(node.right)
            return max(left_height, right_height) + 1
    
    def count_leaves(self) -> int:
        return self._count_leaves(self)
    
    def _count_leaves(self, node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return 1
        return self._count_leaves(node.left) + self._count_leaves(node.right)
    
    def serialize(self) -> str:
        pass
    
    def deserialize(self, tree: str) -> None:
        pass
        
def build_tree(elements):
    if not elements:
        return None
    
    root = BinarySearchTreeNode(elements[0])
    
    for i in range(1, len(elements)):
        root.insert(elements[i])
        
    return root

if __name__ == '__main__':
    numbers = [1, 5, 6, 28, 7, 92, 108]
    number_tree = build_tree(numbers)
    
    print(f"Is 2 in the list?", number_tree.search(2))
    
    
    number_tree.delete(28)
    
    print("After deletion:", number_tree.in_order_traversal())


