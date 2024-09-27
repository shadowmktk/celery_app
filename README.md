# celery_app
Celery异步队列 - 简单示例

构建镜像前，需要修改以下几个参数，CELERY_APP_ENVIRONMENT变量可以固定为production，Celery使用redis和mysql，连接地址请按实际情况修改。
```
CELERY_APP_ENVIRONMENT=production
BROKER_URL=redis://192.168.3.106:6379/0
RESULT_BACKEND=db+mysql+pymysql://root:123456@192.168.3.106:3306/celery?charset=utf8mb4
```
RESULT_BACKEND参数中的celery是数据库名称，在启动Celery程序前务必创建好。

docker build
```
docker build -t celery_app:v1.0.0 .
docker run -d --name celery_app celery_app:v1.0.0
```
