# Personal Notes for Chapter 10: Dynamic Programming

## Key Concepts Explained

### The DP Mindset
- **Don't recompute, reuse**: If you've solved a subproblem before, save the answer
- **Build up systematically**: Start with small problems, combine to solve bigger ones
- **Optimal substructure**: The best solution to a big problem contains the best solutions to smaller problems
- **Overlapping subproblems**: The same small problem appears multiple times

### Top-Down vs Bottom-Up
- **Memoization (Top-Down)**: Start from the big problem, work backwards, cache as you go
  - Natural for recursive thinkers
  - Only computes what's needed
  - Can be slower due to recursion overhead
- **Tabulation (Bottom-Up)**: Start from small problems, build up to the big one
  - More efficient in practice
  - Computes everything systematically
  - Easier to understand the flow

### The DP Recipe (My Checklist)
1. **Define the subproblem**: What smaller problem am I solving?
2. **Write the recurrence**: How does the answer relate to smaller answers?
3. **Identify base cases**: What's the smallest problem I can solve directly?
4. **Choose approach**: Memoization or tabulation?
5. **Implement carefully**: Watch for off-by-one errors
6. **Optimize space**: Can I use less memory?

## Examples That Clicked

### Fibonacci with Memoization
```python
memo = {}
def fib(n):
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
```
- **Before**: 2^n calls, exponential time
- **After**: n calls, linear time
- **Insight**: Cache prevents recomputation of overlapping subproblems

### 0/1 Knapsack
```python
# dp[i][w] = max value using first i items, capacity w
for i in range(1, n+1):
    for w in range(W+1):
        # Don't take item i
        dp[i][w] = dp[i-1][w]
        # Take item i (if it fits)
        if w >= weights[i-1]:
            dp[i][w] = max(dp[i][w], dp[i-1][w-weights[i-1]] + values[i-1])
```
- **Key insight**: For each item, decide whether to include it or not
- **State**: Which items considered, remaining capacity
- **Choice**: Take or leave each item

### Coin Change (Minimum Coins)
```python
# dp[amount] = min coins to make amount
dp[0] = 0  # Base case
for coin in coins:
    for amt in range(coin, amount+1):
        dp[amt] = min(dp[amt], dp[amt-coin] + 1)
```
- **Unbounded choice**: Can use each coin multiple times
- **Greedy fails**: [1,3,4] to make 6: greedy takes 4+1+1=3, optimal is 3+3=2

## Real-World Applications
- **Resource allocation**: Which projects to fund with limited budget?
- **DNA sequencing**: Finding similarities between genetic sequences
- **File compression**: Building optimal Huffman codes
- **Navigation**: Finding shortest routes in graphs
- **Text editing**: Computing edit distance between documents
- **Manufacturing**: Optimizing production schedules

## Common Patterns I See Everywhere Now

### Pattern 1: Choice Problems
- **At each step**: Choose between options
- **State tracks**: What's been chosen, resources remaining
- **Examples**: Knapsack, subset sum, coin change

### Pattern 2: Sequence Alignment
- **Compare two sequences**: Strings, arrays, paths
- **2D table**: i vs j positions
- **Examples**: LCS, edit distance, string similarity

### Pattern 3: Grid/Matrix Problems
- **2D state space**: Position in grid
- **Movement constraints**: Can only move certain ways
- **Examples**: Grid paths, matrix multiplication order

## Performance Optimization Tricks

### Space Optimization
- **1D instead of 2D**: Keep only current and previous rows
- **Rolling array**: Reuse space for periodic patterns
- **Bit manipulation**: Compress state for subset problems

### Time Optimization
- **Early termination**: Stop when optimal found
- **Symmetry exploitation**: Avoid redundant computations
- **Preprocessing**: Sort or transform input for efficiency

## My Thoughts
- DP feels like magic - you cache answers and suddenly exponential problems become polynomial
- The hardest part is recognizing when a problem is "DP-shaped"
- Once you see the pattern, it's addictive - you start seeing DP opportunities everywhere
- Tabulation often feels more intuitive than memoization, even if memoization is easier to write

## Common Pitfalls (That I Keep Making)
- **Wrong base cases**: Forgetting to initialize dp[0] or edge cases
- **Off-by-one errors**: Especially with 0-based vs 1-based indexing
- **Wrong recurrence**: Missing a choice or miscalculating transitions
- **Space confusion**: Trying to optimize space before getting logic right

## Exercises/Thoughts
- Try implementing both memoization and tabulation for the same problem
- Look for DP in everyday problems (optimal shopping, scheduling, routing)
- Practice recognizing overlapping subproblems and optimal substructure
- Experiment with space optimizations on large DP tables</content>
<parameter name="filePath">chapter_10_dynamic_programming/notes.md