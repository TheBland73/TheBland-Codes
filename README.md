<div align="center">

# 💪 我的算法刷题笔记

**记录每一次思考，见证每一步成长。**

[![LeetCode](https://img.shields.io/badge/LeetCode-TheBland-orange?logo=leetcode&logoColor=white)](https://leetcode.cn/u/thebland/)
[![Solved](https://img.shields.io/badge/已解决-177%20题-brightgreen?style=flat-square)](#-刷题进度)
[![Language](https://img.shields.io/badge/语言-Python%20%7C%20C%20%7C%20C%2B%2B-blue?style=flat-square)](#-技术栈)
[![Last Commit](https://img.shields.io/github/last-commit/thebland/TheBland-Codes?style=flat-square&color=purple)](https://github.com/thebland/TheBland-Codes/commits)
[![Stars](https://img.shields.io/github/stars/thebland/TheBland-Codes?style=flat-square&color=yellow)](https://github.com/thebland/TheBland-Codes/stargazers)

<img src="https://leetcard.jacoblin.cool/thebland?theme=dark&font=Karma&ext=contest&site=cn" alt="LeetCode Stats Card" />

</div>

---

## 📖 关于这个仓库

这里存放我刷题的**代码**与**题解**。

对我而言，刷题不只是为了通过面试，更是训练思维方式的过程——把模糊的直觉拆解成清晰的步骤，把重复的套路沉淀成可复用的模板。

> 🎯 **目标**：稳定输出，长期主义。宁可慢，不可断。

---

## 📊 刷题进度

<!-- AUTO:PROGRESS:START -->
<!-- AUTO:PROGRESS:END -->

---

## 🗂️ 仓库结构

```
.
├── LeetCode/                 # 力扣题目
│   ├── 0001-两数之和/
│   │   ├── README.md         # 思路 / 复杂度 / 易错点
│   │   ├── solution.py       # Python3（使用为尊）
│   │   ├── solution.cpp      # C++（速度之上）
│   │   └── solution.c        # C（底层理解）
│   └── 0002-两数相加/
├── Templates/                # 常用模板
│   ├── 二分查找.md
│   ├── 并查集.md
│   └── 滑动窗口.md
├── Notes/                    # 专题笔记
└── README.md
```

**命名规范**：`编号-题名`，例如 `0042-接雨水`。编号补零到四位，方便排序与检索。

**语言策略**：每道题以 **Python3** 为主实现（书写快、贴近思路），精选题目补 **C++** 实现（对比 STL 写法与性能），必要时用 **C** 手写底层数据结构（加深对内存和指针的理解）。

---

## 🧭 分类导航

你已涉及的技能标签：

| 专题 | 说明 | 代表题目 |
| :--- | :--- | :--- |
| [数组](./Notes/array.md) | 双指针、前缀和、原地操作 | 两数之和、盛最多水的容器 |
| [二分查找](./Notes/binary-search.md) | 边界处理、答案二分 | 搜索旋转排序数组 |
| [深度优先搜索](./Notes/dfs.md) | 递归、回溯、岛屿问题 | 岛屿数量 |
| [动态规划](./Notes/dp.md) | 背包、区间、状态压缩 | 最长递增子序列 |
| [贪心](./Notes/greedy.md) | 区间调度、交换论证 | 跳跃游戏 |
| [哈希表](./Notes/hash.md) | 计数、去重、前缀和 | 字母异位词分组 |
| [数学](./Notes/math.md) | 数论、牛顿迭代、位运算 | 各位相加 |
| [排序](./Notes/sorting.md) | 快排、归并、堆排 | 数组中的第K个最大元素 |
| [字符串](./Notes/string.md) | KMP、回文、滑动窗口 | 最小覆盖子串 |
| [双指针](./Notes/two-pointers.md) | 对撞指针、快慢指针 | 三数之和 |

> 链接指向 `Notes/` 下的笔记文件，还没写的可以先留空。

---

## 🛠️ 技术栈

![Python](https://img.shields.io/badge/Python3-3776AB?logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?logo=cplusplus&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?logo=c&logoColor=white)

<!-- AUTO:LANGUAGE:START -->
<!-- AUTO:LANGUAGE:END -->

---

## 📝 每道题的记录方式

每道题目录下的 `README.md` 统一使用下面的结构：

```markdown
# 0001. 两数之和

- **难度**：🟢 简单
- **标签**：数组 / 哈希表
- **链接**：https://leetcode.cn/problems/two-sum/
- **语言**：Python3 / C++

## 思路

一句话概括核心想法，再展开关键步骤。

## 复杂度

- 时间：O(n)
- 空间：O(n)

## 易错点

- 边界条件、下标越界、空输入……

## 代码

见 `solution.py`、`solution.cpp`
```

原则是：**先写思路，再写代码**。半年后回看，代码能读懂，思路才是真正值钱的部分。

---

## 🚀 如何食用

1. 直接点开感兴趣的题目目录，先看 `README.md` 的思路部分，**自己动手写一遍**再对照代码。
2. 复习时只看思路，能独立复现代码就算过关。
3. 想找某个专题的套路，去 [`Templates/`](./Templates) 和 [`Notes/`](./Notes) 翻模板。

```bash
git clone https://github.com/thebland/TheBland-Codes.git
cd TheBland-Codes
```

---

## 📌 刷题心法

- **重复 > 数量**。同一道题做三遍，胜过三道题各做一遍。
- **先暴力，再优化**。写出能跑的解法，再想怎么把 O(n²) 降到 O(n log n)。
- **写完必复盘**。记录错在哪、卡在哪、下次怎么绕过。
- **不要硬磕**。卡住 40 分钟就看题解，理解后合上题解重写一遍。
- **保持节奏**。每天一道，比周末突击十道更有效。

---

## 📈 竞赛与成就

<!-- AUTO:CONTEST:START -->
<!-- AUTO:CONTEST:END -->

> 🏅 勋章成就：4 枚（含月度每日一题全部完成）

<!-- AUTO:UPDATED:START -->
<!-- AUTO:UPDATED:END -->

---

<div align="center">

**如果这个仓库对你有帮助，欢迎点个 ⭐ Star**

Made with ☕ and 🧠 by [TheBland](https://github.com/thebland)

</div>
