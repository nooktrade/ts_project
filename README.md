# "ASK ME" Mini Quora Platform - Django Based Q&A Web App

A simple question and answer web application like Quora, built using Django, where users can ask questions, answer them, and like answers.

---

## Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## How to Use

### Navigation Bar

- Home – Displays all answered questions.
- Answer Me – Lists questions that are not yet answered.
- My Questions – Shows questions asked by the logged-in user.
- Ask Question – Form to post a new question.
- Login / Sign Up – User authentication system.

---

### User Flow

1. Register 2-3 accounts (To ask , Answer and Like) using the Sign Up option.
2. After registration, you’ll be redirected to the Home page.
3. Already registered? Use the Login page.
4. Initially, Home will be empty (no answered questions).
5. Post a question via Ask Question.
6. That question will appear under My Questions for the user who posted it.
7. It will also be listed in Answer Me for all users (since it’s unanswered).
8. Login from another account and answer the question via Answer Me.
9. Once answered, it will appear on the Home page.
10. On the Home page, users can also Like answers.
11. Click on the username in the top-right corner to access Profile or Logout.

---

## Key Functional Notes

- Only answered questions are visible on the Home page.
- Unanswered questions appear under the Answer Me tab.
- To answer, go to Answer Me and click the "Answer me" button.
- All critical views (asking, answering, liking) require login.
- UI is responsive and mobile-friendly.

---

## Tech Stack

- Backend: Django
- Frontend: HTML, Bootstrap
- Database: SQLite (default)

---

Tip: Make sure you run `makemigrations` and `migrate` before starting the development server.
