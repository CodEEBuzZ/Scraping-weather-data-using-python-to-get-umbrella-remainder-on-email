# scraping-weather-data-using-python-to-get-umbrella-reminder-on-email

🌂 Umbrella Reminder – Python Automation

This project is a simple Python automation script that checks the weather (using the OpenWeather API
) and sends you an email reminder to carry an umbrella whenever it’s cloudy, rainy, or stormy.

✨ Features

Fetches real-time weather data for your city.

Sends an email reminder via Gmail when the weather is rainy/cloudy.

Runs automatically in the background and checks weather every 30 minutes.

Prevents duplicate spam emails by only sending one alert per weather condition.

🛠️ Requirements

Python 3.7+

Gmail account with App Password enabled

OpenWeather API Key

📦 Installation

Clone the repo

git clone https://github.com/your-username/umbrella-reminder.git
cd umbrella-reminder


Install dependencies

pip install requests


Set up Gmail App Password

Enable 2-Step Verification on your Gmail.

Generate an App Password from Google Security Settings
.

Copy the 16-character app password.

Get OpenWeather API Key

Sign up on OpenWeather
.

Go to API Keys → Copy your key.

⚙️ Usage

Edit umbrella.py and update these values:

sender_email = "your_email@gmail.com"
sender_pass = "your_gmail_app_password"
receiver_email = "receiver_email@gmail.com"
api_key = "your_openweather_api_key"
city = "Hyderabad"   # change to your city

---

🐳 Running with Docker

You can also run this script as a background service using Docker, which is a great way to "set it and forget it."

1.  **Build the Docker image:**
    ```bash
    docker build -t umbrella-reminder .
    ```

2.  **Run the container:**
    Make sure your `.env` file is complete and in the same directory. This command mounts your `.env` file into the container securely and runs it.
    ```bash
    docker run -d --rm \
      --env-file ./.env \
      --name umbrella-service \
      umbrella-reminder
    ```
    * `-d` runs the container in detached (background) mode.
    * `--rm` automatically removes the container when it stops.
    * `--env-file` securely passes your secrets to the container.
    * `--name` gives your container an easy-to-find name.

3.  **To see the logs:**
    ```bash
    docker logs -f umbrella-service
    ```

4.  **To stop the container:**
    ```bash
    docker stop umbrella-service
    ```


Run the script:

python umbrella.py


The script will:

Check the weather every 30 minutes

📸 Example Output
⏳ Umbrella Reminder Service is running...
🌡️ Temp: 26.15°C, Sky: Clouds
✅ Email Sent!
<img width="905" height="471" alt="image" src="https://github.com/user-attachments/assets/b84ba1e5-fb88-4894-87a2-762bac929c75" />


⏳ Umbrella Reminder Service is running...
🌡️ Temp: 24.23°C, Sky: Mist
☀️ No umbrella needed right now.




🚀 Future Improvements

Support for multiple cities.

Desktop notifications instead of email.

Docker setup for background service.

📜 License

This project is licensed under the MIT License – feel free to use and modify.


Print the current condition

Send an email reminder when it’s rainy/cloudy
