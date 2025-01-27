from flask import Flask, jsonify
from scrape_data_selenium import scrape_data_with_selenium

app = Flask(__name__)

@app.route('/scrape', methods=['GET'])
def get_scraped_data():
    try:
        # Scrape data
        data = scrape_data_with_selenium()  # Call the correct function
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": "Failed to scrape data", "details": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
