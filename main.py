"""File that contain the main function of the program"""
import random
import sys
import mysql.connector


CATEGORIES = [None, 'Vie', 'Gens', 'Travail', 'Amitié', 'Amour', 'Soi-même', \
              'Famille', 'Argent', 'Autre']

def random_quote():
    """Generate a random quote"""
    #Retreive all ids
    cursor.execute('select id from quotes')
    id_list = cursor.fetchall()
    #Get a random number between 1 and the number of quotes (it is represented
    #by the number of ids)
    randid = random.randint(1, len(id_list))
    #Select the quote with the random id
    cursor.execute('select * from quotes where id = %d' % randid)
    quote = cursor.fetchall()
    #Extract only quote and author
    quote = (quote[0][1], quote[0][2])
    print('\n"%s" - %s\n' % quote)
    after_quote_menu(quote)


def print_cats():
    """List CATEGORIES"""
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


def cat_quote(cat_choice):
    """Generate a quote from a selected category"""
    cat = CATEGORIES[int(cat_choice)]
    #Retreive all ids of quotes of the asked category
    cursor.execute("select id from quotes where cat = '%s'" % cat)
    id_list = cursor.fetchall()
    #Get a random number between 0 and the number of quotes of the wanted
    #category  (it is represented by the number of ids)
    randint = random.randint(0, len(id_list)-1)
    randid = id_list[randint][0]
    #Select the quote with the random id
    cursor.execute('select * from quotes where id = %d' % randid)
    quote = cursor.fetchall()
    #Extract only quote and author
    quote = (quote[0][1], quote[0][2])
    print('\n"%s" - %s\n' % quote)
    after_quote_menu(quote)


def invalid_choice():
    """Ask the user to make a valid choice"""
    print('\nVeuillez entrer un chiffre valide\n')


def cats_menu():
    """Call category menu and category quote functions"""
    print_cats()
    cat_choice = input('Choisissez la catégorie dont la citation qui vous '\
                        'sera proposée sera issue : ')
    #If the user selected a valid category
    try:
        if int(cat_choice) in range(1, 10):
            cat_quote(cat_choice)
    except:
        invalid_choice()
        cats_menu()
    #If choice is invalid, asked to make a valid choice and reprint menu
    else:
        invalid_choice()
        cats_menu()


def after_quote_menu(quote):
    """Ask what the user want after printing a quote"""
    print('Souhaitez-vous :')
    print('1 - Enregistrer cette citation et retourner au menu principal')
    print('2 - Retourner au menu principal directement')
    print('3 - Quitter le programme')
    choice = input('\nEntrez le chiffre correspondant à votre choix : ')
    #If the user choose 3, exit the program
    if choice == '3':
        sys.exit()
    if choice == '1':
        #Save the quote in the reg_quotes table
        cursor.execute('insert into reg_quotes (quote, author) values \
                        ("%s", "%s")' % quote)
        CONN.commit()
    if choice == '2':
        main_menu()
    else:
        invalid_choice()
        after_quote_menu(quote)


def reg_quotes():
    """Retreive and print saved quotes"""
    cursor.execute('select * from reg_quotes')
    quotes = cursor.fetchall()
    #Print every quotes contains in the reg_quotes table
    for quote in quotes:
        quote = (quote[1], quote[2])
        print('\n"%s" - %s\n' % quote)
    #New after_quote_menu because the original contains an option to save a
    #quote and it's not adapted for here
    print('\nSouhaitez-vous :')
    print('1 - Retourner au menu principal')
    print('2 - Quitter le programme')
    choice = input('\nEntrez le chiffre correspondant à votre choix : ')
    if choice == '2':
        sys.exit()
    if choice == '1':
        pass
    else:
        invalid_choice()
        reg_quotes()


def main_menu():
    """Main menu"""
    print('\nChoisissez ce que vous désirez :')
    print('1 - Consulter une citation aléatoire')
    print('2 - Voir les catégories proposées')
    print('3 - Consulter les citations enregisrées\n')
    choice = input('Entrez le chiffre correspondant à votre choix : ')
    #If the user choose to have a random quote
    if choice == '1':
        random_quote()
    #If the user want to see CATEGORIES
    if choice == '2':
        cats_menu()
    #If the user choice is invalid
    if choice == '3':
        reg_quotes()
    if choice not in ('1', '2'):
        invalid_choice()
    main_menu()


if __name__ == "__main__":
    #Connect to MySQL
    CONN = mysql.connector.connect(host="localhost", user="root",\
                                   database="quotes_db")
    cursor = CONN.cursor()
    #Welcome sentence
    print('\nBienvenue dans ce programme proposant des citations\n')
    #Menu
    main_menu()
