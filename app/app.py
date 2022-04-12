from flask import Flask, render_template, request
from models import convert
from flask import Flask, request, make_response, send_file
from PIL import Image
from io import BytesIO
from PIL import ImageFont
from PIL import ImageDraw
import emoji

# Flaskオブジェクトの生成
app = Flask(__name__)

# @app.route('/')
# def index():
#     # 単純に文字列を表示するだけ
#     return 'hello world.'


@app.route('/', methods=['get'])
def img():
    font_path = "seguiemj.ttf"

    body = request.args.to_dict(True)
    x = int( body["x"] )
    y = int( body["y"] )
    w = body["w"]

    e = emoji.emojize(f":{w}:")

    # Pillowに変換 
    img = Image.new('RGB', (x, y))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font=font_path, size=int(x / 2))
    draw.text((x / 2 - ( x/4 ), y / 2 - (y/4) ), e ,(255,255,255),font=font)

    # 画像処理。ret_imgはPillowイメージ
    # ret_img = somet
    ret_img = img

    img_io = BytesIO()
    ret_img.save(img_io, 'JPEG', quality=95)
    img_io.seek(0)

    response = make_response(send_file(img_io, mimetype='image/jpeg'))
    return response

# 〜/index にアクセスがあった場合、index.htmlを描写する
@app.route('/index')
def post():
    return render_template('index.html')