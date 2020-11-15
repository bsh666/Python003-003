### 说明

使用django自带的model、modelform和auth

需要先做migrate，生成认证相关数据表

支持的路由：

- `/index`
- `/login`
- `/register`
- `/logout`

全部复用django自带的认证功能，页面只有简单的空白form表单，仅支持简单的注册注销用户、登录跳转功能