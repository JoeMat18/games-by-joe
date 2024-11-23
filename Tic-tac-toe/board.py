from constants import *

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(3)] for _ in range(3)]
        self.cell_size = WIDTH // 3

        # Uploading images for X and O
        self.image_x = pygame.image.load("assets/images/cross.png")
        self.image_o = pygame.image.load("assets/images/circle.png")

    def reset(self):
        self.grid = [[None for _ in range(3)] for _ in range(3)]

    def draw(self, screen):
        # Drawing meshes
        for k in range(1, 3):
            pygame.draw.line(screen, GREY, (0, k * self.cell_size), (WIDTH, k * self.cell_size), 2)
            pygame.draw.line(screen, GREY, (0, k * self.cell_size, 0), (k * self.cell_size, HEIGHT), 2)

        # Drawing symbols
        for row in range(3):
            for col in range(3):
                symbol = self.grid[row][col]
                if symbol == "X":
                    screen.blit(self.image_x, (col * self.cell_size, row * self.cell_size))
                elif symbol == "O":
                    screen.blit(self.image_o, (col * self.cell_size, row * self.cell_size))

    def get_cell(self, x, y):
        col = x // self.cell_size
        row = y // self.cell_size

        if 0 <= row < 3 and 0 <= col < 3:
            return row, col
        return None, None

    def make_move(self, row, col, symbol):
        if self.grid[row][col] is None:
            self.grid[row][col] = symbol
            return True
        return False

    def check_winner(self):
        for row in self.grid:
            if row[0] == row[1] == row[2] and row[0] is not None:
                return row[0]

        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] and self.grid[0][col] is not None:
                return self.grid[0]
            # Checking diagonals
            if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] is not None:
                return self.grid[0][0]
            if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] is not None:
                return self.grid[0][2]
            return None


