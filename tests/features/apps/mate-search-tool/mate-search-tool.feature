#language: zh-CN
功能: 搜索文件
	场景: 搜索指定目录
		假如 存在应用程序 "mate-search-tool"
		当   打开应用,应用名称为 "mate-search-tool"
		而且 选择元素name="搜索文件夹",roleName="filler",des="选择您想要开始搜索的文件夹或设备。",并且 "单" 击 "左" 键
		而且 选择元素name="其它…",roleName="menu item",des="None",并且 "单" 击 "左" 键
        而且 在路径选择窗口中进入 "dataPath" 目录
		而且 选择元素name="打开(O)",roleName="push button",des="None",并且 "单" 击 "左" 键
		而且 选择元素name="查找(F)",roleName="push button",des="None",并且 "单" 击 "左" 键
		那么 "存" 在元素name="engrampa-yasuo",roleName="table cell",des="None"
		那么 关闭对应应用


