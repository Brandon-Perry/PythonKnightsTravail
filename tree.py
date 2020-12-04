
class Node:
    def __init__(self,value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    @property
    def parent(self):
        return self._parent

    def add_child(self,new_child):
        if new_child not in self._children:
            self._children.append(new_child)
            new_child.parent = self

    def remove_child(self,child):
        if child in self._children:
            self._children.remove(child)
            child.parent = None

    @parent.setter
    def parent(self,new_parent):
        if self._parent == new_parent:
            return 
        if self._parent is not None:
            self._parent.remove_child(self)
        self._parent = new_parent
        if new_parent != None:
            new_parent.add_child(self)

    def depth_search(self,value):

       
        
        if self._value == value:
            return self
        
        for child in self._children:
            node = child.depth_search(value)
            if node is not None:
                return node 

        
        # if len(self.children) > 0:
        #     for child in self.children:
        #         child.depth_search(value)
        # if self.value = value:
        #     return self

        
        

    def breadth_search(self,value):
        que = [self]
        current_node = self

        if self.value == value:
            return self

        while True:
            current_node = que[0]
            que.remove(current_node)

            if current_node.value == value:
                return current_node
            else:
                children = current_node.children
                que = children + que

            if len(que) == 0:
                return None
        


# node1 = Node("root1")
# node2 = Node("root2")
# node3 = Node("root3")

# node3.parent = node1
# node3.parent = node2

# for child in node1.children:
#     print('node1',child.value)
# for child in node2.children:
#     print('node2',child.value)