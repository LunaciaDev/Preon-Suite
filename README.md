# Preon Suite

> Preon *(noun)*: Hypothetical point particle, conceived of as sub-component of quarks and leptons.

Preon Suite is a collection of small things that helps out with small tasks.  
This is a project for the Introduction to Computer Science class.

## Features

- **Account System**: A pair of username and password is required to use this application.
- **Face Identification**: Login by recognizing the user's face.
- **E-Mail Client**: Send email as well as viewing the author and header of the 10 most recent email sent/received.
- **Weather Forecasting**: View the current weather as well as weather forecasting for the next 3 days. Weather data is provided by [**OpenWeather**](https://openweathermap.org/).
- **Reminders**: Create reminders and be notified about it at a certain time.

## Getting Started

### Required Dependencies

Before you proceed, ensure that you have Python 3.11 installed with these libraries:

- PySide6
- libsass
- keyring
- google-api-python-client
- google-auth-oauthlib
- pyttsx3
- SpeechRecognition
- plyer

You will also need API keys for Google API and [**OpenWeather**](https://openweathermap.org/) for the mail and weather system.

## Installation

1. Clone the repository.
2. Install the required dependencies: `pip install -r requirement.txt`.
3. Run `main.py`.