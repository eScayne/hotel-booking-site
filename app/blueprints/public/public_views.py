from flask import render_template, redirect, url_for

from . import public_bp

@public_bp.route('/')
def index():
    return render_template('landing_page.html')


@public_bp.route('/rooms')
def rooms():
    return render_template('/pages/room.html')

@public_bp.route('/about')
def about():
    return render_template('/pages/about.html')

@public_bp.route('/contact')
def contact():
    return render_template('/pages/contact.html')