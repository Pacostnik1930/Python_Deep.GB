import datetime

def is_date_valid(date_string):
    try:
        date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2:
        date_string = sys.argv[1]
        if is_date_valid(date_string):
            print(f"{date_string} is a valid date.")
        else:
            print(f"{date_string} is not a valid date.")
    else:
        print("Please provide a date in the format YYYY-MM-DD as a command line argument.")



def is_attacking(x1, y1, x2, y2):
    # Проверяем, находятся ли ферзи на одной вертикали или горизонтали
    if x1 == x2 or y1 == y2:
        return True
    # Проверяем, находятся ли ферзи на одной диагонали
    if abs(x1 - x2) == abs(y1 - y2):
        return True
    # Если ни одно из условий не выполнено, то ферзи не бьют друг друга
    return False

def check_queens(queens):
    for i in range(len(queens)):
        for j in range(i+1, len(queens)):
            if is_attacking(queens[i][0], queens[i][1], queens[j][0], queens[j][1]):
                return False
    return True

if __name__ == '__main__':
    import sys

    if len(sys.argv) == 9:
        queens = [(int(sys.argv[i]), int(sys.argv[i+1])) for i in range(1, 9, 2)]
        if check_queens(queens):
            print("Queens are not attacking each other.")
        else:
            print("Queens are attacking each other.")
    else:
        print("Please provide 8 pairs of integers between 1 and 8 as command line arguments.")



import random

def is_attacking(x1, y1, x2, y2):
    # Проверяем, находятся ли ферзи на одной вертикали или горизонтали
    if x1 == x2 or y1 == y2:
        return True
    # Проверяем, находятся ли ферзи на одной диагонали
    if abs(x1 - x2) == abs(y1 - y2):
        return True
    # Если ни одно из условий не выполнено, то ферзи не бьют друг друга
    return False

def check_queens(queens):
    for i in range(len(queens)):
        for j in range(i+1, len(queens)):
            if is_attacking(queens[i][0], queens[i][1], queens[j][0], queens[j][1]):
                return False
    return True

def generate_random_board():
    queens = []
    for i in range(8):
        queens.append((i+1, random.randint(1, 8)))
    return queens

if __name__ == '__main__':
    successful_boards = 0
    while successful_boards < 4:
        queens = generate_random_board()
        if check_queens(queens):
            print("Successful board:", queens)
            successful_boards += 1