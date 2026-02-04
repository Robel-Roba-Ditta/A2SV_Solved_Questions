if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    scores = list(set(arr))
    scores.sort()
    print(scores[-2])
