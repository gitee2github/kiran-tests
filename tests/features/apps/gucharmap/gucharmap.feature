#language: zh-CN
功能:gucharmap搜索
	场景:搜索关键字
		假如 存在应用程序 "gucharmap"
		当   打开应用,应用名称为 "gucharmap"
		而且 选择元素name="搜索(S)",roleName="menu",des="None",并且 "单" 击 "左" 键
		而且 选择元素name="查找(F)",roleName="menu item",des="None",并且 "单" 击 "左" 键
        而且 选择弹窗 "dialog"
		而且 在弹窗中，修改文本框 "text" 中的内容为 "麒"
        而且 在弹窗中，点击按钮 "下一个(N)"
        而且 在弹窗中，点击按钮 "关闭(C)"
		那么 "存" 在元素name="U+9E92 CJK UNIFIED IDEOGRAPH-9E92   legendary auspicious animal",roleName="status bar",des="None"
		那么 关闭对应应用


