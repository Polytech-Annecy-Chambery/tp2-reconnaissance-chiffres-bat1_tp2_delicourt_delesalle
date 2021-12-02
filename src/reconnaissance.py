from image import Image

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    image_bin=image.binarisation(S)
    image_loc=image_bin.localisation()
    sim_max=0
    sim_tot=0
    for i in range (0,len(liste_modeles)):
        image4=image_loc.resize(liste_modeles[i].H,liste_modeles[i].W)
        sim=image4.similitude(liste_modeles[i])
        if sim>sim_max:
            sim_max=sim
            sim_tot=i
    return sim_tot

