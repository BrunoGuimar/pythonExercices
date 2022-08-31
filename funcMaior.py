def bigger(*nums):
    maior = 0
    for value in nums:
        if value > maior:
            maior = value
    print(maior)
bigger(7, 4, 9)
bigger(1, 2, 3, 9, 7, 22, 65, 9, 74, 4)
bigger(-1)