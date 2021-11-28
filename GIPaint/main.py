from pygame import *
from tkinter import *
from tkinter import filedialog
from random import *
from math import *

root = Tk()
root.withdraw()

init()

# color variables
RED = (255,0,0)
GREY = (127,127,127)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)

# a list of loading screen images
loading_screen_images = [
                        transform.scale(image.load("images/loading-screen.jpg"), (1300, 700)),
                        transform.scale(image.load("images/loading-screen2.jpg"), (1200, 700)),
                        transform.scale(image.load("images/loading-screen3.jpg"), (1200, 700)),
                        transform.scale(image.load("images/loading-screen4.jpg"), (1200, 700))
                        ]

def loadingscreen(): # display loading screen
    # load stuff
    painter_font = font.Font("fonts/painter-font.ttf", 100)

    logoimage = image.load("images/GI_logo.png")
    #####
    screen.blit(choice(loading_screen_images), (0, 0))
    screen.blit(logoimage, (260, 100))

    paint_text = painter_font.render("Paint", True, (WHITE))
    screen.blit(paint_text, (470, 350))
    
    running=True
    
    while running:
        screen.blit(transform.scale(image.load("images/start-screen-text.png"), (500,106)), ((600 - 250), 500))
        
        for evt in event.get():
            if evt.type == QUIT:
                running = False
                quit()
            if evt.type == MOUSEBUTTONDOWN:
                # start program once the button is pressed
                return
        display.flip()

running = True

bgcol = WHITE
selectedcol = BLACK
previewcol = selectedcol

thickness = 10
MAX_THICKNESS = 40
stamp_dimensions = 128

tool = ""
stamp = ""
menu = "tools"

# Canvas
drawingScreen = Rect(350, 100, 800, 550)

# Rects
menu_bg = Rect(10, 100, 300, 500)

thickness_text_bg = Rect(110, 500, 100, 60)
plus_thickness_bg = Rect(230, 500, 60, 60)
minus_thickness_bg = Rect(30, 500, 60, 60)

plus_stamp_bg = Rect(230, 500, 60, 60)
minus_stamp_bg = Rect(30, 500, 60, 60)

mouse_pos_bg = Rect(110, 605, 200, 50)

# Images
exitButtonImage = image.load("images/exitButton.png")
exitButtonImage = transform.scale(exitButtonImage, (40, 40))
exitButtonRect = exitButtonImage.get_rect(topleft=(10, 650))

color_map = image.load("images/color-map.png")
color_map = transform.scale(color_map, (280, 250))
basic_color_map = image.load("images/basic-color-map.png")
basic_color_map = transform.scale(basic_color_map, (280, 130))

pencil_icon = transform.scale(image.load("images/Pencil-Icon.png"), (80, 80))
eraser_icon = transform.scale(image.load("images/Eraser-Icon.png"), (80, 80))
line_icon = transform.scale(image.load("images/Line-Icon.png"), (80, 80))
FRect_icon = transform.scale(image.load("images/FRect-Icon.png"), (80, 80))
UFRect_icon = transform.scale(image.load("images/UFRect-Icon.png"), (80, 80))
FOval_icon = transform.scale(image.load("images/FOval-Icon.png"), (80, 80))
UFOval_icon = transform.scale(image.load("images/UFOval-Icon.png"), (80, 80))
Clr_icon = transform.scale(image.load("images/Clr-Icon.png"), (80, 80))
Fill_icon = transform.scale(image.load("images/Fill-Icon.png"), (80, 80))
Brush_icon = transform.scale(image.load("images/Brush-Icon.png"), (80, 80))
Spray_icon = transform.scale(image.load("images/Spray-Icon.png"), (80, 80))

primogemStamp = image.load("images/Stamp_Primogem.png")
moraStamp = image.load("images/Stamp_Mora.png")
blueStamp = image.load("images/Stamp_Acquaint_Fate.png")
pinkStamp = image.load("images/Stamp_Intertwined_Fate.png")
fragileStamp = image.load("images/Stamp_Fragile_Resin.png")
heroStamp = image.load("images/Stamp_Heros_Wit.png")

