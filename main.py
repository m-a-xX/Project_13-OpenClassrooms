"""File that contain the main function of the program"""
import mysql.connector
import random

categories = [None, 'Vie', 'Gens', 'Travail', 'Amitié', 'Amour', 'Soi-même', 'Famille', 'Argent', 'Autre']

def menu():
    #Connect to MySQL
    conn = mysql.connector.connect(host="localhost",user="root",database="quotes_db")
    cursor = conn.cursor()
    #Main menu
    print('\nChoisissez ce que vous désirez :')
    print('1 - Consulter une citation aléatoire')
    print('2 - Voir les catégories proposées\n')
    choice = input('Entrez le chiffre correspondant à votre choix : ')
    #If the user choose to have a random quote
    if choice == '1':
        #Retreive all ids
        cursor.execute('select id from quotes')
        id_list = cursor.fetchall()
        #Get a random number between 1 and the number of quotes (it is represented by the number of ids)
        randid = random.randint(1, len(id_list))
        #Select the quote with the random id
        cursor.execute('select * from quotes where id = %d' % randid)
        quote = cursor.fetchall()
        #Extract only quote and author
        quote = (quote[0][1], quote[0][2])
        print('\n"%s" - %s\n' % quote)
    #If the user want to see categories
    if choice == '2':
        #List categories
        print('\nVoici les catégotries proposées :')
        print('1 - Vie')
        print('2 - Gens')
        print('3 - Travail')
        print('4 - Amitié')
        print('5 - Amour')
        print('6 - Soi-même')
        print('7 - Famille')
        print('8 - Argent')
        print('9 - Autre\n')
        cat_choice = input('Choisissez la catégorie dont la citation qui vous sera proposée sera issue : ')
        #If the user selected a valid category
        if cat_choice == '1' or cat_choice == '2' or cat_choice == '3' or cat_choice == '4' or cat_choice == '5' or cat_choice == '6' or cat_choice == '7' or cat_choice == '8' or cat_choice == '9':
            cat = categories[int(cat_choice)]
            #Retreive all ids of quotes of the asked category
            cursor.execute("select id from quotes where cat = '%s'" % cat)
            id_list = cursor.fetchall()
            #Get a random number between 0 and the number of quotes of the wanted category  (it is represented by the number of ids)
            randint = random.randint(0, len(id_list)-1)
            randid = id_list[randint][0]
            #Select the quote with the random id
            cursor.execute('select * from quotes where id = %d' % randid)
            quote = cursor.fetchall()
            #Extract only quote and author
            quote = (quote[0][1], quote[0][2])
            print('\n"%s" - %s\n' % quote)
    if choice != '1' and choice != '2':
        print('\nVeuillez entrez le chiffre 1 ou le chiffre 2 en fonction de votre choix')
    menu()

if __name__ == "__main__":
    print('\nBienvenue dans ce programme proposant des citations\n')
    menu()
