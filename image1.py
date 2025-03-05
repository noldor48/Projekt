import sqlite3, os

def write_to_file(data, filename):
    # Преобразование двоичных данных в нужный формат
    with open(filename, 'wb') as file:
        file.write(data)
    print("Данный из blob сохранены в: ", filename, "\n")

def read_blob_data(emp_id):
    try:
        sqlite_connection = sqlite3.connect('Persons.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_fetch_blob_query = """SELECT * from Personas where person_id = 2"""
        cursor.execute(sql_fetch_blob_query, (emp_id,))
        record = cursor.fetchall()
        for row in record:
            print("Id = ", row[0], "Name = ", row[1])
            name  = row[1]
            photo = row[7]
            resume_file = row[3]

            print("Сохранение изображения сотрудника и резюме на диске \n")
            photo_path = os.path.join("db_data", name + ".jpg")
            resume_path = os.path.join("db_data", name + "_resume.txt")
            write_to_file(photo, photo_path)
            write_to_file(resume_file, resume_path)
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")

read_blob_data(1)
read_blob_data(2)