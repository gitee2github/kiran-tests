#language: zh-CN
功能:Atril查看文件
	场景:打开PDF文件
		假如 存在应用程序 "eom"
		当   打开应用,应用名称为 "eom"
		而且 选择元素name="图像(I)",roleName="menu",des="None",并且 "单" 击 "左" 键
		而且 选择元素name="打开(O)...",roleName="menu item",des="None",并且 "单" 击 "左" 键
		而且 在路径选择窗口中进入 "dataPath" 目录
		而且 选择元素name="kylin.jpg",roleName="table cell",des="None",并且 "单" 击 "左" 键
		而且 选择元素name="打开(O)",roleName="push button",des="None",并且 "单" 击 "左" 键
		那么 "存" 在元素name="324 × 171 像素  7.0 KB    100%",roleName="status bar",des="None"
		那么 关闭对应应用


