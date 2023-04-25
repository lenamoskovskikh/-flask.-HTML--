from flask import Flask, url_for, request

app = Flask('my web app')


@app.route('/carousel')
def carousel():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                  </head>
                  <body>
                    <h1>Пейзажи Марса</h1>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <div id="carousel" class="carousel slide span12" data-ride="carousel">
                      <ol class="carousel-indicators">
                        <li data-target="#carouselExampleIndicators" data-slide-to="0"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                      </ol>
                      <div class="carousel-inner">
                        <div class="carousel-item active" data-interval="200">
                          <img class="img-fluid" src="/static/img/mars1.jpg" class="d-block w-20" alt="First slide">
                        </div>
                        <div class="carousel-item" data-interval="200">
                          <img class="img-fluid" src="/static/img/mars2.jpg" class="d-block w-20" alt="Second slide">
                        </div>
                        <div class="carousel-item" data-interval="200">
                          <img class="img-fluid" src="/static/img/mars3.jpg" class="d-block w-20" alt="Third slide">
                        </div>
                      </div>
                    </div>
                    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
                    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js"></script>
                  </body>
                </html>"""


app.run(debug=True, port=8080)
