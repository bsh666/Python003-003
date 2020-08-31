#### work01

1. 提前在`settings.py`中设置MySQL配置
2. 由于猫眼首次访问需要滑动解锁，需要先对代理做手动验证
3. 代理列表保存在 `work01/proxies.txt` 文件


#### work02

需要提前设置 `SHIMO_USERNAME` 和 `SHIMO_PASSWORD` 环境变量，或在实例化传入用户名密码。
默认headless，通过console查看登录情况，登录成功会列出最近使用文档列表

