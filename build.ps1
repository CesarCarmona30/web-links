venv/Scripts/activate
pip install --upgrade pip
pip install -r requirements.txt
rm public
reflex init
reflex export --frontend-only
Expand-Archive -Path C:\Users\cesar\Documents\Development\Webs\web-links\frontend.zip -DestinationPath C:\Users\cesar\Documents\Development\Webs\web-links\public
rm frontend.zip
deactivate