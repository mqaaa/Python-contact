#! python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Firefox()
#最大化文件
driver.maximize_window()
driver.get('http://www.mail.163.com')
sleep(2)

#切换列表
driver.switch_to.frame("x-URS-iframe")
driver.find_element_by_name("email").clear()
driver.find_element_by_name("email").send_keys("qmeng1128")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("7047162",Keys.ENTER)
sleep(5)

#在表单里面操作完毕后，无论页面是否进行跳转，必须有退出表单的操作
driver.switch_to_default_content()

#定位写信按钮
driver.find_elements_by_class_name("oz0")[1].click()
sleep(1)

#定位收件人输入框并输入收件人信息
driver.find_element_by_class_name("nui-editableAddr-ipt").clear()
driver.find_element_by_class_name("nui-editableAddr-ipt").send_keys('1163306125@qq.com')
#定位邮件的主题并输入信息
driver.find_elements_by_class_name("nui-ipt-input")[2].clear()
driver.find_elements_by_class_name("nui-ipt-input")[2].send_keys("发送邮件测试")

#添加附件
driver.find_element_by_xpath('//input[@type="file"]').send_keys("D:\\python\\try.py")

#由于在邮件正文中有iframe，需先定位并切换到表单中
frame = driver.find_element_by_class_name("APP-editor-iframe")
driver.switch_to_frame(frame)

#输入正文
driver.find_element_by_xpath('//body[@class="nui-scroll"]').click()
driver.find_element_by_xpath('//body[@class="nui-scroll"]').send_keys("Good study, day day up!")
driver.switch_to_default_content()
driver.switch_to_default_content()
#点击发送
driver.find_elements_by_class_name("nui-btn-text")[-2].click()
sleep(5)
driver.quit()
