# Rasa Core and Rasa NLU
- What do Rasa Core & NLU do? 
  [Read About the Rasa Stack](https://rasa.com/products/rasa-stack/)

## Introduction
这个项目是参考了[_rasa_chatbot](https://github.com/zqhZY/_rasa_chatbot)。_rasa_chatbot存在的问题，一是版本更新不及时，API没有做相应的更改；二是里面的story太少。
由于rasa社区最近版本更新很频繁，以前很多方法被弃用，而且还增加了好多新的功能，这个demo比较全面和及时。
```
rasa-nlu:      0.13.4
rasa-core:     0.11.4
rasa-core-sdk: 0.11.4
```

## Command
### train nlu model
```
python bot.py train-nlu
```

### train dialogue
```
python bot.py train-dialogue
```

### train dialogue in online mod
```
python -m rasa_core_sdk.endpoint --actions actions &
python -m rasa_core.train --online -o models/dialogue -d mobile_domain.yml -s data/mobile_story.md --endpoints endpoints.yml
```

### test dialogue
```
python -m rasa_core_sdk.endpoint --actions actions &
python -m rasa_core.run --nlu models/nlu/default/current --core models/dialogue --endpoints endpoints.yml
```

### provide dialogue service
```
python -m rasa_core_sdk.endpoint --actions actions &
python -m rasa_core.train --online -o models/dialogue -d mobile_domain.yml -s data/mobile_story.md --endpoints endpoints.yml
```
