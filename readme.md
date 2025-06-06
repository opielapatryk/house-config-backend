# 🏠 House Config Backend

A modular Django backend following **Clean Architecture**, **TDD (Test-Driven Development)**, and best practices for maintainability and scalability.

---

## 📦 Project Structure

```text
house-config-backend/
├── apps/
│   └── users/
│       ├── domain/
│       ├── application/
│       ├── infrastructure/
│       ├── migrations/
│       ├── presentation/
│       └── tests/
├── configurator/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── run_tests.sh
├── pytest.ini
├── requirements.txt
└── README.md

🧱 Architectural Layers
	•	Domain: Business models and core logic (pure Python)
	•	Application: Use cases and business rules
	•	Infrastructure: Django models, serializers, ORM adapters
	•	Interface (optional): APIs, views, and external I/O

⸻

🚀 Getting Started

1. Clone the repository

git clone https://github.com/opielapatryk/house-config-backend.git
cd house-config-backend

2. Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Create migrations

python manage.py makemigrations

5. Apply migrations

python manage.py migrate

6. Run development server

python manage.py runserver


⸻

✅ Testing

This project uses pytest with TDD principles.

Run tests

pytest

Or run tests in a specific app:

pytest apps/users

Sample test command (with config)

# pytest.ini
[pytest]
pythonpath = .


⸻

📐 Tech Stack
	•	Python 3.11+
	•	Django 4.x
	•	pytest
	•	Clean Architecture
	•	Modular App Structure

⸻

🧪 TDD Workflow (Suggested)
	1.	Write test first in apps/<feature>/tests/
	2.	Create minimal implementation in domain or application
	3.	Run tests with pytest
	4.	Refactor, repeat 🔁

⸻

🗃️ License

MIT License. See LICENSE for details.

⸻

👨‍💻 Author

Patryk Opiela
📍 Kraków, Poland
🧠 BSc Informatics | Backend Developer

⸻


---