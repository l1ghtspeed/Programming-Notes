class Node:
    def __init__(self, val, start_ind, end_ind, left=None, right=None):
        self.val = val
        self.start_ind = start_ind
        self.end_ind = end_ind
        self.left = left
        self.right = right

    @property
    def interval(self):
        return (self.start_ind, self.end_ind)


def make_segment_tree(lst):
    return _make_segment_tree(lst, 0, len(lst) - 1)


def _make_segment_tree(lst, start_ind, end_ind):
    if start_ind == end_ind:
        assert(len(lst) == 1)
        val = lst[0]
        return Node(val, start_ind, end_ind)

    mid = len(lst) // 2

    left = _make_segment_tree(lst[:mid], start_ind, start_ind + mid - 1)
    right = _make_segment_tree(lst[mid:], start_ind + mid, end_ind)

    root_val = left.val + right.val

    return Node(root_val, start_ind, end_ind, left, right)

def query(node, start_ind, end_ind):
    if node.start_ind == start_ind and node.end_ind == end_ind:
        return node.val

    result = 0
    left = node.left
    right = node.right

    if left.start_ind <= start_ind <= left.end_ind:
        result += query(left, start_ind, min(end_ind, left.end_ind))

    if right.start_ind <= end_ind <= right.end_ind:
        result += query(right, max(start_ind, right.start_ind), end_ind)

    return result
