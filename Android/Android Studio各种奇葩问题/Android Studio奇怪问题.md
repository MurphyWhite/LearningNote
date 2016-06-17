# Android Studio奇怪问题

**问题1:The SDK platform-tools version (23.1) is too old to check APIs compiled with API 24**
![问题一](//问题1)
并不一定影响编译代码或者其他问题，但是不爽。
可以在Android Studio未打开项目的界面进入SDK Manager里面进行升级。SDK platform tool版本

**问题2：Android Studio不能使用手机进行调试，主要表现为在选择设备时没有显示连接的设备**
使用real手机真机调试步骤：

1.  在build.gradle 文件中确定你的App是否可以调试

         <span class="hljs-title">android</span> {
         <span class="hljs-title">buildTypes</span> {
             <span class="hljs-title">debug</span> {
                 <span class="hljs-title">debuggable</span> <span class="hljs-built_in">true</span>
             }

2.  在手机设置中打开USB调试，android 4.2和更新的版本。开发者模式系隐藏的，在设置&gt;关于手机，点击系统版本7次就可以在前一个页面找到开发者选项。_（一般手机会有提示）_

3.在电脑中安装设备的驱动。找不到的话可以使用豌豆荚等手机管理工具。即可自动安装。_（Mac OS和linu并不需要安装）_ 