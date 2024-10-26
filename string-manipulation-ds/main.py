def solution(s):
    freq_dict = {}
    output_dict = {}
    
    for c in s:
        if c in freq_dict:
            freq_dict[c] += 1
        else:
            freq_dict[c] = 1
    
    for char, freq in freq_dict.items():
        replace = chr(((ord(char) - 100) % 26) + 97)
        output_dict[char] = ord(replace) * freq
        
    return(output_dict)