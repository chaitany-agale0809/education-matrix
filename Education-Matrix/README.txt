============================================================
  EDUCATION MATRIX — Flask Web Application
============================================================

HOW TO RUN:
-----------
1. Install Python 3.8+ if not already installed

2. Install Flask:
   pip install flask

3. Run the app:
   python app.py

4. Open browser and go to:
   http://127.0.0.1:5000

============================================================
LOGIN CREDENTIALS:
------------------
  Admin :  admin@gmail.com  /  admin123
  Users :  Register via the Register page

============================================================
FULL NAVIGATION FLOW:
---------------------
  /                  → Home (Login / Register buttons)
  /login             → Login page
  /register          → Register new account
  /dashboard         → Student dashboard (after login)
  /logout            → Logout

  /edu/              → Education Matrix splash screen
  /edu/main          → Year selection (FE / SE / TE / BE)
  /edu/fe            → First Year subjects (hexagon layout)
  /edu/se            → Second Year (coming soon)
  /edu/te            → Third Year (coming soon)
  /edu/be            → Fourth Year (coming soon)
  /edu/fe/bxe        → Basic Electronics Engineering (PDFs)
  /edu/fe/ccc        → Co-Curricular Activities (PDFs)

============================================================
PROJECT STRUCTURE:
------------------
  app.py
  requirements.txt
  database.db          ← auto-created on first run
  static/
    image/             ← bg.jpg, fe.jpg, sppu.jpg
    files/FE/
      bxe/             ← 3 PDF files
      ccc/             ← 3 PDF files
  templates/
    index.html         ← landing page
    login.html
    register.html
    dashboard.html
    admin.html
    edu/
      index.html       ← splash screen
      main.html        ← year selection
      fe.html          ← FE subjects
      se.html, te.html, be.html
      fe_html_files/
        bxe.html
        ccc.html

============================================================
