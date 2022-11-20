def count_substring(string, sub_string):
    # Find a string in Python - Hacker Rank Solution START
    count = 0
    for i in range(len(string)-len(sub_string)+1):
        if (string[i:i+len(sub_string)] == sub_string):
            count += 1
    
    # Find a string in Python - HackerRank Solution END
    return count
