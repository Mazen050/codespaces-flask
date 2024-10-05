from flask import Flask, render_template,request,jsonify
from captcha_audio import captcha_audio_ai
from captcha_spin import captcha_spin_ai
from captcha_img_ai import captchaai_img

app = Flask(__name__)

@app.route("/audio",methods=["GET","POST"])
def audio():
    if request.method=='POST':
        return str(captcha_audio_ai(request.form['url']))
    return render_template("index.html", title="Hello")

@app.route("/spin",methods=["GET","POST"])
def spin():
    if request.method=='POST':
        f = request.files['media']
        f.save("spin.png")
        return str(captcha_spin_ai())
    return render_template("index.html", title="Hello")

@app.route("/img",methods=["GET","POST"])
def img():
    if request.method=='POST':
        u = request.form['url']
        result = captchaai_img(u)
        return jsonify(result)
    return render_template("index.html", title="Hello")