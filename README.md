StudyBuddy
StudyBuddy is a Discord-like application designed for students to collaborate and share knowledge in a structured and organized environment. Built with Django, HTML, CSS, JavaScript, and SQLite, StudyBuddy allows users to create, manage, and engage in topic-specific rooms, making it an ideal platform for academic discussions.

Features
Room Creation & Management: Users can create and delete rooms based on different topics, such as AI, web development, and more.
Latest Messages Display: The home page showcases the most recent messages from all rooms, providing a quick overview of ongoing discussions.
Topic-Specific Categorization: Rooms are categorized under relevant topics, making it easy for students to find and join discussions that interest them.
User Authentication: A robust authentication system ensures secure access, allowing users to sign up, log in, and manage their accounts.
Technologies Used
Backend: Django
Frontend: HTML, CSS, JavaScript
Database: SQLite
Authentication: Django's built-in authentication system
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/yourusername/studybuddy.git
Navigate to the project directory:
bash
Copy code
cd studybuddy
Install dependencies:
bash
Copy code
pip install -r requirements.txt
Apply migrations:
bash
Copy code
python manage.py migrate
Run the development server:
bash
Copy code
python manage.py runserver
Usage
After starting the server, open your web browser and go to http://localhost:8000/.
Create an account or log in if you already have one.
Start creating rooms under various topics, or join existing ones to participate in discussions.
View the latest messages on the home page and stay updated with ongoing conversations.