# Text
genshin_font_60 = font.Font("fonts/genshin-font.ttf", 60)
genshin_font_40 = font.Font("fonts/genshin-font.ttf", 40)
genshin_font_20 = font.Font("fonts/genshin-font.ttf", 20)
genshin_font_10 = font.Font("fonts/genshin-font.ttf", 10)

tools_label = genshin_font_40.render("Tools", True, WHITE)
color_label = genshin_font_40.render("Color", True, WHITE)
stamp_label = genshin_font_40.render("Stamps", True, WHITE)
bg_label = genshin_font_40.render("Backgrounds", True, WHITE)
extra_label = genshin_font_40.render("Extra", True, WHITE)

thickness_label = genshin_font_20.render("Thickness", True, WHITE)
plus_button_text = genshin_font_40.render("+", True, WHITE)
minus_button_text = genshin_font_40.render("-", True, WHITE)

stamp_dimension_label = genshin_font_20.render("Dimensions", True, WHITE)

save_text = genshin_font_60.render("Save", True, WHITE)
load_text = genshin_font_60.render("Load", True, WHITE)
info_text = genshin_font_60.render("Info", True, WHITE)

# shortcut text for tools
pencil_key = genshin_font_20.render("P", True, BLACK)
eraser_key = genshin_font_20.render("E", True, BLACK)
line_key = genshin_font_20.render("L", True, BLACK)
fr_key = genshin_font_20.render("M", True, BLACK) # filled rect
ufr_key = genshin_font_20.render("N", True, BLACK) # unfilled rect
fo_key = genshin_font_20.render("B", True, BLACK) # filled oval
ufo_key = genshin_font_20.render("V", True, BLACK) # unfilled oval
clear_key = genshin_font_20.render("C", True, BLACK)
fill_key = genshin_font_20.render("F", True, BLACK)
brush_key = genshin_font_20.render("O", True, BLACK)
spray_key = genshin_font_20.render("S", True, BLACK)

plus_thickness_key = genshin_font_10.render("UP", True, BLACK)
minus_thickness_key = genshin_font_10.render("DOWN", True, BLACK)

# shortcut text for stamps
primo_key = genshin_font_20.render("1", True, BLACK)
mora_key = genshin_font_20.render("2", True, BLACK)
blue_key = genshin_font_20.render("3", True, BLACK)
pink_key = genshin_font_20.render("4", True, BLACK)
fragile_key = genshin_font_20.render("5", True, BLACK)
hero_key = genshin_font_20.render("6", True, BLACK)

# after loading most images and text, make screen
width,height = 1200, 700
screen = display.set_mode((width,height))
display.set_caption('Genshin Impact Paint')
display_image = image.load("images/mini-logo.png")
display_image = transform.scale(display_image, (32, 32))
# change cursor
mouse.set_cursor((1,1), transform.scale(image.load("images/default-cursor.png"), (32, 32)))
# start intro screen
loadingscreen()
display.set_icon(display_image)

# Buttons

toolsButton = Rect(20, 20, 125, 50)
colorButton = Rect(155, 20, 125, 50)
stampButton = Rect(290, 20, 155, 50)
bgButton = Rect(455, 20, 275, 50)
extraButton = Rect(740, 20, 125, 50)

pencilRect = Rect(20, 110, 85, 85)
eraserRect = Rect(115, 110, 85, 85)
lineRect = Rect(210, 110, 85, 85)
filledrectRect = Rect(20, 205, 85, 85)
unfilledrectRect = Rect(115, 205, 85, 85)
filledovalRect = Rect(210, 205, 85, 85)
unfilledovalRect = Rect(20, 300, 85, 85)
clearRect = Rect(115, 300, 85, 85)
fillRect = Rect(210, 300, 85, 85)
brushRect = Rect(20, 395, 85, 85)
sprayRect = Rect(115, 395, 85, 85)

primogemsRect = Rect(20, 110, 85, 85)
moraRect = Rect(115, 110, 85, 85)
blueRect = Rect(210, 110, 85, 85)
pinkRect = Rect(20, 205, 85, 85)
fragileRect = Rect(115, 205, 85, 85)
heroRect = Rect(210, 205, 85, 85)

saveButton = Rect(20, 110, 280, 85)
loadButton = Rect(20, 205, 280, 85)
infoButton = Rect(20, 300, 280, 85)

