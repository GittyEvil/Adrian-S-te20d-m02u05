# Skriv en kommentar för varje fel du identifierar och löser.
# Beskriv vad som var fel och hur du har löst det.

#du kan inte ha dubbla ord i variabel, inga understräck eller mellanrum.

dollartosek = 8,82
#glömt ""
print("Detta är ett program där vi kan växla mellan SEK & dollar")
#glömt sista "" och du måste antingen ha semikolon i variabel namn eller inga intergears.
sek = input("Hur många SEK vill du växla till dollar:")
#glömt definiera exchange_rate_dollar_to_sek och samma som innan. antingen semikolon eller inga intergears.
dollar = sek / dollartosek
#Här så har du satt in .format mitt i vilket funkar men du har glömt en andra slutparantes.
print("Du ville växla {0} SEK vilket blir {1} dollar.".format(sek, dollar))