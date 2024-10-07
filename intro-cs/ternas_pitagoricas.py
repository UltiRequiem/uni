def pytagoric_pairs_up_to(number: int):
    pairs = []

    # carajo mierda, los pares los estoy generando de mayor a menor

    while number > 0:
        for x in range(0,number):
            for y in range(0, number):
                if  x>y and x**2 + y**2 == number**2:
                    
                    is_repeated = False

                    for pair in pairs:
                        print(pair)
                        if x % pair[0] == 0 and y % pair[1] == 0:
                            print(x & pair[0])
                            is_repeated = True
                            

                    if not is_repeated:
                        pairs.append([x,y, number])

        number-=1

    return pairs


pairs_found= pytagoric_pairs_up_to(10)

print(pairs_found)
