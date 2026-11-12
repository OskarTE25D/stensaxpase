#----------------------------------------------------------------------------------------------------------------
def spela(score,):
    import random
    weakness_dict = {"sten":"påse", "påse":"sax", "sax":"sten" } #returnarar det 'vapen' som slår 'input-vapnet'
    bot_vapen = random.choice(["sten","sax","påse"])
    #felsäkerhet---------------------------------------------------------------------------
    while True:
        användare_vapen = "".join(input("Ange ditt val av 'sten', 'påse', eller 'sax' --> ").lower().split())
        if not användare_vapen.isalpha() or användare_vapen.lower() not in ["sten", "sax", "påse"]:
            print("Ogiltigt val!")
            continue
        else:
            break
    #--------------------------------------------------------------------------------------
        
    print(f"Användarens val: {användare_vapen}, Bottens val: {bot_vapen}")
    if användare_vapen == bot_vapen:
        print("Lika")
    elif weakness_dict[användare_vapen] == bot_vapen:
        print("Botten vann!")
        score[1] += 1   #ändra score så bot ökar med ett
    else:
        print("Användaren vann!")
        score[0] += 1   #ändra score så användare ökar med ett
    return score
#---------------------------------------------------------------------------------------------------------------
'''
exempel på användning:
score = [0,0]         # format för poängvariabeln,[user_score, bot_score]
score = spela(score)  #<--skiten ni ska skriva för att använda funktionen, variabelnamn kan ändras
'''
