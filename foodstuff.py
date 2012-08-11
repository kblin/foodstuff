#!/usr/bin/env python
# FoodStuff - Manage recipes, plan meals and organize shopping
# Copyright (C) 2012  Kai Blin <kai.blin@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from os import path
from flask import Flask, render_template, request, jsonify, after_this_request
from flask import send_from_directory

app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recipes')
def recipes():
    return "Recipes"

@app.route('/recipe/<int:rid>')
def recipe(rid):
    return "This is recipe %s" % rid

@app.route('/ingredients')
def ingredients():
    return "Ingredients"

@app.route('/shopping')
def shopping():
    return "Shopping list"

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype="image/vnd.microsoft.icon")

if __name__ == '__main__':
    app.run(debug=True)
