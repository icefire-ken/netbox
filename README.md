# Docker 部署 NetBox （带有plugins）

## 1、clone 项目

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

## 3、添加 plugins

下载准备好的为netbox-docker添加的plugins文件：

`plugin_requirements.txt`，想要安装的plugins。 

`Dockerfile-Plugins`，构建带有plugins的image。（命令以官网为准）

`docker-compose.override.yml`，注意与不带有plugins的override文件的差异，如若不需要带有plugins安装，请修改。

`configuration/plugins.py`，在配置中启用想要安装的plugins。

```bash
curl -LsSO https://raw.githubusercontent.com/icefire-ken/netbox/main/plugin_requirements.txt
curl -LsSO https://raw.githubusercontent.com/icefire-ken/netbox/main/Dockerfile-Plugins
curl -LsSO https://raw.githubusercontent.com/icefire-ken/netbox/main/docker-compose.override.yml
curl -LsSo configuration/plugins.py https://raw.githubusercontent.com/icefire-ken/netbox/main/plugins.py
```

## 4、启动容器

```bash
# 拉取索取镜像（不带有Plugins）
docker compose pull

# 构建镜像（带有Plugins）
docker compose build --no-cache

# 启动容器
docker compose up -d
```


# 备份与迁移

## 1、创建备份脚本

```bash
curl -LsSO https://raw.githubusercontent.com/icefire-ken/netbox/main/backup_netbox-data.sh
```

## 2、创建定时任务

```bash
apt -y install cron
systemctl start cron
systemctl enable cron
crontab -l
crontab -e

# 每小时运行一次备份脚本
0 * * * * /opt/netbox-docker/backup_netbox-data.sh
```

## 3、使用备份

```bash
# 手动创建备份
tar -czf "/backup/netbox-data-backup/netbox-data_$(date +"%Y%m%d_%H%M%S").tar.gz" /opt/netbox-data
# 将备份文件保存至/opt/目录
# 使用下面的命令解压
tar -xzvf netbox-data_20260111_130001.tar.gz --strip-components=1
```
