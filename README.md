# pairwise-ambisonics-decode

## 领域

游戏、图形与多媒体

## 主题

环绕声场解码

## 说明

头追预测、阶数渐变与设备布局路由。

初始状态下 `av/ambisonic_decode.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
