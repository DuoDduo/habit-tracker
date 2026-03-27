# HabitOS Installation Manual

Welcome to HabitOS! This guide will provide step-by-step instructions to set up the **HabitOS: Achievement Engine** locally on your machine.

---

## Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10+**: [Download here](https://www.python.org/downloads/)
- **Node.js 18+** & **npm**: [Download here](https://nodejs.org/)
- **Git**: [Download here](https://git-scm.com/downloads)

---

##  Project Structure

- `/backend`: Flask (Python) API & SQLite Database
- `/frontend`: React (Vite) + Tailwind CSS Dashboard

---

## 1. Backend Setup

1.  **Navigate to the backend directory**:
    ```bash
    cd backend
    ```

2.  **Create a virtual environment**:
    ```bash
    # Windows
    python -m venv venv
    
    # macOS/Linux
    python3 -m venv venv
    ```

3.  **Activate the virtual environment**:
    ```bash
    # Windows
    .\venv\Scripts\activate
    
    # macOS/Linux
    source venv/bin/activate
    ```

4.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Initialize & Seed the Database**:
    *The database auto-seeds on first run, but you can manually seed it for a fresh start*:
    ```bash
    python generate_test_data.py
    ```

6.  **Run the Backend Server**:
    ```bash
    python run.py
    ```
    *The API will be available at:* `http://localhost:5000`

---

## 2. Frontend Setup

1.  **Navigate to the frontend directory**:
    ```bash
    # From project root
    cd frontend
    ```

2.  **Install dependencies**:
    ```bash
    npm install
    ```

3.  **Run the Frontend Dev Server**:
    ```bash
    npm run dev
    ```
    *The application will be available at:* `http://localhost:5173` (or the port shown in your terminal).

---

## 3. Deployment Configuration

### Render (Backend)
1.  Connect your GitHub repository.
2.  Set **Build Command**: `pip install -r backend/requirements.txt`
3.  Set **Start Command**: `gunicorn --chdir backend --worker-class uvicorn.workers.UvicornWorker asgi:asgi_app --bind 0.0.0.0:$PORT`
4.  Add environment variables: `FLASK_ENV=production`, `FLASK_DEBUG=False`.

### Vercel (Frontend)
1.  Connect your GitHub repository.
2.  Set **Framework Preset**: `Vite`.
3.  Set **Root Directory**: `frontend`.
4.  Add environment variable: `VITE_API_BASE_URL` pointing to your Render service URL.

---

## 4. Verification

1.  Open `http://localhost:5173`.
2.  You should see the **HabitOS Landing Page**.
3.  Click **Get Started**, enter your name, and log in.
4.  **Important**: You should immediately see the **5 predefined habits** (Drink Water, Exercise, etc.) with 4 weeks of data pre-populated.

---

### Troubleshooting
- **Database Empty?**: Re-run `python generate_test_data.py` in the `backend` folder.
- **Port 5000 Busy?**: Ensure no other Flask/Python processes are running. 
- **CORS Issues?**: Ensure the frontend origin is whitelisted in `backend/app/core/config.py`.

---

**Author**: Blessing Oluwapelumi James  
**Version**: 1.2.0 (Premium Achievement Engine)  
**Status**: Submission Ready
