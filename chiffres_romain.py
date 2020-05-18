def conversion():
    nombre = int(input("entrer un nombre à convertir"))

    database = [[1000, 'M'], [900, 'CM'], [500, 'D'], [400, 'CD'], [ 100, 'C'], [ 90, 'XC'], [ 50, 'L'], [ 40, 'XL'], [  10, 'X'], [  9, 'IX'], [  5, 'V'], [  4, 'IV'], [   1, 'I']]

    resultat = ""
    cpt = 0

    while nombre > 0:
        while database[cpt][0] > nombre:
            cpt = cpt + 1
        resultat = resultat + database[cpt][1]
        nombre = nombre - database[cpt][0]

    print("le nombre demander donne ",resultat," en chifre romain")

conversion()