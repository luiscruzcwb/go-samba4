# -*- coding: utf-8 -*-


from flask import Blueprint, render_template
from flask import session, current_app, jsonify
from flask import request


from app.model.users import login_required, get_users
from app.model.users import user_delete


mod = Blueprint('users', __name__, url_prefix='/users')


@mod.route('/')
@login_required
def index():
    ls_users = get_users()
    return render_template('users/index_new.html', users=ls_users)


@mod.route('/add/')
@login_required
def add():
    return render_template('users/add_user.html')


@mod.route('/del/', methods=['POST'])
@login_required
def users_del():
    username = request.json['username']
    if username.lower() != session['username'].lower():
        res = user_delete(username)
        if res:
            current_app.cache.clear()
        return jsonify(message=res)
    return jsonify(message="No Deleted User")