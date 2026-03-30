def mergeSort(arr):
    """
    Sorts an array in ascending order using the Divide and Conquer paradigm.
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) > 1:
        # 1. Recursive splitting of the array [cite: 29]
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively call mergeSort on both halves
        mergeSort(left_half)
        mergeSort(right_half)

        # 2. Merge function implementation [cite: 30]
        i = j = k = 0

        # Compare elements from both halves and place the smaller one in the main array
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check for any remaining elements in the left half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check for any remaining elements in the right half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            
    return arr


def activitySelection(start_times, finish_times):
    """
    Selects the maximum number of non-overlapping activities.
    """
    n = len(finish_times)
    if n == 0:
        return [], 0

    # Combine start and finish times into a list of tuples: (start, finish, original_index)
    activities = list(zip(start_times, finish_times, range(n)))

    # Sort activities based on their finish time 
    activities.sort(key=lambda x: x[1])

    selected_activities = []
    
    # Apply greedy selection: Always pick the first activity after sorting 
    selected_activities.append(activities[0])
    last_finish_time = activities[0][1]

    # Iterate through the remaining activities
    for i in range(1, n):
        # If the start time is greater than or equal to the finish time of the 
        # previously selected activity, select it
        if activities[i][0] >= last_finish_time:
            selected_activities.append(activities[i])
            last_finish_time = activities[i][1]

    # Calculate the total number of activities selected [cite: 49]
    total_selected = len(selected_activities)
    
    # Returns the selected activities and the total count 
    return selected_activities, total_selected


def knapsack(weights, values, capacity):
    """
    Finds the maximum value achievable in a 0/1 Knapsack using a 2D DP table.
    """
    n = len(values)
    
    # Initialize a 2D table with zeros [cite: 58]
    # dp[i][w] will store the max value using the first 'i' items with capacity 'w'
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If the current item's weight is less than or equal to the current capacity
            if weights[i-1] <= w:
                # Maximize between including the item and excluding it
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                # If the item is too heavy, we must exclude it
                dp[i][w] = dp[i-1][w]

    # The bottom-right cell contains the maximum value achievable [cite: 61]
    return dp[n][capacity]