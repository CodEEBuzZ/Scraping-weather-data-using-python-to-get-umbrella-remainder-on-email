# scraping-weather-data-using-python-to-get-umbrella-reminder-on-email

🌂 Umbrella Reminder – Python Automation

This project is a simple Python automation script that checks the weather (using the OpenWeather API) and sends you an email or desktop reminder to carry an umbrella whenever it’s cloudy, rainy, or stormy.

✨ Features

* Fetches real-time weather data for **one or more cities**.
* Sends alerts via **email or desktop notification**.
* Runs automatically in the background and checks weather every 30 minutes.
* Prevents duplicate spam emails by only sending one alert per weather condition.
* Secure setup using environment variables (no hardcoded keys).
* **Docker support** for easy background service deployment.

🛠️ Requirements

* Python 3.7+
* Gmail account with App Password enabled
* OpenWeather API Key

📦 Installation

1.  Clone the repo:
    ```bash
    git clone [https://github.com/your-username/umbrella-reminder.git](https://github.com/your-username/umbrella-reminder.git)
    cd umbrella-reminder
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  Set up Gmail App Password:
    * Enable 2-Step Verification on your Gmail.
    * Generate an App Password from Google Security Settings.
    * Copy the 16-character app password.

4.  Get OpenWeather API Key:
    * Sign up on [OpenWeather](https://openweathermap.org/api).
    * Go to API Keys → Copy your key.

⚙️ Usage

This script uses environment variables to keep your API keys and passwords secure.

1.  Create a `.env` file. You can copy the example file:
    ```bash
    cp .env.example .env
    ```

2.  Edit the `.env` file with your information:
    ```
    OPENWEATHER_API_KEY="your_openweather_api_key_here"
    SENDER_EMAIL="your_gmail@gmail.com"
    SENDER_PASS="your_16_digit_app_password"
    RECEIVER_EMAIL="receiver_email@example.com"
    CITIES="Hyderabad"
    ALERT_METHOD="email"
    ```
    * You can add multiple cities: `CITIES="Hyderabad,Mumbai,Kolkata"`
    * You can change the alert type: `ALERT_METHOD="desktop"`

3.  Run the script:
    ```bash
    python umbrella.py
    ```
The script will print the current conditions to your terminal and send an alert if needed.

---

🐳 Running with Docker

You can also run this script as a background service using Docker.

1.  **Build the Docker image:**
    ```bash
    docker build -t umbrella-reminder .
    ```

2.  **Run the container:**
    Make sure your `.env` file (from the 'Usage' section) is complete.
    ```bash
    docker run -d --rm \
      --env-file ./.env \
      --name umbrella-service \
      umbrella-reminder
    ```
    * `-d` runs the container in detached (background) mode.
    * `--rm` automatically removes the container when it stops.
    * `--env-file` securely passes your secrets to the container.

3.  **To see the logs:**
    ```bash
    docker logs -f umbrella-service
    ```

4.  **To stop the container:**
    ```bash
    docker stop umbrella-service
    ```

📸 Example Output

⏳ Umbrella Reminder Service is running for: Hyderabad, Mumbai 🔔 Alert Method: desktop 📍 Hyderabad | 🌡️ Temp: 28.0°C, Sky: Clouds ✅ Desktop Notification Sent! 📍 Mumbai | 🌡️ Temp: 29.5°C, Sky: Clear ☀️ No umbrella needed for Mumbai right now. --- Cycle complete, sleeping for 30 minutes ---

<img width="905" height="471" alt="image" src="https://github.com/user-attachments/assets/b84ba1e5-fb88-4894-87a2-762bac929c75" />

🚀 Future Improvements

*(All items completed!)*

📜 License

This project is licensed under the MIT License – feel free to use and modify.
