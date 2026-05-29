
@echo off
echo Starting Ticketmaster Server...
echo Server will be available at http://localhost:8000
echo Press Ctrl+C to stop the server
python -m http.server 8000
pause
