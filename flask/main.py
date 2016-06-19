import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
import flask
from werkzeug.utils import secure_filename
import json as json_m

#import os
#from flask import Flask, render_template, request, redirect, url_for, send_from_directory
#from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/home/emerson/github/AngelHacks/flask/uploads/'
TRANS_FOLDER = '/home/emerson/github/AngelHacks/flask/transcripts/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'wav'])


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def test():
    print "it workedsdsfdkojflskdfghnkldsjgdfklrg"
    
        
    obj = donger

    #return "hello there"
    return flask.jsonify(obj)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        #if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            AUDIO_FILE = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            jsonString = "hello there"
            return jsonString
            #return redirect(url_for('uploaded_file', filename=filename))
            #speech_to_telxt(AUDIO_FILE)

    return render_template("index.html")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(debug=True)
