""" 
@author: Victor
@time: 2018/8/19 11:43 
"""
import xlrd
from util import log
from config import root_path

logs = log.log_message('获取数据')


def get_testcase(filepath, index, module):
    '''
    参考：https://www.2cto.com/kf/201805/745595.html
    :param filepath:  测试数据存放路径
    :param index:   Execl 里面sheet(工作表)的下标 从0开始
    :param module: 指定sheet中用例模块
    :return:
    '''
    try:
        file = xlrd.open_workbook(filepath)
        sheet = file.sheets()[index - 1]  # index 表单 默认一个Excel表中只存储一个表单  从0开始
        nrows = sheet.nrows  # 获取表单行数
        listdata = []
        for i in range(1, nrows):
            dict_canshu = {}
            dict_canshu['module'] = sheet.cell(i, 0).value  # 获取第'i'行'n'列内容
            if dict_canshu['module'] == module:  # dict_canshu['module'] 等于 module 则获取这行数据
                dict_canshu['case_name'] = sheet.cell(i, 1).value
                dict_canshu['url'] = sheet.cell(i, 2).value
                dict_canshu['method'] = sheet.cell(i, 3).value
                dict_canshu['body'] = sheet.cell(i, 4).value
                dict_canshu['asserts'] = sheet.cell(i, 5).value
                listdata.append(dict_canshu)
        logs.logger.info('获取%s内第%s个sheet(工作表)用例模块为"%s"的测试数据' % (filepath, index,module))
        logs.logger.info('测试数据listdata：%s' % listdata)
        return listdata
    except Exception as e:
        logs.logger.error('获取测试用例数据失败，原因：%s' % e)


if __name__ == '__main__':
    # 测试类
    file_path = root_path + '\\data\\case.xlsx'
    get_testcase(file_path, 1, '登录')

