## PYTHON
---
### 1.자료형

* 1+1 =2 x
1+1 =11 문자열 주의

* 문자열 곱
a = "a"
a* 100 = a 100 번 출력

* 문자열 인덱싱
a = "012345678"
a[2] =2
a[-1] = 8

* 슬라이싱
a[이상:미만:간격]
a[0:4] = 0123<br>
a.count(1) 1이 몇번 들어갔는가?<br>
a.find(1) 1이 어디에 있는가?<br>
a.append 뒤에 추가<br>
a.sort 정렬 가나다 abc 순<br>
a.reverse 뒤집기<br>
a.pop<br>

---
### 2 튜플, 딕셔너리 , 집합

1. 튜플
* ex) t1 = (1, 2, 'a' , 'b')
* 값 변경 불가
* 인덱싱 슬라이싱 가능

2. 딕셔너리

* key value 구조
* ex) dic = {'name' : 'test' , 'age' = 1}
* dic.keys() / dic.values() / dic.items() = > 튜플로 뽑아서 사용가능
* dic[1] error / dic.get(1) 없음을 출력

3. 집합

* ex) s1 = set([1,2,3])
[1,2,3]  = > list
or
s1 = {1,2,3}

* 문자열을 set에 넣을시 문자열이 쪼개 진다 [중복은 없어짐]

* 교집합 차집합 기능 가능



1. 교집합

s1과 s2의 교집합을 구해 보자.

> s1 & s2
{4, 5, 6}
"&" 기호를 이용하면 교집합을 간단히 구할 수 있다.

또는 다음과 같이 intersection 함수를 사용해도 동일한 결과를 돌려준다.

>s1.intersection(s2)
{4, 5, 6}
s2.intersection(s1)을 사용해도 결과는 같다.

2. 합집합

합집합은 다음과 같이 구할 수 있다. 이때 4, 5, 6처럼 중복해서 포함된 값은 한 개씩만 표현된다.

> s1 | s2
{1, 2, 3, 4, 5, 6, 7, 8, 9}
"|" 기호를 사용한 방법이다.

> s1.union(s2)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
또는 union 함수를 사용하면 된다. 교집합에서 사용한 intersection 함수와 마찬가지로 s2.union(s1)을 사용해도 동일한 결과를 돌려준다.

3. 차집합

차집합은 다음과 같이 구할 수 있다.

> s1 - s2
{1, 2, 3}
> s2 - s1
{8, 9, 7}
빼기(-) 기호를 사용한 방법이다.

> s1.difference(s2)
{1, 2, 3}
> s2.difference(s1)
{8, 9, 7}
difference 함수를 사용해도 차집합을 구할 수 있다.

