import pytest
import sqlite3
import os
from database_manager import init_db, connect, anonymize_data, clear_test_data


# En "fixture" som ser till att vi har en ren databas inför testerna
@pytest.fixture(autouse=True)
def setup_database():
    init_db()
    yield
    # Valfritt: Ta bort filen efter testet för att städa upp
    # if os.path.exists("mynewapp.db"): os.remove("mynewapp.db")


def test_init_db_adds_default_users():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM personer')
    count = cursor.fetchone()[0]
    conn.close()

    # Verifierar att de 2 personerna från din init_db lades till
    assert count == 2


def test_anonymize_data_updates_names():
    # Kör din funktion
    anonymize_data()

    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM personer')
    names = cursor.fetchall()
    conn.close()

    # Kontrollera att alla namn nu är "Anonymiserad Namn"
    for row in names:
        assert row[0] == 'Anonymiserad Namn'


def test_clear_test_data_empties_table():
    clear_test_data()

    conn = connect()
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM personer')
    count = cursor.fetchone()[0]
    conn.close()

    assert count == 0