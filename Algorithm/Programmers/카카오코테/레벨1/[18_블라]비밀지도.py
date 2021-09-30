def solution(n, arr1, arr2):
    answer = []
    map1 = [[0] * n for _ in range(n)]
    map2 = [[0] * n for _ in range(n)]

    #이진수를 해석
    for i in range(n):
        arr1[i] = bin(arr1[i])
        arr1[i] = list(arr1[i][2:])
        arr2[i] = bin(arr2[i])
        arr2[i] = list(arr2[i][2:])
    

    
    for i in range(n):
        if len(arr1[i]) < n:
            for j in range(n - len(arr1[i])):
                arr1[i].insert(0, '0')
        if len(arr2[i]) < n:
            for j in range(n - len(arr2[i])):
                arr2[i].insert(0, '0')


    #arr1[i] = str 이진수 
    #지도 생성
    
    for i in range(n):
        for j in range(len(arr1[i])):
            if arr1[i][j] == '1':
                map1[i][j] = '#'
            else:
                map1[i][j] = ' '
    
    for i in range(n):
        for j in range(len(arr2[i])):
            if arr2[i][j] == '1':
                map1[i][j] = '#'
    
    shit = ''
    for i in range(n):
        for j in range(n):
            shit += str(map1[i][j])
        
        map1[i] = shit
        shit = ''
    
    
    answer = map1
    
    return answer