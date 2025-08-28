 from flask import Flask, request, render_template, g, redirect, url_for, flash
 from flask import jsonify
 import logging
 
 import pandas as pd
 import numpy as np
 ## Models
 from sklearn.svm import SVC
 from sklearn.neighbors import KNeighborsClassifier
 
#sys.path.append("backend")
#sys.path.append("Classes")
#sys.path.insert(1, '/Classes/')
 from backend import MLA
 from backend import Validation
 from backend.calculator import Calculator
 def load_possible_experiments():
     list_Algorithms = MLA.getMLAs()
 
    #----------------new Cycon--------------------------->
    # First choice is between various categories of ML 
    g.section_Method = ["MLA: Machine Learning Algorithm", "DLANN: Deep Learning Artifical Neural Networks"]
    g.section_Info = [["Machine learning algorithms are mathematical model mapping methods. They are used to learn patterns embedded in the existing training dataset in order to perform pattern recognition, classification, and prediction.\n\nCurrently, the only algorithms available on cycon is under the classification objective. Other objectives that will be added later include clustering and regression."],
                      ["DLANN info"]]
     g.Methodologies = zip(g.section_Method, g.section_Info)
 
     # Obtain the selection of Algorithm Names and Definition.
     g.Algorithms = zip(g.section_algorithm, g.section_Info)
 
 


 # Old LCA for testing purposes, REMOVE BEFORE SUBMITTING.
 @bp.route("/LCA_Old")
 def LCA_Old():
     return render_template("experiments/LCA_Old.html")
 
 # REMOVE ASAP
 @bp.route("/new_experiment")
 def new_experiment():
     return render_template("experiments/new_experiment.html")
 
 @bp.route("/lca")
 def lca():
     return render_template("experiments/lca.html")
 
 
 @bp.route("/run_experiment", methods=["POST"])
def run_experiment():    
     output = request.get_json()
     formData = json.loads(output)
 
    data = formData['form']
 
     # Split
    if data['validation'] == "Split":
         Metrics = Validation.Split(data)
 
     # K-Fold
    elif data['validation'] == "K-Fold":
         Metrics = Validation.K_Fold(data)
 
    
     # Open json file for the experiment.
     baseFolder = os.getcwd()
    locationSavedResults = baseFolder + "\\SavedResults\\"
    if os.path.exists(locationSavedResults + data['projectName'] + ".json"):
        os.remove(locationSavedResults + data['projectName'] + ".json")
        fp = open(locationSavedResults + data['projectName'] + ".json", 'a')
     else:
        fp = open(locationSavedResults + data['projectName'] + ".json", 'a')
    
     # write to json file
     metrics_Dump = json.dumps(Metrics)
 
 
 
 @bp.route("/getResults", methods=["POST"])
def getResults(): 
     output = request.get_json()
     formData = json.loads(output)
 
    data = formData['form']
 
     baseFolder = os.getcwd()
    locationSavedResults = baseFolder + "\\SavedResults\\"
    fp = open(locationSavedResults + data['projectName'] + ".json", 'r')
 
     Metrics = json.load(fp)
 
     # close the connection
     fp.close()
    
     return json.dumps(Metrics)
 
 
 @bp.route("/results")
 def results():
     return render_template("experiments/results.html")

