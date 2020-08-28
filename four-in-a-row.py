import pygame

pygame.init()
window = pygame.display.set_mode((720,620))
pygame.display.set_caption('Connect4')

BLACK, BLUE, RED, YELLOW = (0, 0, 0), (20, 50, 200), (200, 0, 0), (200, 200, 50)

def make_piece(colour):
    image = pygame.Surface((80, 80))
    image.fill(BLUE)
    pygame.draw.circle(image, colour, (40, 40), 40)
    return image

def new_game():
    turn = 1
    game_pieces = [
        [0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0,],    
        [0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0,],
        [0, 0, 0, 0, 0, 0,],
        ]
    return game_pieces, turn

def insert_piece(column, turn):
    for a in range(5, -1, -1):
        if game_pieces[column][a] == 0:
            game_pieces[column][a] = turn
            check_for_win(column, a, turn)
            turn = 3 - turn
            return turn

def check_direction(column, row, dx, dy, turn):
    add_length = 0
    x, y  = column + dx, row + dy
    while 0 <= x <= 6 and 0 <= y <= 5:
        if game_pieces[x][y] == turn:
            add_length += 1
            x += dx
            y += dy
        else:
            break
    return add_length

def check_for_win(column, row, turn):
    for dir in [[1, 0], [0, 1], [1, 1], [1, -1]]:
        length = 1
        length += check_direction(column, row, dir[0], dir[1], turn)
        length += check_direction(column, row, -dir[0], -dir[1], turn)
        if length >3:
            print('Player', turn, 'is the winner!')
            return

coloured_circles = make_piece(BLACK), make_piece(RED), make_piece(YELLOW)
game_pieces, turn = new_game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if 49 <= event.key <= 55:
                turn = insert_piece(event.key - 49, turn)
            if event.key == pygame.K_SPACE:
                game_pieces, turn = new_game()

    window.fill(BLUE)
    for a in range(0, 7):
        for b in range(0, 6):
            team = game_pieces[a][b]
            window.blit(coloured_circles[team], (20+100*a, 20+100*b))
    pygame.display.update()
