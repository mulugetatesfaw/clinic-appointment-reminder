1. Installation & Setup

   Clone the repository

   git clone https://github.com/mulugetatesfaw/clinic-appointment-reminder.git
 
   go to the project directory
   
   cd clinic-appointment-reminder

3. Create a virtual environment
   python3 -m venv venv
4. Activate the virtual environment
  source venv/bin/activate
5. Install dependencies
   pip install -r requirements.txt

6. Navigate to the core directory
    cd core
7. Create a .env file

   
   GEMINI_API_KEY=your_api_key_here
   
   EMAIL_HOST_USER=your_email@example.com
   
   EMAIL_HOST_PASSWORD=your_app_password_here
   
9. Run the Django server
    python manage.py runserver
    
10. Access the project
     Open your browser and go to
   👉 http://127.0.0.1:8000/

12. Create a superuser (for Django Admin access)

      python manage.py createsuperuser

    Open the Django admin panel 👉 http://127.0.0.1:8000/admin

    Log in with the superuser credentials you created.
    
🗓 Scheduling an Appointment & Receiving Reminder

    Log in to the Django Admin Panel.

    Go to Appointments and create a new appointment with 3 minutes above from the time now and expect email before 3 minutes from your appointment time: for test purpose i set it 3 minute

    Patient details

    Date & time of appointment

    Any other required fields

    The system will send a reminder email to your email account configured in .env (EMAIL_HOST_USER).

   Check your inbox to confirm you received the reminder email.





