# IT Asset Management System

## Overview
This is a Django-based IT Asset Management System that allows users to track IT assets, including serial numbers, software licenses, and maintenance schedules.

## Features
- Add and manage IT assets
- Track software licenses
- Schedule maintenance for assets
- Edit existing assets
- Delete assets

## Screenshots

<div style="display: flex; justify-content: center; gap: 10px;">
  <img src="./screenshots/screenshot1.png" alt="Screenshot 1" width="50%">
  <img src="./screenshots/screenshot2.png" alt="Screenshot 2" width="50%">
</div>

<div style="display: flex; justify-content: center; gap: 10px; margin-top: 10px;" >
  <img src="./screenshots/screenshot3.png" alt="Screenshot 3" width="50%">
  <img src="./screenshots/screenshot4.png" alt="Screenshot 4" width="50%">
</div>

## Requirements
- Python 3.x
- Django 5.x or higher
- SQLite3 

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd it_asset_management
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations to set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

   After starting the server, you can access the application by navigating to `http://127.0.0.1:8000/assets/` in your web browser.

## Usage
- Navigate to `http://127.0.0.1:8000/assets/` to view and manage IT assets.
- You can add new assets, edit existing ones, and delete assets as needed.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 