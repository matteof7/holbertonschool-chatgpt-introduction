def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Vérification des lignes et colonnes
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " " or \
           board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] != " " or \
       board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    return False

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_valid_input(prompt, valid_range):
    while True:
        try:
            value = int(input(prompt))
            if value in valid_range:
                return value
            else:
                print(f"Entrée invalide. Veuillez choisir parmi {valid_range}")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    
    while True:
        print_board(board)
        print(f"Tour du joueur {player}")
        
        row = get_valid_input("Entrez la ligne (0, 1, ou 2) : ", range(3))
        col = get_valid_input("Entrez la colonne (0, 1, ou 2) : ", range(3))
        
        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print(f"Le joueur {player} gagne !")
                break
            elif is_board_full(board):
                print_board(board)
                print("Match nul !")
                break
            player = "O" if player == "X" else "X"
        else:
            print("Cette case est déjà occupée ! Réessayez.")

if __name__ == "__main__":
    tic_tac_toe()
