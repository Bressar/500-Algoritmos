# Algoritmo 61

siglas_estados = {
"AC" : "Acreano",
"AL" : "Alagoano",
"AP" : "Amapaense",
"AM" : "Amazonense",
"BA" : "Baiano",
"CE" : "Cearense",
"DF" : "Brasiliense",
"ES" : "Capixaba",
"GO" : "Goiano",
"MA" : "Maranhense",
"MT" : "Mato-grossense",
"MS" : "Sul-mato-grossense",
"MG" : "Mineiro",
"PA" : "Paraense",
"PB" : "Paraibano",
"PR" : "Paranaense",
"PE" : "Pernambucano",
"PI" : "Piauiense",
"RJ" : "Carioca",
"RN" : "Potiguar",
"RS" : "Gaúcho",
"RO" : "Rondoniense",
"RR" : "Roraimense",
"SC" : "Catarinense",
"SP" : "Paulista",
"SE" : "Sergipano",
"TO" : "Tocantinense"
}

sigla = input("Digite a sigla do Estado que você quer saber o gentílico\n(nome dos indivíduos que nascem nesses estados): ").strip().upper()

for key in siglas_estados:
    if key == sigla:
        print(siglas_estados[key])