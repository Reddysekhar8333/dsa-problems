def linear_search(n:int,lists:list[int])->int:
    for i in range(len(lists)):
        if lists[i]==n:
            return f"{n} is found at {i+1}th location in the list !"
    return f"{n} is not found in the list !"

lis=[1,88,45,98,23,13,99,76,33,65,18,27,36,63,72,81]

print(linear_search(81,lis))
