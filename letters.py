def solution(N):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_length = len(alphabet)
    
    repeat_count = N // alphabet_length
    
    remaining_chars = N % alphabet_length
    
    result = alphabet * repeat_count
    
    result += alphabet[:remaining_chars]
    
    return result
print(solution(3)) 
print(solution(5))  
print(solution(30))  

