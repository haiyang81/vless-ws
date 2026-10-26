# VLESS-WS 免费节点

基于 sing-box 的 VLESS + WebSocket 代理，可部署到 Koyeb / Render / Railway。

## 部署到 Koyeb

1. Fork 这个仓库
2. 打开 https://app.koyeb.com/
3. Create Service → GitHub → 选这个仓库
4. Instance: **Free**（512MB）
5. Region: **Frankfurt** 或 **Washington**
6. Ports: HTTP 8000
7. 环境变量: `UUID=3d94bd61-6b1c-4236-8235-decdd55e0ad5`
8. Deploy

## 客户端配置

```
vless://3d94bd61-6b1c-4236-8235-decdd55e0ad5@你的应用.koyeb.app:443?encryption=none&security=tls&sni=你的应用.koyeb.app&type=ws&host=你的应用.koyeb.app&path=%2Fws&fp=chrome#Koyeb-免费
```

## 保活（Koyeb 1 小时无流量会休眠）

用 https://cron-job.org/ 每 20 分钟访问一次：
```
https://你的应用.koyeb.app/ws
```

## 密钥

- UUID: `3d94bd61-6b1c-4236-8235-decdd55e0ad5`
- WS 路径: `/ws`
- 端口: `8000`（平台会自动注入 PORT）

## 注意

- ⚠️ 免费实例有流量限制，不要滥用
- ⚠️ 只用于个人学习
