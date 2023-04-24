from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def root():
    return "<b>Миссия Колонизация Марса</b>"


@app.route('/index')
def index():
    return "<b>И на Марса будут яблони цвести</b>"


@app.route('/promotion')
def promotion():
    return "<b>Человечество вырастает из детства.<br>Человечеству мала одна планета." \
           "<br>Мы сделаем обитаемыми безжизненные пока планеты.<br>И начнем с Марса!<br>Присоединяйся!</b>"


@app.route('/image_mars')
def image():
    return f'''<title>Привет, Марс</title><h1>Жди нас, Марс!</h1><img src="{url_for('static', filename='mars2.jpg')}" 
           alt="здесь должна была быть картинка, но не нашлась"><br>Вот она какая, красная планета'''

@app.route('/promorion_image')
def promo():
    return f'''<head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
               <div class="link-danger" role="alert"> 
               </title><h1>Жди нас, Марс!</h1>
               </div>
               <img src="{url_for('static', filename='img/mars.jpg')}" 
                alt="здесь должна была быть картинка, но не нашлась">
                </head>
                <body>
                  <link rel="stylesheet" 
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                  <div class="alert alert-danger" role="alert">
                    Человечество вырастет из детства 
                  </div>
                  <div class="alert alert-success" role="alert">
                    Человечеству мала одна планета
                  </div>
                  <div class="alert alert-secondary" role="alert">
                    Мы сделаем обитаемыми безжизненные пока планеты
                  </div>
                  <div class="alert alert-warning" role="alert">
                    И начнем с Марса
                  </div>
                  <div class="alert alert-warning" role="alert">
                    Присоединяйся
                  </div>
                    </body>
                    </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')