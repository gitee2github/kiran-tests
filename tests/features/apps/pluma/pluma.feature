#language: zh-CN
功能: 保存 
	场景: 编辑保存到桌面
		假如 存在应用程序 "pluma"
		当   打开应用,应用名称为 "pluma"
		而且 输入文本 "hello world~"
		而且 点击按钮 "保存"
		而且 选择弹窗 "file chooser"
		而且 在弹窗中，修改文本框 "text" 中的内容为 "pluma-test.txt"
		而且 在弹窗中，点击对象，名称为 "list item" 描述为 "在文件夹中打开桌面的内容"
		而且 在弹窗中，点击按钮 "保存(S)"
		那么 "桌面" 下存在文件 "pluma-test.txt",文件内容为 "hello world~"
        而且 删除 "桌面" 目录中存在文件 "pluma-test.txt"
		而且 关闭对应应用
