flask app

from pyexpat import model
from flask import *
import pandas as pd
import numpy as np
import pickle
import os,sys
import json

sys.path.append(os.path.abspath(os.path.join("./Scripts/")))

from prompter import Prompter

app = Flask(__name__, static_folder='staticFiles') 



@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    try:
        if request.method == 'POST':
            j_d = request.form['j_d']
            ch_model = request.form['model']
            prompt_type = request.form['prompt_type']
            num_token = int(request.form['num_token'])
            example_num = int(request.form['num_example'])

            if len(j_d.strip()) == 0:
                raise Exception("Please enter Job Description")
            else:
                model = 'xlarge'
                if int(ch_model) != 1:
                    model = 'f0cc02b7-c49e-4b41-b57d-101095e559a9-ft'
                jdpipeline = Prompter(j_d, model=model, prompt_type=int(prompt_type), num_tokens=num_token, example_num=example_num)
                response,val = jdpipeline.make_request()
               
                return render_template('home.html', title='Home', error_text='', response=response, process_dict=val)
                
        return render_template('home.html', title='Home', error_text='')
    except Exception as e:
        return render_template('home.html', title='Home', error_text=str(e))
        

if __name__ == '__main__':  
   app.run(debug = True)  