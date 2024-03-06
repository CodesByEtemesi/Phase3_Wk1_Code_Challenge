def digit_sum(num):
    return sum(int(digit) for digit in str(num))

def solution(A):
    # Dictionary to store the maximum sum for each digit sum
    max_sums = {}

    for num in A:
        
        d_sum = digit_sum(num)
        max_sums[d_sum] = max(max_sums.get(d_sum, -1), num)

    max_pair_sum = 1
    for i in range(1, 100):
        if i in max_sums:
            for j in range(i + 1, 100):
                if j in max_sums:
                    max_pair_sum = max(max_pair_sum, max_sums[i] + max_sums[j])

    return max_pair_sum if max_pair_sum != 1 else -1


print(solution([51, 71, 17, 42]))  
print(solution([42, 33, 60]))       
print(solution([51, 32, 43]))       
