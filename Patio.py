from flask import Flask, render_template

app = Flask(__name__)

@app.route('/play')
def index():
    return render_template('nivel2.html', cantidad=int(3), color='blue')

@app.route('/play/<veces>')
def play_render(veces):
    return render_template('nivel2.html', cantidad=int(veces), color='blue')

@app.route('/play/<veces>/<color>')
def play_color_render(veces, color):
    return render_template('nivel2.html', cantidad=int(veces), color=color)





if __name__=="__main__":
    app.run(debug=True, port='5001')
# debi cambiar el puerto pues no me cargaba el browser
    