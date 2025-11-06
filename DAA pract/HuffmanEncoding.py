# Step 1: Count frequency
def get_freq(text):
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

# Step 2: Build Huffman tree (using simple list)
def build_tree(freq):
    nodes = []  # will store [frequency, character/node]

    for ch, wt in freq.items(): # Convert dictionary to list like [freq, char]
        nodes.append([wt, ch])

    # Repeat until only 1 root node remains
    while len(nodes) > 1:
        # Sort nodes by frequency (smallest first)
        nodes.sort(key=lambda x: x[0])

        left = nodes.pop(0)   # remove and get the smallest
        right = nodes.pop(0)  # remove and get the second smallest

        # Merge them -> new node's frequency = sum of both
        new_node = [left[0] + right[0], [left, right]]
        nodes.append(new_node)

    return nodes[0]  # final root node

# Step 3: Generate binary codes by traversing the tree
def make_codes(node, code="", code_map={}):
    # If node contains a character (leaf node)
    if type(node[1]) == str:
        if code == "":
            code = "0"   # if only one character in input
        code_map[node[1]] = code
    else:
        # Left child = add '0'
        make_codes(node[1][0], code + "0", code_map)
        # Right child = add '1'
        make_codes(node[1][1], code + "1", code_map)

    return code_map

# Step 4: Main program
text = input("Enter text: ")
freq = get_freq(text)
tree = build_tree(freq)
codes = make_codes(tree)

# Step 5: Display result
print("\nCharacter\tCode")
for ch, cd in codes.items():
    print(f"{ch}\t\t{cd}")

# Step 6: Complexity info
print("\nTime Complexity: O(n log n)")
print("Space Complexity: O(n)")


"""
Let’s say the text = “aabc”
| Character | Frequency |
| --------- | --------- |
| a         | 2         |
| b         | 1         |
| c         | 1         |

Tree building (greedy):
Step 1: pick smallest two → b(1) + c(1) → new node(2)
Step 2: now we have [a(2), node(2)]
Step 3: combine → a(2) + node(2) → root(4)


Tree structure:
        (4)
       /   \
     a(2)  (2)
          /   \
        b(1)  c(1)



Codes (Left=0, Right=1):
a → 0
b → 10
c → 11

🧩 Summary
| Aspect               | Description                                  |
| -------------------- | -------------------------------------------- |
| **Algorithm Type**   | Greedy                                       |
| **Goal**             | Shorter binary codes for frequent characters |
| **Time Complexity**  | O(n log n)                                   |
| **Space Complexity** | O(n)                                         |

"""
#----------------------------------------------------------------------------------------------------

"""
OUTPUT...

Enter text: aabc

Character       Code
a               0
b               10
c               11

Time Complexity: O(n log n)
Space Complexity: O(n)

"""