# A restaurant project
# A restaurant project
# 🍽️ Django Restaurant Project

A dynamic **restaurant web application** built with **Django, Python, HTML, CSS, Bootstrap, and SQLite**.  
The app allows users to browse categorized menus, add items to cart, choose payment method, book tables, and receive **order confirmation emails**.  
It features a **modern dark-themed UI** with stylish order receipts and session-based cart management.  

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🚀 Features

- 📋 **Menu Browsing** – Categorized food and drink items.
- 🛒 **Cart System** – Add/remove items, update quantity.
- 💳 **Payments** – COD (Cash on Delivery) / UPI / Razorpay integration.
- 🍽️ **Table Booking** – Reserve tables online.
- 📧 **Email Notifications** – Order confirmation via Gmail SMTP.
- 🧾 **Receipt Generation** – Stylish order invoice/receipt with details.
- 🎨 **Dark Themed UI** – Modern, sleek, and responsive design.
- 🔒 **Session-based Cart Management** – Works without login.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🤖 **Chatbot Integration**

This project includes a built-in AI-powered chatbot to assist users.

✨ **Chatbot Features**

💬 Small Talk – Greets users and responds to casual messages (hi, hello, thanks).

📋 FAQs Support – Instantly answers common queries about menu, timings, location, booking, offers, and delivery.

📍 Context-Aware – Detects phrases like "where are you located?" or "how do I book a table?".

🎨 UI Integration – Chatbot opens in a floating widget on the website with smooth toggle.

⌨️ Typing Indicator – Shows “Bot is typing…” animation for a realistic experience.

⚙️ **How It Works**

Frontend: JavaScript handles chat window, typing effect, and message rendering.

Backend: Django view (chatbot_reply) processes user queries and returns a JSON response.

Responses: Predefined FAQs + fuzzy matching + regex detection.

**Example**:

You: menu  
Bot: Our menu includes Pizza, Burger, Pasta, Garlic Bread, Fries, Wraps and Momos.  
     👉 <a href="/menu/" target="_blank" style="color: brown; text-decoration: underline;">View Menu</a>
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Django (Python)
- **Database:** SQLite
- **Payment Gateway:** Razorpay (UPI/Cards/COD)
- **Email Service:** Gmail SMTP

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 📂 Project Structure

restaurant_project/
│
├── restaurant/ # Main app
│ ├── templates/ # HTML templates
│ ├── static/ # CSS, JS, images
│ ├── models.py # Database models
│ ├── views.py # Application logic
│ ├── urls.py # URL routing
│
├── manage.py
├── requirements.txt
├── README.md

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## ⚙️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/restaurant_project.git
   cd restaurant_project

2. Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Run migrations:
python manage.py migrate

5. Start development server:
python manage.py runserver

6. Open in browser:
http://127.0.0.1:8000/
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

💳 Payment Integration

Integrated with Razorpay for secure payments.

COD (Cash on Delivery) also supported.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📧 Email Notifications

Integrated Gmail SMTP for sending order confirmations.

Requires an App Password (if using Gmail).

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
👩‍💻 Author
Shruti Bhalerao
📍 Mumbai, India
💼 Aspiring Python/Django Developer
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

⭐ Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork this repo and submit a pull request.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

📜 License

This project is open-source and available under the MIT License
👉 Shruti, you just need to:  
- **GitHub username: shrutirao123**.  
