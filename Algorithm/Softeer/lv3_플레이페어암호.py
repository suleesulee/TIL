import sys
input = sys.stdin.readline

def make_playpair(plain_text):
    #J는 없다.
    alpha = [0] * 26
    plain_text_len = len(plain_text)
    cnt = 0
    front = 0

    for i in range(plain_text_len): 
        if alpha[ord(plain_text[i]) - ord('A')] == 0:
            playfair[front].append(plain_text[i])
            alpha[ord(plain_text[i]) - ord('A')] = 1
            if plain_text[i] == 'I':
                alpha[ord('J') - ord('A')] = 1
            cnt += 1
            
            if cnt % 5 == 0:
                front += 1
                cnt = 0

    for i in range(len(alpha)):
        if alpha[i] == 0:
            playfair[front].append(chr(i + ord('A')))
            if alpha[ord('I') - ord('A')] == 0:
                alpha[ord('J') - ord('A')] = 1
            cnt += 1
            if cnt % 5 == 0:
                front += 1
                cnt = 0

    #print(playfair)

def divide_plain_text(plain_text):    

    plain_text_list = list(plain_text)
    
    while 1:
        flag = 0

        for i in range(1, len(plain_text_list), 2):
            if plain_text_list[i-1] == plain_text_list[i]:
                if plain_text_list[i-1] == 'X':
                    plain_text_list.insert(i, 'Q')
                    flag = 1
                    break
                else:    
                    plain_text_list.insert(i, 'X')
                    flag = 1
                    break        
        
        if flag == 0:
            break
    
    if len(plain_text_list) % 2 == 1:
        plain_text_list.append('X')


    return ''.join(plain_text_list)


def encrypt(text):
    #3가지 조건
    text_len = len(text)
    encrypt_text = ""
    for i in range(0, text_len, 2):
        fc, fr, sc, sr = -1, -1, -1, -1
        for j in range(5):
            for k in range(5):
                if playfair[j][k] == text[i]:
                    fc, fr = j, k
                    
                if playfair[j][k] == text[i + 1]:
                    sc, sr = j, k
                    

            if fc != -1 and sc != -1:
                break

        #1번 같은행
        if fc == sc:
            if fr+1 > 4:
                fr = 0
            else:
                fr += 1
            encrypt_text += playfair[fc][fr]

            if sr+1 > 4:
                sr = 0
            else:
                sr += 1
            encrypt_text += playfair[sc][sr]

            
        #2번 같은열
        elif fr == sr:
            if fc+1 > 4:
                fc = 0
            else:
                fc += 1
            encrypt_text += playfair[fc][fr]

            if sc+1 > 4:
                sc = 0
            else:
                sc += 1
            encrypt_text += playfair[sc][sr]

        #3번 둘다 아닐때
        else:
            encrypt_text += playfair[fc][sr]
            encrypt_text += playfair[sc][fr]


    return encrypt_text

if __name__ == "__main__":
    plain_text = str(input().rstrip())
    key = str(input().rstrip())
    playfair = [[] for _ in range(5)]

    make_playpair(key)
    new_plain_text = divide_plain_text(plain_text)
    answer = encrypt(new_plain_text)
    print(answer)

