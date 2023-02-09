#language: zh-CN
功能: 应用
	场景大纲: 打开关闭应用-1
		假如 存在应用程序 "<execname>"
		当   打开应用,应用名称为 "<appname>"
		那么 打开应用窗口名称为 "<windowname>"
		而且 关闭对应应用

    例子: 窗口类型为Frame
    |execname                    |appname                     |windowname           |
    |pluma                       |pluma                       |未保存文档 1 - Pluma |
    |transmission-gtk            |transmission-gtk            |文件传输             |
#    |shotwell                    |shotwell                    |Shotwell             |
    |simple-scan                 |simple-scan                 |扫描易               |
    |brasero                     |brasero                     |Brasero              |
    |pavucontrol                 |pavucontrol                 |音量控制             |
    |rhythmbox                   |rhythmbox                   |音乐播放器           |
    |engrampa                    |engrampa                    |归档管理器           |
    |gnote                       |gnote                       |便签                 |
    |gucharmap                   |gucharmap                   |字符映射表           |
#    |mate-calc                   |mate-calc                   |计算器               |
    |mate-font-viewer            |mate-font-viewer            |字体查看器           |
#    |seahorse                    |seahorse                    |密码和密钥           |
    |gnome-software              |gnome-software              |应用商店             |
    |dconf-editor                |dconf-editor                |dconf 系统配置编辑器 |
    |mate-disk-usage-analyzer    |mate-disk-usage-analyzer    |磁盘使用分析器       |
    |mate-control-center         |mate-control-center         |控制中心             |
    |firefox                     |Firefox                     |Mozilla Firefox      |


	场景大纲: 打开关闭应用-2
		假如 存在应用程序 "<execname>"
		当   打开应用,应用名称为 "<appname>"
		那么 打开应用,其中一个窗口名称为 "<windowname>"
		而且 关闭对应应用

    例子: 存在多个frame类型窗口 
    |execname                    |appname                     |windowname           |
    |thunderbird                 |Thunderbird                 |Thunderbird          |
    |gnome-disks                 |gnome-disks                 |硬盘\|磁盘           |
#    |gpartedbin                  |gpartedbin                  |GParted\|分区工具    |


	场景大纲: 打开关闭应用-2
		假如 存在应用程序 "<execname>"
		当   打开应用,应用名称为 "<appname>"
		那么 打开的对话框名称为 "<windowname>"
		而且 关闭对应应用

    例子: 窗口类型为Dialog
    |execname                    |appname                     |windowname           |
    |mate-color-select           |mate-color-select           |颜色选择             |
    |mate-notification-properties|mate-notification-properties|通知设定             |


	场景大纲: 打开关闭应用-3
		假如 存在应用程序 "<execname>"
		当   打开应用,应用名称为 "<appname>"
		那么 关闭对应应用

    例子: 窗口没有名称
    |execname                    |appname                     |
    |atril                       |atril                       | 
    |eom                         |eom                         |
#    |ksplayer                    |ksplayer                    |
    |mate-search-tool            |mate-search-tool            |
    |simplescreenrecorder        |simplescreenrecorder        |
    |smplayer                    |smplayer                    |
    |qt5-fsarchiver              |qt5-fsarchiver              |
    # 窗口名称会变化
    |mate-power-statistics       |mate-power-statistics       |


#	场景大纲: 打开关闭应用-4
#		假如 存在应用程序 "<execname>"
#		当   打开应用,应用名称为 "<appname>"
#		那么 关闭对应应用
#
#    例子: 无法识别窗口 
#    |execname                    |appname                     | 
#    |kiran-flameshot             |kiran-flameshot             |
