artstation-scrape-likes
====
This is a python script to download all the images from your artstation likes to the location of the script.

Quick install guide:
----
1. Download/clone repository

2. Install python 3: https://www.python.org/downloads/

3. Install selenium:
```
pip3 install selenium
```

4. Download chromedriver: https://sites.google.com/a/chromium.org/chromedriver/

5. Add chromedriver to $PATH

Running the script:
----
1. cd to the location of the script.

2. Execute in terminal:

```
python3 artstation_selenium_scrape.py 
```
3. Input your artstation username.

4. Wait until it is done!

If the artstation like counter does not equal the actual amount of likes:
----
The script will count the amount of likes it has found, if it hits the same amount of likes 3 times it will request input, here you can put the amount of likes there actually are.

Or if you think it should have more likes just hit enter and it will continue trying to find more likes.
