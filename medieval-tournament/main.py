def tournament(knights):
    rounds = 0
    all_equivalent = False
    
    while len(knights) > 1 and all_equivalent == False:
        rounds += 1
        current_knights = []
        
        for i in range(len(knights)):
            if i+1 >= len(knights):
                if (knights[i]-knights[0]) > 0:
                    current_knights.append(knights[i]-knights[0])
            else:
                if (knights[i]-knights[i+1]) > 0:
                    current_knights.append(knights[i]-knights[i+1])
        
        knights = current_knights.copy()
        score = knights[0]
        
        for i in range(len(knights)):
            if knights[i] != score:
                break
            elif i == len(knights) - 1:
                all_equivalent == True
        
    return rounds