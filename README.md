# Docker部署NetBox（带有plugins）

## 1、clone项目

```bash
#git clone netbox-docker项目
cd /opt/
git clone -b release https://github.com/netbox-community/netbox-docker.git
cd /opt/netbox-docker/
```

## 2、创建数据挂载目录

```bash
# 创建主机数据host挂载目录
mkdir -p /opt/netbox-data/{\
netbox-media-files,\
netbox-postgres-data,\
netbox-redis-cache-data,\
netbox-redis-data,\
netbox-reports-files,\
netbox-scripts-files\
}

# 修改netbox相关的3个文件夹的uid
chown -R 999:0 /opt/netbox-data/netbox-media-files
chown -R 999:0 /opt/netbox-data/netbox-reports-files
chown -R 999:0 /opt/netbox-data/netbox-scripts-files
# 因为netbox容器的账户uid是999

# 并修改netbox相关的3个文件夹的权限
chmod -R 775 /opt/netbox-data/netbox-media-files
chmod -R 775 /opt/netbox-data/netbox-reports-files
chmod -R 775 /opt/netbox-data/netbox-scripts-files

# 也可以考虑在override文件中修改netbox服务的user字段“user:root”（不推荐）
```

## 3、添加plugins

1. 添加`plugin_requirements.txt`文件，内容是要安装的plugins。（github仓库）
2. 添加`Dockerfile-Plugins`文件，内容是构建带有plugins的镜像。（命令以官网为准）
```bash
FROM netboxcommunity/netbox:latest

COPY ./plugin_requirements.txt /opt/netbox/
RUN /usr/local/bin/uv pip install -r /opt/netbox/plugin_requirements.txt

# These lines are only required if your plugin has its own static files.
COPY configuration/configuration.py /etc/netbox/config/configuration.py
COPY configuration/plugins.py /etc/netbox/config/plugins.py
RUN DEBUG="true" SECRET_KEY="dummydummydummydummydummydummydummydummydummydummy" \
    /opt/netbox/venv/bin/python /opt/netbox/netbox/manage.py collectstatic --no-input
```
3. 添加`docker-compose.override.yml`文件，注意与不带有plugins的override文件的差异。（github仓库）
4. 编辑`configuration/plugins.py`文件，在配置中启用想要安装的plugins。（github仓库）

## 4、启动容器

```bash
# 拉取索取镜像（不带有Plugins）
docker compose pull

# 构建镜像（带有Plugins）
docker compose build --no-cache

# 启动容器
docker compose up -d
```

## 