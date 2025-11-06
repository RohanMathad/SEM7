# Step 1: Input values and weights
items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
capacity = 50

# Step 2: Calculate value/weight ratio
for i in range(len(items)):
    value, weight = items[i]
    ratio = value / weight
    items[i] = (value, weight, ratio)

# Step 3: Sort by highest ratio (greedy choice)
items.sort(key=lambda x: x[2], reverse=True)

# Step 4: Pick items
total_value = 0
for value, weight, ratio in items:
    if capacity >= weight:
        total_value += value
        capacity -= weight
    else:
        total_value += ratio * capacity  # take fraction
        break

# Step 5: Output
print("Maximum value in Knapsack =", total_value)

# Step 6: Complexity
print("\nTime Complexity: O(n log n)  (due to sorting)")
print("Space Complexity: O(1)")


"""
Quick Step Explanation
| Step | What Happens                                 | Example                         |
| ---- | -------------------------------------------- | ------------------------------- |
| 1️⃣  | List all items with their values and weights | (60,10), (100,20), (120,30)     |
| 2️⃣  | Compute value/weight ratio                   | [6, 5, 4]                       |
| 3️⃣  | Sort by ratio (descending)                   | pick highest value/weight first |
| 4️⃣  | Fill knapsack until full                     | take full or fractional         |
| 5️⃣  | Output total value                           | 240                             |


Summary Table
| Concept              | Description                              |
| -------------------- | ---------------------------------------- |
| **Strategy**         | Greedy (pick highest value/weight first) |
| **Time Complexity**  | O(n log n)                               |
| **Space Complexity** | O(1)                                     |
| **Best Used When**   | Items can be divided (fractions allowed) |
"""

#---------------------------------------------------------------------------------------

"""
OUTPUT....

Maximum value in Knapsack = 240.0

Time Complexity: O(n log n)  (due to sorting)
Space Complexity: O(1)

"""