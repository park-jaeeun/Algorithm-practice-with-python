# 그리디 문제1 ( 1이 될 때까지 )

n, k = map(int, input().split())

result = 0

while True:
  # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
  target = (n//k) * k #N에 가장 가까운 K로 나누어떨어지는 수
  result += (n -target) # 1을 빼는 횟수
  n = target
  #N이 K보다 작을 때 반복문 탈출
  if n < k :
    break

  #K로 나누기
  result += 1
  n //= k

result += (n-1)
print(result)
