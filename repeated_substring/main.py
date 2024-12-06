def repeat_substring(s):
    k = 2
    
    while k <= len(s) // 2:
        part_length = len(s) // k
        parts = []
        
        for i in range(0,len(s),part_length):
            parts.append(s[i:i+part_length])
            
        if all(i == parts[0] for i in parts):
            return parts[0]
            
        k += 1
        
    return ""

print(repeat_substring("ababab")) #should return "ab"
print(repeat_substring("PythonPythonPython")) #should return "Python"