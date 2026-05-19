def solution(numbers):
    result = []
    stack = []

    # 뒤에서부터 순회하며 뒷 큰수 찾기
    for i in range(len(numbers) - 1, -1, -1):
        # 스택이 비어있지 않고 현재 숫자보다 작은 수를 만날 때까지 pop
        while stack and stack[-1] <= numbers[i]:
            stack.pop()

        # 뒷 큰수가 없으면 -1을 결과에 추가, 있으면 해당 값을 추가
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])

        # 현재 숫자를 스택에 추가
        stack.append(numbers[i])

    # 결과를 뒤집어서 반환
    return result[::-1]