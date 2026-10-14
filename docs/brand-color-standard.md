# 品牌颜色标准

## 唯一主色

看见音乐 Logo 的像素取样色为 `#0040FF`，它是官网与企业运营后台唯一允许使用的实体蓝色。

```css
:root {
  --brand-blue: #0040ff;
  --brand-blue-rgb: 0, 64, 255;
}
```

## 使用规则

- 按钮、链接、选中态和重点数字使用 `var(--brand-blue)`。
- 浅色背景、边框和阴影只允许从主色透明度派生，例如 `rgba(var(--brand-blue-rgb), .08)`。
- 深色背景上的正文与辅助文字使用白色或白色透明度，避免额外引入“浅蓝色”。
- 中性灰、深色背景以及成功、警告、错误等语义色不属于品牌蓝，可按语义继续使用。
- 禁止直接新增其他蓝色十六进制、RGB 或 RGBA 色值。

## 自动检查

提交前运行：

```bash
node scripts/check-brand-colors.mjs
```

GitHub Actions 会在每次 push 和 pull request 时执行同一检查，发现非标准蓝色会阻止检查通过。
