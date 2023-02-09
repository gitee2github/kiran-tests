#language: zh-CN
功能:gnote新建便签，编辑便签内容
	场景:新建便签
		假如 存在应用程序 "gnote"
		当   打开应用,应用名称为 "gnote"
		而且 选择元素name="添加",roleName="push button",des="Create New Note",并且 "单" 击 "左" 键
		而且 选择弹窗 "frame"
		而且 在弹窗中，修改文本框 "text" 中的内容为 "测试便签"
		而且 选择元素name="Back",roleName="push button",des="全部便笺",并且 "单" 击 "左" 键
		而且 选择元素name="测试便签",roleName="table cell",des="None",并且 "单" 击 "右" 键
		而且 选择元素name="删除(D)",roleName="menu item",des="None",并且 "单" 击 "左" 键
		而且 选择元素name="删除(D)",roleName="push button",des="None",并且 "单" 击 "左" 键
		那么 "不存" 在元素name="测试便签",roleName="table cell",des="None"
		那么 关闭对应应用


