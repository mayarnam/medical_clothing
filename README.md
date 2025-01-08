# medical_clothing
## Description
medical_clothing est une application conçue pour gérer et vendre des vêtements médicaux (comme des blouses, des tenues d’infirmiers, etc.). Elle vise à faciliter la gestion des stocks et des commandes.
## Installation

1. Clone le dépôt GitHub :
   ```bash
   git clone https://github.com/mayarnam/medical_clothing.git
  ## Utilisation

Une fois que l’application est lancée :
- Connecte-toi avec ton compte administrateur.
- Ajoute des produits (vêtements médicaux) dans le stock.
- Gère les commandes et les ventes via l’interface.
## Technologies Used

- Frontend: React.js
- Backend: Node.js, Express, Django
- Database: MongoDB
- Programming Languages: Python, JavaScript
- ## Screenshots
- ![Dashboard]![Capture d'écran 2025-01-08 190537](https://github.com/user-attachments/assets/0445e1b8-25c8-4ba7-ad40-09478909024a)![Capture d'écran 2025-01-08 190609](https://github.com/user-attachments/assets/b04d4c12-62a7-472c-9653-a7eeaf1d53ac)
- ## How to Create and Set Up the Project
### Step 1: Clone the Repository

1. Open the terminal (or Git Bash).
2. Run the following command to clone the repository:
   ```bash
   git clone https://github.com/mayarnam/medical_clothing.git
- ### Step 2:Set Up the Backend (Django)
- Create a virtual environment python -m venv env
- Activate the virtual environment:env\Scripts\activate
- Set up the database:python manage.py migrate
- Create superuser for Django (for admin access):python manage.py createsuperuser
- Start the Django development server:python manage.py runserver
  ### Project Structure
  medical_clothing/
│
├── backend/                   # Contains the backend code (Django)
│   ├── store/                  # Django app for the store logic
│   │   ├── models.py           # Django models for products and orders
│   │   ├── views.py            # Django views for handling requests
│   │   ├── urls.py             # API routes for the store app
│   │   └── migrations/         # Database migrations
│   ├── manage.py               # Django management file
│   └── requirements.txt        # Python dependencies for Django
│
├── frontend/                  # Contains the frontend code (React.js)
│   ├── src/
│   │   ├── components/         # React components for various parts of the UI
│   │   ├── pages/              # React pages (views)
│   │   ├── App.js              # Main React component
│   │   └── index.js            # React entry point
│
├── .gitignore                 # Git ignore file
├── README.md                  # Project description and setup instructions
└── package.json               # Node.js package manager file











