# Kevin Nguyen Bot for Discord

## Preview ##
![Preview Image 1](https://raw.githubusercontent.com/mattlau1/Kevin-Nguyen-Bot/master/preview/Preview.jpg)

## About ##
This bot was supposed to be a joke but now it has random features(?)

## Usage ##
Create a new file 'secret_token.py' inside a new folder called secret and insert the following code:
```
# This should be in kevin-nguyen-bot/src/secret/secret_token.py
class token_class():
    def get_token(self):
        self.token = 'REPLACE WITH TOKEN'
        return self.token
```

Install Requirements with ``` pip3 install -r requirements.txt ```

Run with ``` python3 bot.py ```


## Features ##
  - LoL champion build [Usage: /build [lane] [champion]]
      - Uses http://lol.lukegreen.xyz/ API to scrape op.gg data
      - Sends top five builds for champion in specified lane
      - Sends most popular runes, scraped using Selenium
