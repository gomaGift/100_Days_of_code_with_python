import turtle as t

screen = t.Screen()
pic = "map.gif"
screen.addshape(pic)
t.shape(pic)


def get_mouse_click_coor(x, y):
    print(x, y)


t.onscreenclick(get_mouse_click_coor)


t.mainloop()
