from flask import Flask, render_template,redirect
import requests
from db_front_end import Db_Front_End_Methods

db_front_methods = Db_Front_End_Methods()
app = Flask(__name__)


OPERATION_TYPES = [
    'appendectomy',
    'breast biopsy',
    'carotid endarterectomy',
    'cataract surgery',
    'c-section',
    'cholecystectomy',
    'coronary artery bypass',
    'free skin graft',
    'hemorrhoidectomy',
    'partial colectomy',
    'prostatectomy',
    'tonsillectomy',
]

NODES = [1, 2, 3]


@app.route('/')
def index():
    return render_template('index.html', operation_types=OPERATION_TYPES, nodes=NODES)

@app.route('/data',methods=["GET","POST"])
def data_page():
    recent_5,avg_all_time = db_front_methods.fetch_category_data()
    return render_template('data.html', operation_types=OPERATION_TYPES, nodes=NODES,recent_5 = recent_5,avg_all_time = avg_all_time)

@app.route('/start-operation',methods=["POST"])
def start_operation():
    category = requests.form.get("category")
    node = requests.form.get("node_id")
    db_front_methods.create_surgery(node,category)
    redirect("/data")

@app.route('/end-operation',methods=["POST"])
def end_operation():
    node = requests.form.get("node_id")
    db_front_methods.end_surgery(node)
    redirect("/")





if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
