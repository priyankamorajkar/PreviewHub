# PreviewHub

PreviewHub is a responsive demo-hosting platform that showcases live web applications, focusing on secure access, real-time scraping, and modern full-stack integration. It lets users interact with working prototypes—especially the Secure Data Portal—directly in the browser without local setup.

---

## Features
- Secure OAuth 2.0 login (Google)
- Live web scraping via Python backend (Hacker News headlines)
- Real-time data refresh with clear loading states
- Responsive data display
- Frontend–backend integration
- Mobile-friendly UI with Tailwind CSS

---

## Technologies
- ReactJS, Tailwind CSS, JavaScript
- Python, Flask, BeautifulSoup, Requests
- Gunicorn (production server)

---

## Deployment
Live project link:
https://priyankamorajkar.in/PreviewHub/

---

## Installation

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/priyankamorajkar/PreviewHub.git
   cd pre-food

2. Backend (Python API):

   ```bash
   cd backend
   pip install -r requirements.txt
   gunicorn --bind 0.0.0.0:8080 app:app


3. Backend runs at:
   ```bash
   https://previewhub-backend.onrender.com


5. Frontend (React App):
    ```bash
    cd ../frontend
    npm install


6. Create a .env file in the frontend:
   ```bash
   VITE_GOOGLE_CLIENT_ID="YOUR_OAUTH_CLIENT_ID"
   VITE_BACKEND_API_URL="xyz"

7. Run the frontend:
   ```bash
   npm run dev

---

## Example
OAuth Login Page  Scraped Data Display
Real-Time Refresh  Responsive Mobile View

---

## Notes
Use valid API URLs for backend communication.
Designed for desktop and mobile through responsive layout.
Easily extendable to include more demos or secured tools.

---

## License
This project is licensed under the MIT License.

---

## Author: Priyanka Morajkar
Contact:
Priyanka Morajkar - priyankamorajkar291@gmail.com
Linkedin - https://www.linkedin.com/in/priyankamorajkar/
Project Link: https://priyankamorajkar.in/PreviewHub/
