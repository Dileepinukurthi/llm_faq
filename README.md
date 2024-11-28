# Django Project: LLM FAQ

## Description

LLM FAQ is a Django-based web application designed to answer FAQs with AI.

---

## Table of Contents

1. [Features](#features)  
2. [Tech Stack](#tech-stack)  
3. [Setup Instructions](#setup-instructions)  
4. [Usage](#usage)

---

## Features

- AI-based FAQ answering  
- Role-based access control  
- REST API for listing all the FAQs and searching for an FAQ  
- Caching the FAQs  
- Normalized database schema for storing keywords and FAQs  
- Admin panel for managing database items  

---

## Tech Stack

- **Backend:** Django Rest Framework  
- **Database:** Sqlite3  
- **Frontend:** DRF Docs  

---

## Setup Instructions

Follow these steps to set up the project on your local machine:

### Prerequisites

Make sure you have the following installed:
- Python 3.x  
- pip (Python package manager)  
- Virtualenv (optional but recommended)  
- Sqlite  
- Git  

### Instructions

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/Dileepinukurthi/llm_faq.git
   cd llm_faq
   ```
2. Set up a virtual environment:
   - **Windows**:
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```
   - **Linux/Mac**:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py makemigrations faq
   python manage.py migrate
   ```
5. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```
---

## Usage

- Access the development server at: `http://127.0.0.1:8000/`  
- Use the admin panel for managing database items: `http://127.0.0.1:8000/admin/`
- Listing endpoint `http://127.0.0.1:8000/api/faqs`
- Search endpoint `http://127.0.0.1:8000/api/query`. Body should contain the following content `{"query" : "Tell me about the quality of the product"}`
