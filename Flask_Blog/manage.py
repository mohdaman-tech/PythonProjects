import numpy as np
import matplotlib.pyplot as plt
from flask import Flask,render_template,request
import time

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


if __name__ == '__main__':
    app.run(debug=True)
