def get_multiples(n=5, divisor=2):
    multiples_lst = []
    for element in range(n):
        if element % divisor == 0:
            multiples_lst.append(element)
    return multiples_lst
