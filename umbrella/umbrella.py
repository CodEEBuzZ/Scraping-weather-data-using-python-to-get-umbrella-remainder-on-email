import smtplib
import requests
import time
import os
from plyer import notification  # <-- Import plyer

# --- Load Environment Variables ---
API_KEY = os.environ.get("OPENWEATHER_API_KEY")
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PASS = os.environ.get("SENDER_PASS")
RECEIVER_EMAIL = os.environ.get("RECEIVER_EMAIL")
CITIES_STRING = os.environ.get("CITIES")
# New variable to choose alert type, defaulting to 'email'
ALERT_METHOD = os.environ.get("ALERT_METHOD", "email").lower()


# Check if all required variables are set
if not all([API_KEY, SENDER_EMAIL, SENDER_PASS, RECEIVER_EMAIL, CITIES_STRING]):
    print("❌ Error: Missing one or more environment variables.")
    print("Please set OPENWEATHER_API_KEY, SENDER_EMAIL, SENDER_PASS, RECEIVER_EMAIL, and CITIES.")
    exit()

CITIES_LIST = [city.strip() for city in CITIES_STRING.split(',')]

# --- Weather function ---
# (This function remains exactly the same)
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        condition = data['weather'][0]['main']
        return temp, condition
    else:
        print(f"❌ Error fetching weather for {city}:", response.json().get("message"))
        return None, None

# --- Email function ---
# (This function remains exactly the same)
def send_email(subject, body):
    try:
        smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_object.starttls()
        smtp_object.login(SENDER_EMAIL, SENDER_PASS)
        msg = f"Subject:{subject}\n\n{body}".encode("utf-8")
        smtp_object.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg)
        smtp_object.quit()
        print("✅ Email Sent!")
    except Exception as e:
        print("❌ Email Error:", e)

# --- NEW: Desktop Notification function ---
def send_desktop_notification(title, message):
    try:
        notification.notify(
            title=title,
            message=message,
            app_name="Umbrella Reminder",
            timeout=10  # Notification will stay for 10 seconds
        )
        print("✅ Desktop Notification Sent!")
    except Exception as e:
        print("❌ Desktop Notification Error:", e)

# --- Umbrella Reminder ---
def umbrellaReminder(cities, last_alerts):
    
    for city in cities:
        temp, sky = get_weather(city)

        if not temp or not sky:
            print(f"--- Skipping {city} (could not fetch weather) ---")
            continue

        print(f"📍 {city} | 🌡️ Temp: {temp}°C, Sky: {sky}")
        
        last_alert_for_city = last_alerts.get(city)

        # Check if condition is rainy/cloudy
        if sky in ["Rain", "Rain And Snow", "Showers", "Thunderstorm", "Clouds", "Drizzle"]:
            if last_alert_for_city != sky:
                
                # --- This is the new logic ---
                subject = f"🌂 Umbrella Reminder for {city}!"
                message_body = f"Weather: {sky} | Temp: {temp}°C. Take an umbrella!"

                if ALERT_METHOD == "desktop":
                    send_desktop_notification(subject, message_body)
                else:
                    # Default to email
                    email_body = f"""
Hello,

Take an umbrella before leaving the house today!
Weather condition: {sky}
Temperature: {temp}°C
City: {city}

Stay safe!
"""
                    send_email(subject, email_body)
                
                last_alerts[city] = sky # Update last alert *after* sending
                # --- End of new logic ---

            else:
                print(f"🌥️ Weather in {city} is still {sky}, but an alert was already sent. No spam.")
        else:
            print(f"☀️ No umbrella needed for {city} right now.")
            last_alerts[city] = sky

    print("--- Cycle complete, sleeping for 30 minutes ---")


# --- Main Loop ---
last_alerts_map = {} 
print(f"⏳ Umbrella Reminder Service is running for: {', '.join(CITIES_LIST)}")
print(f"🔔 Alert Method: {ALERT_METHOD}") # <-- Added this line for clarity

while True:
    umbrellaReminder(CITIES_LIST, last_alerts_map)
    time.sleep(1800)
