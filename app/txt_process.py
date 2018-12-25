# coding=utf-8

import sys

reload(sys)
sys.setdefaultencoding('utf8')


def get_passenger(ticket_obj):
    content = ''
    temp = ticket_obj.passengers.split("][")
    for t in temp:
        t = t.replace("[", "").replace("]", "").replace("_1", "").split(",")
        content = content + t[0] + "," + t[2] + "</br>"

    return content


def get_contact_info(ticket_obj):
    return "订单号: " + ticket_obj.ticket_id + " <br/>电话: " + ticket_obj.tel_phone + "<br/>订单单价: " + str(ticket_obj.price) \
           + "<br/>订单人数: " + str(ticket_obj.passenger_num) + "<br/>总价: " + str(int(ticket_obj.price) * int(ticket_obj.passenger_num))


def get_ticket_json(ticket_obj, num):
    # ticket = {"TaskNum": num, "Username": "", "Passwd": "",
    #           "From": ticket_obj.start_from, "To": ticket_obj.end_to,
    #           "Date": ticket_obj.ticket_date, "TaskTime": "",
    #           "FromTo": ticket_obj.from_to, "Passengers": ticket_obj.passengers,
    #           "SeatType": ticket_obj.seat_type, "TrainNum": ticket_obj.train_number,
    #           "Interval": "500", "Partial": "1", "Autocancel": "0", "Student": ticket_obj.is_student,
    #           "Note": "",
    #           "EndTime": ""}
    content_t = '{"TaskNum":"%d", "Username": "", "Passwd": "", "From": "%s", "To": "%s",  ' \
                '"Date": "%s", "TaskTime": "", ' \
                '"FromTo": "%s", "Passengers": "%s", "SeatType": "%s", "TrainNum": "%s",' \
                '"Interval": "500", "Partial": "1", "Autocancel": "0", "Student": "%d", ' \
                '"Note": "", "EndTime": ""}' % (
                    num, ticket_obj.start_from, ticket_obj.end_to, ticket_obj.ticket_date, ticket_obj.from_to,
                    ticket_obj.passengers.replace("][", ","), ticket_obj.seat_type, ticket_obj.train_number,
                    ticket_obj.is_student)

    content = "[%s]<br/><br/>任务=%s" % (str(num), content_t)
    return content


def get_task(ticket_obj, count):
    task_name = "任务_" + str(count) + ".txt"
    ticket_json = get_ticket_json(ticket_obj, count)

    passenger_name = "乘客信息_" + str(count) + ".txt"
    passenger_info = get_passenger(ticket_obj)

    other = "其他信息_" + str(count) + ".txt"
    contact_info = get_contact_info(ticket_obj)

    return "***********************</br> >>>>%s<<<< </br></br>%s</br></br> >>>>%s<<<< </br>%s</br></br> >>>>%s<<<< </br>%s<br/></br>****************" \
           % (task_name, ticket_json, passenger_name, passenger_info, other, contact_info)