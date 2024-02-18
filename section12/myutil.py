def get_total(*score:int) -> int:
    total = 0
    for val in score:
        total += val
        
    return total

def get_average(total:int, count:int) -> float:
     return total / count