# a dictionary of all the buttons for tools, [rectObject, isSelected, icon, keybind text, key code]
tools = {
    "pencil": [pencilRect, False, pencil_icon, pencil_key, K_p],
    "eraser": [eraserRect, False, eraser_icon, eraser_key, K_e],
    "line": [lineRect, False, line_icon, line_key, K_l],
    "frect": [filledrectRect, False, FRect_icon, fr_key, K_m],
    "ufrect": [unfilledrectRect, False, UFRect_icon, ufr_key, K_n],
    "foval": [filledovalRect, False, FOval_icon, fo_key, K_b],
    "ufoval": [unfilledovalRect, False, UFOval_icon, ufo_key, K_v],
    "clear": [clearRect, False, Clr_icon, clear_key, K_c],
    "fill": [fillRect, False, Fill_icon, fill_key, K_f],
    "brush": [brushRect, False, Brush_icon, brush_key, K_o],
    "spray": [sprayRect, False, Spray_icon, spray_key, K_s]
}

# a dictionary containing all stamps, [rectObject, isSelected, icon, originalStamp, keybing text, key code]
stamps = {
    "primogem": [primogemsRect, False, transform.scale(primogemStamp, (80, 80)), primogemStamp, primo_key, K_1],
    "mora": [moraRect, False, transform.scale(moraStamp, (80, 80)), moraStamp, mora_key, K_2],
    "blue-fate": [blueRect, False, transform.scale(blueStamp, (80, 80)), blueStamp, blue_key, K_3],
    "pink-fate": [pinkRect, False, transform.scale(pinkStamp, (80, 80)), pinkStamp, pink_key, K_4],
    "fragile-resin": [fragileRect, False, transform.scale(fragileStamp, (80, 80)), fragileStamp, fragile_key, K_5],
    "heros-wit": [heroRect, False, transform.scale(heroStamp, (80, 80)), heroStamp, hero_key, K_6]
}

# a dictionary containing all backgrounds, [rectObject, isSelected, icon, actualBG]
backgrounds = {
    "1": [Rect(20, 110, 280, 150), False, 
    transform.scale(image.load("images/loading-screen.jpg"), (280, 150)), 
    transform.scale(image.load("images/loading-screen.jpg"), (1000, 550))],
    "2": [Rect(20, 270, 280, 150), False, 
    transform.scale(image.load("images/loading-screen2.jpg"), (280, 150)), 
    transform.scale(image.load("images/loading-screen2.jpg"), (875, 550))],
    "3": [Rect(20, 430, 280, 150), False, 
    transform.scale(image.load("images/loading-screen3.jpg"), (280, 150)), 
    transform.scale(image.load("images/loading-screen3.jpg"), (875, 550))]
}

# a dictionary of all the menu buttons, [rectObject, isSelected, text, textpos]
menuButtons = {
    "tools": [toolsButton, True, tools_label, (25, 20)],
    "color": [colorButton, False, color_label, (160, 20)],
    "stamps": [stampButton, False, stamp_label, (295, 20)],
    "backgrounds": [bgButton, False, bg_label, (460, 20)],
    "extra": [extraButton, False, extra_label, (745, 20)]
}

screen.fill((156, 126, 74))

# Drawing
draw.rect(screen, bgcol, drawingScreen)

screen.blit(exitButtonImage, (10, 650))
# draw menu buttons text before because it wont change
for i in menuButtons:
    screen.blit(menuButtons[i][2], menuButtons[i][3])

screen.blit(transform.scale(image.load("images/GI_logo.png"), (265, 115)), (900, -10))

