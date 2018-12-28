# Rasa Core and Rasa NLU
## rasa对话系统系列文章
- [rasa对话系统踩坑记（一）](https://www.jianshu.com/p/5d9aa2a444a3)
- [rasa对话系统踩坑记（二）](https://www.jianshu.com/p/4ecd09be4419)
- [rasa对话系统踩坑记（三）](https://www.jianshu.com/p/ae028903d748)
- [rasa对话系统踩坑记（四）](https://www.jianshu.com/p/9393d319e698)
- [rasa对话系统踩坑记（五）](https://www.jianshu.com/p/eec63e56db07)
- [rasa对话系统踩坑记（六）](https://www.jianshu.com/p/21808ac8d409)
- [rasa对话系统踩坑记（七）](https://www.jianshu.com/p/405c087c2f7f)
- [rasa对话系统踩坑记（八）](https://www.jianshu.com/p/6a93209c48a4)
- [rasa对话系统踩坑记（九）](https://www.jianshu.com/p/1a4abe93635e)
- [rasa对话系统踩坑记（十）](https://www.jianshu.com/p/debcf0041fcb)

## Introduction
这个demo是用rasa-nlu完成slot filling和intent classify，用rasa-core完成DM(dialogue management)和NLG(natural language generate)。demo完成的对话主要有办理套餐和查询话费和流量，其他意图做了default回答。demo是参考了[_rasa_chatbot](https://github.com/zqhZY/_rasa_chatbot)。_rasa_chatbot存在的问题，一是版本更新不及时，API没有做相应的更改；二是没有自定义的component。
由于rasa社区最近版本更新很频繁，以前很多方法被弃用，而且还增加了好多新的功能，这个demo比较全面和及时。
```
rasa-nlu:      0.13.4
rasa-core:     0.12.3
rasa-core-sdk: 0.12.1
```

## Command
### train nlu model
```
python bot.py train-nlu
```
**total_word_feature_extractor.dat**可去https://pan.baidu.com/s/1-ma0ndXBWL0rnbUqCAcL-w ，密码：lhi4 下载。nlu_model_config.yml中的pipeline可自定义，这里由于数据量较少，用了开源的方法和词向量。如果你的rasa_dataset_training.json上数据足够多，可以尝试使用nlu_embedding_config.yml配置来训练nlu model.


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

### compare policy
```
python -m rasa_core.train compare -c keras_policy.yml embed_policy.yml -d mobile_domain.yml -s data/mobile_edit_story.md -o comparison_models/ --runs 3 --percentages 0 25 50 70
```

### evaluate policy
```
python -m rasa_core.evaluate compare -s data/mobile_edit_story.md --core comparison_models/ -o comparison_results/
```

## Some tips
### rename and count story
utils/re_story.py 是用来对mobile_story.md里面的故事进行重命名和重新计数
### auto generate rasa_dataset_training.json
data/rasa_dataset_training.json 是通过一些规则自动生成的，节省很多人力。仓库是[chatito_gen_nlu_data](https://github.com/GaoQ1/chatito_gen_nlu_data)
具体用法可参考[官方文档](https://rodrigopivi.github.io/Chatito/)


## Some magical functions
最近自己开源了基于rasa-nlu的[rasa-nlu-gao](https://github.com/GaoQ1/rasa_nlu_gq)新增了N多个个自定义组件，具体用法和说明请参考[rasa对话系统踩坑记](https://www.jianshu.com/u/4b912e917c2e)。那下面就是介绍如何使用了。
### 首先需要下载rasa-nlu-gao
```
pip install rasa-nlu-gao
```
### 训练模型
```
python bot.py train-nlu-gao
```
### 测试使用模型
```
python -m rasa_nlu_gao.server -c config_embedding_bilstm.yml --path models/nlu_gao/
```
后续[rasa-nlu-gao](https://github.com/GaoQ1/rasa_nlu_gq)会持续更新，也欢迎贡献。