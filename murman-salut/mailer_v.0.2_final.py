import smtplib
from email.mime.text import MIMEText
from http import HTTPStatus
from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class MyHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        '''Обработка POST запросов к серверу'''
        self.send_response(HTTPStatus.OK)
        self.send_header("Content_Type", "app/json; charset=utf-8")
        self.end_headers()
        content_type = self.headers["Content-Type"]
        if content_type == "application/x-www-form-urlencoded":
            length = int(self.headers["Content-Length"])
            data = self.rfile.read(length).decode("utf-8")
            result = json.loads(data)
            print(result)
            send_email(result)
        else:
            self.log_error("Unknown content_type: %s", content_type)


def send_email(message):
    sender = 'dima.greensfan@gmail.com'
    password = ''
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    true, false = True, False
    basket_list = []
    for i in range(len(message['items'])):
        item = f"{i+1}. {message['items'][i]['_id']} {message['items'][i]['title']}: {message['items'][i]['amount']} шт."
        basket_list.append(item)

    final_message = \
    f'''
    Данные заказчика:
    ФИО: {message["name"]}
    Телефон: {message["phone"]}
    E-mail: {message["email"]}
    Адрес доставки: {message["address"]}

    Состав заказа:
    '''
    for i in range(len(basket_list)):
        final_message += f'\n{basket_list[i]}'

    try:
        server.login(sender, password)
        msg = MIMEText(str(final_message))
        msg['Subject'] = 'НОВЫЙ ЗАКАЗ НА САЙТЕ!'
        server.sendmail(sender, sender, msg.as_string())
        return 'The message was sent successfully!'
    except Exception as _ex:
        return f'{_ex}\nCheck your login or password, please!'


if __name__ == '__main__':
    with HTTPServer(('', 8000), MyHandler) as server:
        server.serve_forever()
