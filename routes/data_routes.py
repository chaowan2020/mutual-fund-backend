from flask import Blueprint, jsonify
from services.scraper import scrape_mutual_fund_data

data_blueprint = Blueprint('data', __name__)

@data_blueprint.route('/api/mutual-funds', methods=['GET'])
def get_mutual_funds():
    data = scrape_mutual_fund_data()
    return jsonify(data)