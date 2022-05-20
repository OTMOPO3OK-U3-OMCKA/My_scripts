from flask import Flask, request, render_template, send_from_directory, Blueprint
from functions import JsonF
from json import JSONDecodeError
from logger import my_logg


POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"


bp = Blueprint('bp', __name__)

@bp.route("/")
def page_index():
    return render_template('index.html')
"""
@app.route("/list")
def page_tag():
    pass
"""

@bp.route("/post_form")
def page_post_form():
    return render_template('post_form.html')


@bp.route("/search", methods=['GET'])
def page_post_upload():
    reg = request.args.get('s')
    try:
        jf = JsonF(POST_PATH)
    except FileNotFoundError:
        my_logg.warning("no server")
        return "зайдите на сайт в другой раз"
    except:
        my_logg.warning("global except")
        return "автор так и не понял как работает JSONDecodeError потому что торопился"
    listik = jf.filter_reverse(reg)
    return render_template('post_list.html', reg=reg, listik=listik)


@bp.route("/uploads", methods=['POST'])
def static_dir():
    try:
        formats = [".png", ".jpg", "jpeg"]
        picture = request.files.get('picture')
        filename = picture.filename
        element = {"pic": filename,
                   "content": request.form.get('content')}
        if filename[-4::].lower() in formats:
            if bool(element["content"]):
                try:
                    picture.save(f'./static/images/{filename}')
                    jf = JsonF(POST_PATH)
                    jf.add_element(element)
                    f = jf.opener()
                    f.reverse()
                    ff = []
                except:
                    my_logg.warning("not json-file")
                    return "json не грузится"
                else:
                    return render_template("post_uploaded.html", f=f)
            return "не введен текст"
        else:
            return "нет картинки"
    except:
        return "вообще не знаю чё произошло"
    finally:
        my_logg.warning("there was an attempt to publish a post")
