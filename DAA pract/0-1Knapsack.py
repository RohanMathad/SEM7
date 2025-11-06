# Step 1: Inputs
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
n = len(values)

# Step 2: Create DP table (n+1 x capacity+1)
dp = [[0 for x in range(capacity + 1)] for y in range(n + 1)]

# Step 3: Fill table
for i in range(1, n + 1):
    for w in range(1, capacity + 1):
        if weights[i - 1] <= w:
            dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
        else:
            dp[i][w] = dp[i - 1][w]

# Step 4: Output result
print("Maximum value in Knapsack =", dp[n][capacity])

# Step 5: Complexity
print("\nTime Complexity: O(n * W)")
print("Space Complexity: O(n * W)")


"""
💡 How It Works (Easiest Explanation)
| Step | What Happens                                                                   | Example |
| ---- | ------------------------------------------------------------------------------ | ------- |
| 1️⃣  | Make a table `dp[i][w]` → max value using first `i` items within weight `w`    |         |
| 2️⃣  | For each item, you decide — take it or skip it                                 |         |
| 3️⃣  | Use formula: `dp[i][w] = max(value[i-1] + dp[i-1][w-weight[i-1]], dp[i-1][w])` |         |
| 4️⃣  | Last cell `dp[n][capacity]` = answer                                           |         |


🧩 Summary
| Concept              | Description                                    |
| -------------------- | ---------------------------------------------- |
| **Algorithm Type**   | Dynamic Programming                            |
| **Decision Type**    | Take (1) or Leave (0) → 0/1                    |
| **Time Complexity**  | O(n × W)                                       |
| **Space Complexity** | O(n × W)                                       |
| **Best Used When**   | Items **cannot be divided** (whole items only) |

"""

#---------------------------------------------------------------------------------------------

"""
OUTPUT...

Maximum value in Knapsack = 220

Time Complexity: O(n * W)
Space Complexity: O(n * W)

"""