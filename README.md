# Pokemon Battle Simulator

## 目录

- [目录](#目录)
- [简介](#简介)
- [实现](#实现)

## 简介

> 宝可梦对战是宝可梦游戏的核心，通常为1对1的回合制战斗。
>
> 游戏中，每回合的实际顺序以双方所采用的命令的 **优先度** 以及双方宝可梦的 **速度** 为标准判断。
> 
> 对战时，双方宝可梦会使出各种招式来削减对方宝可梦的 **HP** 。当HP减为0时宝可梦就会倒下。若是双方宝可梦都在同一回合中相继倒下，后倒下的一方获胜。
> 
> 游戏中的基本对战命令为：
> - 战斗
> - 道具
> - 宝可梦
> - 逃跑
> 
> 道具的使用将优先于所有宝可梦的招式使用，同时玩家的宝可梦在本回合无法使出招式。

## 实现

1. 设置己方宝可梦和对方宝可梦的基本信息
   1. 默认基础点数为1
   2. 默认所有宝可梦为50级
2. 对战
   1. 优先度
   2. 攻击和防御算式
   3. 属性克制
