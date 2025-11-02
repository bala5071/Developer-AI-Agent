# API Documentation

This project is primarily a frontend React portfolio website. The contact form is designed to integrate with an external email sending API.

## Contact Form API

- **POST** `/contact`
  - Accepts JSON with fields:
    - `name`: string, required
    - `email`: string, required, valid email
    - `message`: string, required
  - Sends an email to the recipient configured on the server backend.
  - Responds with success or error message in JSON.

> Note: You need to implement the backend separately to handle form submissions using Nodemailer or other mail services.

## Environment Variables

- `REACT_APP_API_URL`: Base URL for API endpoints.

## Usage

Frontend submits contact form data as POST request to `${REACT_APP_API_URL}/contact`.
