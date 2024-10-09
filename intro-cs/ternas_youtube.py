def pytagoric_pairs_up_to(top: int):
    pytagoric_pairs = []

    for number in range(0,top):
        number_square = number * number

        for x in range(0, number):

            x_square = x*x

            for y in range(0, x):
                if x_square + y**2 ==number_square:

                    is_repeated = False

                    for pair in pytagoric_pairs:
                        if x % pair[0] == 0 and y % pair[1] == 0:
                            is_repeated = True
    
                    if not is_repeated:
                        pytagoric_pairs.append([x,y, number])
    

    return pytagoric_pairs

def main():
    cota = input("Ingrese la cota: ")
    pairs = pytagoric_pairs_up_to(int(cota))
    print("Las ternas que verifican i), ii), iii) son:")

    for pair in pairs:
        x,y,z = pair
        print(f'{x}^2 + {y}^2 = {z}^2')

if __name__ == "__main__":
    main()
