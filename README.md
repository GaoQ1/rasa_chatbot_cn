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
五月份rasa官方发布了release版本，做了比较大的改动。介于此，[rasa_chatbot_cn](https://github.com/GaoQ1/rasa_chatbot_cn)这个demo也做出相对应的更新，更新到master分支上。之前基于`0.13`的版本在0.13.x分支上，你可以自由切换。

## Command
### install packages
```
pip install -r requirements.txt
```
下载依赖package

### train model
```
make train
```
训练nlu和core模型，新版本中会将模型自动打包成zip文件

### run model
```
make run
```

### test in cmdline
```
make run-cmdline
```
可以在命令行中测试

### test by http server
`http://localhost:5005/webhooks/rest/webhook` post请求，请求参数例如：
```
{
    "sender": "0001",
    "message": "你好"
}
```
可以使用postman去请求调用

## Some magical functions
之前在[rasa-nlu-gao](https://github.com/GaoQ1/rasa_nlu_gq)增加了若干个自定义组件。而在release版本中可以直接将组建在外部调用，比如这里我举个之前的`JiebaPsegExtractor component`的栗子，直接将该组建放在*components*下面，在*config.yml*中：
```
- name: "components.extractors.jieba_pseg_extractor.JiebaPsegExtractor"
  part_of_speech: ["nr"]
```
这样就ok了，后续我会考虑将rasa-nlu-gao重新修改下。
