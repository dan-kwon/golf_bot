from splinter import Browser
from splinter.driver.zopetestbrowser import ZopeTestBrowser
browser = Browser("zope.testbrowser")


browser.visit('http://google.com')
input_element = browser.find_by_name('q')
input_element.fill('splinter - python acceptance testing for web applications')
button_element = browser.find_by_name('btnK')
button_element.click()
if browser.is_text_present('splinter.readthedocs.io'):
    print("Yes, the official website was found!")
else:
    print("No, it wasn't found... We need to improve our SEO techniques")

browser.quit()