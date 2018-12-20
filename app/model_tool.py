# coding=utf-8
import random

from app.config import SINGLE_PRICE
from app.models import Ticket

import sys

reload(sys)
sys.setdefaultencoding('utf8')

def get_tid():
    flag = True
    tid = ""
    while flag:
        tid = create_ticket_id()
        num = Ticket.query.filter(
            Ticket.ticket_id == tid
        ).count()
        if num <= 0:
            flag = False
    return tid


def create_ticket_id():
    t_id = ""
    for i in range(0, 2):
        s = random.randint(65, 90)
        t_id += chr(s)
    for i in range(0, 2):
        s = random.randint(0, 9)
        t_id += str(s)
    return t_id


def get_price(passenger_num, percent):
    if str(percent) == "0":
        return 0

    if str(percent) == "25":
        return SINGLE_PRICE * int(passenger_num)

    if str(percent) == "50":
        return SINGLE_PRICE * int(passenger_num)

    if str(percent) == "75":
        return SINGLE_PRICE * int(passenger_num)

    if str(percent) == "96":
        return SINGLE_PRICE * int(passenger_num)


def get_from_to(start_from, end_to):
    temp = start_from.split("][")[0].replace("[", "") + "--" + end_to.split("][")[0].replace("[", "")
    return temp


def get_ticket_json2(ticket):
    ticket = {'ticket_id': ticket.ticket_id, 'tel_phone': ticket.tel_phone, 'idcard_num': ticket.idcard_num,
              'ticket_date': ticket.ticket_date, 'start_from': ticket.start_from, 'end_to': ticket.end_to,
              'train_number': ticket.train_number, 'passengers': ticket.passengers,
              'passenger_num': ticket.passenger_num,
              'success_rate': ticket.success_rate, 'price': ticket.price,
              'status': ticket.status}
              # 'create_date': ticket.create_date,
              # 'update_date': ticket.update_date}
    return ticket

def get_ticket_json2(ticket):
    ticket = {'ticket_id': ticket.ticket_id, 'tel_phone': ticket.tel_phone, 'idcard_num': ticket.idcard_num,
              'ticket_date': ticket.ticket_date, 'start_from': ticket.start_from, 'end_to': ticket.end_to,
              'train_number': ticket.train_number, 'passengers': ticket.passengers,
              'passenger_num': ticket.passenger_num,
              'success_rate': ticket.success_rate, 'price': ticket.price,
              'status': ticket.status}
              # 'create_date': ticket.create_date,
              # 'update_date': ticket.update_date}
    return ticket

def mock_ticket():
    ticket = Ticket(ticket_id='tid01',
                    tel_phone='1199883',
                    idcard_num="988223",
                    ticket_date='[2018-12-15][2018-12-16]',
                    start_from='[北京][北京北][北京东][北京南][北京西][昌平北]',
                    end_to='[汉口][武昌][武汉]',
                    train_number='[C7084][D944][T96][G2922]',
                    passengers='[岑晓威,1,440307199608140313_1][付新鹏,1,652325199009083410_1][方章伟,1,445224199104012452_1][黄河长,1,43282219761010097X_1][康志香,1,430523198004150064]',
                    passenger_num=5,
                    success_rate=80,
                    price=100,
                    status=1,
                    seat_type='[一等座][二等座][软卧][硬卧][硬座]',
                    is_student=0,
                    from_to='北京--武汉')
    return ticket