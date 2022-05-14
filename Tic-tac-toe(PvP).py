base = [[" ","|"," ","|"," "],[" ","|"," ","|"," "],[" ","|"," ","|"," "]]

hl = ["-","-","-","-","-"]
def outputG():
    for outputrow in range(3):
        for outputcol in range(5):
            print(base[outputrow][outputcol],end = " ")
        print("")
        if outputrow <= 1:
            print(*hl)

def matrixplace(pos):
    if pos == 1:
        row,col = 0,0
    elif pos == 2:
        row,col = 0,2
    elif pos == 3:
        row,col = 0,4
    elif pos == 4:
        row,col = 1,0
    elif pos == 5:
        row,col = 1,2
    elif pos == 6:
        row,col = 1,4
    elif pos == 7:
        row,col = 2,0
    elif pos == 8:
        row,col = 2,2
    elif pos == 9:
        row,col = 2,4
    return row,col

def rowcheck(player,asset):
    
    for row in range(0,3):
        rowwin = True
        for col in range(0,5,2):
            if base[row][col] != asset:
                rowwin = False
                continue
        if rowwin == True:
            return rowwin
    return rowwin
            
def colcheck(player,asset):
    
    for col in range(0,5,2):
        colwin = True
        for row in range(0,3):
            
            if base[row][col] != asset:
                colwin = False
                continue
        if colwin == True:
            return colwin
    
    return colwin

def diagcheck(asset):
    diawin = True
    for diag in range(3):
        if base[diag][diag + diag] != asset:
            diawin = False
            continue
    if diawin == True:
        return diawin
    diawin = True
    if diawin:
        diay = 4
        for diax in range(3):
            if base[diax][diay] != asset:
                diawin = False
            diay = diay - 2
    return diawin
        
    

spaceava = 9
print("Player1 -> x\nPlayer2 -> 0\n")
print("Note: Mention the row and col by num like 1 or 2 or 3\n")

player1 = True
player2 = False
while spaceava != 0:
    outputG()
    if player1 == True:
        pos = input("Player1: ")
        row,col = matrixplace(int(pos))
        if base[row][col] == " ":
            base[int(row)][int(col)] = "x"
            if rowcheck(1,"x") or colcheck(1, "x") or diagcheck("x"):
                print("\nPlayer1 win!!\n*Match End*\n")
                outputG()
                break
            player1 = False
            player2 = True
            spaceava = spaceava - 1
        elif base[int(row)][int(col)] != " ":
            print("You cant place there")
            
    elif player2 == True:
        
        pos = input("Player2: ")
        row,col = matrixplace(int(pos))
        if base[int(row)][int(col)] == " ":
            base[int(row)][int(col)] = "o"
            if rowcheck(1,"o") or colcheck(1, "o") or diagcheck("o"):
                print("\nPlayer2 win!!\n*Match End*\n")
                outputG()
                break
            player1 = True
            player2 = False
            spaceava = spaceava - 1
        else:
            print("You cant place there")
    if spaceava == 0:
        spaceava = 9
        outputG()
        print("\nMatch Tie!")
        break
    
