filed = list(range(1,10))

def game_field(field):
    print("_____________")
    for d in range(3):
        print (field[0+d*3], field[1+d*3], field[2+d*3])
        print("_____________")

def t_input(player):
    valid = False
    while not valid:
        p_answer = input("Куда ставим" + player+ "?")
        try:
            answer = int(p_answer)
        except:
            print("Невернный ввод. Вы ввели число?")
            continue
        if p_answer >= 1 and p_answer <= 9:
            if (str (field[p_answer-1]) not in "XO"):
                field[p_answer-1] = player
                valid = True
            else:
                print ("Клетка занята")
        else:
            print("Введите чилос от 1 до 9 для хода.")

def win(field):
    win_combinations = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_combinations:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
        return False

def main(field):
    coun = 0
    win = False
    while not win:
        draw_field(field)
        if coun % 2 == 0:
            t_input("X")
        else:
            t_input("O")
        coun += 1
        if coun > 4:
            w = check_win(field)
            if w:
                print(w, "Победа!")
                win = True
                break
        if coun == 9:
            print("Ничья")
            break
    draw_field(field)

main(field)
