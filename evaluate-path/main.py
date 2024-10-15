def evaluatePath(numbers):
    # TODO: implement the function
    direction = 1
    pos = 0
    moves = 0
    reverse_count = 0
    
    while True:
        steps = pos + (numbers[pos] * direction)
        
        if numbers[pos] == 0:
            return (pos, moves)
        elif steps >= len(numbers) or steps < 0:
            reverse_count += 1
            direction *= -1
            steps = pos + (numbers[pos] * direction)
            
            if reverse_count > 1:
                return (pos, moves)
        else:
            pos = steps
            moves += 1
            
            
