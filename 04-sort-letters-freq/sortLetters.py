def sort_letters_by_frequency(s):
    # Create a frequency dictionary
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
            
    # Sort the characters by frequency (highest first) and then alphabetically
    sorted_chars = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    
    # Build the result string
    result = ''
    for char, count in sorted_chars:
        result += char * count
        
    return result