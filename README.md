# SpikeIt Project

## 📌 Overview
SpikeIt is a microservices-based application for managing volleyball workouts. It consists of three microservices:
1. **Backend Microservice** - Handles API requests using FastAPI.
2. **Database Microservice** - Manages SQLite database operations.
3. **Frontend Microservice** - Provides a Streamlit-based UI.

This README provides setup instructions, including installation, testing, and running the project.

---

## 🔧 Prerequisites
Ensure you have the following installed:
- Python 3.9+
- pip (Python package manager)
- Virtual environment (`venv`) for running tests
- Docker & Docker Compose for running the application

---

## 🚀 Setting Up for Testing (Without Docker)
### **1️⃣ Clone the Repository**
```bash
# Navigate to your project directory
cd ~/projects  # Change as needed

# Clone the repository
git clone https://github.com/your-repo/spikeit.git
cd spikeit
```

### **2️⃣ Create & Activate Virtual Environment for Testing**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### **3️⃣ Install Dependencies for Testing**
Each microservice has its own dependencies, install them separately:
```bash
pip install -r backend_microservice/requirements.txt
pip install -r db_microservice/requirements.txt
pip install -r frontend_microservice/requirements.txt
```

---

## 🧦 Running Unit Tests in a Virtual Environment
We use **pytest** for unit testing. No need to run Docker since we mock external dependencies.

### **🔹 Backend Microservice Tests**
```bash
cd backend_microservice/tests
pytest unit_test.py
```

### **🔹 Database Microservice Tests**
```bash
cd ../../db_microservice/tests
pytest unit_test.py
```

### **🔹 Frontend Microservice Tests**
```bash
cd ../../frontend_microservice/test
pytest unit_test.py
```

If everything is correct, you should see `PASSED` messages.

To exit the virtual environment:
```bash
deactivate
```

---

## 🛠️ Running the Application with Docker Compose
Since the application is designed to run inside Docker, use the following commands to start it:

```bash
docker-compose up --build
```

Once started:
- Backend runs on **http://localhost:8000**
- Database runs on **http://localhost:8001**
- Frontend runs on **http://localhost:8501**

To stop the services, use:
```bash
docker-compose down
```

---

## 🛠️ Debugging & Common Issues
- **Virtual environment not found?** Run `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows).
- **Port conflicts?** Ensure no other service is using ports `8000`, `8001`, or `8501`.
- **Tests failing due to missing modules?** Run `pip install -r requirements.txt` in the respective microservice directory.
- **Docker network issues?** Try `docker-compose down --volumes` and restart.

---

## 🎥 Video Demonstration
For a step-by-step guide, watch this video tutorial:  
[![Unit Test Setup Tutorial](https://img.youtube.com/vi/ArNPxXf3f2w/0.jpg)](https://youtu.be/ArNPxXf3f2w)

