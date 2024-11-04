def solution(array1, array2):
    if array1 == array2:
        return (array1,0)
    
    m_distance = 0
    distance_dict = {}
    
    for i in range(len(array1)):
        for arr1, arr2 in zip(array1, array2):
            m_distance += abs(arr1-arr2)
        if m_distance in distance_dict.keys():
            if int(''.join(map(str, array1))) < int(''.join(map(str,distance_dict[m_distance]))):
                distance_dict[m_distance] = array1[:]
        else:
            distance_dict[m_distance] = array1[:]
        m_distance = 0
        array1.append(array1[0])
        del array1[0]
    
    min_distance = min(distance_dict.keys())
    return (distance_dict[min_distance],min_distance)
