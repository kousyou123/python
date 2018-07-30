from pynput import mouse

def on_move(x,y):
    print(f"鼠标移动到坐标：{(x,y)}")

def on_click(x,y,button,pressed):
    print(f"{'按下' if pressed else '释放'},当前位置是：{(x,y)}")

with mouse.Listener(on_move=on_move,on_click=on_click) as listener:
    listener.join()