from flask import Blueprint, render_template, request, redirect, jsonify
# import dataengine
from helpers import checkpoint
import os, runpy, glob
from settings import cms_version

THEMES = "templates/SYSTEM/"
THEMES_STAT = "static/SYSTEM/"
THEME_DATA = "theme.py"

THEME_STORE = {}
SERVER_STORE = {}

VERIFIED_THEMES = []


editor = Blueprint("editor", __name__)

def verify_theme(theme,theme_pack):

    try:
        if float(cms_version) < float(theme_pack[theme][1]):
            print("Version not compat")
        else:
            for theme_ in os.listdir(THEMES_STAT):
                theme_fold = THEMES_STAT+theme_
                if os.path.isdir(theme_fold):
                    theme_fold_in = runpy.run_path(theme_fold+"/"+THEME_DATA)
                    try:
                        _ = theme_fold_in['linecms_name']
                        _ = theme_fold_in['linecms_compat']
                        _ = theme_fold_in['linecms_info']

                        if theme_ not in VERIFIED_THEMES:
                            if theme_ == theme:
                                VERIFIED_THEMES.append(theme_)
                                THEME_STORE[theme_] = theme_pack
                    except Exception as e:
                        print(e) # not a template file

    except:
        pass

def get_templates():
    for theme_ in os.listdir(THEMES):
        theme_fold = THEMES+theme_
        if os.path.isdir(theme_fold):
            theme_fold_in = runpy.run_path(theme_fold+"/"+THEME_DATA)
            try:
                t_data = {theme_:[theme_fold_in['linecms_name'],theme_fold_in['linecms_compat'],theme_fold_in['linecms_info']]}
                verify_theme(theme_,t_data)
            except:
                pass # not a template file
    return THEME_STORE

def get_robotssitemap():
    pass

def get_enginepublic():
    files = glob.glob("enginepublic/*py")
    for py in files:
        spl = py.split("/")
        SERVER_STORE[spl[1]] = spl

    return SERVER_STORE.keys()

@editor.route("/edit",methods=['GET','POST'])
@checkpoint.onlylogged
def codeedit():
    templates = get_templates()
    sfiles = get_enginepublic()

    if request.method == "POST":
        pass
    
    return render_template("/dashboard/editor.html",templates=templates,serverfiles=list(sfiles))