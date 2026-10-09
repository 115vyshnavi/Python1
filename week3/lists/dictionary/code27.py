import sys
from collections import deque

def solve():
    # Read all input from standard input efficiently
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    W = int(input_data[1])
    nums = [int(x) for x in input_data[2:]]
    
    # dq will store tuples of (value, index)
    dq = deque()
    max_count = 0
    
    # Process the first window
    for i in range(W):
        # Maintain monotonic decreasing order
        while dq and dq[-1][0] < nums[i]:
            dq.pop()
        
        dq.append((nums[i], i))
        
        # If this element matches the current maximum, increment count
        if nums[i] == dq[0][0]:
            max_count += 1
            
    # Output for the very first window
    output = [f"{dq[0][0]} {max_count}"]
    
    # Slide the window across the rest of the hallway
    for i in range(W, N):
        # 1. Remove the element going out of the window
        out_idx = i - W
        if dq[0][1] == out_idx:
            dq.popleft()
            max_count -= 1
            
        # 2. Insert the new element entering the window
        while dq and dq[-1][0] < nums[i]:
            dq.pop()
            
        dq.append((nums[i], i))
        
        # 3. Update the max_count based on the new state
        # If the deque was completely cleared, the new element is the new max
        if len(dq) == 1:
            max_count = 1
        elif nums[i] == dq[0][0]:
            max_count += 1
            
        output.append(f"{dq[0][0]} {max_count}")
        
    # Print all results separated by newlines
    sys.stdout.write('\n'.join(output) + '\n')

if __name__ == '__main__':
    solve()
