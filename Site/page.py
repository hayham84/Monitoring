from flask import Flask, render_template
import sys

sys.path.append("/home/admin/AMS/Envoiemail_detectCrise_Graphe")
from visualisation2 import generate_graph

sys.path.append("/home/admin/AMS/infoSysteme_infoCERT_data")
from systeme import system

page = Flask(__name__)  # Flask va chercher les templates dans ./templates par défaut

@page.route("/")
def index():

    cpu, ram, disk = system()
    data = {
        "cpu_usage": cpu,
        "ram_usage": ram,
        "disk_usage": disk
    }

    chart_uri = generate_graph()
    return render_template("indexe.html", data=data, chart_uri=chart_uri)

if __name__ == "__main__":
    page.run(host="0.0.0.0")
