import psycopg2
from psycopg2._json import Json
# \copy messages from 'C:\Users\sugawara\Desktop\test.csv' delimiter ',' csv header;

import os
from dotenv import load_dotenv

load_dotenv()


class ConnectionDB:
    def __init__(self, user, password, database):
        self.connect = psycopg2.connect(
            user=user,
            password=password,
            database=database
        )

        self.cursor = self.connect.cursor()

    def get_data_speed(self):
        # 1677877200
        # 1677963540
        self.cursor.execute("select timestamp, speed from messages where terminal_id='433427026902662' and timestamp > 1677877200 and timestamp < 1677963540")
        return [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in self.cursor.fetchall()]


    def get_can_data(self):
        # self.cursor.execute("select timestamp, can_data, speed from messages where terminal_id='433019520494099' and timestamp > 1677877200 and timestamp < 1677963540")
        self.cursor.execute("select timestamp, can_data, speed from messages where terminal_id='433100526928099' and timestamp > 1677877200 and timestamp < 1677963540")
        return [dict((self.cursor.description[i][0], value) for i, value in enumerate(row)) for row in
                self.cursor.fetchall()]

    def add_data(self, x, y, speed, id_car):
        self.cursor.execute("insert into messages(terminal_id, speed, timestamp, can_data) values (%s, %s, %s, %s)", (id_car, speed, x, Json(y)))
        self.connect.commit()


if __name__ == '__main__':
    con = ConnectionDB(user=os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), database='speed_data')
    get_speed = con.get_can_data()
    print(get_speed)
