import sqlite3
import os

db_namn = "mynewapp.db"


def connect():
    return sqlite3.connect(db_namn)


def init_db():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS personer (
           id INTEGER PRIMARY KEY,
           name TEXT,
           ålder INTEGER
         )
    ''')

    cursor.execute('SELECT * FROM personer')
    resultat = cursor.fetchall()
    if resultat:
        conn.close()
        return

    cursor.executemany('''
        INSERT INTO personer(id, name, ålder)
        VALUES(?,?,?)                              
    ''', [(1, 'Sara', 25), (2, 'Matteo', 30)])

    conn.commit()
    conn.close()


def add_new_person_data():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM personer')
    resultat = cursor.fetchall()
    # Vi returnerar resultatet istället för att bara printa,
    # då blir det lättare att skriva assert-tester!
    conn.close()
    return resultat


def clear_test_data():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM personer')
    conn.commit()
    conn.close()


def anonymize_data():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE personer
        SET name = 'Anonymiserad Namn'
    ''')
    conn.commit()
    conn.close()


# Allt under här körs BARA när du kör filen direkt, inte när Pytest importerar den
if __name__ == "__main__":
    print('Starta testa data manuellt')
    init_db()
    print(add_new_person_data())
    anonymize_data()
    print("Efter anonymisering:", add_new_person_data())
    clear_test_data()
    print("Efter rensning:", add_new_person_data())