import google.generativeai as genai
import os


# Configure Gemini with key from .env
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def generate_email_reminder(patient_name,doctor_name, appointment_time):
    prompt = f"""
    Write a short friendly email reminder for patient {patient_name}.
    at Ethi-Care clinic located at Shiro meda addis ababa Their appointment is scheduled for {appointment_time} with {doctor_name}.
    Keep it polite and professional.
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text.strip()