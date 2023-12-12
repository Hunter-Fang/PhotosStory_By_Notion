# PhotosStory_By_Notion

# 用Notion搭一个时间轴画廊

一个使用 简易JS + Python Flask + Notion API 实现的，部署在 Vercel 上的静态相册，主要以时间轴形式展示。为Notion和一些需要摄影展示的朋友设计。

---

# **序章**

方师傅在上次弄完基于Airtale的时间轴画廊后，发现真的确实不好用，比如说管理和请求裸奔。

以前一直都用的notionAPI相关平台搭的博客，效果确实不错，主要是自己在notion上的沉默成本太多了，懒得弄别的地方又不想单独存这些

这次也想学学来试试，先从最简单的database调用属性字段开始

好在自己的时间轴画廊需要的字段并不多，自己的灵感所需：

| 字段 | 属性 | 是否必填 |
| --- | --- | --- |
| 时间 | Date（年月日） | 是 |
| 发生地 | LongText | 是 |
| 故事 | LongText | 是 |
| 照片 | File | 是 |

# **预览效果**

Demo地址：[TimeStory-Photos (helloiamazi.work)](https://timeline.helloiamazi.work/)

- PC/MAC WEB端效果

![image](https://github.com/Hunter-Fang/PhotosStory_By_Notion/assets/50197260/2d615e2b-e42e-49a8-8045-36135e47bbbc)


- 移动端效果

![image](https://github.com/Hunter-Fang/PhotosStory_By_Notion/assets/50197260/e198ed1b-6d1e-47cd-a9ba-780772c64ef9)


# **如何部署**

很简单，可以参考以下流程：

![image](https://github.com/Hunter-Fang/PhotosStory_By_Notion/assets/50197260/02865365-3c6a-4082-82f7-af582ac1d528)


**准备工作：**

1.Duplicate页面模版，并publish online，获取相关Database ID

[TimeLine (notion.site)](https://www.notion.so/e649801ccfa24c59b903148531d60783?pvs=21)

![image](https://github.com/Hunter-Fang/PhotosStory_By_Notion/assets/50197260/33e3f94e-6159-4d73-8690-51ad1b59ece1)

![image](https://github.com/Hunter-Fang/PhotosStory_By_Notion/assets/50197260/7ee1155a-9c21-42ea-b927-b1aa5ecd388f)


2.创建Notion API（官方称为机器人），获取API Token，并API授权链接上面创建的页面

[My integrations | Notion Developers](https://www.notion.so/my-integrations)

![image](https://github.com/Hunter-Fang/PhotosStory_By_Notion/assets/50197260/bb7be318-ba7f-4864-8890-d085956eee10)

![image](https://github.com/Hunter-Fang/PhotosStory_By_Notion/assets/50197260/c9fb56af-8cbc-47c2-afd5-3754edc20933)


至此，准备工作完成，开始部署

**vercel部署**

1.注册GitHub：

略

2.Fork项目：

项目模板地址：[Hunter-Fang/PhotosStory_By_Notion (github.com)](https://github.com/Hunter-Fang/PhotosStory_By_Notion/tree/main)

点击右上角Fork：

![image](https://github.com/Hunter-Fang/PhotosStory_By_Notion/assets/50197260/f3b6b3c0-01d8-4ce9-8a68-bd0b130047a0)


3.用GitHub账号登陆vercel：

略

4.vercel平台New Project，选择刚刚Fork到自己仓库里的项目：

![image](https://github.com/Hunter-Fang/PhotosStory_By_Notion/assets/50197260/3ec5cdc1-3f5c-4441-ad08-3f5c7acf18fe)


5.填入环境变量，将准备工作中获得的两个ID，按下方示意填入

NOTION_DATABASE_ID、NOTION_TOKEN

![image](https://github.com/Hunter-Fang/PhotosStory_By_Notion/assets/50197260/2df87df0-3167-4981-84bf-fd3ddcf47b43)


6.点击deploy即可，待部署完直接访问

**国内域名代理**

vercel目前被国内不定时ban，有条件添加国内域名domain代理，也可提高访问速度，有一定CDN代理

# 简单聊聊怎么实现

**后端实现**

1. 定义了一个路由`/api/main.py`，这是前端应用程序可以使用的API端点。当收到该路径的请求时，将执行`get_data()`函数。
2. `get_data()`函数是处理`/api/main.py`路径请求的处理逻辑。它首先设置请求头，包括使用环境变量中的Notion Token和Notion版本。然后，它发送一个POST请求到Notion API，使用环境变量中的Notion数据库ID作为请求的一部分。最后，它将返回从Notion API获取到的数据作为JSON响应。

**前端数据渲染**

1. 在`<script>`标签中，定义了一段JavaScript代码。这段代码使用Fetch API从后端API获取数据，并将数据动态地渲染到时间轴中。
2. 在JavaScript代码中，通过调用`fetch('/api/main.py')`发送GET请求，获取数据。然后通过处理响应数据，动态地创建和添加`<li>`元素到时间轴中。
3. 每个`<li>`元素代表一个事件，包括地点、日期、消息和图片等信息。
