import streamlit as st
from PIL import Image
import tensorflow as tf
import numpy as np
from flask import Flask
import pickle
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
"""
# Covid 19 Classifier
"""
model = tf.keras.models.load_model("model.h5")
app=Flask(__name__,template_folder="templates")

# @app.route('/',methods=['GET'])
# @cross_origin()
# def home():
#     return render_template('index.html')
# @app.route('/predict',methods=['POST'])
# @cross_origin()
# def predict():
#     uploaded_file = request.form.get("img")

#     image = Image.open(uploaded_file)
#     # To read file as bytes:
#     image.save('E:/Ineuron/Project/Covid-19-Image-Classifier/artifacts/1.jpg')
#     image = Image.open("E:/Ineuron/Project/Covid-19-Image-Classifier/artifacts/1.jpg")
#     img = image.resize((224,224))
#     img_array = np.array(img)
#     img_array = np.expand_dims(img_array, axis=0) # [batch_size, row, col, channel]
#     result = model.predict(img_array) # [[0.99, 0.01], [0.99, 0.01]]

#     argmax_index = np.argmax(result, axis=1) # [0, 0]
#     if argmax_index[0] == 0:
#         return render_template('index.html', prediction_text="predicted: covid. Thank to Tanmay for this help :)")
#             # st.image(image, caption="predicted: covid. Thank to Tanmay for this help :)")
#     elif argmax_index[0] == 1:
#         return render_template('index.html', prediction_text="predicted: Normal. Thank to Tanmay for this help :)")
            
#             # st.image(image, caption="predicted: Normal. Thank to Tanmay for this help :)")
        
#     return render_template('index.html', prediction_text="predicted: viral pneumonia. Thank to Tanmay for this help :)")
#             # st.image(image, caption='predicted: Viral Pneumonia')
        
from flask import Flask,request,render_template,redirect
import os

app = Flask(__name__)


# def predict_label(img_path):
# 	i = image.load_img(img_path, target_size=(100,100))
# 	i = image.img_to_array(i)/255.0
# 	i = i.reshape(1, 100,100,3)
# 	p = model.predict_classes(i)
# 	return dic[p[0]]

def predict_label(img_path):
    image = Image.open(img_path)
    img = image.resize((224,224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    result = model.predict(img_array)
    argmax_index = np.argmax(result, axis=1) 
    if argmax_index[0]==0:
        return "Predicted Covid , thanks to tanmay :)"
    elif argmax_index[0]==1:
        return "Predicted Normal, thanks to tanmay :)"
    return "Predicted viral pneumonia , thanks to tanmay :)"



# routes
@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")


@app.route("/submit", methods = ['GET', 'POST'])
def get_output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/" + img.filename	
		img.save(img_path)

		p = predict_label(img_path)

	return render_template("index.html", prediction = p, img_path = img_path)


if __name__ =='__main__':
	#app.debug = True
	app.run(debug = True)








if __name__=="__main__":
    app.run(debug=True)