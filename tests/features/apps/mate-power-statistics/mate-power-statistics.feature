#language: zh-CN
功能: 电源统计显示功能
	场景: 交流电源适配器内容
		假如 存在应用程序 "mate-power-statistics"
		当   打开应用,应用名称为 "mate-power-statistics"
		而且 选择元素name="交流电源适配器",roleName="table cell",des="None",并且 "单" 击 "左" 键
		那么 "存" 在元素name="细节",roleName="page tab",des="None"
        当   选择元素name="处理器",roleName="table cell",des="None",并且 "单" 击 "左" 键
		那么 "存" 在元素name="唤醒",roleName="page tab",des="None"
		而且 关闭对应应用


