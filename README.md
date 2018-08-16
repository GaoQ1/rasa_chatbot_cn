## train nlu model
```
python bot.py train-nlu
```

## test nlu model

### Run the rasa_nlu server
```
python -m rasa_nlu.server -c mobile_nlu_model_config.yml --path models
```

### Open a new terminal and now you can curl results from the server, for example:
```
$ curl -X POST localhost:5000/parse -d '{"q":"我发烧了该吃什么药？", "project": "nlu", "model": "current"}' | python -mjson.tool
```

## train dialogue
```
python bot.py train-dialogue
```

## test
```
python bot.py run
```