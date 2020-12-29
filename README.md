# jdaobot for Discord
## About ##
This bot was supposed to be a joke but now it has random features(?)

## Usage ##
Create a new file 'secret_token.py' inside a new folder called secret and insert the following code:
```
# This should be in jdaobot/secret/secret_token.py
class token_class():
    def get_token(self):
        self.token = 'REPLACE WITH TOKEN'
        return self.token
```

Run using 
``` python3 bot.py ```

## Features ##
  - jdaomode on [Usage: /jdaomode]
      - changes avatar to jdao1's avatar
      - changes nickname to jdao1
      - sends random jdao1 quote on every message
      - sends "hi ____" if "i'm ____" is detected
  - jdaomode off [Usage: /jdaomode]
      - changes avatar to Kevin Nguyen
      - changes nickname to Kevin Nguyen
      - sends "kys echau" on every message [ITS A JOKE]
  - League of Legends champion build [Usage: /build [lane] [champion]]
      - uses http://lol.lukegreen.xyz/ api to scrape opgg data
      - sends top 5 builds for champion in specified lane
