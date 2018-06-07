## TextToPictures
一个自动化排版工具，可将大段文字打印到（多张）指定大小的图片。

### 功能
1. 可从文本文件中读取文字内容。
1. 根据给定的图片尺寸和字体大小，自动确定每张图片的文字数量，以及图片的数量。
2. 自动避免出现行首标点的问题。
3. 正确处理分段问题。
3. 可以指定字体、字号。
4. 可以指定页边距。
5. 可以指定行距。

### 示例
将朱自清的《荷塘月色》转成适合在iPhone 6s上阅读的图片。

代码：

```Python
import TextToPictures as TTP

if __name__ == "__main__":
    
    # 指定图片尺寸，iPhone 6s屏幕分辨率为750*1334。
    ttp = TTP.TextToPictures((750, 1334))
    
    # 从文件中导入《荷塘月色》全文。
    ttp.load_text('demo.txt')
    
    # 设置页边距均为40px，字体为微软雅黑，字号为35，行距为12px。
    pages_text = ttp.format_text((40, 40, 40, 40), font='msyh.ttc', font_size=35, spacing=12)

    # 生成图片。
    ttp.render()
    
    # 指定图片名称前缀为“demo”，保存图片。
    ttp.save('demo')
```

效果：

<img width="50%" height="50%" style="border: 1px gray" src="https://github.com/Reuynil/TextToPictures/blob/master/demo/demo-0.jpg"/>
<img width="50%" height="50%" style="border: 1px gray" src="https://github.com/Reuynil/TextToPictures/blob/master/demo/demo-1.jpg"/>
<img width="50%" height="50%" style="border: 1px gray" src="https://github.com/Reuynil/TextToPictures/blob/master/demo/demo-2.jpg"/>
<img width="50%" height="50%" style="border: 1px gray" src="https://github.com/Reuynil/TextToPictures/blob/master/demo/demo-3.jpg"/>
