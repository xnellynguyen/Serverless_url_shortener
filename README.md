# Serverless URL Shortener

This project is a serverless URL shortener application built using AWS services and a modern web interface.

## Components

- **AWS Lambda**: Serverless compute service to handle URL shortening and redirection logic.
- **Amazon API Gateway**: API management service to create and maintain RESTful APIs for URL creation and redirection.
- **Amazon DynamoDB**: NoSQL database service to store the mappings between original and shortened URLs.
- **Front-end**: Simple web interface built with HTML, CSS, and Bootstrap.

## Usage
- **Shorten a URL**: Enter a long URL and click "Shorten URL".
The shortened URL hash will be displayed.

- **Redirect to the original URL**: Enter the short URL hash and click "Redirect". You will be redirected to the original URL.

## Tech Used

- **AWS Lambda**: For executing backend code in response to API Gateway requests.
- **Amazon API Gateway**: For exposing RESTful endpoints to the web.
- **Amazon DynamoDB**: For storing URL mappings.
- **HTML**: For structuring the web pages.
- **CSS**: For styling the web pages.
- **Bootstrap**: For responsive design and pre-styled components.
- **JavaScript**: For handling client-side logic and interacting with the APIs.

## Setup and Deployment

1. **Clone the repository**
   ```
   git clone https://github.com/xnellynguyen/Serverless_url_shortener.git
   cd Serverless_url_shortener
   ```

2. **Run locally**
   ```
   python -m http.server
   ```
