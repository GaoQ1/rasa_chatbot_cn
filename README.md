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
- [rasa-nlu的究极形态](https://www.jianshu.com/p/553e37ffbac0)
- [闲聊模型的实践并应用到rasa](https://www.jianshu.com/p/bccf2321bd50)

## Introduction
五月份rasa官方发布了release版本，做了比较大的改动。介于此，[rasa_chatbot_cn](https://github.com/GaoQ1/rasa_chatbot_cn)这个demo也做出相对应的更新，更新到master分支上。之前基于`0.13`的版本在0.13.x分支上，你可以自由切换。新版本中将命令行做的十分简便，具体命令如下。
> 欢迎加入**rasa微信闲聊群**，微信请加：coffee199029

**edit at 2019.06.24**
将之前的[rasa-nlu-gao](https://github.com/GaoQ1/rasa_nlu_gq)进行了修改，以支持新版本的rasa，而且不再在源码里进行修改。首先需要`pip install rasa-nlu-gao>=0.3.1`，具体用法如下。

## Running by command
### install packages
 - python >= 3.6
```
pip install -r requirements.txt
```
下载依赖package

### train model
```
make train
```
训练nlu和core模型，新版本中会将模型自动打包成zip文件。

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

**[edit 2019.06.24]**
继续上次所说的对rasa-nlu-gao进行修改，现在可以直接使用原来rasa-nlu-gao里面的组件。
 - 首先`pip install rasa-nlu-gao>=0.3.1`
 - 下面只需要在*config.yml*中配置：
```
- name: "rasa_nlu_gao.extractors.jieba_pseg_extractor.JiebaPsegExtractor"
  part_of_speech: ["nr"]
```
其他组件也是这样用，具体可参照[README.md](https://github.com/GaoQ1/rasa_nlu_gq/blob/master/README.md)。
而如果是你自己的组件可以放到components里面，如果你想做贡献，欢迎fork [rasa-nlu-gao](https://github.com/GaoQ1/rasa_nlu_gq)，并提交pr。

## use rasa x
rasa新版本中，增加了rasa x这个功能。这里也做了尝试，感觉挺方便。

### install rasa x
```
pip install rasa-x --extra-index-url https://pypi.rasa.com/simple
```
下载rasa-x package

### use rasa x
```
make run-x
```
没错就是这么简单。Have a fun!

## some problems
 Q: 为什么我会报`couldn't find component...`这个错？

 A: rasa使用了importlib动态加载自定义component和policy。这个错误的原因是你没有将component和policy的目录append到PYTHONPATH里面。你需要`export PYTHONPATH=/path/to/your/component`

 Q: 为什么训练会报10000time超时错误？

 A: 这个问题是因为你没有启用bert-as-service服务。启动教程参考[rasa对话系统踩坑记（八）](https://www.jianshu.com/p/6a93209c48a4)，启动之后在config.yml将对用的bert-as-service服务ip改下，本例子默认是127.0.0.1，但是你要在本机启动bert服务

 Q: 如何能够快速尝试例子呢?

 A: 介于各个开发环境不同，报各种错误，所以上传了docker文件。但前提还是你要安装docker，并在运行前确保bert-as-service启用，当然你不用bert的话可以忽略。然后你只需要`sh dev/deploy_dev.sh`，就可以愉快的通过postman或者curl测试这个demo了。记得`docker logs -f chatbot_dev`查看有没有训练完，有没有报错。linux和mac下没有问题。windows下可能需要微调下。
