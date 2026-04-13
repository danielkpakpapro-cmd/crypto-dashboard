Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd /c cd /d C:\Users\utilisateur\Documents\algopy\crypto-dashboard && venv\Scripts\activate && streamlit run app.py", 0, False
WScript.Sleep 3000
WshShell.Run "http://localhost:8501"