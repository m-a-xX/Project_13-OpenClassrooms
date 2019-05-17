"""File that contain the main function of the program"""
import mysql.connector
import random


if __name__ == "__main__":
    #Connect to MySQL
    conn = mysql.connector.connect(host="localhost",user="root",database="quotes_db")
    cursor = conn.cursor()
    #Menu
    print('\nBienvenue dans ce programme proposant des citations\n')
    print('Choisissez ce que vous désirez :')
    print('1 - Consulter une citation aléatoire')
    print('2 - Voir les catégories proposées\n')
    choice = int(input('Entrez le chiffre correspondant à votre choix : '))
    if choice == 1:
        cursor.execute('select id from quotes')
        id_list = cursor.fetchall()
        randid = random.randint(1, len(id_list))
        cursor.execute('select * from quotes where id = %d' % randid)
        quote = cursor.fetchall()
        quote = (quote[0][1], quote[0][2])
        print('\n"%s" - %s\n' % quote)