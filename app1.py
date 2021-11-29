from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/upload": {"origins": "*"}})
CORS(app, resources={r"/": {"origins": "*"}})


@app.route("/")
# @cross_origin(origin='localhost:3000',headers=['Content-Type','multipart/form-data'])
def hello():
    # # request.headers.add("Access-Control-Allow-Origin", "*")
    # img = preprocess_image("NORMAL-img.jpeg")
    # predicted_class = predict(img)
    return "Pathology-Detection"


if __name__ == "__main__":
    # app.run(debug=True)
    # cors.init_app(app)
    app.run(debug=True,host="0.0.0.0", port=5000)


# CORS(app, expose_headers='Authorization')
