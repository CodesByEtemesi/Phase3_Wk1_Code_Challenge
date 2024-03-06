def solution(A):
    N = len(A)
    target = 10
    total_moves = 0

    for i in range(N):
        diff = A[i] - target

        if diff > 0:
            if i == N - 1:
                return -1
            moves = min(diff, A[i + 1] + target - A[i + 1])
            A[i] -= moves
            A[i + 1] += moves
            total_moves += moves
        elif diff < 0:
            if i == 0:
                return -1
            moves = min(-diff, A[i - 1] - target + A[i - 1])
            A[i] += moves
            A[i - 1] -= moves
            total_moves += moves

    # Check if all boxes have exactly 10 bricks
    for brick_count in A:
        if brick_count != target:
            return -1

    return total_moves

# Test cases
print(solution([7, 15, 10, 8]))  
print(solution([11, 10, 8, 12, 8, 10, 11])) 
print(solution([7, 14, 10]))  
