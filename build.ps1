venv/Scripts/activate
pip install --upgrade pip
pip install -r requirements.txt
Remove-Item public
reflex init
reflex export --frontend-only
Expand-Archive frontend.zip public
Remove-Item frontend.zip
deactivate