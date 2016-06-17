# ios 读书笔记

## Objective-c

## Swift

## iOS基础

### 故事板

### xib

### 应用生命周期

AppDelegate类在应用生命周期的不同阶段会回调不同的方法。

*   Not Running:应用没有运行或被系统终止。
*   Inactive:应用正在进入前台状态，但是还不能接受事件处理。
*   Active:应用进入前台状态，能接受事件处理
*   Background:应用进入后台后，依然能够执行代码。如果有可执行代码，就会执行代码，如果没有可执行代码或者将可执行代码执行完毕，应用会马上进入挂起状态
*   Suspended:处于挂起状态的应用马上进入一种“冷冻”状态，不能执行代码。如果系统内存不够，应用会被终止。

**主要是生命周期切换的时候会进行调用的方法，需要进行了解，并在实际的使用中需要用到。**

![生命周期和调用方法](http://cl.ly/013R1P022R2M)

### UIKit框架

#### 基础视图

1.  UIButton
2.  UILabel
3.  UIImageView
4.  UITextField
5.  UIScrollView
6.  UIAlertView

#### 高级视图

#### 自定义视图

### 表视图

### 集合视图