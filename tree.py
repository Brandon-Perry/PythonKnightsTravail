
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

    def add_child(self,new_child):
        if new_child not in self._children and new_child != None:
            self._children.append(new_child)
            new_child._parent = self

    def remove_child(self,child):
        if child in self._children and child != None:
            self._children.remove(child)
            child._parent = None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self,new_parent):
        if new_parent != None:
            if self._parent != None:
                current_children = self._parent._children 
                print(current_children)
                map(self._parent.remove_child,current_children)
           
            self._parent = new_parent
            self._parent.add_child(self)


node1 = Node("root1")
node2 = Node("root2")
node3 = Node("root3")

node3.parent = node1
node3.parent = node2

print(node1.children)
print(node2.children)