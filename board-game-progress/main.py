def solution(numbers, obstacle):
    # TODO: implement function
    moves = 0
    moves_arr = []
    current_step = 0
    i = 0
    
    while i < len(numbers):
        position = numbers[current_step] + current_step
        moves += 1
        
        if numbers[current_step] == obstacle:
            moves_arr.append(-1)
        elif position >= len(numbers):
            moves_arr.append(moves)
        else:
            current_step = position
            continue
        
        moves = 0
        i += 1
        current_step = i    
    
    return moves_arr