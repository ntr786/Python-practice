def main():
    print("There are 20 stones left.")

    left_stone = 20
    player_turn = 1 


    # nimmed_stones = int(input("Would you like to remove 1 or 2 stones? "))


    while left_stone > 0:
        nimmed_stones = int(input("Player " + str(player_turn) + " would you like to remove 1 or 2 stones? "))
        if nimmed_stones not in [1, 2]:
            nimmed_stones = int(input("Please enter 1 or 2: "))
            
        left_stone = left_stone - nimmed_stones
        print("")
        if left_stone > 0:
            print("There are " + str(left_stone) + " stones left.")
        else:
            print("")

                   
        player_turn = 2 if player_turn == 1 else 1  # Toggle between 1 and 2    
        
   
    
    print("Player " + str(player_turn) + " wins!")


    






if __name__ == '__main__':
    main()