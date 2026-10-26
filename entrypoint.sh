#!/bin/sh
set -e

PORT="${PORT:-8000}"
UUID="${UUID:-3d94bd61-6b1c-4236-8235-decdd55e0ad5}"

# 替换端口
sed -i "s/\"listen_port\": 8000/\"listen_port\": ${PORT}/" /etc/sing-box/config.json

# 替换 UUID（如果环境变量提供了新的）
if [ "$UUID" != "3d94bd61-6b1c-4236-8235-decdd55e0ad5" ]; then
  sed -i "s/3d94bd61-6b1c-4236-8235-decdd55e0ad5/${UUID}/" /etc/sing-box/config.json
fi

echo "=========================================="
echo " sing-box VLESS-WS"
echo " 端口: ${PORT}"
echo " UUID: ${UUID}"
echo " 路径: /ws"
echo "=========================================="

exec sing-box run -c /etc/sing-box/config.json
