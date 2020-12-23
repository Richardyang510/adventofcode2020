class Node:
    def __init__(self, next=None, prev=None, data=0):
        self.next = next
        self.prev = prev
        self.data = data


class DLList:
    head = None
    tail = None

    node_map = {}

    def __init__(self, first_val, second_val):
        self.head = Node(data=first_val)
        self.tail = Node(data=second_val)
        self.head.next = self.tail
        self.head.prev = self.tail
        self.tail.next = self.head
        self.tail.prev = self.head
        self.node_map[first_val] = self.head
        self.node_map[second_val] = self.tail

    def insert_after(self, prev_node, new_node):
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next.prev = new_node
        self.node_map[new_node.data] = new_node
        if prev_node == self.tail:
            self.tail = new_node
        return new_node

    def pop_node(self, node):
        if self.head == node:
            self.head = node.next

        if self.tail == node:
            self.tail = node.prev

        node.prev.next = node.next
        node.next.prev = node.prev

        return node

    def get_node(self, val):
        return self.node_map[val]

    def print(self):
        ret = ''
        curr_node = self.head
        while curr_node != self.tail:
            ret += str(curr_node.data) + ','
            curr_node = curr_node.next
        ret += str(curr_node.data) + ','
        print(ret[:-1])


num_it = 10000000
cups_num = 123487596
cups = list(map(int, str(cups_num)))
num_cups = len(cups)

# part 2
cups += list(range(10, 1000001))

smallest_cup = min(cups)
largest_cup = max(cups)

dllist = DLList(cups[0], cups[1])
last_node_inserted = dllist.get_node(cups[1])

for c in cups[2:]:
    new_node = Node(data=c)
    last_node_inserted = dllist.insert_after(last_node_inserted, new_node)

cur_cup = dllist.get_node(cups[0])

for it in range(num_it):
    if it % (num_it // 100) == 0:
        print(it)

    pickup_1 = dllist.pop_node(cur_cup.next)
    pickup_2 = dllist.pop_node(cur_cup.next)
    pickup_3 = dllist.pop_node(cur_cup.next)

    dest_cup_val = cur_cup.data - 1
    while dest_cup_val in [pickup_1.data, pickup_2.data, pickup_3.data]:
        dest_cup_val -= 1

    if dest_cup_val < smallest_cup:
        dest_cup_val = largest_cup
        while dest_cup_val in [pickup_1.data, pickup_2.data, pickup_3.data]:
            dest_cup_val -= 1

    dest_cup = dllist.get_node(dest_cup_val)

    dllist.insert_after(dest_cup, pickup_3)
    dllist.insert_after(dest_cup, pickup_2)
    dllist.insert_after(dest_cup, pickup_1)

    cur_cup = cur_cup.next


node1 = dllist.get_node(1)
a = node1.next
b = a.next

print(a.data, b.data, a.data * b.data)
