from flask import *
from models import *

app = Flask(__name__)

import cv2
import numpy as np
import base64
from io import BytesIO
from PIL import Image



num_input_image = 0
# api to process input
@app.route('/', methods=['GET', 'POST', 'PUT'])
def _upload_file():
    global num_input_image
    if request.method == 'GET':
        return render_template('h1.html')
    if request.method == 'POST':
        res = 0
        predict_time = 0
        # process image
        # filestr return type: byte
        filestr = request.files['file'].read()
        # convert string data to numpy array
        npimg = np.frombuffer(filestr, np.uint8)
        # convert numpy array to image
        img = cv2.imdecode(npimg, 1)
        # save image, path, add_img
        num_input_image += 1
        add_img = "F:/NhanDienLogoWeb/static/"+"img"+str(num_input_image)+".jpg"
        cv2.imwrite(add_img, img)
        # save choose
        choose = request.form['choose']

        # save res, predict_time
        if choose == "Logistic Regression":
            res, predict_time = lr(add_img)
        elif choose == "Decision tree":
            res, predict_time = dt(add_img)
        elif choose == "Naive Bayes":
            res, predict_time = nb(add_img)
        elif choose == "SVM":
            res, predict_time = svm(add_img)

        img = Image.fromarray(img).convert('RGB')
        buffered = BytesIO()
        img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue())

        return render_template('h2.html', choose=choose, path='data:img/jpeg;base64,'+img_str.decode('utf-8'), res=res, predict_time=predict_time)


# run server
if __name__ == '__main__':
    app.run(debug=True)


# # init parameters:
# num_input_image = 0 # numerical logo
# choose = "" # user 's choose
# add_img = "" # full address to store input image
# path = "" # path to store input image
# res = ""
# predict_time = 0.0
#
# # api for user enter the input
# @app.route('/upload')
# def upload_file():
#     return render_template('h1.html')
#
# # api to process input
# @app.route('/uploader', methods=['GET', 'POST'])
# def _upload_file():
#     global num_input_image, add_img, choose, path, res, predict_time
#     if request.method == 'POST':
#         # process image
#         # filestr return type: byte
#         filestr = request.files['file'].read()
#         # convert string data to numpy array
#         npimg = np.frombuffer(filestr, np.uint8)
#         # convert numpy array to image
#         img = cv2.imdecode(npimg, 1)
#         # save image, path, add_img
#         num_input_image += 1
#         path = "static/" + "img" + str(num_input_image) + ".jpg"
#         add_img = "F:/NhanDienLogoWeb/static/"+"img"+str(num_input_image)+".jpg"
#         cv2.imwrite(add_img, img)
#
#         # save choose
#         choose = request.form['choose']
#
#         # save res, predict_time
#         if choose == "Logistic Regression":
#             res, predict_time = lr(add_img)
#         elif choose == "Decision tree":
#             res, predict_time = dt(add_img)
#         elif choose == "Naive Bayes":
#             res, predict_time = nb(add_img)
#         elif choose == "SVM":
#             res, predict_time = svm(add_img)
#
#         return redirect(url_for("result"))
#
# # api to show result
# @app.route('/result')
# def result():
#     global choose, path, res, predict_time
#     return render_template('h2.html', choose = choose, path = path, res = res, predict_time = predict_time)
#
# # run server
# if __name__ == '__main__':
#     app.run(debug=True)


# init parameters:
# num_input_image = 0 # numerical logo
# choose = "" # user 's choose
# add_img = "" # full address to store input image
# path = "" # path to store input image
# res = ""
# predict_time = 0.0

# api for user enter the input
# @app.route('/upload')
# def upload_file():
#     return render_template('h1.html')


