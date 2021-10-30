## BUILD INSTRUCTIONS ##

For the basic functionality:

1) Run pip3 -r requirements.txt. This will grab Flask, Requests and gunicorn
2) Run the command: python3 app.py. The app will be running on port 3000, this can be changed in config.py

To have it run in the background:

1) Edit chainalysis.service to have the correct paths to where the project is and where gunicorn is installed
2) run install.sh. This will install the python requirements and copy chainalysis.service to /etc/systemd/system
3) run the command: sudo systemctl start chainalysis





