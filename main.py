from flask import Flask, render_template
from random import choice
import os

app = Flask(__name__)

@app.route('/random_image')
def random_image():
    # Путь к папке с изображениями
    image_folder = os.path.join(app.root_path, 'static/images')

    # Получение списка всех файлов изображений
    image_files = os.listdir(image_folder)

    # Выбор случайного файла изображения
    random_image_file = choice(image_files)

    # Полный путь к выбранному случайному изображению
    random_image_path = os.path.join('/static/images', random_image_file)

    return render_template('home.html', image_path=random_image_path)

if __name__ == '__main__':
    app.run()
