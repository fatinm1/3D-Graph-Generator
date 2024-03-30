from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-plot', methods=['POST'])
def generate_plot():
    z_max = int(request.form['z_max'])
    num_points = int(request.form['num_points'])

    # Your plotting code here, ending with saving the plot to a buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_url = base64.b64encode(buf.getvalue()).decode()

    return '<img src="data:image/png;base64,{}">'.format(plot_url)

if __name__ == '__main__':
    app.run(debug=True)
