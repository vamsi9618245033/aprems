# Agricultural Products Rural Entrepreneurship Management System  
Empowering rural communities through secure and scalable digital commerce.  

## About the Project  
This project is designed to facilitate the buying and selling of agricultural products for rural communities. It ensures secure and efficient management of users and products using robust **Authentication**, **Authorization**, and **Role-Based Access Control (RBAC)** mechanisms. The system distinguishes between admin and normal users, allowing role-based access to features, ensuring data integrity, and providing a scalable platform for rural entrepreneurship.  

---

## Features  
- **Authentication**: Secure user registration, login, and logout using Django's built-in authentication system and JWT.  
- **Role-Based Access Control (RBAC)**:  
  - **Admin Role**: Full control over users and products.  
  - **Normal User Role**: Limited to managing their own products and accessing the marketplace.  
- **Product Management**:  
  - Normal users can list, edit, and manage their own products.  
  - Admins can review, edit, or delete all products to maintain system integrity.  
- **User Management**: Admins can manage user accounts, reset passwords, and assign roles.  
- Scalable design for future role and permission additions.  

---

## Technologies Used  
- **Backend**: Django, Django REST Framework (DRF).  
- **Authentication**: JWT (via `django-rest-framework-simplejwt`).  
- **Frontend**: Django templates (or integrate with modern frameworks like React if needed).  
- **Database**: PostgreSQL.  
- **Security**: Django's password hashing, token-based authentication, and middleware-based access control.  

---

## Installation  

### Prerequisites  
Ensure you have the following installed:  
- Python (>=3.8)  
- PostgreSQL  
- pip (Python package manager)  

### Steps to Set Up Locally  
1. Clone the repository:  
   ```bash
   git clone https://github.com/msivakartheek9348/aprems
   cd aprems
