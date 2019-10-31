# Thomas Marshall
# Lab 9

def num():
    numList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return numList

def board(numbers):
    print(str(numbers[0]) + " | "  + str(numbers[1]) + " | "  + str(numbers[2]))
    print("---------")
    print(str(numbers[3]) + " | "  + str(numbers[4]) + " | "  + str(numbers[5]))
    print("---------")
    print(str(numbers[6]) + " | "  + str(numbers[7]) + " | "  + str(numbers[8]))

def legal(board, spot):
    return spot <= 9 and spot >= 1 and board[spot - 1] != "O" and board[spot - 1] != "X"


def tester(board, space):
    while legal(board, space) == False:
        print("Illegal move.\n")
        space = eval(input("Please, enter a number between 1 and 9 that hasn't been used: "))
    return space

def victor(numbers, mark):
    if numbers[0] == mark and numbers[1] == mark and numbers[2] == mark:
        return True
    else:
        if numbers[3] == mark and numbers[4] == mark and numbers[5] == mark:
            return True
        else:
            if numbers[6] == mark and numbers[7] == mark and numbers[8] == mark:
                return True
            else:
                if numbers[0] == mark and numbers[4] == mark and numbers[8] == mark:
                    return True
                else:
                    if numbers[2] == mark and numbers[4] == mark and numbers[6] == mark:
                        return True
                    else:
                        if numbers[0] == mark and numbers[3] == mark and numbers[6] == mark:
                            return True
                        else:
                            if numbers[1] == mark and numbers[4] == mark and numbers[7] == mark:
                                return True
                            else:
                                if numbers[2] == mark and numbers[6] == mark and numbers[8] == mark:
                                    return True
                                else:
                                    return False
        
def game():
    numbers = num()
    winner = 0
    start = winner
    for i in range(9):
        player = (i % 2) + 1
        if start == 0:
            start += 1
            if player == 1:
                mark = "X"
            else:
                mark = "O"
        if victor(numbers, mark) == False:
            if player == 1:
                mark = "X"
            else:
                mark = "O"
            print("\nPlayer " + str(player) + "'s turn.\n")
            board(numbers)
            move = eval(input("\nEnter a number between 1 and 9 that hasn't "
                              "been used: "))
            test = tester(numbers, move)
            move = test
            if player == 1:
                numbers[test - 1] = "X"
            else:
                numbers[test - 1] = "O"
            print("")
        else:
            if winner == 0:
                player = ((i + 1) % 2) + 1
                board(numbers)
                print("\nPlayer " + str(player) + " wins!")
                winner += 1

    if victor(numbers, mark) == False:
        board(numbers)
        print("\nIt's a tie!")

def main():
    #print(num())
    numbers = num()
    #board(numbers)
    #test = tester(8)
    #print(test)
    #print(legal(numbers, 9))
    game()

main()
