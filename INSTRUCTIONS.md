#  Habit Tracker - Full-Stack Application

**Author:** Blessing Oluwapelumi James  
**Matriculation Number:** 92134091  
**Course:** Object-Oriented and Functional Programming with Python  


[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com/)
[![React](https://img.shields.io/badge/React-18.2-blue.svg)](https://reactjs.org/)
[![Tests](https://img.shields.io/badge/Tests-45%20Passing-success.svg)](tests/)
[![Coverage](https://img.shields.io/badge/Coverage-92%25-brightgreen.svg)](htmlcov/)

---

##  Table of Contents

1. [Project Overview](#project-overview)
2. [Features & Screenshots](#features--screenshots)
3. [Technology Stack](#technology-stack)
4. [Project Structure](#project-structure)
5. [Installation Guide](#installation-guide)
6. [Running the Application](#running-the-application)
7. [Database Schema](#database-schema)
8. [Unit Testing](#unit-testing)
9. [Analytics Module](#analytics-module)
10. [Predefined Test Data](#predefined-test-data)
11. [API Documentation](#api-documentation)
12. [Code Quality](#code-quality)

---

##  Project Overview

A **professional full-stack habit tracking application** that helps users build and maintain positive habits through:

-  **Daily and Weekly habit tracking**
-  **Automatic streak calculation** (respecting periodicity)
-  **Comprehensive analytics** using functional programming
-  **Data persistence** with SQLite database
-  **RESTful API** with Flask
-  **Modern React frontend** with Tailwind CSS
-  **45 comprehensive unit tests** (92% coverage)
-  **5 predefined habits** with 4 weeks of test data

### Key Programming Paradigms Demonstrated

**Object-Oriented Programming (OOP):**
- `Habit` class with encapsulated data and behavior
- Streak calculation methods within the class
- SQLAlchemy ORM models

**Functional Programming (FP):**
- Pure functions in analytics module
- Uses `filter()`, `map()`, `max()`
- No side effects, immutable operations

---

## Features & Screenshots

### 1. Dashboard with Analytics

![Dashboard](docs/screenshots/dashboard.png)

**Key Features:**
-  Total habits count
-  Longest streak across all habits
-  Daily habits count
-  Weekly habits count

### 2. Five Predefined Habits with 4-Week Data

![Predefined Habits](docs/screenshots/predefined_habits.png)

**Predefined Habits:**

1. **Drink Water** (Daily)
   - Specification: "Drink 8 glasses of water throughout the day"
   - 4 weeks data: 25/28 days completed (89% compliance)
   - Current streak: 7 days
   - Longest streak: 12 days

2. **Exercise** (Daily)
   - Specification: "Complete 30 minutes of physical activity"
   - 4 weeks data: 20/28 days completed (71% compliance)
   - Current streak: 3 days
   - Longest streak: 8 days

3. **Read Book** (Daily)
   - Specification: "Read for at least 20 minutes before bed"
   - 4 weeks data: 17/28 days completed (61% compliance)
   - Current streak: 2 days
   - Longest streak: 5 days

4. **Weekly Review** (Weekly)
   - Specification: "Review and plan weekly goals every Sunday"
   - 4 weeks data: 4/4 weeks completed (100% compliance)
   - Current streak: 4 weeks
   - Longest streak: 4 weeks

5. **Meditation** (Daily)
   - Specification: "Practice 10 minutes of mindfulness meditation"
   - 4 weeks data: 22/28 days completed (79% compliance)
   - Current streak: 5 days
   - Longest streak: 9 days

### 3. Habit Streaks Visualization

![Habit Streaks](docs/screenshots/habit_streaks.png)

**Streak Features:**
- ✅ Current streak calculation (respects periodicity)
- ✅ Longest streak ever achieved
- ✅ Visual progress bar
- ✅ Broken/Active status indicator
- ✅ Streak emoji based on performance

### 4. Create New Habit

![Create Habit](docs/screenshots/create_habit.png)

**Form Validation:**
- ✅ Name is required (1-255 characters)
- ✅ Periodicity selection (Daily/Weekly)
- ✅ Optional description field
- ✅ Client-side validation
- ✅ Server-side Pydantic validation

### 5. Analytics Dashboard

![Analytics](docs/screenshots/analytics_detailed.png)

**Analytics Features:**
- Filter habits by periodicity
- View struggling habits (streak < 3)
- See all tracked habit names
- Overall statistics summary

### 6. Check-Off Functionality

![Check Off](docs/screenshots/check_off.png)

**Check-Off Features:**
- ✅ One-click check-off
- ✅ Instant streak update
- ✅ Success notification
- ✅ Analytics refresh

---

## 🛠️ Technology Stack

### Backend
```
Python 3.9+
├── Flask 3.0              # Web framework
├── SQLAlchemy 2.0         # ORM
├── Pydantic 2.5           # Data validation
├── Flask-CORS 4.0         # CORS support
└── pytest 7.4             # Testing framework
```

### Frontend
```
Node.js 18+
├── React 18.2             # UI library
├── Vite 5.0               # Build tool
├── Tailwind CSS 3.3       # Styling
├── Axios 1.6              # HTTP client
└── React Hot Toast 2.4    # Notifications
```

### Database
```
SQLite 3
└── Foreign key constraints
└── CASCADE DELETE
└── ACID compliance
```

---

## 📁 Project Structure

```
habit-tracker/
│
├── backend/                        # Python Flask Backend
│   ├── app/
│   │   ├── __init__.py            # Package initialization
│   │   ├── main.py                # Flask app factory
│   │   │
│   │   ├── api/                   # REST API Endpoints
│   │   │   └── endpoints/
│   │   │       ├── habits.py      # Habit CRUD operations
│   │   │       └── analytics.py   # Analytics endpoints (FP)
│   │   │
│   │   ├── core/                  # Configuration
│   │   │   └── config.py          # Environment settings (Pydantic)
│   │   │
│   │   ├── models/                # OOP Domain Models
│   │   │   └── habit.py           # Habit & Completion classes
│   │   │                          # - calculate_current_streak()
│   │   │                          # - calculate_longest_streak()
│   │   │                          # - is_broken()
│   │   │
│   │   ├── schemas/               # Data Validation
│   │   │   └── habit_schema.py    # Pydantic schemas
│   │   │
│   │   ├── services/              # Business Logic
│   │   │   ├── habit_service.py   # Habit operations
│   │   │   └── analytics_service.py # Analytics (FP)
│   │   │                           # - get_habits_by_periodicity()
│   │   │                           # - find_longest_streak_all()
│   │   │                           # - Uses filter(), map(), max()
│   │   │
│   │   └── db/                    # Database Layer
│   │       ├── base.py            # SQLAlchemy Base
│   │       └── session.py         # Session management
│   │
│   ├── tests/                     # Unit Tests (45 tests)
│   │   ├── conftest.py            # Pytest fixtures
│   │   ├── test_models.py         # Test Habit class (OOP)
│   │   ├── test_services.py       # Test business logic
│   │   ├── test_analytics.py      # Test analytics (FP)
│   │   └── test_api.py            # Test API endpoints
│   │
│   ├── docs/                      # Documentation
│   │   └── screenshots/           # Application screenshots
│   │
│   ├── .env                       # Environment variables
│   ├── .gitignore                 # Git ignore rules
│   ├── requirements.txt           # Python dependencies
│   ├── asgi.py                    # ASGI wrapper for Uvicorn
│   ├── run.py                     # Application entry point
│   └── generate_test_data.py      # Generate 5 habits + 4 weeks data
│
├── frontend/                      # React Frontend
│   ├── src/
│   │   ├── api/                   # API client
│   │   ├── components/            # React components (23)
│   │   │   ├── common/            # Reusable components
│   │   │   ├── layout/            # Layout components
│   │   │   ├── habits/            # Habit components
│   │   │   └── analytics/         # Analytics components
│   │   ├── hooks/                 # Custom hooks (3)
│   │   ├── utils/                 # Utility functions
│   │   ├── App.jsx                # Main component
│   │   └── main.jsx               # Entry point
│   │
│   ├── package.json               # Node dependencies
│   ├── vite.config.js             # Vite configuration
│   └── tailwind.config.js         # Tailwind configuration
│
├── data/
│   └── habits.db                  # SQLite database (auto-created)
│
├── .gitignore                     # Project-wide ignore
├── README.md                      # This file
└── LICENSE                        # MIT License
```

**Total:**
- 📄 **40+ Files**
- 📝 **4,500+ Lines of Code**
- ✅ **45 Unit Tests**
- 📊 **92% Test Coverage**

---

## 🚀 Installation Guide

### Prerequisites

```bash
# Check versions
python --version  # Should be 3.9+
node --version    # Should be 18+
npm --version     # Should be 9+
```

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/habit-tracker.git
cd habit-tracker
```

### Step 2: Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Generate test data (5 habits + 4 weeks)
python generate_test_data.py
```

**Expected Output:**
```
============================================================
🚀 HABIT TRACKER - TEST DATA GENERATOR
============================================================
✅ Database initialized
🗑️  Clearing existing data...
✅ Database cleared

📝 Creating predefined habits...
✅ Created: Drink Water (daily) - High compliance habit
✅ Created: Exercise (daily) - Moderate compliance habit
✅ Created: Read Book (daily) - Struggling habit
✅ Created: Weekly Review (weekly) - Perfect weekly habit
✅ Created: Meditation (daily) - Good compliance habit

📊 Generating 4 weeks of completion data...
   Drink Water: 25 completions
   Exercise: 20 completions
   Read Book: 17 completions
   Weekly Review: 4 completions
   Meditation: 22 completions

✅ Total completions generated: 88

📈 HABIT TRACKER - TEST DATA SUMMARY
========================================
📊 Total Habits: 5
   • Daily habits: 4
   • Weekly habits: 1

🔥 Habit Details:
----------------------------------------

Drink Water (daily)
   Current Streak: 7
   Longest Streak: 12
   Completions: 25
   Status: ✅ Active

[... output continues ...]
```

### Step 3: Frontend Setup

```bash
# Open new terminal window
cd frontend

# Install dependencies
npm install

# Verify installation
npm list
```

**Expected Package Count:** ~150 packages

---

## 🎮 Running the Application

### Start Backend Server

```bash
cd backend

# Activate virtual environment if not active
source venv/bin/activate  # Mac/Linux
# OR
venv\Scripts\activate     # Windows

# Start server
uvicorn asgi:asgi_app --reload --port 5000
```

**Expected Output:**
```
INFO:     Will watch for changes in these directories: [...]
INFO:     Uvicorn running on http://127.0.0.1:5000 (Press CTRL+C to quit)
INFO:     Started reloader process [...] using StatReload
INFO:     Started server process [...]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**✅ Backend is ready when you see "Application startup complete."**

### Start Frontend (New Terminal)

```bash
cd frontend

# Start development server
npm run dev
```

**Expected Output:**
```
  VITE v5.0.8  ready in 523 ms

  ➜  Local:   http://localhost:3000/
  ➜  Network: http://192.168.1.x:3000/
  ➜  press h + enter to show help
```

### Access Application

Open browser and navigate to: **http://localhost:3000**

**✅ You should see:**
- Header with "Habit Tracker" title
- Analytics dashboard with 4 stat cards
- 5 predefined habits listed
- Each habit showing streaks and status

---

## 🗄️ Database Schema

### SQLite Database Location

```
data/habits.db
```

### Table Structure

#### Table: `habits`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `habit_id` | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique identifier |
| `name` | TEXT | NOT NULL | Habit name (1-255 chars) |
| `specification` | TEXT | | Task description |
| `periodicity` | TEXT | NOT NULL, CHECK IN ('daily', 'weekly') | Tracking frequency |
| `created_at` | TIMESTAMP | DEFAULT CURRENT_TIMESTAMP | Creation time |

#### Table: `completions`

| Column | Type | Constraints | Description |
|--------|------|-------------|-------------|
| `completion_id` | INTEGER | PRIMARY KEY AUTOINCREMENT | Unique identifier |
| `habit_id` | INTEGER | FOREIGN KEY → habits(habit_id) ON DELETE CASCADE | Reference to habit |
| `completion_date` | TIMESTAMP | NOT NULL | When habit was completed |

### Database Features

✅ **Foreign Key Constraints:** Ensures referential integrity  
✅ **CASCADE DELETE:** Deleting a habit automatically deletes all its completions  
✅ **CHECK Constraints:** Validates periodicity is only 'daily' or 'weekly'  
✅ **Timestamps:** Automatic creation time tracking  
✅ **ACID Compliance:** Atomic, Consistent, Isolated, Durable transactions

### Sample SQL Queries

```sql
-- Get all habits with completion count
SELECT 
    h.habit_id,
    h.name,
    h.periodicity,
    COUNT(c.completion_id) as total_completions
FROM habits h
LEFT JOIN completions c ON h.habit_id = c.habit_id
GROUP BY h.habit_id;

-- Get completions for specific habit
SELECT * FROM completions
WHERE habit_id = 1
ORDER BY completion_date DESC;

-- Find habits with no completions in last 7 days
SELECT h.* FROM habits h
WHERE NOT EXISTS (
    SELECT 1 FROM completions c
    WHERE c.habit_id = h.habit_id
    AND c.completion_date >= datetime('now', '-7 days')
);
```

### Viewing Database

```bash
# Install SQLite browser (optional)
# Or use command line:
sqlite3 data/habits.db

# List tables
.tables

# View habits
SELECT * FROM habits;

# View completions
SELECT * FROM completions LIMIT 10;

# Exit
.quit
```

---

## 🧪 Unit Testing

### Test Suite Overview

```
tests/
├── conftest.py          # Shared fixtures and test configuration
├── test_models.py       # Habit class tests (OOP)
├── test_services.py     # Business logic tests
├── test_analytics.py    # Analytics module tests (FP)
└── test_api.py          # API endpoint tests
```

**Total Tests:** 45  
**Test Coverage:** 92%  
**All Tests:** ✅ Passing

### Running Tests

```bash
cd backend

# Run all tests with verbose output
pytest tests/ -v

# Run with coverage report
pytest tests/ --cov=app --cov-report=html

# Run specific test file
pytest tests/test_models.py -v

# Run specific test
pytest tests/test_models.py::TestHabitModel::test_calculate_current_streak -v
```

### Test Output

```
====================== test session starts ======================
platform darwin -- Python 3.9.13, pytest-7.4.3
rootdir: /habit-tracker/backend
plugins: cov-4.1.0
collected 45 items

tests/test_api.py::TestHabitsAPI::test_create_habit PASSED  [ 2%]
tests/test_api.py::TestHabitsAPI::test_list_habits PASSED   [ 4%]
tests/test_api.py::TestHabitsAPI::test_get_habit PASSED     [ 6%]
tests/test_api.py::TestHabitsAPI::test_delete_habit PASSED  [ 8%]
tests/test_api.py::TestHabitsAPI::test_check_off PASSED     [11%]
[... continues ...]

tests/test_models.py::TestHabitModel::test_habit_creation PASSED
tests/test_models.py::TestHabitModel::test_calculate_current_streak_daily PASSED
tests/test_models.py::TestHabitModel::test_calculate_longest_streak PASSED
tests/test_models.py::TestHabitModel::test_is_broken_daily PASSED
tests/test_models.py::TestHabitModel::test_periodicity_daily PASSED
tests/test_models.py::TestHabitModel::test_periodicity_weekly PASSED
[... continues ...]

tests/test_analytics.py::TestAnalytics::test_filter_by_periodicity_daily PASSED
tests/test_analytics.py::TestAnalytics::test_longest_streak_all PASSED
tests/test_analytics.py::TestAnalytics::test_get_tracked_habits PASSED
[... continues ...]

==================== 45 passed in 2.83s =====================

Coverage Report:
Name                                Stmts   Miss  Cover
-------------------------------------------------------
app/__init__.py                        1      0   100%
app/main.py                           25      2    92%
app/models/habit.py                   89      5    94%
app/services/analytics_service.py     35      1    97%
app/services/habit_service.py         42      3    93%
-------------------------------------------------------
TOTAL                                 523     42    92%
```

### Test Screenshots

![Test Results](docs/screenshots/test_results.png)

![Coverage Report](docs/screenshots/coverage_report.png)

### Detailed Test Cases

#### 1. Habit Creation, Editing & Deletion Tests

**File:** `tests/test_models.py`

```python
def test_habit_creation(test_db):
    """Test creating a new habit"""
    # PASSES ✅
    
def test_delete_habit(test_db):
    """Test deleting habit removes completions (CASCADE)"""
    # PASSES ✅
```

**File:** `tests/test_services.py`

```python
def test_create_habit_service(test_db):
    """Test habit creation through service layer"""
    # PASSES ✅
    
def test_delete_habit_cascade(test_db):
    """Test CASCADE DELETE on completions"""
    # PASSES ✅
```

#### 2. Streak Calculation Tests (Respecting Periodicity)

**File:** `tests/test_models.py`

```python
def test_calculate_current_streak_daily(test_db):
    """Test daily habit streak calculation"""
    # Creates habit with consecutive daily completions
    # Verifies streak = 5
    # PASSES ✅

def test_calculate_current_streak_weekly(test_db):
    """Test weekly habit streak calculation"""
    # Creates habit with consecutive weekly completions
    # Verifies streak respects week boundaries
    # PASSES ✅

def test_calculate_longest_streak_daily(test_db):
    """Test longest streak with gaps"""
    # Pattern: 3 days, gap, 5 days
    # Should return 5 (longest consecutive)
    # PASSES ✅

def test_is_broken_daily(test_db):
    """Test broken status for daily habits"""
    # No completion yesterday = broken
    # PASSES ✅

def test_is_broken_weekly(test_db):
    """Test broken status for weekly habits"""
    # No completion last week = broken
    # PASSES ✅
```

#### 3. Analytics Module Tests (Each Functionality)

**File:** `tests/test_analytics.py`

```python
def test_get_habits_by_periodicity_daily(sample_habits):
    """Test filtering habits by daily periodicity"""
    # Uses filter() with lambda
    # PASSES ✅

def test_get_habits_by_periodicity_weekly(sample_habits):
    """Test filtering habits by weekly periodicity"""
    # Uses filter() with lambda
    # PASSES ✅

def test_find_longest_streak_all(test_db):
    """Test finding longest streak across all habits"""
    # Uses map() and max()
    # PASSES ✅

def test_find_longest_streak_for_habit(test_db):
    """Test longest streak for specific habit"""
    # PASSES ✅

def test_get_all_tracked_habits(sample_habits):
    """Test getting list of habit names"""
    # Uses list comprehension
    # PASSES ✅

def test_struggling_habits(test_db):
    """Test finding habits with low streaks"""
    # Uses filter() with lambda
    # PASSES ✅
```

### Test Data Fixtures

**File:** `tests/conftest.py`

```python
@pytest.fixture
def test_db():
    """In-memory database for each test"""
    # Creates fresh SQLite database
    # Drops after test completes

@pytest.fixture
def sample_habit(test_db):
    """Pre-created habit for testing"""
    # Returns habit with ID=1

@pytest.fixture
def habit_with_streak(test_db):
    """Habit with 5-day streak"""
    # Returns habit with completions

@pytest.fixture
def predefined_habits(test_db):
    """All 5 predefined habits with 4 weeks data"""
    # Returns list of 5 habits
    # Each with realistic completion patterns
```

---

## 📊 Analytics Module (Functional Programming)

### Overview

The analytics module is implemented using **pure functional programming** principles:

✅ **Pure Functions** - No side effects  
✅ **Immutable Operations** - Doesn't modify input  
✅ **Built-in Functions** - Uses `filter()`, `map()`, `max()`  
✅ **List Comprehensions** - Pythonic functional style

### File Location

```
backend/app/services/analytics_service.py
```

### All Analytics Functions

#### 1. Get Habits by Periodicity

```python
@staticmethod
def get_habits_by_periodicity(habits: List[Habit], period: str) -> List[Habit]:
    """
    Filter habits by periodicity using filter() and lambda.
    
    Args:
        habits: List of Habit objects
        period: "daily" or "weekly"
    
    Returns:
        Filtered list of habits
        
    Example:
        >>> daily_habits = get_habits_by_periodicity(all_habits, "daily")
        >>> len(daily_habits)  # 4 (from 5 total)
        4
    """
    return list(filter(lambda h: h.periodicity == period, habits))
```

**Test:**
```python
def test_filter_by_periodicity():
    # Input: 5 habits (4 daily, 1 weekly)
    result = get_habits_by_periodicity(habits, "daily")
    assert len(result) == 4  # ✅ PASSES
```

#### 2. Find Longest Streak (All Habits)

```python
@staticmethod
def find_longest_streak_all(habits: List[Habit]) -> int:
    """
    Find longest streak across all habits using map() and max().
    
    Args:
        habits: List of Habit objects
    
    Returns:
        Longest streak count (0 if no habits)
        
    Example:
        >>> longest = find_longest_streak_all(all_habits)
        >>> longest
        12  # From "Drink Water" habit
    """
    if not habits:
        return 0
    
    streaks = map(lambda h: h.calculate_longest_streak(), habits)
    return max(streaks, default=0)
```

**Test:**
```python
def test_longest_streak_all():
    # Input: Habits with streaks [12, 8, 5, 4, 9]
    result = find_longest_streak_all(habits)
    assert result == 12  # ✅ PASSES
```

#### 3. Find Longest Streak (Single Habit)

```python
@staticmethod
def find_longest_streak_for_habit(habit: Habit) -> int:
    """
    Get longest streak for specific habit.
    
    Args:
        habit: Habit object
    
    Returns:
        Longest streak for this habit
        
    Example:
        >>> habit = get_habit_by_id(1)  # "Drink Water"
        >>> streak = find_longest_streak_for_habit(habit)
        >>> streak
        12
    """
    return habit.calculate_longest_streak()
```

**Test:**
```python
def test_longest_streak_single():
    result = find_longest_streak_for_habit(drink_water_habit)
    assert result == 12  # ✅ PASSES
```

#### 4. Get All Tracked Habits

```python
@staticmethod
def get_all_tracked_habits(habits: List[Habit]) -> List[str]:
    """
    Get list of all habit names using list comprehension.
    
    Args:
        habits: List of Habit objects
    
    Returns:
        List of habit names
        
    Example:
        >>> names = get_all_tracked_habits(all_habits)
        >>> names
        ['Drink Water', 'Exercise', 'Read Book', 'Weekly Review', 'Meditation']
    """
    return [h.name for h in habits]
```

**Test:**
```python
def test_get_tracked_habits():
    result = get_all_tracked_habits(habits)
    assert len(result) == 5  # ✅ PASSES
    assert "Drink Water" in result  # ✅ PASSES
```

#### 5. Get Struggling Habits

```python
@staticmethod
def get_struggling_habits(habits: List[Habit], threshold: int = 3) -> List[Habit]:
    """
    Find habits with current streak below threshold using filter().
    
    Args:
        habits: List of Habit objects
        threshold: Minimum acceptable streak (default: 3)
    
    Returns:
        Habits with low streaks
        
    Example:
        >>> struggling = get_struggling_habits(all_habits, threshold=3)
        >>> [h.name for h in struggling]
        ['Read Book']  # Only habit with streak < 3
    """
    from datetime import datetime
    return list(filter(
        lambda h: h.calculate_current_streak(datetime.now()) < threshold,
        habits
    ))
```

**Test:**
```python
def test_struggling_habits():
    result = get_struggling_habits(habits, threshold=3)
    # "Read Book" has streak = 2
    assert len(result) == 1  # ✅ PASSES
    assert result[0].name == "Read Book"  # ✅ PASSES
```

#### 6. Count by Periodicity

```python
@staticmethod
def count_by_periodicity(habits: List[Habit]) -> dict:
    """
    Count habits by periodicity using filter().
    
    Args:
        habits: List of Habit objects
    
    Returns:
        Dict with counts {"daily": x, "weekly": y}
        
    Example:
        >>> counts = count_by_periodicity(all_habits)
        >>> counts
        {'daily': 4, 'weekly': 1}
    """
    daily = len(list(filter(lambda h: h.periodicity == "daily", habits)))
    weekly = len(list(filter(lambda h: h.periodicity == "weekly", habits)))
    
    return {"daily": daily, "weekly": weekly}
```

**Test:**
```python
def test_count_by_periodicity():
    result = count_by_periodicity(habits)
    assert result["daily"] == 4  # ✅ PASSES
    assert result["weekly"] == 1  # ✅ PASSES
```

### Analytics API Endpoints

All analytics functions are exposed via REST API:

| Endpoint | Function | FP Technique |
|----------|----------|--------------|
| `GET /analytics/longest-streak` | `find_longest_streak_all()` | `map()` + `max()` |
| `GET /analytics/by-periodicity?period=daily` | `get_habits_by_periodicity()` | `filter()` + `lambda` |
| `GET /analytics/tracked-habits` | `get_all_tracked_habits()` | List comprehension |
| `GET /analytics/struggling?threshold=3` | `get_struggling_habits()` | `filter()` + `lambda` |
| `GET /analytics/summary` | `count_by_periodicity()` | Multiple `filter()` |

---

## 📦 Predefined Test Data

### Overview

The application comes with **5 predefined habits** with **4 weeks (28 days)** of realistic completion data.

### Generation Script

```bash
python generate_test_data.py
```

**File:** `backend/generate_test_data.py`

### Predefined Habits Details

#### Habit 1: Drink Water (Daily)
```python
{
    "name": "Drink Water",
    "specification": "Drink 8 glasses of water throughout the day",
    "periodicity": "daily",
    "completion_rate": 0.9,  # 90%
    "expected_completions": 25/28 days,
    "expected_current_streak": ~7 days,
    "expected_longest_streak": ~12 days
}
```

#### Habit 2: Exercise (Daily)
```python
{
    "name": "Exercise",
    "specification": "Complete 30 minutes of physical activity",
    "periodicity": "daily",
    "completion_rate": 0.7,  # 70%
    "expected_completions": 20/28 days,
    "expected_current_streak": ~3 days,
    "expected_longest_streak": ~8 days
}
```

#### Habit 3: Read Book (Daily)
```python
{
    "name": "Read Book",
    "specification": "Read for at least 20 minutes before bed",
    "periodicity": "daily",
    "completion_rate": 0.6,  # 60%
    "expected_completions": 17/28 days,
    "expected_current_streak": ~2 days,
    "expected_longest_streak": ~5 days
}
```

#### Habit 4: Weekly Review (Weekly)
```python
{
    "name": "Weekly Review",
    "specification": "Review and plan weekly goals every Sunday",
    "periodicity": "weekly",
    "completion_rate": 1.0,  # 100%
    "expected_completions": 4/4 weeks,
    "expected_current_streak": 4 weeks,
    "expected_longest_streak": 4 weeks
}
```

#### Habit 5: Meditation (Daily)
```python
{
    "name": "Meditation",
    "specification": "Practice 10 minutes of mindfulness meditation",
    "periodicity": "daily",
    "completion_rate": 0.8,  # 80%
    "expected_completions": 22/28 days,
    "expected_current_streak": ~5 days,
    "expected_longest_streak": ~9 days
}
```

### Data Characteristics

✅ **Realistic Patterns:**
- High compliance habit (90%)
- Moderate compliance habits (70-80%)
- Struggling habit (60%)
- Perfect weekly habit (100%)

✅ **Time Series Data:**
- Spans exactly 4 weeks (28 days)
- Random times throughout each day
- Realistic gaps and streaks

✅ **Used in Unit Tests:**
```python
@pytest.fixture
def predefined_habits(test_db):
    """Load 5 predefined habits with 4 weeks data"""
    # Used in multiple tests
    # Verifies streak calculations
    # Tests analytics functions
```

### Verification

After generation, verify data:

```bash
# Check database
sqlite3 data/habits.db "SELECT COUNT(*) FROM habits;"
# Expected: 5

sqlite3 data/habits.db "SELECT COUNT(*) FROM completions;"
# Expected: ~88 (sum of all completions)

# Check via API
curl http://localhost:5000/api/habits | python -m json.tool
```

---

## 📚 API Documentation

### Base URL

```
http://localhost:5000/api
```

### Endpoints Summary

| Method | Endpoint | Description |
|--------|----------|-------------|
| **Habits** |
| GET | `/habits` | List all habits |
| POST | `/habits` | Create new habit |
| GET | `/habits/:id` | Get specific habit |
| DELETE | `/habits/:id` | Delete habit |
| POST | `/habits/:id/check-off` | Mark as completed |
| **Analytics** |
| GET | `/analytics/longest-streak` | Overall longest streak |
| GET | `/analytics/by-periodicity` | Filter by period |
| GET | `/analytics/tracked-habits` | List habit names |
| GET | `/analytics/struggling` | Low-streak habits |
| GET | `/analytics/summary` | Complete statistics |

### Detailed Endpoint Documentation

[See full API documentation in API_REFERENCE.md]

---

## ✨ Code Quality

### Python Naming Conventions

✅ **snake_case** for functions and variables:
```python
def calculate_current_streak(self):
def get_habits_by_periodicity(habits, period):
habit_service = HabitService()
```

✅ **PascalCase** for classes:
```python
class Habit(Base):
class HabitManager:
class AnalyticsService:
```

✅ **UPPER_CASE** for constants:
```python
API_BASE_URL = "http://localhost:5000/api"
PERIODICITY_DAILY = "daily"
```

✅ **Descriptive names:**
```python
# Good
def calculate_longest_streak(self):
    
# Bad
def calc_ls(self):
```

### Code Comments

Every file, class, and complex function has:

✅ **Docstrings:**
```python
def calculate_current_streak(self, current_date: datetime = None) -> int:
    """
    Calculate the current unbroken streak up to current_date.
    
    For daily habits: checks for consecutive days
    For weekly habits: checks for consecutive weeks
    
    Args:
        current_date: Reference date (defaults to now)
        
    Returns:
        The current streak count (days or weeks)
        
    Example:
        >>> habit.calculate_current_streak()
        7
    """
```

✅ **Inline comments for complex logic:**
```python
# Check backwards from current date
check_date = current_date.date()

while True:
    # Check if there's a completion on this date
    has_completion = any(
        c.completion_date.date() == check_date
        for c in self.completions
    )
    
    if has_completion:
        streak += 1
        check_date -= timedelta(days=1)  # Move to previous day
    else:
        break  # Streak is broken
```

### .gitignore

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
*.egg-info/

# Database
*.db
*.sqlite3

# Environment
.env
.env.local

# IDE
.vscode/
.idea/
*.swp

# Testing
.pytest_cache/
.coverage
htmlcov/

# OS
.DS_Store
Thumbs.db

# Node
node_modules/
dist/
```

---

## 🎯 Final Checklist

- [x] ✅ **Project uploaded to GitHub** (not zipped)
- [x] ✅ **Comprehensive README** with installation guide
- [x] ✅ **Unit test suite** (45 tests, 92% coverage)
- [x] ✅ **Screenshots** of 5 default habits and streaks
- [x] ✅ **Python naming conventions** followed
- [x] ✅ **.gitignore** configured (no __pycache__, *.db)
- [x] ✅ **Modular structure** (40+ files, logically split)
- [x] ✅ **Code comments** on all functions/classes
- [x] ✅ **Analytics module complete** (all 6 functions)
- [x] ✅ **Streak calculation respects periodicity**
- [x] ✅ **4 weeks of predefined data**
- [x] ✅ **Database schema documented**
- [x] ✅ **Test coverage report** included

---

## 📞 Support

For questions or issues:

**Student:** Blessing Oluwapelumi James  
**Matric No:** 92134091  
**Email:** [your-email@example.com]  
**GitHub:** [github.com/yourusername/habit-tracker]

---

## 📄 License

MIT License - See LICENSE file for details

---

**Last Updated:** January 17, 2026  
**Version:** 1.0.0  
**Status:** ✅ Ready for Phase 3 Submission

---

## 🎉 Quick Start Commands

```bash
# Backend
cd backend && pip install -r requirements.txt
python generate_test_data.py
python run.py

# Frontend (new terminal)
cd frontend && npm install && npm run dev

# Tests
cd backend && pytest tests/ -v --cov=app
```

**Application:** http://localhost:3000  
**API Docs:** http://localhost:5000  
**Test Coverage:** htmlcov/index.html