# DANI PT

<img src="static/images/danipt.jpg" width=100>

DANI PT is the final project for my CS50x course (https://cs50.harvard.edu/x/2024/), developed as a comprehensive web application to enhance the personal training experience.

#### Video Demo:  <https://www.youtube.com/watch?v=n4m9AW05ULs>

#### Description:
DANI PT is a personal web application designed to streamline and enhance the experience of gym training with the support of Dani, a personal trainer. The platform serves clients by providing an intuitive interface for managing schedules and facilitating communication with the trainer.

## Features

### User Registration and Login
Users can register for an account and log in securely. The registration form captures essential information such as name, surname, gender, birthdate, number of weekly workouts, email, username, and personal goals. Once registered, users can log in and access their personalized dashboard.

### Dark Mode
To enhance user experience, DANI PT includes a dark mode feature. Users can toggle between light and dark themes based on their preference, ensuring comfortable use during different times of the day.

### Booking System
Clients can book training sessions with their personal trainers through an easy-to-use booking system. The system ensures no time conflicts by allowing clients to select available time slots between 7:00 AM and 8:00 PM. The backend validates these bookings to prevent overlaps, ensuring trainers can manage their schedules effectively.

### Profile Management
Users can view their personal information on the profile page. This page displays detailed information about the user, including their name, surname, gender, birthdate, weekly workouts, email, username, and personal goals.

### Reviews
The platform features a review system where clients can leave feedback for the trainer. Reviews include the username, date, title, and comment. This system helps Dani PT to improve her services based on client feedback.

### Responsive Design
The application is built with a responsive design using Bootstrap, ensuring it works seamlessly on various devices, including desktops, tablets, and smartphones.

### Backend
The backend is developed using Flask, a lightweight web framework in Python. Flask handles user authentication, data management, and interaction with the SQLite database, ensuring a smooth and secure user experience.

### Database
DANI PT uses SQLite to manage user data, bookings, and reviews. The database schema ensures data integrity and includes constraints to prevent overlapping bookings.

## Technology Stack
- **Frontend:** HTML, CSS (Bootstrap), JavaScript
- **Backend:** Flask (Python)
- **Database:** SQLite

DANI PT aims to provide a user-friendly and efficient solution for personal trainers and their clients, simplifying the management of training sessions and fostering better communication and feedback.

Feel free to check out the video demo for a more detailed overview of the functionalities and user interface.

## Project Structure

### app.py
This is the main application file where the Flask app is initialized and all the routes are defined. It handles the logic for rendering templates and processing form submissions.

### dani.db
This is the SQLite database file that stores all the user information, reviews, and booking data. It includes tables for users, bookings, and reviews.

### helpers.py
This file contains helper functions used throughout the application. These functions include utilities for handling user authentication, useful functions, and other common tasks.


## Templates (HTML Files)

### aboutme.html
This template displays information about Dani, the personal trainer. It includes details about Dani's background, qualifications, and approach to personal training.

### apology.html
This template is used to display error messages to users. It provides a consistent format for showing apologies when something goes wrong, such as invalid form submissions or authentication errors.

### booknow.html
This template allows users to book training sessions with Dani. It includes a form where users can select the date and time for their session, as well as any specific requests or goals they have.

### index.html
This is the homepage of the application. It provides an overview of the services offered by Dani PT and includes links to other sections of the site, such as booking, reviews, and the profile page.

### layout.html
This is the base template that all other templates extend. It includes the common structure of the HTML document, such as the header, footer, and navigation bar.

### login.html
This template provides a login form for users to access their accounts. It includes fields for username and password, and handles user authentication.

### profile.html
This template displays the personal information of the logged-in user. It includes details such as name, surname, gender, birth date, weekly workouts, email, username, goals, and, if submitted, review and appointment(s).

### register.html
This template provides a registration form for new users to create an account. It includes fields for entering personal information and setting up login credentials.

### reviews.html
This template displays reviews from clients who have trained with Dani. It includes a table with columns for username, date, title, and comment of each review.

## Static Files

### script.js
This JavaScript file contains client-side scripts for enhancing the user experience. It includes functions for handling form validations, toggling dark mode, and other interactive features.

### style.css
This CSS file contains the styles for the application. It includes custom styles for the layout, forms, tables, and other elements to ensure a consistent and visually appealing design.

### images
This directory contains image files used in the application, such as the logo and other graphics. These images are referenced in the templates to enhance the visual appeal of the site.
