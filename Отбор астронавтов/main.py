from flask import Flask,  url_for, request

app = Flask('my web app')


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def astrunaut_selection():
    if request.method == 'GET':
        return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Отбор астронавтов</title>
                  </head>
                  <body>
                    <h2>Анкета претендента</h2>
                    <h3>на участие в миссии</h3>
                     <div>
                        <form class="astronaut_form" method="post" enctype="multipart/form-data")
                        <label for="form-control">  </label>
                        <input type="astro_sname" class="form-control" id="astro_sname" placeholder="Введите фамилию" name="astro_sname">
                        <input type="astro_name" class="form-control" id="name" placeholder="Введите имя" name="astro_name">
                        <label for="form-control">  </label>
                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                        <div class="form-group">
                            <label for="form-control">Какое у Вас образование</label>
                            <select class="form-control" id="form-control" name="class">
                            <option>начальное</option>
                            <option>Высшее неоконченное</option>
                            <option>Высшее </option>
                            <option>Среднее </option>
                            <option>9 классов</option>
                            </select>
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
                            <div class="form-check">
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
                            <label for="form-control">Почему Вы хотите принять участие в миссии</label>       
                            <textarea class="form-control" id="motivation" rows="3" name="about"></textarea>
                        </div>    
                        <div class="form-group">
                            <label for="photo">Приложите фотографию</label>
                            <input type="file" class="form-control-file" id="photo" name="file">
                        </div>
                         <div class="form-group form-check">
                            <input type="checkbox" class="form-check-input" id="stayOnMars" name="stay" checked>
                            <label class="form-check-label" for="stayOnMars">Готов остаться на Марсе</label>
                        </div>
                        <button type="submit" class="btn btn-primary">Отправить</button>
                  </body>
                </html>"""
    elif request.method == 'POST':
        res = request.files['file']
        print('file=', res.read())
        print('astro_sname=', request.form.get('astro_sname'))
        print('astro_name=', request.form.get('astro_name'))
        print('profession=', request.form.get('profession'))
        print('sex=', request.form.get('sex'))
        print('about=', request.form.get('about'))
        print('stay=', request.form.get('stay'))
        return "Форма отправлена"


app.run(debug=True, port=8080)