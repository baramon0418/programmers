#문제 설명
#첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다. 두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

#제한사항
#0 <numer1, denom1, numer2, denom2 < 1,000

import math
def solution(numer1, denom1, numer2, denom2):
    numer = denom1*numer2 + denom2*numer1   #분자
    denom = denom1 * denom2                 #분모
    gcd = math.gcd(denom, numer)            #최대공약수
    answer = [numer//gcd, denom//gcd]      
    return answer
