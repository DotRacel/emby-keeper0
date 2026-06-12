---
head:
  - - meta
    - name: description
      content: Embykeeper0 是一个Emby 影视服务器签到保号的自动执行工具, 提供 TG 机器人签到和 Emby 服务器保活功能.
  - - meta
    - name: keywords
      content: Embykeeper0, Emby, 签到, 保活, Telegram

# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: 'Embykeeper0'
  text: 'Emby 保号自动化'
  tagline: Emby 保活 + TG 签到
  image:
    src: /logo.webp
    alt: Embykeeper0
  actions:
    - theme: brand
      text: Embykeeper0 是什么?
      link: /guide/
    - theme: alt
      text: 快速安装
      link: /guide/安装指南
    - theme: alt
      text: 配置文档
      link: /guide/配置文件
    - theme: alt
      text: GitHub
      link: https://github.com/DotRacel/emby-keeper0

features:
  - icon:
      src: /emby.svg
      width: 28px
      wrap: true
    title: Emby 站点模拟观看
    details: 模拟登陆 Emby 公益站并观看一定时间, 适用于 N 天不登陆/观看即封禁的站点, 支持任意站点.
  - icon:
      src: /tg.svg
      width: 28px
      wrap: true
    title: Telegram 机器人每日签到
    details: 模拟在 Telegram 机器人每日签到, 已支持 50+ 站点.
  - icon: 🐳
    title: Docker 一键部署
    details: 镜像托管于 GHCR, 一条 docker 命令即可部署, 支持 Docker Compose 与自动更新.
  - icon: 🛡️
    title: 高稳定性
    details: 签到和保号已尽可能与真人操作一致, 不容易被识别.
  - icon: 🔒
    title: 高安全性
    details: 代码开源, 不收集任何密钥和隐私数据.
---

<script setup>

import TerminalExampleSection from './components/TerminalExampleSection.vue'

</script>

<hr style="margin-top: 30px; margin-bottom: 30px;">

<TerminalExampleSection />
