def solution(numbers):
    # TODO: implement the function according to the task description
    position = 0
    obstacle_found = False
    output = []
    
    while position < len(numbers):
        if numbers[position] < 0:
            output.append(-1)
            position += 1
            continue
        
        for i in range(position + 1, position + numbers[position] + 1, 1):
            if i == len(numbers):
                break
            if numbers[i] < 0:
                obstacle_found = True
                break
        
        if obstacle_found == True:
            output.append(i)
            obstacle_found = False
        else:
            output.append(numbers[position])
                
        position += 1
        
    return output
    
