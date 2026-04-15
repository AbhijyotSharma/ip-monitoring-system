from flask import Blueprint, render_template, request, jsonify
from .services import get_ip_info

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/lookup', methods=['POST'])
def lookup():
    data = request.get_json()
    ip = data.get('ip')

    result = get_ip_info(ip)
    return jsonify(result)
