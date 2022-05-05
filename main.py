from flask import Flask, request

app = Flask(__name__)
# Ограничиваем размер файла здесь
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024


@app.route('/')
def page_form():
    """ Эта вьюшка показывает форму, которая отправляет файлы"""
    form_content = """
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="picture">
        <input type="submit" value="Отправить">
    </form>
    """
    return form_content


@app.route('/upload', methods=['POST'])
def page_upload():
    """ Эта вьюшка обрабатывает форму"""

    # Получаем объект картинки из формы
    picture = request.files.get("picture")

    # Получаем имя файла у загруженного фала
    filename = picture.filename

    # Сохраняем картинку под родным именем в папку uploads
    picture.save(f"./uploads/{filename}")
    return f"Загружен и сохранен файл"

app.run()