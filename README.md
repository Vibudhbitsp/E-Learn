# E-Learning Web App

## Introduction

This is an E-Learning web application developed using Django, designed to provide a platform for both students and teachers. The application allows students to register for courses, submit reviews, and engage in an interactive learning environment. Teachers, on the other hand, can create courses, manage student enrollment, and track student progress.

## Features

### For Students

- **User Registration**: Students can create accounts to access the platform.

- **Course Enrollment**: Students can browse and enroll in various courses offered on the platform.

- **Course Reviews**: Students can provide feedback and reviews for the courses they have taken.

- **Dashboard**: Students have a personalized dashboard that displays enrolled courses, progress, and announcements.

### For Teachers

- **Course Creation**: Teachers can create new courses, add content, and set up assessments.

- **Student Management**: Teachers can manage student enrollments, view progress, and grade assignments.

- **Announcements**: Teachers can make announcements to communicate important information to students.

- **Analytics**: Teachers can view analytics and insights into student performance.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Vibudhbitsp/E-Learn.git
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

4. **Create a superuser account:**

    ```bash
    python manage.py createsuperuser
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the application in your web browser at** `http://localhost:8000`.

## Usage

1. Access the application and register as a student or teacher.

2. Explore the available courses and enroll as a student or create new courses as a teacher.

3. Interact with the platform based on your role—students can enroll in courses and provide reviews, while teachers can create and manage courses.

4. Utilize the dashboard to track progress and receive updates.

