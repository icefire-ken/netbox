#!/bin/bash

# 定义源数据目录路径
SOURCE_DIR="/opt/netbox-data"

# 定义备份存储目录路径
BACKUP_DIR="/backup/netbox-data-backup"

# 获取当前时间，格式为：年月日_时分秒（例如：20260110_001005）
DATE=$(date +"%Y%m%d_%H%M%S")

# 构造完整的备份文件路径和名称
BACKUP_FILE="${BACKUP_DIR}/netbox-data_${DATE}.tar.gz"

# 定义日志文件路径（放在备份目录内）
LOG_FILE="${BACKUP_DIR}/netbox-backup.log"

# 确保备份目录存在，如果不存在则递归创建（-p 参数保证安全）
mkdir -p "$BACKUP_DIR"

# 定义日志记录函数：将带时间戳的消息追加到日志文件
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" >> "$LOG_FILE"
}

# ================================
# 新增功能：清理 7 天前的旧备份文件
# ================================

# 使用 find 命令查找 BACKUP_DIR 目录下：
#   - 文件名匹配 "netbox-data_*.tar.gz" 的文件
#   - 且修改时间（mtime）超过 7 天（+7 表示“7天前及更早”）
#   - 然后执行删除操作（-delete）
#
# 注意：
#   - mtime 是文件内容最后修改时间，tar.gz 创建时即设定为此时间，适合用于判断备份年龄
#   - -delete 比 -exec rm {} \; 更高效、简洁
find "$BACKUP_DIR" -name "netbox-data_*.tar.gz" -type f -mtime +7 -delete

# 可选：记录本次清理了多少个文件（进阶，当前先不启用以保持简洁）
# 若需记录，可用以下方式替代上面一行（但会稍慢）：
# deleted_count=$(find "$BACKUP_DIR" -name "netbox-data_*.tar.gz" -type f -mtime +7 -print -delete | wc -l)
# log "已删除 $deleted_count 个超过7天的旧备份文件"

# ================================
# 执行打包压缩操作
# ================================

# 使用 tar 命令进行压缩：
#   -c: 创建新归档
#   -z: 通过 gzip 压缩
#   -f: 指定输出文件名
#   -C /: 切换到根目录，避免打包时包含绝对路径前缀（如 /opt/...）
#   "$SOURCE_DIR": 要打包的目录（此时相对路径为 opt/netbox-data）
if tar -czf "$BACKUP_FILE" -C / "$SOURCE_DIR"; then
    # 如果 tar 成功执行，记录成功日志
    log "备份成功: $BACKUP_FILE"
else
    # 如果 tar 失败，记录错误并退出脚本（返回非零状态码）
    log "备份失败！"
    exit 1
fi