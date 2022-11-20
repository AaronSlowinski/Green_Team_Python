if __name__ == '__main__':
    score_list = []
    total_list = []
    name_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        score_list.append(score)
        total_list.append([name, score])
        
    lowest = list(set(score_list))
    lowest.sort()
    #print(lowest[1])
    
    for name,score in total_list:
            if score == lowest[1]:
                name_list.append(name)
    name_list.sort()
    for item in name_list:
        print(item)
    
    
    
    
    
    #print (name_list)
    
    # print(score_list)
    # print(total_list)
 