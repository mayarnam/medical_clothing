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
  ### usage
  1. start the server :
  python manage.py runserver
  2. access the application at:
     http://127.0.0.1:8000/
  admin portal: http://127.0.0.1:8000/admin/
  
  ### Project Structure
 medical_clothing/
│
├── backend/                        # Contains the backend code (Django)
│   ├── store/                       # Django app for store logic
│   │   ├── migrations/              # Database migration files
│   │   ├── models.py                # Models for storing product details (e.g., medical clothing, prices)
│   │   ├── views.py                 # Views for handling requests related to products, categories, and orders
│   │   ├── urls.py                  # URL routing for the store (e.g., to view products, categories)
│   │   ├── serializers.py           # Serializers for data representation (e.g., converting data to JSON)
│   │   ├── admin.py                 # Admin interface setup for managing products, categories
│   │   ├── templates/               # HTML templates for rendering pages
│   │   │   ├── index.html           # Home page template
│   │   │   ├── product_detail.html  # Template to display product details
│   │   │   ├── product_list.html    # Template to display the list of products
│   │   │   └── cart.html            # Template for shopping cart page
│   ├── manage.py                    # Django management file (to handle migrations, testing, etc.)
│   ├── settings.py                  # Django project settings, including database setup, installed apps
│   └── requirements.txt             # Python dependencies required for the backend
│
├── frontend/                       # Contains the frontend code (React.js)
│   ├── public/                      # Static files (e.g., images, favicon)
│   ├── src/                         # React application source code
│   │   ├── components/              # Reusable React components (e.g., ProductList, ProductDetail, Cart, etc.)
│   │   ├── pages/                   # React pages (views) for different sections (e.g., HomePage, ProductPage)
│   │   ├── App.js                   # Main component that holds routing and core structure
│   │   ├── index.js                 # The entry point for React to render the app
│   │   ├── styles/                  # CSS or Styled Components for the UI layout
│   │   ├── api/                     # API functions to fetch data from the backend (e.g., fetching products, categories)
│   ├── package.json                 # Node.js dependencies and configuration for the frontend
│   └── .gitignore                   # Git ignore file for frontend
│
├── .gitignore                      # Git ignore file for the whole project
├── README.md                       # Project documentation with setup and usage instructions
├── requirements.txt                # Project-wide Python dependencies (if any other dependencies are required)
└── docker-compose.yml              # (Optional) Docker configuration to containerize the app (for easy deployment)

## Contributing

We welcome contributions from everyone! If you'd like to help improve this project, follow the steps below to get started.











