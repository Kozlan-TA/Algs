import db
import matplotlib.pyplot as plt
import random

import os
from dotenv import load_dotenv

load_dotenv()

'''
from psycopg2._json import Json
def add_data(self, x, y, speed, id_car):
    self.cursor.execute("insert into messages(terminal_id, speed, timestamp, can_data) values (%s, %s, %s, %s)", (id_car, speed, x, Json(y),))
    self.connect.commit()
'''

x = []
y = []
speed = []
id_car = '123456789'



points = {
    0: {'point': 5, 'type': 'state'},
    1: {'point': 3, 'type': 'fuel'},
    2: {'point': 15, 'type': 'consumption'},
    3: {'point': 2, 'type': 'antifuel'},
    4: {'point': 30, 'type': 'consumption'},
}

x_len = 0

for i in points:
    for j in range(0, points[i]['point']):
        types = points[i]['type']
        if 'state' == types:
            y.append(10)
            speed.append(0)
        if 'fuel' == types:
            y.append(y[-1] + 15)
            speed.append(0)
        if 'consumption' == types:
            if y[-1] - 1 <= 0:
                y.append(y[-1])
                speed.append(speed[-1])
            else:
                y.append(y[-1] - random.random())
                speed.append(random.randint(5, 100))
        if 'antifuel' == types:
            if y[-1] - 5 <= 0:
                y.append(y[-1] + 20)
            else:
                y.append(y[-1] - 5)
            speed.append(0)
    x_len += points[i]['point']

for i in range(0, x_len):
    x.append(i)




if __name__ == "__main__":
    con = db.ConnectionDB(user = os.getenv("DB_USER"), password=os.getenv("DB_PASSWORD"), database='speed_data')
    for i in range(x_len):
        con.add_data(x[i], {'LLS': y[i]}, speed[i], id_car)
        
    plt.plot(x, y)
    plt.show()
