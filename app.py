import os
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
import easyocr
from ar_corrector.corrector import Corrector
import re
import cv2 
corr = Corrector()




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
            text = '</br>\n'.join(map(lambda x: x[1], parsed))
                     # handle file upload
        return(corr.contextual_correct(text)) 
                        
    return '''
    <!doctype html>
<html>
<head>
<meta charset="UTF-8">
<title>Reesha</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cairo&display=swap" rel="stylesheet">
</head>

<body>
    <!-- Main Container -->
<div class="container"> 
  <!-- Navigation -->
  <header> 
      <a class="logo" href="#"><img id="logo" src="http://drive.google.com/uc?export=view&id=1hhZHroXYFpA5iPZiIuDhr1p6Edv9xdz0" style="width: 190px; height: 90px;"></a>
   
    <nav>
      <ul>
        <li><a href="#hero">عن ريشة </a></li>
        <li><a href="#about">الرئيسية </a></li>
      </ul>
    </nav>
  </header>
    
<!-- Hero Section -->
  <section class="hero" id="hero">
      <a class="hero_header" href="#"><img id="hero_header" src="http://drive.google.com/uc?export=view&id=1puFmUToMb3Kau5gQUKc5HukHSzoYy6sn" style=" margin-top: -100px; width: 650px; height: 500px;"></a>
    <p class="tagline"> .. أهلاً بك في المصحح العربي<br><strong>ريشة</strong> </p>
   </section>

  <!-- About Section -->
    
      <!-- About Section -->
  <section class="footer_banner" id="contact">
      
<article class="text_column" style="margin-top: -28px; margin-right: 50px;">
    <p style="text-align: right;"> تحب الكتابة والإملاء؟ ممتاز! <br>:  اختر صورة لكلمة بخط يدك لتقوم ريشة بتصحيحها </p>
       <form method="post" enctype="multipart/form-data" style="text-align: right;">
            <input type="file" name="file" style="text-align: right;"> 
            <input class="button" type="submit" value="تصحيح" style="margin-top: 30px;"> 
            </form>
          </article>
    
    <h2 class="about" id="about" style="margin-top:220px; text-align: center;"> .. عن ريشة</h2>
     <p style="text-align: center;">ريشة منصة تفاعلية وجذابة تهدف إلى تحسين المهارات الاملائية للطلاب وخاصة<br> 
        طلاب وطالبات الصفوف الأولية وتساعد في تحفيز الطلاب وتخفيف العبء على <br>
        . المعلمين وأولياء الأمور
     </p>
  </section>
  <!-- Copyrights Section -->
  <div class="copyright">&copy;2022- <strong>Reesha</strong></div>
</div>
<!-- Main Container Ends -->
</body>
    <style>
    body {
    font-family: 'Cairo', sans-serif;
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
    height: 1300px;
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
    margin: 160px;
    border-radius: 5%;
    color: #fff;
    font-weight: bold;
    text-align: undefined;
    width: 10%;
    float: right;
    margin-top: 19px;
    margin-left: 30px;
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
    margin-top: 70px;
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
    color: #C44B0E;
}
.hero_header {
    color: #FFFFFF;
    text-align: center;
    margin-top: 100px;
    margin-right: 0px;
    margin-bottom: 0px;
    margin-left: 0px;
    letter-spacing: 0px;
}
/* Hero Section */
.hero {
    background-color: #ffffff;
    margin-top: -100px;
    padding-top: 180px;
    padding-bottom: 150px;
}
.light {
    font-weight: bold;
    color: #717070;
}
.tagline {
    text-align: right;
    color: #C44B0E;
    font-size: 25px;
    margin-top: -260px;
    margin-right: 150px;
    font-weight: lighter;
    text-transform: uppercase;
    letter-spacing: 1px;
}
/* About Section */
.text_column {
    margin-top: -12px;
    text-align: center;
    font-weight: lighter;
    line-height: 30px;
    float: unset;
    padding-left: 110px;
    padding-right: 130px;
    margin-right: 50%;
    display: block;
}
.about {
    padding-left: 200px;
    padding-right: 200px;
    padding-top: 0px;
    display: inline-block;
    color: #D19D09;
    margin-top: 0px;
}
/* Stats Gallery */
.stats {
    color: #717070;
    margin-bottom: 5px;
}
.gallery {
    clear: both;
    display: inline-block;
    width: 100%;
    background-color: #FFFFFF;
    /* [disabled]min-width: 400px;
*/
    padding-bottom: 35px;
    padding-top: 0px;
    margin-top: -5px;
    margin-bottom: 0px;
}
.thumbnail {
    width: 25%;
    text-align: center;
    float: left;
    margin-top: 35px;
}
.gallery .thumbnail h4 {
    margin-top: 5px;
    margin-right: 5px;
    margin-bottom: 5px;
    margin-left: 5px;
    color: #52BAD5;
}
.gallery .thumbnail p {
    margin-top: 0px;
    margin-right: 0px;
    margin-bottom: 0px;
    margin-left: 0px;
    color: #A3A3A3;
}
/* Parallax Section */
.banner {
    background-color: #2D9AB7;
    background-image: url(../images/parallax.png);
    height: 400px;
    background-attachment: fixed;
    background-size: cover;
    background-repeat: no-repeat;
}
.parallax {
    color: #FFFFFF;
    text-align: right;
    padding-right: 100px;
    padding-top: 110px;
    letter-spacing: 2px;
    margin-top: 0px;
}
.parallax_description {
    color: #FFFFFF;
    text-align: right;
    padding-right: 100px;
    width: 30%;
    float: right;
    font-weight: lighter;
    line-height: 23px;
    margin-top: 0px;
    margin-right: 0px;
    margin-bottom: 0px;
    margin-left: 0px;
}
/* More info */
footer {
    background-color: #FFFFFF;
    padding-bottom: 35px;
}
.footer_column {
    width: 50%;
    text-align: center;
    padding-top: 0px;

}
footer .footer_column h3 {
    color: #D19D09;
    text-align: center;
}
footer .footer_column p {
    color: #717070;
    background-color: #FFFFFF;
}
.cards {
    width: 100%;
    height: auto;
    max-width: 400px;
    max-height: 200px;
}
footer .footer_column p {
    padding-left: 30px;
    padding-right: 30px;
    text-align: justify;
    line-height: 25px;
    font-weight: lighter;
    margin-left: 20px;
    margin-right: 20px;
}
.button {
    width: 200px;
    margin-top: 40px;
    margin-right: auto;
    margin-bottom: -50px;
    margin-left: auto;
    padding-top: 20px;
    padding-right: 10px;
    padding-bottom: 20px;
    padding-left: 10px;
    text-align: center;
    vertical-align: middle;
    border-radius: 0px;
    text-transform: uppercase;
    font-weight: bold;
    letter-spacing: 2px;
    border: 3px solid #FFFFFF;
    color: #C44B0E;
    transition: all 0.3s linear;
    font-family: 'Cairo', sans-serif;
}
.button:hover {
    background-color: #D19D09;
    color: #FFFFFF;
    cursor: pointer;
}
.copyright {
    text-align: center;
    padding-top: 20px;
    padding-bottom: 20px;
    background-color: #D19D09;
    color: #FFFFFF;
    text-transform: uppercase;
    font-weight: lighter;
    letter-spacing: 2px;
    border-top-width: 2px;
}
.footer_banner {
    text-align: center;
    background-color: #FFFFFF;
    padding-top: 60px;
    padding-bottom: 70PX;
    margin-bottom: 10px;
    background-image: url(../images/pattern.png);
    background-repeat: repeat;
}
footer {
    display: inline-block;
}
.hidden {
    display: none;
}

.center{
    text-align: center;
}
    </style>
</html>

        
        '''
