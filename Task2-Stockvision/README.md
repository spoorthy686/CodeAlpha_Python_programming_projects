# StockVision Pro – Smart Portfolio Manager

## Project Overview

StockVision Pro is an advanced stock portfolio management application developed using Python. The application allows users to manage stock investments through an interactive dashboard with portfolio tracking, analytics, data export functionality, and customizable settings.

This project enhances the original CodeAlpha Stock Portfolio Tracker task by implementing additional real-world features and a modern graphical interface.

---

## Features

### Portfolio Management
- Add stocks with quantity and price
- Portfolio value calculation
- Track multiple stock holdings
- Remove stocks from portfolio
- Dynamic stock cards display

### Analytics Features
- Total portfolio value tracking
- Total stock count display
- Investment analysis
- Portfolio performance insights

### User Features
- User authentication system
- Login and registration functionality
- User-specific portfolio management

### Export Features
- Export portfolio data
- Export analytics reports
- Save investment information

### User Interface Features
- Interactive dashboard
- Modern GUI design
- Dark mode support
- Light mode support
- Settings panel
- Responsive interface

---
## Project Structure

```text
StockVision/
│
├── main.py
│
├── assets/
│   ├── logo.png
│   └── images/
│       └── Dashboard_banner.png
│
├── core/
│   ├── auth.py
│   ├── portfolio_manager.py
│   ├── stock_manager.py
│   ├── analytics.py
│   ├── simulator.py
│   ├── charts.py
│   └── export_manager.py
│
├── ui/
│   ├── login_screen.py
│   ├── register_screen.py
│   ├── dashboard.py
│   ├── add_stock_screen.py
│   ├── portfolio_screen.py
│   ├── analytics_screen.py
│   ├── watchlist_screen.py
│   ├── simulator_screen.py
│   └── settings_screen.py
│
├── data/
│   ├── users.json
│   ├── portfolio.json
│   └── exports/
│       ├── portfolio_report.csv
│       └── analytics_report.csv
│
├── requirements.txt
├── README.mdS
```

---
## Technologies Used

- Python
- CustomTkinter
- Tkinter
- File Handling
- JSON

---

## Concepts Applied

- Object-Oriented Programming
- Authentication Systems
- GUI Development
- Data Management
- File Handling
- Event-driven Programming

---

## How to Run

Clone the repository:

```bash
git clone <repository-link>
```

Navigate to project directory:

```bash
cd StockVisionPro
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

## Learning Outcomes

Through this project I gained practical experience in:

- Portfolio management concepts
- Building authentication systems
- GUI development using Python
- Data storage and management
- Application design principles
- Developing user-friendly dashboards

---

## Developed During

CodeAlpha Python Programming Internship

---

## Author

Katkuri Spoorthy