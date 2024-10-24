# Email Response Generation API

This project is a Flask-based API that generates automatic responses to emails using an AI model. It is designed to receive email content, process it, and send an appropriate response.

## Features
- Email content extraction and processing
- AI-based email response generation
- RESTful API built with Flask
- Integration with external email services

## Getting Started

### Prerequisites
- Python 3.8+
- Flask
- Git
- Any AI model for generating text responses (e.g., OpenAI GPT, etc.)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/amddah/genAI_api.git
    cd genAI_api
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up environment variables for email configuration and AI model.

4. Run the Flask app:
    ```bash
    flask run
    ```

## API Endpoints

- `POST /genai`  
  This endpoint accepts email data (subject, body, sender) and returns an AI-generated response.

## Repositories Associated

- Front-end repository for the application: [Rpa_FrontEnd](https://github.com/amddah/Rpa_FrontEnd)
- Email response sender application: [EmailSender](https://github.com/amddah/EmailSender.git)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
