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
rasa版本已经更新到了2.0版本，改动比较大，等2.0版本稳定后再跟进了。现在这里的代码还是去年上半年的版本，后面rasa做了很多改动，component已经支持bert，对中文的支持也更好。所以这个之前基于1.1.x的版本就转到1.1.x分支，目前master分支的话就分享最新的基于1.10.18的一套支持中文的pipeline
> 欢迎加入**rasa微信闲聊群**，微信请加：coffee199029

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

### run model
```
make run
```

### test in cmdline
```
make shell
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

### use rasa x
```
make run-x
```

### external link
[liveportraitweb](https://www.liveportraitweb.com/)
[novelling](https://www.novelling.com/)
[whatnovel](https://whatnovel.com/)
[omniparser](https://www.omniparser.net/)
[sexting](https://howtosexting.com/)
[Comprimirmp4](https://www.comprimirmp4.com/)
[Rewritifyai](https://www.rewritifyai.com/)
[Sprunki Phase 5](https://www.sprunkiphase5.net/)
[MMAudio](https://www.mmaudio.pro/)
[Creator Viral Video](https://www.creatorviralvideo.com/)
[Transpixar](https://www.transpixar.pro/)
[Flexvalorant](https://www.flexvalorant.com)
[Rednote](https://www.rednote.pro/)
[Body Visualizer](https://www.bodyvisualizer.org/)
[AI Kungfu](https://www.ai-kungfu.net/)
[Image To Video AI](https://imagetovideoai.space/)
[Deepseek Image](https://deepseekimage.net/)
[10minutes.one](https://10minutes.one/)
[Career Dreamer](https://www.careerdreamer.net/)
[Wanx2.1](https://www.wanx.run/)
[AudioX](https://audiox.app/)
[Image To Video AI](https://imagetovideoai.dev/)
[AI Girlfriend](https://ai-girlfriend.me/)
[AI Doll Generator](https://ai-doll-generator.com)
[FramePack](https://frame-pack.net/)
[mRNA](https://mrna.app/)
[GPT-Image-1](https://gpt-image-1.org/)
[Reverse Audio](https://audiox.app/reverse-audio)
[Video to Audio Converter](https://audiox.app/video-to-audio-converter)
[Remove Audio From Video](https://audiox.app/remove-audio-from-video)
[Add Audio to Video](https://audiox.app/add-audio-to-video)
[Extract Audio from Video](https://audiox.app/extract-audio-from-video)
[Convert Video to Audio](https://audiox.app/convert-video-to-audio)
[Audio Remover](https://audiox.app/audio-remover)
[How to Remove Audio From Video](https://audiox.app/how-to-remove-audio-from-video)
[Text to Speech](https://audiox.app/text-to-speech)
[Lyria 2](https://audiox.app/lyria2)
[Sound Effects](https://audiox.app/sound-effects)
[AI Mermaid](https://audiox.app/ai-mermaid)
[AI Kiss](https://audiox.app/ai-kiss)
[Flux Kontext](https://audiox.app/flux-kontext)
[Kling 2.1](https://audiox.app/kling-2-1)
[Wan 2.1](https://audiox.app/wan2-1)
[SYFM](https://audiox.app/sound-effects/syfm)
[Lip Sync](https://lip-sync.net/)
