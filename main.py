import pyautogui

# https://www.itread01.com/content/1541652985.html

""" 螢幕操作 """

# 取得螢幕大小
width, height = pyautogui.size()
print(width, height)

# 截圖 返回一個Pillow/PIL的Image物件
pyautogui.screenshot()
pyautogui.screenshot('foo.png')
pyautogui.screenshot(region=(0, 0, 300 ,400))

""" 滑鼠操作 """
# 取得滑鼠目前位置
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)

# 移動到(300, 200)
pyautogui.moveTo(300, 200)

# 花1.5秒移動到(300, 200)
pyautogui.moveTo(500, 200, duration = 1.5)

# 滑鼠向下移動移動500
pyautogui.moveRel(0, 500)

#  用緩動/漸變函式讓滑鼠2秒後移動到(1800,500)位置
#  use tweening/easing function to move mouse over 2 seconds.
pyautogui.moveTo(1800, 500, duration=2, tween=pyautogui.easeInOutQuad)

# 左鍵點擊一次
pyautogui.click(100, 100)

# 左鍵按下 跟左鍵放開
pyautogui.mouseDown(x=100, y=100, button='left')
pyautogui.mouseUp(x=100, y=100, button='left')

pyautogui.doubleClick() # 滑鼠雙擊，其實就是執行兩次click()函式。
pyautogui.rightClick() # 右擊
pyautogui.middleClick() # 中擊

# 滾輪
pyautogui.scroll(200)

# 根據截圖找到按鈕位置
buttonLocation = pyautogui.locateOnScreen('button.png')
x, y = pyautogui.center(buttonLocation)
pyautogui.click(x, y)
"""  """




#  在每次輸入之間暫停0.25秒
# pyautogui.typewrite('Hello world!', interval=0.25)

pyautogui.press('enter')

# pyautogui.press('esc')
# pyautogui.keyDown('shift')
pyautogui.press(['left', 'a', 'a', 'left', 'left', 'left'])
# pyautogui.keyUp('shift')
# pyautogui.hotkey('ctrl', 'c')

pyautogui.press('a')