class DatabaseHelper:
    __database_connection = None
    __data: str = ''

    def __new__(cls):
        if cls.__database_connection is None:
            cls.__database_connection: DatabaseHelper = object.__new__(cls)
            print('Con to DB')
        return cls.__database_connection

    def select_data(self) -> str:
        return self.__data

    def insert_data(self, new_data: str):
        self.__data = new_data


if __name__ == '__main__':
    db_con = DatabaseHelper()
    db_con.insert_data('12345')

    db = DatabaseHelper()
    print(db.select_data())
