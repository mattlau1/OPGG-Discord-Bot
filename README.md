# Kevin Nguyen Bot for Discord

## Preview ##
![Preview Image 1](https://raw.githubusercontent.com/mattlau1/Kevin-Nguyen-Bot/master/preview/Preview.jpg)

## Features ##
- League of Legends champion build [Usage: /build [lane] [champion]]
    - Uses http://lol.lukegreen.xyz/ api to scrape OP.GG data
    - Sends top 5 builds for champion in specified lane
    - Lanes: [ top | mid | jg | adc | sup ]
    - Usage: /build top katarina
- OP.GG Search [Usage: /opgg [region]\(optional) [name]]
    - Sends OP.GG page
    - Defaults to Discord username if no name or region specified
    - Regions: [ oce | na | las | jp | br | tr | ru | eune | kr | lan | euw ]
    - Usage: /opgg kr hide on bush

## Setup ##
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
