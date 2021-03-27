import re

#pattern des regex
startbot = [r"[Ff]ifa",r"[Bb]onjour", r"[Ss]alut",r"[Ss]tart",r"[Hh]ello",r"[Dd][ée]marrer"]
poids = [r"[Pp]oids", r"p[eè]se"]
taille = [r"[Tt]aille"]
pied = [r"pied[s]?\spr[eé]f[eé]r[eé][s]?", r"[Gg]aucher", r"[Dd]roitier"]
photo = [r"[Pp]hoto[s]?",r"[Ii]mage[s]?"]
note = [r"[Nn]ote[s]?", r"[Pp]erformance[s]?", r"[Nn]ote[s]?\sdu\s[Jj]oueur",r"[Pp]erformance[s]?\sdu\s[Jj]oueur",r"[Nn]ote[s]?\s[Gg]lobal[e]?",r"[Ss]tats",r"[Ss]tatistique[s]?"]
club = [r"[Cc]lub"]
age = [r"[Aa]ge",r"[Aa]ge\sdu\s[Jj]oueur[s]?"]
salaire = [r"[Ss]alaire",r"[Pp]ay[eé][r]?"]
stop = [r"[Bb]ye", r"[Aa]u\srevoir",r"[Ss]top(er)?",r"[Aa]rr[eê]t(er)?",r"[Ee]xit"]
joueurs = [r"Cristiano\sRonaldo", r"Neymar\sJr",r"L\.\sMessi",r"De\sGea",r"K\.\sDe\sBruyne",r"E\.\sHazard",r"L\.Modrić",r"L\.\sSuárez",r"Sergio\sRamos",r"J\.\sOblak",r"R\.\sLewandowski",r"T\.\sKroos",r"D\.\sGodín",r"N\.\sKanté",r"P\.\sDybala",r"H\.\sKane",r"A\.\sGriezmann",r"E\.\sCavani",r"M\.\sNeuer",r"K\.\sMbappé",r"M\.\sSalah",r"Casemiro",r"J\.\sRodríguez",r"Isco",r"P\.\sAubameyang",r"H\.\sLloris",r"G\.\sHiguaín",r"G\.\sBuffon",r"S\.\sUmtiti",r"R\.\sLukaku",r"Jordi\sAlba"]






