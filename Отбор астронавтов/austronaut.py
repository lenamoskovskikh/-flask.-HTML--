from flask import Flask
from flask import url_for
from flask import request

app = Flask(__name__)


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style1.css')}" />
                          </head>
                          <body>
                            <h1>Анкета претендента</h1>
                            <h1>на участие в миссии</h1>
                            <form class="login_form" method="post">
                <input class="form-control" placeholder="Введите фамилию" name="surname">
                <input class="form-control" placeholder="Введите имя" name="name">

                <div class="form-group">
                    <label for="email"></label>
                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                </div>

                <div class="form-group">
                    <label for="classSelect">Какое у Вас образование?</label>
                    <select class="form-control" id="classSelect" name="education">
                      <option>Начальное</option>
                      <option>Среднее</option>
                      <option>Неполное высшее</option>
                      <option>Высшее</option>
                      <option>Другое</option>
                    </select>
                 </div>

                <div class="form-group">
                    <label for="form-check-">Какие у Вас есть профессии?</label>
                    <div class="form-check" id="form-check-">
                        <input type="checkbox" class="form-check-input" id="prof1" name="prof1"
                               value="микробиолог">
                        <label class="form-check-label" for="prof1"> микробиолог </label>
                        <input type="hidden" name="prof1" value="0">
                    </div>
                    <div class="form-check">
                        <input type="checkbox" class="form-check-input" id="prof2" name="prof2" value="пилот">
                        <label class="form-check-label" for="prof2"> пилот </label>
                        <input type="hidden" name="prof2" value="0">
                    </div>
                    <div class="form-check">
                        <input type="checkbox" class="form-check-input" id="prof3" name="prof3" value="программист">
                        <label class="form-check-label" for="prof3"> программист </label>
                        <input type="hidden" name="prof3" value="0">
                    </div>
                    <div class="form-check">
                        <input type="checkbox" class="form-check-input" id="prof4" name="prof3" value="физик-ядерщик">
                        <label class="form-check-label" for="prof4"> физик-ядерщик </label>
                        <input type="hidden" name="prof4" value="0">
                    </div>
                    <div class="form-check">
                        <input type="checkbox" class="form-check-input" id="prof5" name="prof3" value="строитель">
                        <label class="form-check-label" for="prof5"> строитель </label>
                        <input type="hidden" name="prof5" value="0">
                    </div>
                    <div class="form-check">
                        <input type="checkbox" class="form-check-input" id="prof6" name="prof3" value="врач">
                        <label class="form-check-label" for="prof6"> врач </label>
                        <input type="hidden" name="prof6" value="0">
                    </div>
                    <div class="form-check">
                        <input type="checkbox" class="form-check-input" id="prof7" name="prof3" value="инженер">
                        <label class="form-check-label" for="prof7"> инженер </label>
                        <input type="hidden" name="prof7" value="0">
                    </div>
                </div>

                <div class="form-group">
                    <label for="form-check">Укажите пол</label>
                    <div class="form-check" id="form-check">
                      <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                      <label class="form-check-label" for="male">
                        Мужской
                      </label>
                    </div>
                    <div class="form-check">
                      <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                      <label class="form-check-label" for="female">
                        Женский
                      </label>
                    </div>
                </div>

                <div class="form-group">
                    <label for="about">Почему Вы хотите принять участие в миссии?</label>
                    <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                </div>
                <div class="form-group">
                    <label for="photo">Приложите фотографию</label>
                    <input type="file" class="form-control-file" id="photo" name="file">
                </div>

                <div class="form-group form-check">
                    <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                    <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                    <input type="hidden" name="accept" value="0">
                </div>
                <button type="submit" class="btn btn-primary">Отправить</button>
            </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form['surname'])
        print(request.form['name'])
        print(request.form['email'])
        print(request.form['education'])
        print(request.form['prof1'])
        print(request.form['prof2'])
        print(request.form['prof3'])
        print(request.form['prof4'])
        print(request.form['prof5'])
        print(request.form['prof6'])
        print(request.form['prof7'])
        print(request.form['sex'])
        print(request.form['about'])
        print(request.form['file'])
        print(request.form['accept'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
