mot_mystère = 'arifot'
nb_de_vies = 7

mot_public = '_' * len(mot_mystère)

while nb_de_vies > 0 and mot_mystère != mot_public :
    lettre = input('entrez une lettre : ')

    if lettre in mot_mystère:
        for i in range(len(mot_mystère)):
            if mot_mystère[i] == lettre:
                mot_public = mot_public[:i] + lettre + mot_public[i + 1:]
    else:
        nb_de_vies -= 1

    if mot_public == mot_mystère :
        print ('vous avez réussi!')
    elif nb_de_vies == 0:
        print('vous avez perdu')
    else:
        print ('vous avez', nb_de_vies)
        print ('le mot est', mot_public)
