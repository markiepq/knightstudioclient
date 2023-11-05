from flask import Blueprint, render_template, request, redirect, g, session, jsonify
import dataengine
from flask_paginate import Pagination, get_page_parameter
import json
from icecream import ic
from helpers import emailparser, combine
from ast import literal_eval as lite
import time

api = Blueprint("api", __name__)
version = "1.4"

def epoch():
    return time.time()

@api.route("/api/product-fulfill", methods=['POST'])
def prodfulfill():
    try:
        if (request.data):
            _d = json.loads(request.data)
            _de = dataengine.knightclient()
            _load_h = _de.orderhistory_get(_d['ordernumber'])
            sk, pk, ck, _, wk, wsk,shipstatus,shiprates,shipcountries,_,_,_,_,_,_ = _de.productsettings_get() # wk is not needed
            temp_settings = _de.productsettings_get()
            comp_data = _de.load_data_index(0)
            _order = _de.productorders_single_get(0,_d['ordernumber'])
            history = False
            
            if _order:
                _order = combine.zipper("orders",_order)
                
            try:
                history = lite(_load_h[0])
            except Exception as e:
                history = {}

            # data = {"ordernumber":orn,"tracking":trv,"addition":adv,"template":""}
            if _de.orderfulfill(_d):
                # Load required
                
                # Load required
                shipstatus = False
                if shipstatus == "on":
                    shipstatus = True
                

                
                sendmailer = False
                history_obj = history
                history_obj[5] = {"title":"No Notification sent","message":"Disabled in 'Placed template' settings or Mail configuration","timestamp":epoch()}
                try:
                    _set = lite(temp_settings[12])['fulfilled']
                    if int(_set):
                        emailparser.parse_send(which="fulfilled",ps=temp_settings,order=_order,company=comp_data,shipstatus=shipstatus,template=_d['template'])
                        history_obj[5] = {"title":"Customer Notified","message":"Email sent to customer with order details","timestamp":epoch()}
                except Exception as e:
                    print("Error, ",e)
                    history_obj[5] = {"title":"No Notification sent","message":"Disabled in Placed template settings or Mail configuration","timestamp":epoch()}

                history_obj[4] = {"title":"Order Fulfilled","message":"This order is now on archived as its mark as completed","timestamp":epoch()}
                args = {"obj":history_obj,"ordernumber":_d['ordernumber']}
                _de.orderhistory_add(args)
            
                return jsonify({"status": 1,"message":"Order fulfilled","obj":{}})
            
            return jsonify({"status": 0,"message":"Unable to fulfill"})
    except Exception as r:
        return jsonify({"status": 0,"message":"Request error, Unable to fulfill"})

        

@api.route("/api/prodset-smtp", methods=['POST', 'GET'])
def prodset_smtp():
    try:
        if (request.data):
            _d = json.loads(request.data)
            _de = dataengine.knightclient()
            if _de.productsettings_smtp(_d):
                return jsonify({"status": 1,"message":"SMTP Credentials updated"})
            return jsonify({"status": 0,"message":"Unable to update"})
    except:
        return jsonify({"status": 0,"message":"Settings unable to update"})


@api.route("/api/prodset-temp", methods=['POST', 'GET'])
def prodset_template():
    try:
        if (request.data):
            _d = json.loads(request.data)
            _de = dataengine.knightclient()
            if _de.productsettings_temp(_d):
                return jsonify({"status": 1,"message":"Order templates updated"})
            return jsonify({"status": 0,"message":"Unable to update"})
    except:
        return jsonify({"status": 0,"message":"Settings unable to update"})


@api.route("/api/prodset-str", methods=['POST', 'GET'])
def prodset_stripe():
    try:
        if (request.data):
            _d = json.loads(request.data)
            _de = dataengine.knightclient()
            if _de.productsettings_str(_d):
                return jsonify({"status": 1,"message":"Shipping options updated"})
            return jsonify({"status": 0,"message":"Unable to update"})
    except:
        return jsonify({"status": 0,"message":"Settings unable to update"})


@api.route("/api/prodset-ship", methods=['POST', 'GET'])
def prodset_ship():
    try:
        if (request.data):
            _d = json.loads(request.data)
            _de = dataengine.knightclient()
            if _de.productsettings_ship(_d):
                return jsonify({"status": 1,"message":"Shipping options updated"})
            return jsonify({"status": 0,"message":"Unable to update"})
    except:
        return jsonify({"status": 0,"message":"Settings unable to update"})


