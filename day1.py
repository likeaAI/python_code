"""
최대공약수와 최소공배수
문제 설명
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

제한 사항
두 수는 1이상 1000000이하의 자연수입니다.
입출력 예
n	m	return
3	12	[3, 12]
2	5	[1, 10]
입출력 예 설명
입출력 예 #1
위의 설명과 같습니다.

입출력 예 #2
자연수 2와 5의 최대공약수는 1, 최소공배수는 10이므로 [1, 10]을 리턴해야 합니다.
"""


import math

def solution(n, m):
     answer = []           
     
     # 최대공약수 라이브러리 이용 
     test01 = math.gcd(n,m)
     print(test01)
     answer.append(test01)`
     minnum = [] 
     for i in range(max(n, m), (n * m) + 1):
          if i % n == 0 and i % m == 0:
             minnum.append(i)
     minnum = min(minnum)
     answer.append(minnum)
            
            
     return answer 


문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

제한 사항
문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.
입출력 예
s	return
"try hello world"	"TrY HeLlO WoRlD"
입출력 예 설명
"try hello world"는 세 단어 "try", "hello", "world"로 구성되어 있습니다. 각 단어의 짝수번째 문자를 대문자로, 홀수번째 문자를 소문자로 바꾸면 "TrY", "HeLlO", "WoRlD"입니다. 따라서 "TrY HeLlO WoRlD" 를 리턴합니다.

import re 

def solution(s):
    # 문자열 s를 구분 후 for 문으로 한단어씩 읽은 후 조건문 
    # if 인덱스가 짝수이면 -> 나중에 다시 합친다. 
    
    result = [] 
    s = re.sub(' +', ' ', s)  # 다중공백을 변환
    words = s.split(" ")
    for oneword in words : 
        for speling in enumerate(oneword) :
            
            if speling[0] %2 == 0 :
                s = speling[1].upper()
                result.append(s)               
            else :                 
                s = speling[1].lower()
                result.append(s)
        result.append(" ")
            
        new_word = "".join(result)
    return new_word.strip()
    
    

                
