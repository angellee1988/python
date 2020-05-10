
"""
注1.xlwt和pandas每个工作页最多写入256列，因此测试用例修改为每页有2000行256列的整数.
    注2.xlutils读写依赖于xlrd和xlwt，不单独测试。
    注3.openpyxl测试两种模式，一是普通加载写入，二是read_only/write_only模式下的加载写入。
    注4.DataNitro要收费，且需依托Excel使用，本次不测试。

读写性能比较
    单从读写的性能上考虑，win32com的性能是最好的，xlwings其次。
    openpyxl虽然操作Excel的功能强大，但读写性能过于糟糕，尤其是写大表时，会占用大量内存（把我的4G内存用完了），开启read_only和write_only模式后对其性能有大幅提升，尤其是对读的性能提升很大，使其几乎不耗时（0.01秒有点夸张，不过确实是加载上了）。pandas把Excel当作数据读写的容器，为其强大的数据分析服务，因此读写性能表现中规中矩，但其对Excel文件兼容性是最好的，支持读写.xls，.xlsx文件，且支持只读表中单一工作页。同样支持此功能的库还有xlrd，但xlrd只支持读，并不支持写，且性能不突出，需要配合xlutils进行Excel操作，并使用xlwt保存数据，而xlwt只能写入.xls文件（另一个可以写入.xls文件的库是pandas，且这两个写入的Excel文件最多只能有256列，其余库就我目前的了解均只能写入.xlsx文件），性能一般。xlsxwriter功能单一，一般用来创建.xlsx文件，写入性能中庸。win32com拥有最棒的读写性能，但该库存在于pywin32的库中，自身没有完善的文档，使用略吃力。xlwings拥有和win32com不相伯仲的读写性能，强大的转换器可以处理大部分数据类型，包括二维的numpy array和pandas DataFrame，可以轻松搞定数据分析的工作。
    综合考虑，xlwings的表现最佳，正如其名，xlwings——Make Excel Fly！

便捷性比较
    本测试目前只是针对Excel文件的读写，并未涉及Excel操作，单从读写的便捷性来讲，各库的表现难分上下，但是win32com和xlwings这两个库可以在程序运行时实时在打开的Excel文件中进行操作，实现过程的可视化，其次xlwings的数据结构转换器使其可以快速的为Excel文件添加二维数据结构而不需要在Excel文件中重定位数据的行和列，因此从读写的便捷性来比较，仍是xlwings胜出。


"""