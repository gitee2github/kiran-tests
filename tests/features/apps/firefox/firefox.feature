#language: zh-CN
功能: 浏览网页
	场景: 打开URL
		假如 存在应用程序 "firefox"
		当   打开应用,应用名称为 "Firefox"
		而且 选择元素name="None",roleName="entry",des="None",输入文本 "10.60.3.150:7777"
		而且 选择元素name="转到地址栏中指向的网址",roleName="None",des="None",并且 "单" 击 "左" 键
		那么 "存" 在元素name="麒麟安全公告",roleName="heading",des="None" 
		那么 关闭对应应用

