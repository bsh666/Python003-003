### 表结构

```python
class MovieModel(models.Model):
    name = models.CharField("Movie", max_length=155, db_index=True)
    published_date = models.DateField("Publish date", null=True)
    description = models.TextField("Description of movie")
    stars = models.FloatField("Stars", default=0)

    class Meta:
        app_label = "movie"
        db_table = "movie"
```

### 关于url

`/movie?name=电影名`  

请求接收name参数，当name为空时，默认为数据中第一个电影名称

`/movie?q=关键字`  

q参数为查询关键字，查询字段为description

`/movie?p=页码`  

支持分页，但不支持自定义page size

### 运行步骤

1. `pip install -r requirements.txt`；
2. 配置数据库，可通过migrate命令，也可以导入根目录下的sql文件(推荐)；
3. runserver && 访问 `/movie?name=八佰`