# screenshot
screenshot = screen.subsurface(drawingScreen).copy()
clickedColMenu = False
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
            quit()
        # checks if keyboard shortcuts are pressed
        if evt.type == KEYDOWN:
            keys = key.get_pressed()
            if menu == "tools":
                # change thickness using arrow keys
                if keys[K_UP]:
                    if thickness < MAX_THICKNESS:
                        thickness += 1
                    # max thickness for the pencil tool is 3
                    if thickness >= 3 and tool == "pencil":
                        thickness = 3
                if keys[K_DOWN]:
                    if thickness > 1:
                        thickness -= 1
                # set tool if shortcut is pressed
                for i in tools:
                    if keys[tools[i][4]]:
                        # when a tool is changed, set the thickness to 10, if the current tool is pencil
                        if tool == "pencil":
                            thickness = 10
                        tool = i
                        # max thickness for the pencil tool is 3
                        if thickness > 3 and tool == "pencil":
                            thickness = 3
            if menu == "stamps":
                # change stamp dimension using arrow keys
                if keys[K_UP]:
                    if stamp_dimensions < 256:
                        stamp_dimensions += 8
                if keys[K_DOWN]:
                    if stamp_dimensions > 8:
                        stamp_dimensions -= 8
                # set stamp if shortcut is pressed
                for i in stamps:
                    if keys[stamps[i][5]]:
                        stamp = i

        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 1:
                # set the startpos when clicked
                startpos = evt.pos

            # check if tool is selected and handle thickness changes
            if menu == "tools":
                for i in tools:
                    if tools[i][0].collidepoint((mx, my)):
                        # when a tool is changed, set the thickness to 10, if the current tool is pencil
                        if tool == "pencil":
                            thickness = 10
                        tool = i
                        # max thickness for the pencil tool is 3
                        if thickness > 3 and tool == "pencil":
                            thickness = 3
                if plus_thickness_bg.collidepoint((mx, my)):
                    if thickness < MAX_THICKNESS:
                        thickness += 1
                    # max thickness for the pencil tool is 3
                    if thickness >= 10 and tool == "pencil":
                        thickness = 10
                if minus_thickness_bg.collidepoint((mx, my)):
                    if thickness > 1:
                        thickness -= 1
            
            # check if stamp is selected and handle dimension changes
            if menu == "stamps":
                for i in stamps:
                    if stamps[i][0].collidepoint((mx, my)):
                        stamp = i

                if plus_stamp_bg.collidepoint((mx, my)):
                    if stamp_dimensions < 256:
                        stamp_dimensions += 8
                if minus_stamp_bg.collidepoint((mx, my)):
                    if stamp_dimensions > 8:
                        stamp_dimensions -= 8
            
            # if statements for color
            if menu == "color":
                if color_map.get_rect(topleft=(20, 330)).collidepoint((mx, my)):
                    selectedcol = screen.get_at((mx, my))
                    # sets this to true so it doesnt change the preview color, that way you can see the selected color
                    clickedColMenu = True
                    
                if basic_color_map.get_rect(topleft=(20, 110)).collidepoint((mx, my)):
                    selectedcol = screen.get_at((mx, my))
                    
            # draw background when clicked
            if menu == "backgrounds":
                for i in backgrounds:
                    if backgrounds[i][0].collidepoint((mx, my)):
                        screen.set_clip(drawingScreen)
                        screen.blit(backgrounds[i][3], (325, 100))
                        screen.set_clip(None)

            # save and load and info
            if menu == "extra":
                if saveButton.collidepoint((mx, my)):
                    fname=filedialog.asksaveasfilename(defaultextension=".png")
                    image.save(screenshot, fname)
                if loadButton.collidepoint((mx, my)):
                    fname=filedialog.askopenfilename()
                    supported_extensions = ['.png', '.jpg', '.jpeg']
                    # find extension
                    extension = fname[fname.find('.'):len(fname)]
                    # if extension is valid, load image
                    if extension in supported_extensions:
                        user_image = image.load(fname)
                        # clears canvas first
                        draw.rect(screen, bgcol, drawingScreen)
                        # resizes the image if it is bigger than the canvas
                        if user_image.get_width() > 800:
                            user_image = transform.scale(user_image, (800, user_image.get_height()))
                        if user_image.get_height() > 550:
                            user_image = transform.scale(user_image, (user_image.get_width(), 550))
                        # blit the image
                        screen.blit(user_image, drawingScreen)

                if infoButton.collidepoint((mx, my)):
                    screen.blit(image.load("images/Info.png"), drawingScreen)

            # exit if the button is pressed
            if exitButtonRect.collidepoint((mx, my)):
                running = False
                quit()
                
            # check if menu buttons are pressed
            for i in menuButtons:
                if menuButtons[i][0].collidepoint((mx, my)):
                    menu = i
        
        if evt.type == MOUSEBUTTONUP:
            # screenshot the current screen and then blit it
            screenshot = screen.subsurface(drawingScreen).copy()
            screen.blit(screenshot, drawingScreen)
            mouse.set_visible(True) # make it visible again after using a stamp
            fname = "" # clear fname once image has been added
            # change cursor
            mouse.set_cursor((1,1), transform.scale(image.load("images/default-cursor.png"), (32, 32)))

        # for loop to change menu button color
        for i in menuButtons:
            if i == menu:
                menuButtons[i][1] = True
            else:
                menuButtons[i][1] = False
                        
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    # interact with canvas
    if drawingScreen.collidepoint((mx, my)):
        screen.set_clip(drawingScreen)
        # you can use tools while being in any tab except stamps
        if menu != "stamps" and mb[0]:
            if tool == "pencil":
                # change cursor
                mouse.set_cursor((1,47), transform.scale(image.load("images/pencil-cursor.png"), (48, 48)))
                draw.line(screen, selectedcol, (omx, omy), (mx, my), thickness)
            if tool == "eraser":
                mouse.set_cursor((1,47), transform.scale(image.load("images/eraser-cursor.png"), (48, 48)))
                # calculate slope and draw circles based on that so there are no gaps
                distance = sqrt((omx-mx)**2+(omy-my)**2)
                dx = mx - omx
                dy = my - omy
                draw.circle(screen, bgcol, (startpos), thickness)
                for d in range(1, int(distance), 1):
                    # calculate the position of each circle
                    dotX=omx+dx*d/distance
                    dotY=omy+dy*d/distance  
                    draw.circle(screen, bgcol, (int(dotX), int(dotY)), thickness)
            if tool == "line":
                mouse.set_cursor(SYSTEM_CURSOR_CROSSHAIR)
                screen.blit(screenshot, drawingScreen)
                draw.line(screen, selectedcol, startpos, (mx, my), thickness)
            if tool == "frect":
                mouse.set_cursor(SYSTEM_CURSOR_CROSSHAIR)
                screen.blit(screenshot, drawingScreen)
                rectObject = Rect(startpos[0], startpos[1], (mx - startpos[0]), (my - startpos[1]))
                rectObject.normalize()
                draw.rect(screen, selectedcol, rectObject)
            if tool == "ufrect":
                mouse.set_cursor(SYSTEM_CURSOR_CROSSHAIR)
                screen.blit(screenshot, drawingScreen)
                draw.rect(screen, selectedcol, Rect(startpos[0], startpos[1], (mx - startpos[0]), (my - startpos[1])), thickness)
                # draw square at each corner to get fill them up
                # top left
                draw.rect(screen, selectedcol, Rect(startpos[0] + 1 - thickness / 2, startpos[1] + 1 - thickness / 2, thickness, thickness))
                # top right
                draw.rect(screen, selectedcol, Rect(mx - thickness / 2, startpos[1] + 1 - thickness / 2, thickness, thickness))
                # bottom left
                draw.rect(screen, selectedcol, Rect(startpos[0] + 1 - thickness / 2, my - thickness / 2, thickness, thickness))
                # bottom right
                draw.rect(screen, selectedcol, Rect(mx - thickness / 2, my - thickness / 2, thickness, thickness))
            if tool == "foval":
                mouse.set_cursor(SYSTEM_CURSOR_CROSSHAIR)
                screen.blit(screenshot, drawingScreen)
                rectObject = Rect(startpos[0], startpos[1], (mx - startpos[0]), (my - startpos[1]))
                rectObject.normalize()
                draw.ellipse(screen, selectedcol, rectObject)
            if tool == "ufoval":
                mouse.set_cursor(SYSTEM_CURSOR_CROSSHAIR)
                screen.blit(screenshot, drawingScreen)
                rectObject = Rect(startpos[0], startpos[1], (mx - startpos[0]), (my - startpos[1]))
                rectObject.normalize()
                draw.ellipse(screen, selectedcol, rectObject, thickness)
            if tool == "clear" and mb[0]:
                screen.blit(screenshot, drawingScreen)
                draw.rect(screen, bgcol, drawingScreen)
            if tool == "fill" and mb[0]:
                bgcol = selectedcol
                screen.blit(screenshot, drawingScreen)
                # just draw a rect of over the entire image
                draw.rect(screen, selectedcol, drawingScreen)
            if tool == "brush":
                mouse.set_cursor((1,45), transform.scale(image.load("images/brush-cursor.png"), (48, 48)))
                # calculate slope and draw circles based on that so there are no gaps
                distance = sqrt((omx-mx)**2+(omy-my)**2)
                dx = mx - omx
                dy = my - omy
                draw.circle(screen, selectedcol, (startpos), thickness)
                for d in range(1, int(distance), 1):
                    dotX=omx+dx*d/distance
                    dotY=omy+dy*d/distance  
                    draw.circle(screen, selectedcol, (int(dotX), int(dotY)), thickness)
            if tool == "spray":
                mouse.set_cursor((3,20), transform.scale(image.load("images/spray-cursor.png"), (48, 48)))
                # draw thickness//2 amount of dots for each thickness
                for i in range(thickness//2):
                    randX = randint(-thickness, thickness)
                    randY = randint(-thickness, thickness)
                    if (randX)**2 + (randY)**2 <= thickness**2:
                        draw.circle(screen, selectedcol, (mx + randX, my + randY), 1)
        # draggable stamps
        # you can use stamps while being in the stamps tab
        if menu == "stamps" and mb[0] and len(stamp) > 0:
            mouse.set_visible(False)
            screen.blit(screenshot, drawingScreen)
            # blit the selected stamp to the screen
            screen.blit(transform.scale(stamps[stamp][3], (stamp_dimensions, stamp_dimensions)), (mx - stamp_dimensions // 2, my  - stamp_dimensions // 2))
        screen.set_clip(None)

    # for loop to change selected tool button color
    for i in tools:
        if i == tool:
            tools[i][1] = True
        else:
            tools[i][1] = False

    # draw the tools menu
    if menuButtons["tools"][1]:
        draw.rect(screen, (186, 156, 104), menu_bg)
        for i in tools:
            toolcol = WHITE
            outline = 3
            # changes button color and thickness if hovering or selected
            if tools[i][0].collidepoint((mx, my)):
                toolcol = GREY
                outline = 5
            if tools[i][1]:
                toolcol = GREEN
                outline = 5
            draw.rect(screen, toolcol, tools[i][0], outline, 15)
            screen.blit(tools[i][2], (tools[i][0][0] + 2, tools[i][0][1] + 2))
            screen.blit(tools[i][3], (tools[i][0].topleft[0] + 5, tools[i][0].topleft[1] + 2))

        # everything used for thickness adjustment
        draw.rect(screen, (156, 126, 74), thickness_text_bg)
        draw.rect(screen, (156, 126, 74), plus_thickness_bg)
        draw.rect(screen, (156, 126, 74), minus_thickness_bg)

        thickness_num_label = genshin_font_40.render(f"{thickness}", True, WHITE)

        screen.blit(thickness_label, (106, 560))
        # the x pos value here keeps the thickness text centered at all times 
        screen.blit(thickness_num_label, ((206 + thickness_label.get_width())/2 - thickness_num_label.get_width()/2 + 5, 507))
        screen.blit(plus_button_text, (248, 507))
        screen.blit(minus_button_text, (50, 503))
        screen.blit(plus_thickness_key, (253, 500))
        screen.blit(minus_thickness_key, (43, 500))

    # draw the color menu
    if menuButtons["color"][1]:
        draw.rect(screen, (186, 156, 104), menu_bg)
        screen.blit(color_map, (20, 330))
        screen.blit(basic_color_map, (20, 110))
        
        if color_map.get_rect(topleft=(20, 330)).collidepoint((mx, my)):
            # if the mouse hovers over the color select, make the preview color change color so its easy to see what your selecting
            if not clickedColMenu:
                previewcol = screen.get_at((mx, my))
        else:
            # this turns false until you start hovering again in the color select again
            clickedColMenu = False
            
        # display preview
        draw.rect(screen, previewcol, Rect(20, 275, 280, 50))
        color_text = genshin_font_20.render(f"{previewcol[0], previewcol[1], previewcol[2]}", True, WHITE)
        previewcol = selectedcol
        screen.blit(color_text, (20, 245))

    # for loop to change selected stamp button color
    for i in stamps:
        if i == stamp:
            stamps[i][1] = True
        else:
            stamps[i][1] = False
    
    if menuButtons["stamps"][1]:
        draw.rect(screen, (186, 156, 104), menu_bg)
        for i in stamps:
            stampcol = WHITE
            outline = 3
            # changes button color and thickness if hovering or selected
            if stamps[i][0].collidepoint((mx, my)):
                stampcol = GREY
                outline = 5
            if stamps[i][1]:
                stampcol = GREEN
                outline = 5
            draw.rect(screen, stampcol, stamps[i][0], outline, 15)
            screen.blit(stamps[i][2], (stamps[i][0][0] + 2, stamps[i][0][1] + 2))
            screen.blit(stamps[i][4], (stamps[i][0].topleft[0] + 5, stamps[i][0].topleft[1] + 2))

        # everything used for stamp dimension adjustment
        draw.rect(screen, (156, 126, 74), thickness_text_bg) # reused for the dimensions of stickers
        draw.rect(screen, (156, 126, 74), plus_stamp_bg) # reused for the dimensions of stickers 
        draw.rect(screen, (156, 126, 74), minus_stamp_bg) # reused for the dimensions of stickers
        
        stamp_num_label = genshin_font_20.render(f"{stamp_dimensions}x{stamp_dimensions}", True, WHITE)

        screen.blit(stamp_dimension_label, (100, 560))
        # the x pos value here keeps the dimension text centered at all times
        screen.blit(stamp_num_label, ((200 + stamp_dimension_label.get_width())/2 - stamp_num_label.get_width()/2, 520))
        screen.blit(plus_button_text, (248, 507))
        screen.blit(minus_button_text, (50, 503))
        screen.blit(plus_thickness_key, (253, 500))
        screen.blit(minus_thickness_key, (43, 500))
    
    # draw the bg menu
    if menuButtons["backgrounds"][1]:
        draw.rect(screen, (186, 156, 104), menu_bg)
        for i in backgrounds:
            draw.rect(screen, WHITE, backgrounds[i][0])
            screen.blit(backgrounds[i][2], (backgrounds[i][0][0], backgrounds[i][0][1]))

    # draw the save menu
    if menuButtons["extra"][1]:
        draw.rect(screen, (186, 156, 104), menu_bg)
        extraCol1 = extraCol2 = extraCol3 = WHITE
        outline1 = outline2 = outline3 = 3
        # change colours when hovering
        if saveButton.collidepoint((mx, my)):
            extraCol1 = GREY
            outline1 = 5
        if loadButton.collidepoint((mx, my)):
            extraCol2 = GREY
            outline2 = 5
        if infoButton.collidepoint((mx, my)):
            extraCol3 = GREY
            outline3 = 5
        # save rect
        draw.rect(screen, extraCol1, saveButton, outline1, 15)
        # load rect
        draw.rect(screen, extraCol2, loadButton, outline2, 15)
        # info rect
        draw.rect(screen, extraCol3, infoButton, outline3, 15)
        # blit text
        screen.blit(save_text, (85, 120))
        screen.blit(load_text, (85, 215))
        screen.blit(info_text, (95, 310))

    # draw the mouse pos rect
    draw.rect(screen, (186, 156, 104), mouse_pos_bg)
    # if mouse is in drawing screen, draw the position
    if drawingScreen.collidepoint((mx, my)):
        mouse_position = genshin_font_40.render(f"{mx-350}x{my-100}", True, WHITE)
        screen.blit(mouse_position, (mouse_pos_bg.centerx - mouse_position.get_width()/2, 607))
    else:
        mouse_position = genshin_font_40.render(f"N/A", True, WHITE)
        screen.blit(mouse_position, (mouse_pos_bg.centerx - mouse_position.get_width()/2, 607))
    
    # loop thru menu dictionary and draw the buttons
    for i in menuButtons:
        menucol = (186, 156, 104)
        if menuButtons[i][0].collidepoint((mx, my)):
            menucol = GREY
        if menuButtons[i][1]:
            menucol = GREEN
        draw.rect(screen, menucol, menuButtons[i][0], 3, 15)
    
    # old mouse positions
    omx, omy = mx, my
    
    display.flip()

quit()
