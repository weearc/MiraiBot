直播监控
-------------

### 功能

将监控频道的开播信息发送到对应的群。
支持的频道类型: bilibili, youtube, 网易cc
支持批量添加/删除频道

### 使用方法

```plain
直播监控添加 <频道1> <频道2> ...
直播监控移除 <频道1> <频道2> ...
直播监控列表 [页码]
直播监控详细列表 [页码]

频道: 频道url 或 频道名称（仅用于移除）

例：
直播监控添加 https://live.bilibili.com/1
直播监控移除 哔哩哔哩直播
直播监控列表 1
```