#!/usr/bin/env python3
"""Koyeb 保活脚本 - 防止 1 小时休眠"""

import sys
import time
import urllib.request

URL = "https://你的应用.koyeb.app/ws"
INTERVAL = 20 * 60   # 20 分钟


def ping():
    try:
        req = urllib.request.Request(URL, headers={"User-Agent": "keepalive/1.0"})
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.status
    except urllib.error.HTTPError as e:
        return e.code
    except Exception as e:
        return str(e)[:40]


def main():
    if len(sys.argv) > 1:
        global URL
        URL = sys.argv[1]

    print("保活目标: {}".format(URL))
    print("间隔: {} 分钟\n".format(INTERVAL // 60))

    while True:
        t0 = time.time()
        code = ping()
        ms = round((time.time() - t0) * 1000)
        print("[{}] {} ({}ms)".format(
            time.strftime("%H:%M:%S"), code, ms), flush=True)
        time.sleep(INTERVAL)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n已停止")
