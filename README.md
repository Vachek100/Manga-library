# Manga Library Management System

[🇨🇿 Česká verze níže](#česká-verze)

## 📚 English Version

### Project Description
A web application for managing manga collections in libraries. Users can:
- Browse available manga titles
- Borrow and return manga
- Search through the collection
- View detailed information about each manga

### 🚀 Installation Guide

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Vachek100/manga-library.git
   cd manga-library
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**:
   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - Main page: http://localhost:8000
   - Admin: http://localhost:8000/admin

### 🛠️ Project Structure
```
manga_library/
├── library/          # Main app with manga management
├── manga_library/    # Project configuration
├── templates/        # HTML templates
├── static/           # CSS and static files
├── media/            # Uploaded manga covers
├── requirements.txt  # Dependencies
└── README.md         # This file
```

---

<a id="česká-verze"></a>
## 📚 Česká verze

### Popis projektu
Webová aplikace pro správu mangy v knihovnách. Uživatelé mohou:
- Prohlížet dostupné tituly mangy
- Půjčovat a vracet mangu
- Vyhledávat v kolekci
- Zobrazovat podrobné informace o každé mangě

### 🚀 Návod k instalaci

1. **Naklonujte repozitář**:
   ```bash
   git clone https://github.com/Vachek100/manga-library.git
   cd manga-library
   ```

2. **Vytvořte a aktivujte virtuální prostředí**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Na Windows: venv\Scripts\activate
   ```

3. **Nainstalujte závislosti**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Spusťte migrace**:
   ```bash
   python manage.py migrate
   ```

5. **Vytvořte superuživatele**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Spusťte vývojový server**:
   ```bash
   python manage.py runserver
   ```

7. **Přístup k aplikaci**:
   - Hlavní stránka: http://localhost:8000
   - Administrace: http://localhost:8000/admin

### 🛠️ Struktura projektu
```
manga_library/
├── library/          # Hlavní aplikace pro správu mangy
├── manga_library/    # Konfigurace projektu
├── templates/        # HTML šablony
├── static/           # CSS a statické soubory
├── media/            # Nahrané obaly mangy
├── requirements.txt  # Závislosti
└── README.md         # Tento soubor
```
