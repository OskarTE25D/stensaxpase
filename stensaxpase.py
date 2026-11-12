from spelafunktion import spela

#1 skapa nödvändiga variabler som score, score ska vara en lista
score=[0,0]         #score är variabeln som innehåller både användarens och datorns poäng, index 0 (vänstra) är spelaren, index 1 (högra) är datorn
#användarens poäng ges av "score[0]", datorns ges av "score[1]"

winner = "Botten"   #ändrar denna till användaren ifall det behövs
loser = "Botten"    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

winner_points = 0   #poäng för att avgöra vem som vann
loser_points = 0    #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

print(f"Välkommen till sten, sax och påse!\n{"="*35}")


#2 nedan fortsätts 'main menu', vi ska ha en input som frågar spelaren om hen vill spela (ja/nej, j/n)


#3 användaren ska mata in ett användarnamn och köra mot en bot som heter the final chud
namn = input("Ange spelarnamn --> ")
print(f"Hej, {namn}!")


#4 fråga spelaren hur många omgångar hen vill köra. 
#här bör en while-True loop skapas som breakas om man inte vill köra längre, och därmed avslutar spelet.

while True:     #loop som innehåller spelet
    #--------------inmatningssäkerhet för antal_rundor:
    while True:     
        try:
            antal_rundor=int(input("Ange antal rundor som ska köras --> "))
            break
        except ValueError:
            continue        
    #-------------slut på inmatningssäkerhet
    for runda in range(antal_rundor):
        print(f"Omgång {runda+1}:") #"+1" eftersom runda börjar på noll
        #OBS!! formatera senare
        score=spela(score)


    #6 resultat och fråga spelaren om de vill köra igen (ja/nej, j/n)
    if score[0] > score[1]:
        winner_points = score[0]   #användaren vinner
        loser_points = score[1]
        winner = namn
    elif score[0] < score[1]:
        winner_points = score[1]   #botten vinner
        loser_points = score[0]
        loser = namn
    else:
        score[0] = winner_points    #bara för att ha användarens poäng först
    print(f'''{'='*10} RESULTAT {'='*10}
{winner:>6} : {winner_points} poäng
{loser:>6} : {loser_points} poäng
    
Vinnaren är {winner}!
''')
    rematch_svar=input("Kör igen? (j/n) -->")
    if rematch_svar == "n":
        print("Hejdå!")
        break
    elif rematch_svar == "j":
        continue

#7 om svar nej säg hejdå(breaka loopen) och delete C:system32

