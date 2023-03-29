"""

분할 알고리즘

호어/ 로무트

호어가 조금 더 좋다 (swap이 더 적게 일어남)


"""
# 분할 함수 partition

def partition(A, l, r):
    # 피봇 정하기( 비교대상) 가장 왼쪽 원소로
    p = A[l]    # pivot의 값

    # 피봇보다 작은 거는 맨 왼쪽부터 채우고, 큰 것은 맨 오른쪽부터 채운다.
    i, j = l, r

    # i 왼쪽에 있으면 안되는 친구의 위치 (피봇보다 큰값
    # j 오른쪽에 있으면 안되는 친구의 위치 (피봇보다 작은값
    # 만약 둘다 있으면 교환
    while i <= j:   # 왼쪽에 있으면 안되는 친구가 있고 오른쪽에 있으면 안되는 친구가있다는 의미
                    # 서로 교차한다면(제대로 피봇보다 작은 부분과 큰 부분으로나눴다면) while문 종료

        # 피봇보다 큰 것을 왼쪽부터 찾기 시작
        # i는 피봇보다 큰 값이 있으면 멈출 것임

        while i <= j and A[i] <= p: # 교차하지 않았고 피봇보다 작으면
            # 현재 i 위치에 있는게 피봇보다 작으면 큰 거를 찾아서 오른쪽으로 한칸 이동
            i += 1

        # 피봇보다 작은 것을 오른쪽부터 찾기 시작
        # j는 피봇보다 작은 값이 있으면 멈출 것임
        while i <= j and A[j] >= p:
            # 현재 j위치에 있는게 피봇보다 크면 작은 것을 찾아 왼쪽으로 한칸 이동
            j -= 1

        # 큰 것이 왼쪽에 있으면 안되고 작은 것이 오른쪽에 있으면 안되기 때문에 서로 자리를 교환해준다.
        if i < j: #i가 j보다 작으면 위치가 잘못되어있다는 것임
            A[i], A[j] = A[j], A[i]

    # while 반복이 끝나면 작은 것과 큰 것들이 큰 틀에서 다 제자리에 있기 때문에
    # 피봇 위치를 정해준다.
    # 피봇 위치를 어떻게 정해줄까?
    # 교차하는 곳
    # 왜 교차하는 곳이냐?
    # 교차했따는 의미는 다들 올바른 위치에 존재한다는 것
    # A[l] 이 피봇 A[j]가 교차한 곳 둘의 위치를 바꿔준다.
    A[l], A[j] = A[j], A[l]

    # 피봇의 위치 리턴
    # 왜 i가 아니라 j임?
    return j  # 이 피봇의 위치는 quickSort에서 s 값이 됨

def quickSort(A, l, r):
    if l < r:
        # 분할하고 피봇의 위치를 구한다.
        s = partition(A, l, r)  # s = pivot
        # 피봇위치를 정했으니 피봇 제외 왼쪽 정렬
        quickSort(A, l, s-1)

        # 이후 오른쪽 정렬
        quickSort(A, s+1, r)


A = [7, 2, 5, 3, 1, 4, 1]
N = len(A)
quickSort(A, 0, N-1)
print(A)