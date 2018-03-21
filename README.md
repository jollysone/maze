# 技术栈
* Python + Tkinter + Pyinstaller

# 开发环境
* JetBrains Pycharm 2016
* Python 3.5.2

# 技术点
* 使用的 `OOP` 面向对象编程技术，使代码更加容易修改和扩展，搭载Python自带的GUI工具 `Tkinter` ， `递归` 显示迷宫界面和答案，生成迷宫结构用了 `随机整数规划算法` 、 `传播算法` ，
同时生成迷宫等都是 `动态规划` 生成。

# 用户使用手册
### 用前须知
* 双击 `dist` 目录下的“迷宫小游戏.exe” 文件即可打开游戏，当弹出第一个设置规模的窗口时设置需要的规模，设置完成显示迷宫界面，点击最下面的功能按键“开始游戏”，即可开始游戏，然后控制按键'↑'  '↓'  '←'  '→'进行游戏，从蓝点走到红点并出去即可通关迷宫，游戏无论有无完成，可选择 “再来一次”按钮重置迷宫，也可选择“退出游戏”按钮退出游戏。当然为了增加游戏体验，在撞墙后会提示，在每次运行游戏赋予了一次查看答案的机会，以便于玩家解不出答案查看机器自动递归的答案。从第一个小点移动开始计时30s则弹出失败框。
### 游戏规则
1.   蓝点是入口，红点是出口处
2.   使用按键 `'↑'  '↓'  '←'  '→'` 进行游戏
3.   请在 `30s` 内完成游戏
4.   您只拥有一次看答案的机会

### 界面和功能描述
> 进入游戏游戏后出现的第一个界面，已经自动填入最佳迷宫规模 `10*10` ，当然可以自定义规模，但是数字最好不要太大或者太小以免显示超出范围等问题，要求只能填入数字，如果填写为空或者直接关闭窗口系统会给一个默认规模。

![Alt 图 1：设置迷宫规模](/build/images/设置迷宫规模.png)

* 　　　　　　图 1：设置迷宫规模
> 生成迷宫后会弹出另一个迷宫窗口，分为上中下三部分，上面显示整个迷宫，中间是游戏规则，下面是功能按键，点击“开始游戏“后使用方向键控制迷宫移动，“再来一次”即可刷新游戏，“悄悄看答案”功能每次运行游戏只有一次机会，所以要在实在走不出迷宫的情况下使用，使用后机器会接着自动递归出答案（浅色蓝点是自己走的轨迹，绿色是机器走的路径） 。从第一个小点移动开始计时30s则弹出失败框。
![Alt 图 2：迷宫界面](/build/images/迷宫界面.png)

* 　　　　　　图 2：迷宫界面
- - -
![Alt 图 3：撞墙提示](/build/images/撞墙提示.png)

* 　　　　　　图 3：撞墙提示
- - -
![Alt 图 4：超时提示](/build/images/超时提示.png)

* 　　　　　　图 4：超时提示
- - -
![Alt 图 5：使用悄悄看答案后提示](/build/images/悄悄看答案后提示.png)

*　　　　　　 图 5：使用悄悄看答案后提示
- - -
![Alt 图 6：悄悄看答案后的答案界面](/build/images/答案界面.png)

* 　　　　　  图 6：悄悄看答案后的答案界面

