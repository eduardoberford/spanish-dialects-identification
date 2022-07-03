#import libraries
from flask import Flask, request, render_template, jsonify
import pickle
import os
from flask import send_from_directory

human_readable_label = {
    0 : 'Emilian-Romagnol',
    1 : 'Neapolitan',
    2 : 'Piedmontese',
    3 : 'Friulian',
    4 : 'Ladin',
    5 : 'Ligurian',
    6 : 'Lombard',
    7 : 'Tarantino',
    8 : 'Sicilian', 
    9 : 'Venetian',
    10 : 'Sardinian'
}

#Initialize the flask App
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))


#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route('/map_<int:num>.png')
def image_map(num):
    image =  f'maps/map_{num}.png'
    print(image)
    return send_from_directory(os.path.join(app.root_path, 'static'), image)


#To use the predict button in our web-app
@app.route('/predict',methods=['GET'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    text = request.args.get('sentence')

    pred = model.predict(text)
    proba = model.predict_proba(text).tolist()[0]

    

    res = 'Predicted dialect: '+human_readable_label[pred[0]] + '<br><br><br><div class="proba"> <canvas id="marksChart"></canvas> </div>' \
            + '<script>   draw(' + str(proba) + ') </script>'

    res += f'<div class="map"><img src="map_{pred[0]}.png" alt="User Image" width="80%" height="80%"></div>'
    
    return jsonify(res)

if __name__ == "__main__":
    app.run(debug=True)