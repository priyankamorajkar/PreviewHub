from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "https://priyankamorajkar.in"}}) 
PORT = 5000

def scrape_data(url="https://news.ycombinator.com/"):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
    
        items = []
        rows = soup.find_all('tr', class_='athing', limit=10)
        
        for index, row in enumerate(rows):
            title_tag = row.find('span', class_='titleline').find('a')            
            title = title_tag.get_text(strip=True) if title_tag else "No Title"
            link = title_tag['href'] if title_tag and 'href' in title_tag.attrs else "#"
            
            items.append({
                'id': index + 1,
                'title': title,
                'link': link,
            })
            
        return items

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return [] 
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

#API Endpointsi

@app.route('/api/scrape', methods=['GET'])
def get_scraped_data():
    scraped_items = scrape_data()
    
    if scraped_items:
        return jsonify({
            "status": "success",
            "message": "Data fetched successfully from target site.",
            "data": scraped_items
        }), 200
    else:
        return jsonify({
            "status": "error",
            "message": "Failed to scrape data. Check backend logs."
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        "status": "ok",
        "service": "Preview Hub Backend API"
    }), 200

if __name__ == '__main__':
    print(f"Running Flask API on http://127.0.0.1:{PORT} ---")

    app.run(port=PORT, debug=True)

