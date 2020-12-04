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

        self._considered_positions.union(valid_move_set)

        return valid_move_set

    def build_move_tree(self):

        root_moves = self.new_move_positions(self._pos)

        for coord in root_moves:
            child_node = Node(coord)
            self._root.add_child(child_node)


    def find_path(self,end_position):

        pass

    def trace_to_root(self,end_node):
        pass







test_knight = KnightPathFinder((0,0))
test_knight.build_move_tree()

print(test_knight._root.children)
