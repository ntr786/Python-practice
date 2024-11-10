"""Nimm is an ancient game of strategy that is named after the old German word for "take." It is also called Tiouk Tiouk in West Africa and Tsynshidzi in China. Players alternate taking stones until there are zero left. The game of Nimm goes as follows:

The game starts with a pile of 20 stones between the players

The two players alternate turns

On a given turn, a player may take either 1 or 2 stone from the center pile

The two players continue until the center pile has run out of stones.

The last player to take a stone loses.

Write a program to play Nimm.""" 

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
