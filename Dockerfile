# syntax=docker/dockerfile:1
#
# 站点为纯静态内容，直接用 nginx:alpine 承载，无 Node 运行时、无 npm 依赖。
#
# 与部署环境的约定：
# - 监听 3000 端口。.gitlab/auto-deploy-values-{prod,test}.yaml 中 internalPort / externalPort 为 3000，
#   同时该端口落在 GitLab Auto Deploy chart 默认安全上下文允许的非特权范围内。
# - 容器内以 UID/GID 1000 运行。GitLab Auto Deploy chart 默认 securityContext 为 runAsUser: 1000,
#   runAsNonRoot: true, fsGroup: 1000；静态文件与 nginx 运行时目录都必须属于该用户，否则容器启动即失败。
# - 因此 nginx 主进程作为 PID 1 直接启动（不切 user），而非以 root 启动后降权。

FROM nginx:alpine

# 基础镜像把 nginx 用户建成 101:101 /var/cache/nginx 且 /var/run 不可写；
# 这里改为 1000:1000，与 chart 默认安全上下文一致，并补上全部运行时目录。
RUN set -eux; \
    if ! getent group 1000 >/dev/null; then addgroup -g 1000 -S app; fi; \
    if ! getent passwd 1000 >/dev/null; then adduser -u 1000 -S -D -H -G "$(getent group 1000 | cut -d: -f1)" app; fi; \
    sed -i 's/^user[[:space:]]\+nginx;$/user  app;/' /etc/nginx/nginx.conf; \
    mkdir -p /var/cache/nginx /var/log/nginx /run; \
    chown -R 1000:1000 /var/cache/nginx /var/log/nginx /run /etc/nginx/conf.d

# 站点内容
COPY prototype-v4 /usr/share/nginx/html/prototype-v4
COPY enterprise-admin /usr/share/nginx/html/enterprise-admin

# 路由重写、平台 logo 代理与压缩规则
COPY nginx.conf /etc/nginx/conf.d/default.conf

# 去除基础镜像自带的欢迎页，避免存在路由范围外的内容
RUN rm -f /usr/share/nginx/html/index.html /usr/share/nginx/html/50x.html; \
    chown -R 1000:1000 /usr/share/nginx/html

USER 1000:1000

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]
