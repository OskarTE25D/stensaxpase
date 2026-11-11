#----------------------------------------------------------------------------------------------------------------
def spela(score,):
    import random
    weakness_dict = {"sten":"påse", "påse":"sax", "sax":"sten" } #returnarar det 'vapen' som slår 'input-vapnet'
    bot_vapen = random.choice(["sten","sax","påse"])
    användare_vapen = input("ange ditt val av 'sten', 'sax', eller 'påse' ==> ")
    print(f"användare val: {användare_vapen}, bot val: {bot_vapen}")
    if användare_vapen == bot_vapen:
        print("lika")
    elif weakness_dict[användare_vapen] == bot_vapen:
        print("bot vann")
        score[1] += 1   #ändra score så bot ökar med ett
    else:
        print("användare vann")
        score[0] += 1   #ändra score så användare ökar med ett
    return score
#---------------------------------------------------------------------------------------------------------------
'''
exempel på användning:
score = [0,0]         # format för poängvariabeln,[user_score, bot_score]
score = spela(score)  #<--skiten ni ska skriva för att använda funktionen, variabelnamn kan ändras
'''
