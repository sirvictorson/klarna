from flask import Flask,render_template,request
from utils import get_pred, predicted

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html', name='Klarna')

# Define an API endpoint
@app.route('/prediction')
def prediction():
    print('We are in the prediction function')
    userid = request.args.get('uuid')
    print(userid)
    pred_def = get_pred(userid)
    return render_template('prediction.html', prediction=pred_def)

if __name__ == '__main__':
    app.run(debug=True)