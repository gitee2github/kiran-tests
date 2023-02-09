#language: zh-CN
功能:归档管理器解压和压缩文件
#	场景:解压文件
#		假如 存在应用程序 "engrampa"
#		当   打开应用,应用名称为 "engrampa"
#		而且 选择元素name="归档文件(A)",roleName="menu",des="None",并且 "单" 击 "左" 键
#		而且 选择元素name="打开...",roleName="menu item",des="None",并且 "单" 击 "左" 键
#		而且 在路径选择窗口中进入 "dataPath" 目录
#		而且 选择元素name="engrampa-jieya.tar.gz",roleName="table cell",des="None",并且 "单" 击 "左" 键
#		而且 选择元素name="打开(O)",roleName="push button",des="None",并且 "单" 击 "左" 键
#		而且 选择元素name="归档文件(A)",roleName="menu",des="None",并且 "单" 击 "左" 键
#		而且 选择元素name="解压缩 (E) ...",roleName="menu item",des="None",并且 "单" 击 "左" 键
#		而且 在路径选择窗口中进入 "tmpPath" 目录
#		而且 选择元素name="解压缩(E)",roleName="push button",des="None",并且 "单" 击 "左" 键
#		而且 选择元素name="退出(Q)",roleName="push button",des="None",并且 "单" 击 "左" 键
#		那么 "tmpPath" 下存在文件 "engrampa-jieya",文件内容为 "hello world"
#	    而且 删除 "tmpPath" 目录中存在文件 "engrampa-jieya"
	
	场景大纲: 压缩文件

		假如 存在应用程序 "engrampa"
		当   打开应用,应用名称为 "engrampa"
		而且 选择元素name="归档文件(A)",roleName="menu",des="None",并且 "单" 击 "左" 键
		而且 选择元素name="新建...",roleName="menu item",des="None",并且 "单" 击 "左" 键
		而且 在路径选择窗口中进入 "tmpPath" 目录
		而且 选择弹窗 "file chooser"
		而且 在弹窗中，修改文本框 "text" 中的内容为 "<CompressPkgFormat>"
        而且 休眠 "0.5" 秒
		而且 选择元素name="创建(R)",roleName="push button",des="None",并且 "单" 击 "左" 键
		而且 选择元素name="编辑（E）",roleName="menu",des="None",并且 "单" 击 "左" 键
		而且 选择元素name="添加文件 (A) ...",roleName="menu item",des="None",并且 "单" 击 "左" 键
		而且 在路径选择窗口中进入 "dataPath" 目录
		而且 选择元素name="<CompressFile>",roleName="table cell",des="None",并且 "单" 击 "左" 键
		而且 选择元素name="添加(A)",roleName="push button",des="None",并且 "单" 击 "左" 键
		那么 关闭对应应用
		
		当 打开应用,应用名称为 "engrampa"
		而且 选择元素name="归档文件(A)",roleName="menu",des="None",并且 "单" 击 "左" 键
		而且 选择元素name="打开...",roleName="menu item",des="None",并且 "单" 击 "左" 键
		而且 在路径选择窗口中进入 "tmpPath" 目录
		而且 选择元素name="<CompressPkgFormat>",roleName="table cell",des="None",并且 "单" 击 "左" 键
		而且 选择元素name="打开(O)",roleName="push button",des="None",并且 "单" 击 "左" 键
		而且 选择元素name="归档文件(A)",roleName="menu",des="None",并且 "单" 击 "左" 键
		而且 选择元素name="解压缩 (E) ...",roleName="menu item",des="None",并且 "单" 击 "左" 键
		而且 在路径选择窗口中进入 "tmpPath" 目录
		而且 选择元素name="解压缩(E)",roleName="push button",des="None",并且 "单" 击 "左" 键
		而且 选择元素name="退出(Q)",roleName="push button",des="None",并且 "单" 击 "左" 键
		那么 "tmpPath" 下存在文件 "<CompressFile>",文件内容为 "<FileContext>"
        而且 删除 "tmpPath" 目录中存在文件 "<CompressFile>"
        而且 删除 "tmpPath" 目录中存在文件 "<CompressPkgFormat>"


    例子: 各种压缩包格式
    |CompressPkgFormat     |CompressFile  |FileContext                    |
    |engrampa-yasuo.tar.bz2|engrampa-yasuo|helloworld,这是一个压缩测试文件|
    |engrampa-yasuo.tar.gz |engrampa-yasuo|helloworld,这是一个压缩测试文件|
    |engrampa-yasuo.7z     |engrampa-yasuo|helloworld,这是一个压缩测试文件|
    |engrampa-yasuo.zip    |engrampa-yasuo|helloworld,这是一个压缩测试文件|
    |engrampa-yasuo.tar    |engrampa-yasuo|helloworld,这是一个压缩测试文件|
    |engrampa-yasuo.cbz    |engrampa-yasuo|helloworld,这是一个压缩测试文件|
    |engrampa-yasuo.war    |engrampa-yasuo|helloworld,这是一个压缩测试文件|

## 解压出来为tar包
#    |engrampa-yasuo.tar.7z |engrampa-yasuo|helloworld,这是一个压缩测试文件|
## 必须要搜索全部文件，不然无法查看到
#    |engrampa-yasuo.ar     |engrampa-yasuo|helloworld,这是一个压缩测试文件|
## 无法 编辑-添加文件
#    |engrampa-yasuo.xz     |engrampa-yasuo|helloworld,这是一个压缩测试文件|
