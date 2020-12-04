from tree import Node

class KnightPathFinder:
    def __init__(self,pos):
        self._pos = pos 
        self._root = Node(self._pos)
        self._considered_positions = set(self._pos)

    def get_valid_moves(self,pos):
        valid_move_set = set()
        
        move_set = {
            'up_left': (2,-1),
            'up_right': (2,1),
            'right_up' :(1,2),
            'left_up': (1,-2),
            'right_down': (-1,2),
            'left_down' :(-1,-2),
            'down_right' :(-2, 1),
            'down_left' :(-2, -1)
        }

        for key in move_set:
            new_coord = (pos[0]+move_set[key][0], pos[1]+move_set[key][1])
            if (new_coord[0] < 0 or new_coord[1] < 0) or (new_coord[0] > 7 or new_coord[1] > 7):
                continue
            else:
                valid_move_set.add(new_coord)

        return valid_move_set

    def new_move_positions(self,pos):

        move_set = self.get_valid_moves(pos)

        valid_move_set = move_set.difference(self._considered_positions)

        self._considered_positions = self._considered_positions.union(valid_move_set)

        return valid_move_set

    def build_move_tree(self):

        # root_moves = self.new_move_positions(self._pos)

        # for coord in root_moves:
        #     child_node = Node(coord)
        #     self._root.add_child(child_node)

        que = [self._root]

        while len(que) > 0:
            current_node = que.pop(0)
            moves = self.new_move_positions(current_node.value)
            for move in moves:
                child_node = Node(move)
                current_node.add_child(child_node)
                que.append(child_node)



    def find_path(self,end_position):

        end_node = self._root.breadth_search(end_position)

        root_trace = self.trace_to_root(end_node)

        root_trace.reverse()

        return root_trace

    def trace_to_root(self,end_node):
        
        trace = []

        current_node = end_node

        while current_node.parent != None:
            trace.append(current_node.value)
            current_node = current_node.parent

        trace.append(self._root.value)

        return trace







finder = KnightPathFinder((0, 0))
finder.build_move_tree()
print(finder.find_path((2, 1))) # => [(0, 0), (2, 1)]
print(finder.find_path((3, 3))) # => [(0, 0), (2, 1), (3, 3)]
print(finder.find_path((6, 2))) # => [(0, 0), (1, 2), (2, 4), (4, 3), (6, 2)]
print(finder.find_path((7, 6))) # => [(0, 0), (1, 2), (2, 4), (4, 3), (5, 5), (7, 6)]