from spelafunktion import spela

# skapar nödvändiga variabler som score, score ska vara en lista
score=[0,0]         # score är variabeln som innehåller både användarens och datorns poäng, index 0 (vänstra) är spelaren, index 1 (högra) är datorn
# användarens poäng ges av "score[0]", datorns ges av "score[1]"


loser = "Botten"

winner_points = 0   # poäng för att avgöra vem som vann
loser_points = 0    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

print(f"Välkommen till sten, sax och påse!\n{"="*35}")




# användaren ska mata in ett användarnamn

namn = input("Ange spelarnamn --> ")
print(f"Hej, {namn}!")
winner = namn


# while-True loop som breakas om man inte vill köra längre, och därmed avslutar spelet.

while True:     # loop som innehåller spelet
    #--------------inmatningssäkerhet för antal_rundor:
    while True:     
        try:
            antal_rundor=int(input("Ange antal rundor som ska köras --> ")) # frågar hur många rundom som ska köras, och sparar det som en int i variabeln antal_rundor
            break
        except ValueError:
            continue        
    #-------------slut på inmatningssäkerhet
    for runda in range(antal_rundor):
        print(f"Omgång {runda+1}:") # "+1" eftersom runda börjar på noll
        score=spela(score)


    # resultat och fråga spelaren om de vill köra igen (ja/nej, j/n)
    if score[0] < score[1]:
        score = score[::-1]   #botten vinner
        winner="bot"
        loser=namn
    print(f'''{'='*10} RESULTAT {'='*10}
{winner:>6} : {score[0]} poäng
{loser:>6} : {score[1]} poäng
    
Vinnaren är {winner}!
''')
    
    # frågar om spelaren vill spela igen (j/n) och har felinmatningssäkerhet
    while True:
        rematch_svar=input("Kör igen? (j/n) -->")
        if rematch_svar in ("j", "n"):
            break
        else:
            print("Ogiltig inmatning")  # allting som inte är "j" eller "n" är ogiltigt

    if rematch_svar == "n":
        print("Tråkmåns")
        break