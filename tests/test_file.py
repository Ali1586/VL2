import os


def test_that_file_handling_works():
    # 1. Definiera filnamn
    filename = "temp_test_file.txt"
    content_to_write = "Hello World!"

    # 2. Skapa och skriv till filen
    with open(filename, "w") as f:
        f.write(content_to_write)

    # 3. Läs från filen och validera
    with open(filename, "r") as f:
        content_read = f.read()

    assert content_read == content_to_write

    # 4. Städa upp (ta bort filen)
    os.remove(filename)

    # Validera att filen är borta
    assert not os.path.exists(filename)