## BUILD INSTRUCTIONS ##

For the basic functionality:

1) Run pip3 -r requirements.txt. This will grab Flask, Requests and gunicorn
2) Run the command: python3 app.py. The app will be running on port 3000, this can be changed in config.py

To have it run in the background:

1) Edit chainalysis.service to have the correct paths to where the project is and where gunicorn is installed
2) Run install.sh. This will install the python requirements and copy chainalysis.service to /etc/systemd/system
3) Run the command: sudo systemctl start chainalysis

## QUESTIONNAIRE ##

1) Are there any sub-optimal choices( or short cuts taken due to limited time ) in your implementation?


* There are some inefficient for loops that do not scale well for updating the prices.
* The updating of prices happens in a daemon thread that probably could be implemented better.
* The format of the config file could be changed to be more human readable.


2) Is any part of it over-designed? ( It is fine to over-design to showcase your skills as long as you are clear about it)


* The app is designed to be hyper modular to work with a large number of cryptocurrencies aside from BTC and ETH as well as any apis that follows the format <api url>/<coin> and return JSON with the price of the coin.


3) If you have to scale your solution to 100 users/second traffic what changes would you make, if any?


* I would first increase the amount of workers in gunicorn.

4) What are some other enhancements you would have made, if you had more time to do this implementation

* I would add a chart to clearly illustrate the differences between the exchanges and improve the look of the frontend. 
* I would also add unit/load testing with k6.js







