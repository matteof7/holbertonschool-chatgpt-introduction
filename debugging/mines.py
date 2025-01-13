#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]
        self.flags = set()

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                elif (y * self.width + x) in self.flags:
                    print('F', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True
        if self.revealed[y][x]:
            return True
        if (y * self.width + x) in self.mines:
            return False
        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    self.reveal(x + dx, y + dy)
        return True

    def is_win(self):
        return all(self.revealed[y][x] or (y * self.width + x) in self.mines
                   for x in range(self.width) for y in range(self.height))

    def play(self):
        while True:
            self.print_board()
            action = input("Enter action (r for reveal, f for flag, q to quit) and coordinates (e.g., r 3 4): ").split()
            if len(action) == 1 and action[0].lower() == 'q':
                print("Thanks for playing!")
                break
            if len(action) != 3:
                print("Invalid input. Please enter action and two coordinates.")
                continue
            act, x, y = action
            try:
                x, y = int(x), int(y)
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordinates out of bounds. Try again.")
                    continue
                if act.lower() == 'r':
                    if not self.reveal(x, y):
                        self.print_board(reveal=True)
                        print("Game Over! You hit a mine.")
                        break
                    if self.is_win():
                        self.print_board(reveal=True)
                        print("Congratulations! You won!")
                        break
                elif act.lower() == 'f':
                    pos = y * self.width + x
                    if pos in self.flags:
                        self.flags.remove(pos)
                    else:
                        self.flags.add(pos)
                else:
                    print("Invalid action. Use 'r' for reveal or 'f' for flag.")
            except ValueError:
                print("Invalid input. Please enter numbers for coordinates.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
