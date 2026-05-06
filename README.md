[![build status](https://img.shields.io/github/actions/workflow/status/DotRacel/emby-keeper0/ci.yml?branch=main)](https://github.com/DotRacel/emby-keeper0/actions/workflows/ci.yml) [![pypi badge](https://img.shields.io/pypi/v/embykeeper)](https://pypi.org/project/embykeeper/) [![container](https://img.shields.io/badge/GHCR-ghcr.io%2Fdotracel%2Femby--keeper0-blue)](https://github.com/DotRacel/emby-keeper0/pkgs/container/emby-keeper0) [![license badge](https://img.shields.io/github/license/DotRacel/emby-keeper0)](https://github.com/DotRacel/emby-keeper0/blob/main/LICENSE) 

<p align="center">
  <a href='https://github.com/DotRacel/emby-keeper0'>
    <img src="https://github.com/DotRacel/emby-keeper0/raw/main/images/logo.svg" alt="Embykeeper" />
  </a>
</p>
<p align="center">
    <b>自动签到 定时保号</b>
</p>

---

## 功能

Embykeeper0 是一个 Emby 影视服务器签到保号的自动执行工具, 它主要提供两大核心功能:

1. **TG 机器人签到** - 可以自动完成 50+ 站点的 Telegram 机器人每日签到, 以获取积分.

2. **Emby 保号** - 通过模拟登录和播放视频, 定期保持 Emby 账号的活跃状态, 支持任何 Emby 站点.

除此之外, Embykeeper0 还提供基于 Pyrogram 的二次开发框架, 便于维护新的签到器.

项目支持 Python 运行、Docker 部署或云部署, 且完全开源, 不存储任何密钥或隐私信息, 经两年的开发已经在稳定和安全性方面有一定保证.

## 声明

本项目涉及的一切 Emby 服务器与 Embykeeper0 开发团队无关, 在使用 Embykeeper0 时造成的一切损失 (包括但不限于 Emby 或 Telegram 账号被封禁或被群封禁) 与开发团队无关. 为了您的账号安全, 推荐使用小号. 运行该工具的 Telegram 账号若通过接码注册, 请使用一段时间再接入本工具.

本项目设计初衷是在中文 Emby 社群规则下, 保号要求逐渐苛刻 (部分要求每月登录或每日签到), 这使得休闲时间紧张的人士难以安心使用. 本项目仅旨在帮助该类人群保号, 不鼓励持有大量 Emby 账号而不使用, 导致真正需要的人、为中文影视资源分享和翻译有贡献的人难以获得账号的行为, 开发团队也呼吁仅保留 1-2 个较全面质量较高的 Emby 服务器. 本项目仅提供工具, 具体使用形式及造成的影响和后果与开发团队无关.

当您安装并使用该工具, 默认您已经阅读并同意上述声明, 并确认自己并非出于"集邮"目的而安装.

## 安装与使用

Embykeeper0 目前仅支持 Docker 部署, 请点击下方按钮开始部署:

```bash
docker run -v $(pwd)/embykeeper:/app --rm -it --net=host ghcr.io/dotracel/emby-keeper0 -i
```

**注意**: 由于近期 Telegram 风控等级上升, 请尽可能先使用服务器所在地区的代理在手机上先登陆一次, 再使用 Embykeeper.

您也可以使用 [Docker Compose 部署](https://emby-keeper.github.io/guide/Linux-Docker-Compose-部署).

更多安装和配置方面的帮助请参考 [**📖 教程文档**](https://emby-keeper.github.io/).

本项目欢迎友善讨论与建议, 您可以通过 [Github Issue](https://github.com/DotRacel/emby-keeper0) 途径反馈, 并认可开发团队可以关闭与项目开发不直接相关的不友善讨论. 

## 运行截图

![Screenshot](https://github.com/emby-keeper/emby-keeper/raw/main/images/screenshot.png)

## 完整功能支持列表

- **Emby 保活**
  - 定时模拟账号登录视频播放
  - 播放时间与进度模拟
- **Telegram 机器人签到**
  - **更多签到站**可通过[模板配置](https://emby-keeper.github.io/guide/配置文件#service-子项)或[二次开发](https://emby-keeper.github.io/guide/参与开发#每日签到站点)实现.

  - 测试中新签到器 (默认禁用, 请参考[教程文档](https://emby-keeper.github.io/guide/配置文件#service-子项)启用):

  - 其他非 Emby 相关 (默认禁用, 请参考[教程文档](https://emby-keeper.github.io/guide/配置文件#service-子项)启用):
