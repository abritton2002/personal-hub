# Personal Knowledge Hub (Second Brain)

A self-hosted personal productivity and knowledge management app. Designed for developers, builders, and lifelong learners to capture, organize, and reflect on their knowledge, project work, online discoveries, and blog ideas.

## Features

- 📥 Capture entries for: learning notes, project updates, blog ideas, online finds
- 🔍 View all entries in a searchable dashboard
- 📊 Tag cloud, entry type stats, learning streaks
- 🔗 Auto-link GitHub projects and embed Tweet previews (future)
- 💾 Local SQLite database with timestamped entries
- 🎨 Clean, modern UI with dashboard visuals
- 🔐 Private by default, but can be made remotely accessible via Ngrok or Tailscale

## Tech Stack
- **Language:** Python 3
- **Framework:** Flask
- **Database:** SQLite
- **Frontend:** HTML5, CSS3 (Tailwind), Jinja2 templates

## Setup

1. **Clone the repo:**
   ```bash
   git clone https://github.com/abritton2002/personal-hub.git
   cd personal-hub
   ```
2. **Create a virtual environment and activate it:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment variables:**
   - Create a `.env` file with your secrets (see below).
5. **Run the app:**
   ```bash
   python run.py
   ```
   The app will be available at `http://localhost:5050`.

## Environment Variables Example
```
SECRET_KEY=your_flask_secret_key
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_USERNAME=your_github_username
SUBSTACK_URL=https://yourname.substack.com/feed
```

## Usage
- Visit the dashboard to capture ideas, view project updates, and see your latest Substack articles.
- Click "View README" on any GitHub project to see its overview.
- Mobile-friendly and can be accessed remotely with Ngrok or Tailscale.

## Folder Structure
```
personal-hub/
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── templates/
│   └── __init__.py
├── venv/
├── .gitignore
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## License
MIT 