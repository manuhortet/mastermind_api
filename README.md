# Mastermind Rest API
Rest API made on Python and Flask to play the [Mastermind game](https://en.wikipedia.org/wiki/Mastermind_(board_game))

## How to
Execute the file `run.py` to launch the Flask app:
```
python3 run.py
```

### Creating a new game
To create a new game, send a GET request to ```<HOST>:<PORT>/new_game```

For example, using curl:
```
curl http://<HOST>:<PORT>/new_game
```
**Note:** The default value for `<HOST>:<PORT>` is `localhost:5000` but it can be edited on `app/configuration.py`

### Trying to guess the code
To try a new guess, send a PUT request to ```<HOST>:<PORT>/new_guess``` adding your guess as a json.
The correct format for the guess can be seen in the example:
```
curl -H 'Content-Type: application/json' -X PUT -d '["BLUE", "BLUE", "BLUE", "BLUE"]' http://<HOST>:<PORT>/new_guess
```

### Checking last guesses
To check the guesses history, just send a GET request to `<HOST>:<PORT>/history`
```
curl http://<HOST>:<PORT>/history
```
