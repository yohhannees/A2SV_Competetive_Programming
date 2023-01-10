def max_dominoes(M: int, N: int) -> int:
    squares = M * N
    if (M*N) % 2 == 0:
        return squares // 2
    else:
        return (squares // 2) + (min(M, N) % 2)


if __name__ == '__main__':
    m, n = map(int, input("Enter the size of the board (M N): ").split())
    result = max_dominoes(m, n)
    print("Maximum number of dominoes that can be placed:", result)
