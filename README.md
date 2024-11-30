# Vue/Django Simple Web API Project

## Overview

This repository contains a basic web application built using **Django** (as the backend) and **Vue.js** (as the frontend) for the purpose of demonstrating my skills with these technologies. The app features a simple many-to-many object model, a reactive frontend, and CRUD operations for interacting with the models via AJAX requests. 

This project was created as part of a university coursework assignment and is designed as a learning demonstration of Django and Vue.js fundamentals.

---

## Features

### Backend
- **Django Framework**: A robust and efficient Python web framework is used to manage data and serve the API.
- **Models with a Many-to-Many Relationship**: 
  - Includes a *through model* with an additional field to enhance the many-to-many relationship.
  - Makes use of various field types: `CharField`, `TextField`, `BooleanField`, `IntegerField`, and `DateField`.
- **CRUD Operations via Ajax**: 
  - Supports HTTP methods (`GET`, `POST`, `PUT`, `DELETE`) for handling data.
  - Uses Django's `JsonResponse` for structured data exchange.
- **PEP 8 Compliance**: The code is written following Python's PEP 8 standards, with detailed docstrings for all functions and classes.

### Frontend
- **Vue.js**: A reactive JavaScript framework for creating an interactive and dynamic user experience.
  - Utilizes **Vue components** organized via props and emits to manage data flow between parent and child components.
  - Employs **Vue Options API** for state and logic handling.
- **Fetch API**: AJAX requests are used to interact with the Django backend without requiring page reloads.
- **Bootstrap Styling**: Clean and responsive UI using Bootstrap, including modals and tabs.
  - **Tabbed Interface**: Separate tabs for each model, with one dedicated tab to manage the many-to-many relationship.

### Functionalities
- Fetch and display all elements of each model on page load.
- Add new elements to any model (POST).
- Edit existing elements (PUT).
- Delete elements from any model (DELETE).
- Manage many-to-many relationships, including adding, removing, and editing relationship data.

---
