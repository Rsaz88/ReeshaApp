import os
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import easyocr

reader = easyocr.Reader(['ar'], True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
FILE_DIR = 'files'

app = Flask(__name__)

if not os.path.exists(FILE_DIR):
    os.makedirs(FILE_DIR)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = FILE_DIR + '/' + secure_filename(file.filename)
            file.save(filename)
            parsed = reader.readtext(filename)
            text = '\n'.join(map(lambda x: x[1], parsed))
            # handle file upload
            return (text)
            
    return '''
    <!doctype html>
    <html>

    <head>

    <meta charset="UTF-8">

    <title>Reesha</title>

    </head>



    <body>

        <!-- Main Container -->

    <div class="container"> 

    <!-- Navigation -->

    <header> 

        <a class="logo" href="#"><img id="logo" src="reeshaLOGO.png" style="width: 180px; height: 90px;"></a>

    

        <nav>

        <ul>

            <li><a href="#hero">عن ريشة </a></li>

            <li><a href="#about">الرئيسية </a></li>

        </ul>

        </nav>

    </header>


        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
        </form>

        <style>

            body {

            font-family: Shamel Family ;

            font-weight: 50% ;

            background-color: #f2f2f2;

            margin-top: 0px;

            margin-right: 0px;

            margin-bottom: 0px;

            margin-left: 0px;

            font-style: normal;

            font-weight: 100;

        }

        /* Container */

        .container {

            width: 90%;

            margin-left: auto;

            margin-right: auto;

            height: 1000px;

            background-color: #FFFFFF;

        }

        /* Navigation */

        header {

            width: 100%;

            height: 10%;

            background-color: #FFFFFF;

            border-bottom: 1px solid #FFFFFF;

        }

        .logo {

            width: 130px;

            height: 130px;

            

            margin: 150px;

            border-radius: 5%;

            color: #fff;

            font-weight: bold;

            text-align: undefined;

            width: 10%;

            float: right;

            margin-top: 19px;

            margin-left: 20px;

            letter-spacing: 4px;

        }

        nav {

            float: left;

            width: 30%;

            text-align: left;

            margin-right: 5px;

        }

        header nav ul {

            list-style: none;

            float: right;

        }

        nav ul li {

            margin-top: 55px;

            float: left;

            color: #D19D09;

            font-size: 16px;

            text-align: center;

            margin-left: 30px;

            letter-spacing: 0px;

            font-weight: bold;

            transition: all 1.3s linear;

        }

        ul li a {

            color: #D19D09;

            text-decoration: none;

        }

        ul li:hover a {

            color: #2C9AB7;

        }

        .hero_header {

            color: #FFFFFF;

            text-align: center;

            margin-top: 0px;

            margin-right: 0px;

            margin-bottom: 0px;

            margin-left: 0px;

            letter-spacing: 0px;

        }

        /* Hero Section */

        .hero {

            background-color: #B3B3B3;

            padding-top: 150px;

            padding-bottom: 150px;

        }

        .light {

            font-weight: bold;

            color: #717070;

        }

        .tagline {

            text-align: right;

            color: #FFFFFF;

            margin-top: 4px;

            font-weight: lighter;

            text-transform: uppercase;

            letter-spacing: 1px;

        }

        </style>
        </html>



        
        '''