def pytagoric_pairs_up_to(top: int):
    pairs = []

    for number in range(0,top):

        for x in range(0,number):
            for y in range(0, number):
                if  x>y and x**2 + y**2 == number**2:
                    
                    is_repeated = False

                    for pair in pairs:
                        if x % pair[0] == 0 and y % pair[1] == 0:
                            is_repeated = True
                            

                    if not is_repeated:
                        pairs.append([x,y, number])

    return pairs


pairs_found= pytagoric_pairs_up_to(254)

print(pairs_found)
