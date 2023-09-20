import arcade

row_spacing=20
col_spacing=20
left_margin=200
bottom_margin=200

arcade.open_window(580,580,"Complex Loop")
arcade.set_background_color(arcade.color.ALMOND)

arcade.start_render()

for i in range(10):
    for j in range(10):
        x=left_margin+i*row_spacing
        y=bottom_margin+j*col_spacing
        if (i+j)%2==0:
            arcade.draw_rectangle_filled(x,y,10,10,arcade.color.DARK_BLUE,45)
        else:
            arcade.draw_rectangle_filled(x,y,10,10,arcade.color.RED,45)

arcade.finish_render()

arcade.run()