@api.route("/api/themeset", methods=['POST', 'GET'])
def themeup():
    if (request.data):
        _d = json.loads(request.data)
        _de = dataengine.knightclient()
        if _de.themeset(_d['set']):
            return jsonify({"status": 1})
        return jsonify({"status": 0})
    return jsonify({"status": 0})


@api.route("/product-update", methods=['POST', 'GET'])
def productupd():
    _d = json.loads(request.data)
    _de = dataengine.knightclient()
    if _d['id']:
        rs = _de.product_update(_d)
        if rs:
            return jsonify({"status": 1, "url": rs})
        return jsonify({"status": 0})
    return jsonify({"status": 0})


@api.route("/product-d", methods=['POST', 'GET'])
def productdel():
    _d = json.loads(request.data)
    _de = dataengine.knightclient()
    if _d['id']:
        rs = _de.delete_pr(_d['id'])
        if rs:
            return jsonify({"status": 1, "url": rs})
        return jsonify({"status": 0})
    return jsonify({"status": 0})


@api.route("/product-publish", methods=['POST', 'GET'])
def productpub():
    _d = json.loads(request.data)
    _de = dataengine.knightclient()

    if _d['id']:
        rs = _de.product_publish(_d)
        if rs:
            return jsonify({"status": 1, "url": rs})
        return jsonify({"status": 0})
    return jsonify({"status": 0})


@api.route("/module_update", methods=['POST', 'GET'])
def modupdate():
    if request.method == "POST":
        if 'authenticated' in session:  # Logged in
            de = dataengine.knightclient()
            if (de.update_module(request.data)):
                return jsonify({'status': True})
            return jsonify({'status': False})
        return "KnightStudio Dashboard build ", version
    else:
        return "KnightStudio Dashboard build ", version


@api.route("/knightclientapi", methods=['POST', 'GET'])
def knightapi():
    if request.method == "POST":
        if 'authenticated' in session:  # Logged in
            d = dataengine.knightclient()
            if (d.knightclientapi(eval(request.data)['action'])):
                return jsonify({'status': True})
            return jsonify({'status': False})
        return "KnightStudio Dashboard build ", version
    else:
        return "KnightStudio Dashboard build ", version


@api.route("/deleapip", methods=['POST', 'GET'])
def delete_apip():
    if request.method == "POST":
        if 'authenticated' in session:  # Logged in
            table = request.json['table']
            column = request.json['column']
            value = request.json['value']
            de = dataengine.knightclient()
            if (de.delete_apip(table, column, value)):
                return jsonify({"status": 1, "message": "Blog post has been deleted"})
            return jsonify({"status": 0, "message": "Blog post cannot delete right now"})
    else:
        return jsonify({"status": 0})


@api.route("/deleapi", methods=['POST', 'GET'])
def delete_api():
    if request.method == "POST":
        if 'authenticated' in session:  # Logged in
            table = request.json['table']
            column = request.json['column']
            value = request.json['value']
            de = dataengine.knightclient()
            if (de.delete_api(table, column, value)):
                return jsonify({"status": 1, "message": "Blog post has been deleted"})
            return jsonify({"status": 0, "message": "Blog post cannot delete right now"})
    else:
        return jsonify({"status": 0})


@api.route("/knightclientapiv2", methods=['POST', 'GET'])
def knightapi2():
    if request.method == "POST":
        if 'authenticated' in session:  # Logged in
            d = dataengine.knightclient()
            if (d.knightclientapiv2(eval(request.data))):
                return jsonify({'status': True})
            return jsonify({'status': False})
        return "KnightStudio Dashboard build ", version
    else:
        return "KnightStudio Dashboard build ", version


@api.route("/api/delpartialim", methods=['POST', 'GET'])
def api_deletepartialimage():
    if request.method == "POST":
        if 'authenticated' in session:  # Logged in
            d = dataengine.knightclient()
            d.delete_image_partial(eval(request.data))
        return "KnightStudio Dashboard build ", version
    else:
        return "KnightStudio Dashboard build ", version


@api.route("/delete/<table>/<id>")
def delete(table, id):
    mid = id
    if 'authenticated' in session:
        d = dataengine.knightclient()
        if d.delete(table, id):
            return jsonify({"status": True})
        return jsonify("status", False)
    return jsonify({"status": False})
