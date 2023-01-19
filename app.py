import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
pkl_file = open('model.pkl','rb')
model = pickle.load(open('model.pkl', 'rb'))
index_dict = pickle.load(pkl_file)


@app.route('/')
def home():
    return jsonify({"Project is working..."})



@app.route('/api/predict',methods=['POST'])
def predict():

    if request.method=='POST':
        result = request.form
        

        index_dict = pickle.load(open('cat','rb'))
        location_cat = pickle.load(open('location_cat','rb'))

        new_vector = np.zeros(151)

        result_location = result['location']

        if result_location not in location_cat:
            new_vector[146] = 1
        else:
            new_vector[index_dict[str(result['location'])]] = 1


        new_vector[index_dict[str(result['area'])]] = 1

        new_vector[0] = result['sqft']
        new_vector[1] = result['bath']
        new_vector[2] = result['balcony']
        new_vector[3] = result['size']

    new = [new_vector]

    print(new)
    prediction = model.predict(new)
    print(prediction)

    return jsonify({"prediction": '{}'.format(prediction)[1:-1]})

@app.route('/api/test')
def test():
    return jsonify({"Project is working just fine"})

@app.route('/api/test2')
def test2():
    return jsonify({"Project is working just fine"})


@app.route('/api/test21')
def test21():
    return jsonify({"Project is working just fine"})



if __name__ == "__main__":
    app.run(debug=True, port= 5000)
