from flask import Blueprint, jsonify, request
from services.scraper import scrape_mutual_fund_data, analyze_mutual_fund, get_market_news_and_sentiment

data_blueprint = Blueprint('data', __name__)

@data_blueprint.route('/api/funds', methods=['POST'])
def get_mutual_funds():
    id = request.json.get('id')
    if not id:
        return jsonify({'error': 'No ID provided'}), 400
    data = scrape_mutual_fund_data(id)
    if data:
        return jsonify(data), 200
    else:
        return jsonify({'error': 'Fund not found'}), 404

@data_blueprint.route('/api/funds/analysis', methods=['POST'])
def get_fund_analysis():
    id = request.json.get('id')
    if not id:
        return jsonify({'error': 'No ID provided'}), 400
    analysis = analyze_mutual_fund(id)
    if analysis:
        return jsonify(analysis), 200
    else:
        return jsonify({'error': 'Analysis not available'}), 404

@data_blueprint.route('/api/news', methods=['GET'])
def get_news():
    tickers = request.args.get('tickers')
    time_from = request.args.get('time_from')
    time_to = request.args.get('time_to')
    sort = request.args.get('sort', 'LATEST')
    limit = request.args.get('limit', 50)
    
    news_data = get_market_news_and_sentiment(
        tickers=tickers, 
        time_from=time_from, 
        time_to=time_to, 
        sort=sort, 
        limit=limit
    )
    
    if news_data:
        return jsonify(news_data), 200
    else:
        return jsonify({'error': 'Failed to retrieve news data'}), 404