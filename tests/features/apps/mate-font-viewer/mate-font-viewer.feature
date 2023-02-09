#language: zh-CN
功能:MATE字体查看器查看字体
	场景:搜索字体，查看内容
		假如 存在应用程序 "mate-font-viewer"
		当   打开应用,应用名称为 "mate-font-viewer"
		而且 选择元素name="查找",roleName="toggle button",des="None",并且 "单" 击 "左" 键
		而且 选择元素name="搜索",roleName="text",des="None",输入文本 "Aby"
		而且 休眠 "5" 秒
		那么 存在元素name="None",roleName="icon",des="None",文本等于 "Abyssinica SIL"		
		而且 关闭对应应用


