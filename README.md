
# Building a RESTful API with Flask

Error
Handling, Authentication, and File Handling with Public and Admin
Routes. 


Team Members :  Shwetank Singh (CWID:813968286) & Mahitha Pasupuleti (CWID:867114134)

[Project Video](https://www.loom.com/share/7fd694784a174b28b34be62818e60d92?sid=e64f9595-61e2-4641-ade2-a41e589b3a4a) | [Download Video](https://drive.google.com/file/d/1aw3eTV4IROVjYGDRwJvKVML7ZReBypRi/view?usp=sharing)



## Installation

Prerequisites
Make sure you have the following installed on your machine:
- Python 3.x
- Flask
- A SQL database (e.g., MySQL, PostgreSQL, SQLite)



    
## Setup

1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/repository-name.git
cd repository-name
```

2. Configure the Database URI
- Open the config.py file & env.py.
- Update the SQLALCHEMY_DATABASE_URI variable with the correct database connection string for your SQL database.


3. Set Up a Virtual Environment
Create and activate a virtual environment to manage your dependencies:
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

4. Install Requirements
Install the necessary packages:
```bash
pip install -r requirements.txt
```

5. Start the SQL Server
Make sure your SQL server is running. The steps depend on the database you're using. For example:
- MySQL: Start MySQL server using your system's service manager.


6. Run Migrations
Run the following commands to handle the database migrations:
```bash
# Initialize the migration repository
flask db init

# Generate migration scripts
flask db migrate -m "Initial migration"

# Apply migrations to the database
flask db upgrade
```

7. Start the Flask Application
Finally, start the Flask application:
```bash
flask run / python app.py
```
Visit Postman to start testing the endpoints!



<img width="400" alt="Endpoints" src="https://github.com/user-attachments/assets/07efb0c8-3323-4c3d-9ab4-bc5e07c7bb8b">


Additional Notes
- Ensure you have your environment variables set up, especially for any sensitive information like API keys or secret tokens.
- Check the config.py file for additional configuration options.


