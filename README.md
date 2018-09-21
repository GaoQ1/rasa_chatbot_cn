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
**total_word_feature_extractor.dat**可去https://pan.baidu.com/s/1-ma0ndXBWL0rnbUqCAcL-w ，密码：lhi4 下载。nlu_model_config.yml中的pipeline可自定义，这里由于数据量较少，用了开源的方法和词向量。


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

## Some tips
### rename and count story
utils/re_story.py 是用来对mobile_story.md里面的故事进行重命名和重新计数
### auto generate rasa_dataset_training.json
data/rasa_dataset_training.json 是通过一些规则自动生成的，节省很多人力。仓库是[chatito_gen_nlu_data](https://github.com/GaoQ1/chatito_gen_nlu_data)
具体用法可参考[官方文档](https://rodrigopivi.github.io/Chatito/)
