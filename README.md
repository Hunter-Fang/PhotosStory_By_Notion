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

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d03f8357-15f4-4a13-ba69-286f6383a67c/575657fa-6632-4040-9308-b2e949706b79/Untitled.png)

- 移动端效果

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d03f8357-15f4-4a13-ba69-286f6383a67c/0b890dc5-51bd-4909-b0be-781a3bf00f0e/Untitled.png)

# **如何部署**

很简单，可以参考以下流程：

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d03f8357-15f4-4a13-ba69-286f6383a67c/e9a31e4b-8def-4b48-b12e-8558641346bb/Untitled.png)

**准备工作：**

1.Duplicate页面模版，并publish online，获取相关Database ID

[TimeLine (notion.site)](https://www.notion.so/e649801ccfa24c59b903148531d60783?pvs=21)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d03f8357-15f4-4a13-ba69-286f6383a67c/278a540c-8a0f-43d4-a767-11b7e3e1f5cd/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d03f8357-15f4-4a13-ba69-286f6383a67c/79a452ee-062f-4b22-9fc3-1bd3c543bc16/Untitled.png)

2.创建Notion API（官方称为机器人），获取API Token，并API授权链接上面创建的页面

[My integrations | Notion Developers](https://www.notion.so/my-integrations)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d03f8357-15f4-4a13-ba69-286f6383a67c/86e58756-4add-411f-99fd-1ed3e6916805/Untitled.png)

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d03f8357-15f4-4a13-ba69-286f6383a67c/f8b90506-00e0-469c-b1e1-dc9920abafff/Untitled.png)

至此，准备工作完成，开始部署

**vercel部署**

1.注册GitHub：

略

2.Fork项目：

项目模板地址：[Hunter-Fang/PhotosStory_By_Notion (github.com)](https://github.com/Hunter-Fang/PhotosStory_By_Notion/tree/main)

点击右上角Fork：

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d03f8357-15f4-4a13-ba69-286f6383a67c/6a9bf354-e755-49a2-85e4-29d06902fdfc/Untitled.png)

3.用GitHub账号登陆vercel：

略

4.vercel平台New Project，选择刚刚Fork到自己仓库里的项目：

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d03f8357-15f4-4a13-ba69-286f6383a67c/a4905d49-c72f-4dcd-82f5-d1fd8831e2f3/Untitled.png)

5.填入环境变量，将准备工作中获得的两个ID，按下方示意填入

NOTION_DATABASE_ID、NOTION_TOKEN

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/d03f8357-15f4-4a13-ba69-286f6383a67c/c599ff3e-a3cd-4c73-9ed7-3d5dd8e54416/Untitled.png)

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
