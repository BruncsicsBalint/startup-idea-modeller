# Setup
## Backend
- Initial setup
  - ```python -m venv venv```
  - Windows: ```venv\Scripts\activate```
  - Unix or macOS: ```source venv/bin/activate```
  - ```pip install -r requirements.txt```
- Start venv
  - Windows: ```venv\Scripts\activate```
  - Unix or macOS: ```source venv/bin/activate```
- Exit venv: 
  - ```deactivate```
## Frontend 
- ```npm install```

# Start app
## Backend
- Start venv
  - Windows: ```venv\Scripts\activate```
  - Unix or macOS: ```source venv/bin/activate```
- Run app
  - ```uvicorn app.main:app --reload```
- Exit venv: 
  - ```deactivate```

## Frontend
- ```npm run dev```