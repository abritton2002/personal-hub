# Personal Hub

A personal website and dashboard to showcase your GitHub projects, Substack articles, and more—all in one place. Built for developers and creators who want a modern, minimalist, and self-hosted way to present their work, writing, and online presence.

## Features

- 🛠 **GitHub Integration:** Display your latest repositories and view project READMEs directly on your site.
- 📰 **Substack Integration:** Show your latest Substack articles with thumbnails and summaries.
- 📊 **Dashboard:** Clean, modern UI with a responsive layout for desktop and mobile.
- 🔍 **Quick Access:** Jump to your projects, blog, or journal from a single hub.
- 🔐 **Private by default:** Runs locally or on your own server (Raspberry Pi, Linux, etc.).

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
   The app will be available at `http://localhost:5050` (or your Pi's IP).

## Environment Variables Example
```
SECRET_KEY=your_flask_secret_key
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_USERNAME=your_github_username
SUBSTACK_URL=https://yourname.substack.com/feed
```

## Usage
- Visit your dashboard to see your latest GitHub projects and Substack posts.
- Click "View README" to see project overviews.
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