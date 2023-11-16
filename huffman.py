import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

def print_nodes(node, val=''):
    newVal = val + str(node.huff)
    if node.left:
        print_nodes(node.left, newVal)
    if node.right:
        print_nodes(node.right, newVal)
    if not node.left and not node.right:
        print(f"{node.symbol} -> {newVal}")

num_chars = int(input("Enter the number of characters: "))
chars = []
freq = []
for i in range(num_chars):
    char = input(f"Enter character {i + 1}: ")
    chars.append(char)
    frequency = int(input(f"Enter frequency for {char}: "))
    freq.append(frequency)

nodes = []
for x in range(len(chars)):
    heapq.heappush(nodes, Node(freq[x], chars[x]))

while len(nodes) > 1:
    left = heapq.heappop(nodes)
    right = heapq.heappop(nodes)
    left.huff = 0
    right.huff = 1
    newNode = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
    heapq.heappush(nodes, newNode)

print_nodes(nodes[0])
