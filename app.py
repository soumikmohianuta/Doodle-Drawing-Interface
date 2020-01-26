from __future__ import division
from flask import Flask, render_template, request, url_for,send_from_directory,session,redirect,make_response,jsonify

import os

import StrokeSave
import StrokeParse
import ElementToShow

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'templates/uploads')
STYLESHEETS_FOLDER = os.path.join(APP_ROOT, 'templates','stylesheets')
IMAGES_FOLDER = os.path.join(APP_ROOT, 'templates','images')
FONTS_FOLDER = os.path.join(APP_ROOT, 'templates','fonts')
FONTS_AWESOME_CSS_FOLDER = os.path.join(APP_ROOT, 'templates','font-awesome','css')
FONTS_AWESOME_FONTS_FOLDER = os.path.join(APP_ROOT, 'templates','font-awesome','fonts')
SCRIPTS_FOLDER = os.path.join(APP_ROOT, 'templates','javascripts')
STORAGE_FOLDER = os.path.join(APP_ROOT,'StoreElement')
UI_IMAGES_FOLDER= os.path.join(APP_ROOT, 'PrimaryScreenShots')
TemplateFolder = os.path.join(APP_ROOT, 'templates')

app = Flask(__name__)
app.secret_key = "DrawKey"


# redirect to homepage
@app.route('/')
def form():
    return render_template('homepage.html')



# save the stroke locally
    
@app.route('/DrawSave/', methods=['GET','POST'])
def SaveDraw():
    if request.method == 'POST':
        canvas_strokes = request.form['save_data']
        CURRENT_ELEMENT = session['current_element']
        currentFile = StrokeSave.getFileName(STORAGE_FOLDER, CURRENT_ELEMENT)
        compressStroke = StrokeParse.compressData(canvas_strokes)
        StrokeSave.savelocally(STORAGE_FOLDER, currentFile, compressStroke)  
        return 



@app.route('/uploads/<filename>')
def send_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/stylesheets/<filename>')
def send_css(filename):
    return send_from_directory(STYLESHEETS_FOLDER, filename)

@app.route('/images/<filename>')
def send_img(filename):
    return send_from_directory(IMAGES_FOLDER, filename)

@app.route('/fonts/<filename>')
def send_fonts(filename):
    return send_from_directory(FONTS_FOLDER, filename)

@app.route('/font-awesome/css/<filename>')
def send_fontawscss(filename):
    return send_from_directory(FONTS_AWESOME_CSS_FOLDER, filename)

@app.route('/font-awesome/fonts/<filename>')
def send_fontawsfont(filename):
    return send_from_directory(FONTS_AWESOME_FONTS_FOLDER, filename)
    

@app.route('/NewImage/<filename>')
def send_new_img(filename):

    curelement = ElementToShow.getElementName(UI_IMAGES_FOLDER )   
    session['current_element'] =  curelement
     
    curDrawingName= session['current_element']+ ".png"

    return send_from_directory(UI_IMAGES_FOLDER, curDrawingName)


@app.route('/CurentImage/<filename>')
def send_interval_img(filename):


    curDrawingName=  session['current_element']+ ".png"
      
    return send_from_directory(UI_IMAGES_FOLDER, curDrawingName)

@app.route('/IntervalImage/<filename>')
def send_interval_blur_img(filename):

    newName = "blur.jpg"
    return send_from_directory(IMAGES_FOLDER, newName)
    
@app.route('/javascripts/<filename>')
def send_jss(filename):
    return send_from_directory(SCRIPTS_FOLDER, filename)

@app.route('/doodle/images/<filename>')
def send_fullUI_img(filename):
    return send_from_directory(IMAGES_FOLDER, filename)
if __name__ == "__main__":
    
    app.run(threaded=True)
