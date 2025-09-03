import pygame
import pygame_textinput
import random
import time
import webbrowser
import appdirs
import os
import requests
from PIL import Image
import asyncio
import threading
import cv2
import sys


if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

if base_path not in sys.path:
    sys.path.insert(0, base_path)


app_name = "Timberly"

data_dir = appdirs.user_data_dir(app_name)
os.makedirs(data_dir, exist_ok=True)

application_allowed = True
pygame.init()
screen = pygame.display.set_mode((1000,667))
pygame.display.set_caption(app_name)
logo = pygame.image.load(os.path.join(base_path,"assets/logo.png"))
wood = pygame.image.load(os.path.join(base_path,"assets/wood.png"))
pygame.display.set_icon(logo)
clock = pygame.time.Clock()


font = pygame.font.Font(os.path.join(base_path,"fonts/VarelaRound-Regular.ttf"),30)
loading_man = pygame.image.load(os.path.join(base_path,"assets/loading.png"))
timberly = pygame.image.load(os.path.join(base_path,"assets/timberly.png"))
# timberly = pygame.transform.scale(timberly,(350,525))


main_menu_bg = pygame.image.load(os.path.join(base_path,"assets/bgg.png"))
landing_bg = pygame.image.load(os.path.join(base_path,"assets/landing_bg.png"))
screen.blit(landing_bg,(0,0))
screen.blit(timberly,(292,30))
pygame.display.update()


USER_ID = None
USER_NAME = None
HIGH_SCORE = 0
online_game = True
show_name_input = False

if not os.path.exists(os.path.join(data_dir,"user.env")):
    USER_ID = random.randint(100000,9999999)
    try:
        a = requests.get("https://www.example.com")
        show_name_input = True
    except Exception as e:
        count = 10
        i = 0
        while True:
            online_game = False
            screen.blit(main_menu_bg,(0,0))
            pygame.draw.rect(screen,(169,122,87),(30,200,930,207),border_radius=30)
            pygame.draw.rect(screen,(79,32,15),(30,200,930,207),15,30)
            if i%30==0:
                count-=1
            text2 = font.render(f"Restart for online !! Offline Mode Initiating ... {count}",True,(0,0,0))
            screen.blit(note,(430,230))
            screen.blit(text,(70,280))
            screen.blit(text2,(70,330))
            pygame.display.update()
            i+=1
            if i==300:
                break
            events = pygame.event.get()
            for event in events:
                if event.type ==  pygame.QUIT:
                    sys.exit()
            clock.tick(30)
else:
    with open(os.path.join(data_dir,"user.env"),'r') as file:
        a = file.read()
        a = eval(a)
        if a:
            USER_ID = int(a['ID'])
            USER_NAME = a['NAME']
            HIGH_SCORE = a['HIGH SCORE']
        else:
            USER_ID = random.randint(100000,9999999)
            show_name_input = True
            
            
#audio
pygame.mixer.music.load(os.path.join(base_path,"audio/magic_forest.wav"))
dead_sound = pygame.mixer.Sound(os.path.join(base_path,"audio/dead.wav"))
time_up_sound = pygame.mixer.Sound(os.path.join(base_path,"audio/time_up.wav"))
chop_sound = pygame.mixer.Sound(os.path.join(base_path,"audio/chop.wav"))


# Image loads
bg = pygame.image.load(os.path.join(base_path,"assets/bg.png"))
bg2 = pygame.transform.scale(bg, (500,333.5))
tree = pygame.image.load(os.path.join(base_path,"assets/tree.png"))
tree2 = pygame.transform.scale(tree, (100,315))
tree_log = pygame.image.load(os.path.join(base_path,"assets/log.png"))
man_up_left = pygame.image.load(os.path.join(base_path,"assets/man_up_left.png"))
man_down_left = pygame.image.load(os.path.join(base_path,"assets/man_down_left.png"))
man_up_right = pygame.image.load(os.path.join(base_path,"assets/man_up_right.png"))
man_down_right = pygame.image.load(os.path.join(base_path,"assets/man_down_right.png"))


man_up_left2 = pygame.transform.scale(man_up_left,(100,150))
man_down_left2 = pygame.transform.scale(man_down_left,(100,150))
man_up_right2 = pygame.transform.scale(man_up_right,(100,150))
man_down_right2 = pygame.transform.scale(man_down_right,(100,150))




branch = pygame.image.load(os.path.join(base_path,"assets/branch.png"))
branch2 = pygame.transform.scale(branch,(150,30))
branch_flipped = pygame.image.load(os.path.join(base_path,"assets/branch_flipped.png"))
branch_flipped2 = pygame.transform.scale(branch_flipped,(150,30))

dead_man = pygame.image.load(os.path.join(base_path,"assets/dead.png"))
unchanged = pygame.image.load(os.path.join(base_path,"assets/dead.png"))
unchanged = pygame.transform.scale(unchanged,(500,333))
unchanged = pygame.transform.rotate(unchanged,10)
dead_man = pygame.transform.scale(dead_man,(300,200))
dead_man = pygame.transform.rotate(dead_man,10)
dead_man_flipped = pygame.image.load(os.path.join(base_path,"assets/dead_flipped.png"))
dead_man_flipped = pygame.transform.scale(dead_man_flipped,(300,200))
dead_man_flipped = pygame.transform.rotate(dead_man_flipped,-10)

squished_img = pygame.image.load(os.path.join(base_path,"assets/squished.png"))
time_over = pygame.image.load(os.path.join(base_path,"assets/time_over.png"))

wood2 = pygame.transform.scale(wood,(60,60))
wood = pygame.transform.scale(wood,(50,50))

board = pygame.image.load(os.path.join(base_path,"assets/menu.png"))
smiling_man = pygame.image.load(os.path.join(base_path,"assets/smiling_man.png"))
github = pygame.image.load(os.path.join(base_path,'assets/github.png'))
slack = pygame.image.load(os.path.join(base_path,'assets/slack.png'))
watching_man = pygame.image.load(os.path.join(base_path,"assets/watching_man.png"))
tick = pygame.image.load(os.path.join(base_path,"assets/tick.png"))
cloud = pygame.image.load(os.path.join(base_path,"assets/cloud.png"))
cloud = pygame.transform.rotate(cloud,347)
leaderboard_img = pygame.image.load(os.path.join(base_path,"assets/leaderboard.png"))
info_panel = pygame.image.load(os.path.join(base_path,"assets/info_panel2.png"))
aleft = pygame.image.load(os.path.join(base_path,"assets/leftji.png"))
aleft2 = pygame.transform.scale(aleft,(30,30))
aright = pygame.transform.rotate(aleft,180)
aright2 = pygame.transform.scale(aright,(30,30))
wave = pygame.image.load(os.path.join(base_path,"assets/wave.png"))
info_icon = pygame.image.load(os.path.join(base_path,"assets/info.png"))
info_icon_rect = info_icon.get_rect()
info_icon_rect.topleft = (730, 129)

volume = pygame.image.load(os.path.join(base_path,"assets/volume.png"))
mute = pygame.image.load(os.path.join(base_path,"assets/mute2.png"))
sound_rect1 = volume.get_rect()
sound_rect1_alter = volume.get_rect()
sound_rect2 = sound_rect1.copy()
sound_rect2_alter = sound_rect1.copy()
sound_rect3 = sound_rect1.copy()
sound_rect4 = sound_rect1.copy()
mute_rect1 = mute.get_rect()
mute_rect1_alter = mute.get_rect()
mute_rect2 = mute_rect1.copy()
mute_rect2_alter = mute_rect1.copy()
mute_rect3 = mute_rect1.copy()
mute_rect4 = mute_rect1.copy()


sound_rect1.topleft = (728, 519)
mute_rect1.topleft = (730,524)

sound_alter_rect = pygame.Rect(sound_rect1[0]-165,sound_rect1[1],sound_rect1[2]+170,sound_rect1[3])

sound_rect1_alter.topleft = (568+35, 519)
mute_rect1_alter.topleft = (570+35,524)

sound_rect2.topleft = (930,20)
mute_rect2.topleft = (932,25)

sound_alter_rect2 = pygame.Rect(sound_rect2[0]-5, sound_rect2[1]-20, sound_rect2[2]+35, sound_rect2[3]+165)

sound_rect2_alter.topleft = sound_rect2.topleft
mute_rect2_alter.topleft = mute_rect2.topleft

sound_rect3.topleft = (930,20)
mute_rect3.topleft = (932,25)

#fonts
font2 = pygame.font.Font(os.path.join(base_path,"fonts/VarelaRound-Regular.ttf"),24)
font3 = pygame.font.Font(os.path.join(base_path,"fonts/BebasNeue-Regular.ttf"),30)
font4 = pygame.font.Font(os.path.join(base_path,"fonts/VarelaRound-Regular.ttf"),40)
font5 = pygame.font.Font(os.path.join(base_path,"fonts/VarelaRound-Regular.ttf"),28)
font6 = pygame.font.Font(os.path.join(base_path,"fonts/VarelaRound-Regular.ttf"),32)
font7 = pygame.font.Font(os.path.join(base_path,"fonts/BebasNeue-Regular.ttf"),70)
font8 = pygame.font.Font(os.path.join(base_path,"fonts/BebasNeue-Regular.ttf"),45)
font9 = pygame.font.Font(os.path.join(base_path,"fonts/VarelaRound-Regular.ttf"),50)
font10 = pygame.font.Font(os.path.join(base_path,"fonts/VarelaRound-Regular.ttf"),18)

gmail = pygame.image.load(os.path.join(base_path,'assets/gmail.png'))
email = font10.render("yogya.developer@gmail.com",True, (255,255,255))
email_rect = email.get_rect()
email_rect.topleft = (500,213)


#renders
score_ = font.render("Logs:", True, (0,0,0))
menu_return1 = font6.render("Main Menu",True,(255,255,255))
menu_return2 = font6.render("Replay",True,(255,255,255))
play = font.render("PLAY", True, (255,255,255))
leader = font.render("LEADERBOARD", True, (255,255,255))
agi = font.render("Github",True,(255,255,255))
offline = font.render("Offline Mode",True,(0,0,0))
user_name1 = font4.render("Username",True,(255,255,255))
note = font.render("NOTE",True,(255,255,255))
text = font.render("Internet is required, the first time you run the application !!",True,(0,0,0))

manager = pygame_textinput.TextInputManager(validator=lambda input: len(input) <= 12)
textinput = pygame_textinput.TextInputVisualizer(manager=manager, font_object=font4)

textinput.font_color = (255, 255, 255)

ANIMATE_MAN = pygame.USEREVENT
ANIMATE_LOG = pygame.USEREVENT
still_man = True
still_man2 = True
left = True
left2 = True
do_action = False
branch_locs = []
branch_locs2 = []
game_running = False
score = 0
leaderboard_screen = False
BASE_BRANCH_LOC = 510
TOTAL_BRANCHES = 6
time_left = 240
transparency = 255
just_game_over = False
main_menu = False
squished = False
doit = False
score_updated = True
is_there_a_problem = False
log_location = [400,520]
val = 0
credit = font.render("Credits",True,(0,0,0))
credit_rect = credit.get_rect()
credit_rect.topleft = (880,620)
info = False
timer_started = False
SOUND = True
SOUND_PLAYING = False
on_credits_page = False
frame_num = 0
hscore_thread = False
thread_for_hscore = None
leaderboard_thread = False
thread_for_leaderboard = None
on_page = 1
left_allowed = False
right_allowed = False
instruction_num = 0
game_over_screen = False
prev_branch = None
altered_allowed = False
alter_over = False
SOUND_VOLUME = 100
PREV_SOUND_VOLUME = 100
offset_x, offset_y = 0, 0
DRAG_ALLOWED = False

SOUND_RECT = pygame.Rect(sound_rect1_alter[0]+60,sound_rect1_alter[1]+20,100,sound_rect1_alter[3]-40)
SOUND_RECT2 = pygame.Rect(sound_rect2_alter[0]+20,sound_rect2_alter[1]+53,sound_rect2_alter[2]-40,100)


gif = Image.open(os.path.join(base_path,"assets/man.gif"))
frames = []
try:
    while True:
        frame = gif.copy().convert("RGBA")
        mode = frame.mode
        size = frame.size
        data = frame.tobytes()
        surf = pygame.image.fromstring(data, size, mode)
        frames.append(surf)
        gif.seek(gif.tell() + 1)
except EOFError:
    pass  # All frames loaded




def show_high_score():
    try:
        bb = requests.get("https://yogya.pythonanywhere.com/get_score",data={'id': USER_ID})
        # print(bb.content)
        bro = pygame.Surface((370,60))
        bro.blit(main_menu_bg,(0,0),(20,10,370,60))
        if main_menu and online_game:
            if eval(bb.content) != "":
                if eval(bb.content)<999:
                    pygame.draw.rect(bro,(169,122,87),(0,0,270,60),border_radius=30)
                    pygame.draw.rect(bro,(79,32,15),(0,0,270,60),8,30)
                elif eval(bb.content)<9999:
                    pygame.draw.rect(bro,(169,122,87),(0,0,320,60),border_radius=30)
                    pygame.draw.rect(bro,(79,32,15),(0,0,320,60),8,30)
                else:
                    pygame.draw.rect(bro,(169,122,87),(0,0,370,60),border_radius=30)
                    pygame.draw.rect(bro,(79,32,15),(0,0,370,60),8,30)
                offline = font8.render(f"High Score: {eval(bb.content)}",True,(0,0,0))
                if len(str(eval(bb.content)))==1:
                    bro.blit(offline,(41,7))
                elif len(str(eval(bb.content)))==2:
                    bro.blit(offline,(31,7))
                else:
                    bro.blit(offline,(21,7))
                if main_menu:
                    screen.blit(bro,(20,10))
                    pygame.display.update()
    except:
        bro = pygame.Surface((370,60))
        bro.blit(main_menu_bg,(0,0),(20,10,370,60))
        if main_menu and online_game:
            if HIGH_SCORE<999:
                pygame.draw.rect(bro,(169,122,87),(0,0,270,60),border_radius=30)
                pygame.draw.rect(bro,(79,32,15),(0,0,270,60),8,30)
            elif HIGH_SCORE<9999:
                pygame.draw.rect(bro,(169,122,87),(0,0,320,60),border_radius=30)
                pygame.draw.rect(bro,(79,32,15),(0,0,320,60),8,30)
            else:
                pygame.draw.rect(bro,(169,122,87),(0,0,370,60),border_radius=30)
                pygame.draw.rect(bro,(79,32,15),(0,0,370,60),8,30)
            offline = font.render(f"High Score: {HIGH_SCORE}",True,(0,0,0))
            if len(str(HIGH_SCORE))==1:
                bro.blit(offline,(41,8))
            elif len(str(HIGH_SCORE))==2:
                bro.blit(offline,(31,8))
            else:
                bro.blit(offline,(21,8))
            if main_menu:
                screen.blit(bro,(20,10))
                pygame.display.update()


def get_leaderboard():
    fetched = True
    screen.blit(leaderboard_img,(0,20))
    lead = font4.render("LEADERBOARD",True,(255,255,255))
    screen.blit(lead,(350,90))
    try:
        content = eval(requests.get("https://yogya.pythonanywhere.com/get_leaderboard",data={'id': USER_ID,'name': USER_NAME}).content)
        # print(content)
        if (content == "" or type(content)!=list) and leaderboard_screen==True:
            fetched = False
            couldnt = font.render("Couldn't Fetch details ! Try Again Later !!", True, (0,0,0))
            screen.blit(couldnt,(212,350))
            pygame.display.update()
    except:
        fetched = False
        if online_game and leaderboard_screen==True:
            couldnt = font.render("Couldn't Fetch details ! Try Again Later !!", True, (0,0,0))
            screen.blit(couldnt,(212,350))
            pygame.display.update()
        elif leaderboard_screen==True:
            couldnt2 = font.render("| Offline Mode | ", True, (0,0,0))
            couldnt3 = font.render("Re-start application with Internet to exit mode !!",True,(0,0,0))
            screen.blit(couldnt2,(212,350))
            screen.blit(couldnt3,(212,380))
            pygame.display.update()
    if fetched and leaderboard_screen==True:
        if len(content)<=4:
            for i in range(len(content)):
                pygame.draw.rect(screen,(169,122,87),(202,220+(i*80),600,60),border_radius=30)
                pygame.draw.rect(screen,(79,32,15),(202,220+(i*80),600,60),5,30)
                if str(content[i][1])==USER_NAME and int(content[i][2])==HIGH_SCORE:
                    temp_id = font.render(str(content[i][0]),True,(0,0,0))
                    temp_name = font.render(str(content[i][1]),True,(0,0,0))
                    temp_score = font.render(str(content[i][2]),True,(0,0,0))
                else:
                    temp_id = font.render(str(content[i][0]),True,(255,255,255))
                    temp_name = font.render(str(content[i][1]),True,(255,255,255))
                    temp_score = font.render(str(content[i][2]),True,(255,255,255))
                screen.blit(temp_id,(225,233+(i*80)))
                screen.blit(temp_name,(300,233+(i*80)))
                screen.blit(wood,(626,227+(i*80)))
                screen.blit(temp_score,(685,233+(i*80)))
        else:
            for i in range(3):
                pygame.draw.rect(screen,(169,122,87),(202,220+(i*80),600,60),border_radius=30)
                pygame.draw.rect(screen,(79,32,15),(202,220+(i*80),600,60),5,30)
                if str(content[i][1])==USER_NAME and int(content[i][2])==HIGH_SCORE:
                    temp_id = font.render(str(content[i][0]),True,(0,0,0))
                    temp_name = font.render(str(content[i][1]),True,(0,0,0))
                    temp_score = font.render(str(content[i][2]),True,(0,0,0))
                else:
                    temp_id = font.render(str(content[i][0]),True,(255,255,255))
                    temp_name = font.render(str(content[i][1]),True,(255,255,255))
                    temp_score = font.render(str(content[i][2]),True,(255,255,255))
                screen.blit(temp_id,(225,233+(i*80)))
                screen.blit(temp_name,(300,233+(i*80)))
                screen.blit(wood,(626,227+(i*80)))
                screen.blit(temp_score,(685,233+(i*80)))
            pygame.draw.line(screen,(0,0,0),(472,455),(532,455),5)
            pygame.draw.line(screen,(0,0,0),(452,465),(552,465),5)
            pygame.draw.line(screen,(0,0,0),(402,475),(602,475),5)
            pygame.draw.rect(screen,(169,122,87),(202,490,600,60),border_radius=30)
            pygame.draw.rect(screen,(79,32,15),(202,490,600,60),5,30)
            if str(content[-1][1])==USER_NAME and int(content[-1][2])==HIGH_SCORE:
                temp_id = font.render(str(content[-1][0]),True,(0,0,0))
                temp_name = font.render(str(content[-1][1]),True,(0,0,0))
                temp_score = font.render(str(content[-1][2]),True,(0,0,0))
            else:
                temp_id = font.render(str(content[-1][0]),True,(255,255,255))
                temp_name = font.render(str(content[-1][1]),True,(255,255,255))
                temp_score = font.render(str(content[-1][2]),True,(255,255,255))
            screen.blit(temp_id,(225,263+(3*80)))
            screen.blit(temp_name,(300,263+(3*80)))
            screen.blit(wood,(626,257+(3*80)))
            screen.blit(temp_score,(685,263+(3*80)))
        pygame.display.update()


def hscore():
    global hscore_thread
    show_high_score()
    hscore_thread = True
    # print('done hscore')
    
def leading():
    global leaderboard_thread
    get_leaderboard()
    leaderboard_thread = True
    # print('done leading')


def get_random_branch_status():
    global score, prev_branch
    allowed = [1,2,3,4,5,6,7]
    if score<30:
        allowed = [1,2,3,4,5,6,7,8]
    elif score<100:
        allowed = [1,2,3,4,5,6,7,8,9]
    else:
        allowed = [1,2,3,4,5,6,7,8,9,10]
    rr = random.randint(1,10)
    if rr in allowed or prev_branch==None:
        if score<30:
            if prev_branch==None:
                if rr <= len(allowed)//2:
                    prev_branch = 'left'
                    return 'left'
                else:
                    prev_branch = 'right'
                    return 'right'
            if prev_branch=='right':
                if rr<=(len(allowed)-3):
                    prev_branch = 'left'
                    return 'left'
                else:
                    prev_branch = 'right'
                    return 'right'
            if prev_branch=='left':
                if rr<=(len(allowed)-3):
                    prev_branch = 'right'
                    return 'right'
                else:
                    prev_branch = 'left'
                    return 'left'
        else:
            if prev_branch==None:
                if rr <= len(allowed)//2:
                    prev_branch = 'left'
                    return 'left'
                else:
                    prev_branch = 'right'
                    return 'right'
            if prev_branch=='right':
                if rr<=(len(allowed)-2):
                    prev_branch = 'left'
                    return 'left'
                else:
                    prev_branch = 'right'
                    return 'right'
            if prev_branch=='left':
                if rr<=(len(allowed)-2):
                    prev_branch = 'right'
                    return 'right'
                else:
                    prev_branch = 'left'
                    return 'left'
    else:
        prev_branch = None
        return None
    
    
def generate_branch_locs():
    global branch_locs
    if branch_locs==[]:
        last_loc = BASE_BRANCH_LOC
        for i in range(TOTAL_BRANCHES):
            if i==0:
                branch_locs.append([None,(100,last_loc)])
                last_loc-= 200
                continue
            option = get_random_branch_status()
            if option:
                if option=='left':
                    branch_locs.append([option,(600,last_loc)])
                elif option=='right':
                    branch_locs.append([option,(100,last_loc)])
            else:
                branch_locs.append([option,(100,last_loc)])
            last_loc-= 200
    else:
        for i in branch_locs:
            i[1] = (i[1][0],i[1][1]+200)
        option = get_random_branch_status()
        if option:
            if option=='left':
                branch_locs.append([option,(600,branch_locs[-1][1][1]-200)])
            elif option=='right':
                branch_locs.append([option,(100,branch_locs[-1][1][1]-200)])
        else:
            branch_locs.append([option,(100,branch_locs[-1][1][1]-200)])
        branch_locs = branch_locs[1:]

def load_game():
    global score, branch_locs,left,game_running, time_left,screen, just_game_over, squished, main_menu, show_name_input, leaderboard_screen, game_over_screen
    screen.blit(bg, (0,0))
    game_done = False
    if (branch_locs[0][0]=='left' and left==False) or (branch_locs[0][0]=='right' and left==True):
        if SOUND:
            dead_sound.play()
        game_running = False
        just_game_over = True
        squished = True
        score-=1
        main_menu = False
        show_name_input = False
        leaderboard_screen = False
        game_done = True
    for i in branch_locs:
        if i[0]=='left':
            screen.blit(branch,i[1])
        elif i[0]=='right':
            screen.blit(branch_flipped,i[1])
    if game_running:
        if not still_man:
            if left:
                screen.blit(man_down_left,(230,370))
            else:
                screen.blit(man_down_right,(570,370))
        screen.blit(tree, (400,0))
        # screen.blit(bamboo, (300,230))
        if still_man:
            if left:
                screen.blit(man_up_left,(230,360))
            else:
                screen.blit(man_up_right,(570,360))
        screen.blit(tree_log,log_location)
    else:
        screen.blit(tree, (400,0))
        if left:
            screen.blit(dead_man,(120,490))
        else:
            screen.blit(dead_man_flipped,(550,490))
        pygame.display.update()
        time.sleep(1)
    pygame.draw.rect(screen,(169,122,87),(20,20,220,50),border_radius=5)
    pygame.draw.rect(screen,(79,32,15),(20,20,220,50),5,5)
    screen.blit(wood,(30,20))
    score_text = font.render(f"{score}", True, (0,0,0))
    screen.blit(score_,(92,28))
    screen.blit(score_text,(172,28))
    
    if SOUND:
        pygame.draw.rect(screen,(169,122,87),(sound_rect3[0]-5,sound_rect3[1],sound_rect3[2]+10,sound_rect3[3]),border_radius=5)
        pygame.draw.rect(screen,(79,32,15),(sound_rect3[0]-5,sound_rect3[1],sound_rect3[2]+10,sound_rect3[3]),5,5)
        screen.blit(volume, sound_rect3)
    else:
        pygame.draw.rect(screen,(169,122,87),(sound_rect3[0]-5,sound_rect3[1],sound_rect3[2]+10,sound_rect3[3]),border_radius=5)
        pygame.draw.rect(screen,(79,32,15),(sound_rect3[0]-5,sound_rect3[1],sound_rect3[2]+10,sound_rect3[3]),5,5)
        screen.blit(mute, mute_rect3)
    
    pygame.draw.rect(screen,(55,55,55),(670,20,250,50),border_radius=5)
    pygame.draw.rect(screen,(255,255,255),(670,20,250,50),2,5)
    pygame.draw.rect(screen,(255, 234, 0),(675,25,time_left,40),border_radius=5)
    if not timer_started:
        textji = font.render("Press      or      to start !",True,(0,0,0))
        screen.blit(textji,(650,380))
        screen.blit(aleft,(737,385))
        screen.blit(aright,(812,385))
    textji2 = font2.render("Press 'Esc' to exit !",True,(0,0,0))
    screen.blit(textji2,(20,630))
    
    pygame.display.update()
    if game_done:
        loading()
        game_over_page()
        game_over_screen = True


def credits_page():
    screen.blit(landing_bg,(0,0))
    pygame.draw.rect(screen,(169,122,87),(20,20,70,50),border_radius=10)
    pygame.draw.rect(screen,(79,32,15),(20,20,70,50),2,10)
    screen.blit(aleft,(40,30))
    pygame.draw.rect(screen, (31, 42, 54), (100, 100, 800, 270),border_radius=20)
    pygame.draw.rect(screen, (0,0,0), (100, 100, 800, 270),5,border_radius=20)
    
    bbj = font9.render("Yogya Chugh", True, (255, 255, 255))
    screen.blit(bbj, (450, 150))
    screen.blit(gmail,(450,210))
    screen.blit(email, email_rect)
    
    pygame.draw.rect(screen, (0,0,0),(450, 260, 150,50),border_radius=20)
    pygame.draw.rect(screen, (0,0,0),(450, 260, 150,50),4,border_radius=20)
    pygame.draw.rect(screen, (44, 42, 49), (471, 260, 45, 45),border_radius=10)
    screen.blit(github, (471,260))
    agi = font10.render("Github",True,(255,255,255))
    screen.blit(agi, (515,273))
    
    
    pygame.draw.rect(screen, (255,250,250),(610, 260, 150,50),border_radius=20)
    pygame.draw.rect(screen, (0,0,0),(610, 260, 150,50),4,border_radius=20)
    screen.blit(slack, (630, 262))
    
    hey = font3.render('Resource Attributions', True, (255,255,255))
    screen.blit(hey, (120,400))
    pygame.draw.line(screen, (255,255,255),(120,440),(420,440),4)
    hey2 = font2.render('Due to a lot of resources being used,', True, (255,255,255))
    hey3 = font2.render('credits/attributions can be found by clicking on the button below !', True, (255,255,255))
    screen.blit(hey2, (120,460))
    screen.blit(hey3, (120,490))
    
    pygame.draw.rect(screen, (255, 215, 0), (120, 550, 180, 50), border_radius=12)
    pygame.draw.rect(screen, (0,0,0), (120, 550, 180, 50),4, border_radius=12)
    c = font3.render("Credits", True, (0,0,0))
    screen.blit(c, (170,559))
    
    if SOUND:
        pygame.draw.rect(screen,(169,122,87),(sound_rect2[0]-5,sound_rect2[1],sound_rect2[2]+10,sound_rect2[3]),border_radius=5)
        pygame.draw.rect(screen,(79,32,15),(sound_rect2[0]-5,sound_rect2[1],sound_rect2[2]+10,sound_rect2[3]),5,5)
        screen.blit(volume, sound_rect2)
    else:
        pygame.draw.rect(screen,(169,122,87),(sound_rect2[0]-5,sound_rect2[1],sound_rect2[2]+10,sound_rect2[3]),border_radius=5)
        pygame.draw.rect(screen,(79,32,15),(sound_rect2[0]-5,sound_rect2[1],sound_rect2[2]+10,sound_rect2[3]),5,5)
        screen.blit(mute, mute_rect2)
    
    pygame.display.update()



    
def update_timer():
    pygame.draw.rect(screen,(55,55,55),(670,20,250,50),border_radius=5)
    pygame.draw.rect(screen,(255,255,255),(670,20,250,50),2,5)
    pygame.draw.rect(screen,(255, 234, 0),(675,25,time_left,40),border_radius=5)
    pygame.display.update()
    
    
def reset():
    global still_man, left, branch_locs, score, BASE_BRANCH_LOC, TOTAL_BRANCHES, time_left,transparency,just_game_over,main_menu,squished,doit,score_updated,is_there_a_problem, do_action, timer_started
    still_man = True
    left = True
    do_action = False
    branch_locs = []
    score = 0
    BASE_BRANCH_LOC = 510
    TOTAL_BRANCHES = 6
    time_left = 240
    transparency = 255
    just_game_over = False
    main_menu = False
    squished = False
    doit = False
    score_updated = True
    is_there_a_problem = False
    timer_started = False
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    generate_branch_locs()

def reset2():
    global still_man2, left2
    still_man2 = True
    left2 = True
    
    
def game_over_page():
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen,(169,122,87),(200,30,600,607),border_radius=30)
    pygame.draw.rect(screen,(79,32,15),(200,30,600,607),15,30)
    # pygame.draw.rect(screen,(55,55,55),(410,480,180,50),border_radius=5)
    # pygame.draw.rect(screen,(255,255,255),(410,480,190,50),2,5)
    # score_ = font.render("Score:", True, (255,255,255))
    score_text = font4.render(f"{score}", True, (0,0,0))
    aa = 455
    bb = 518
    screen.blit(wood2,(aa-(10*len(str(score))),430))
    screen.blit(score_text,(bb-(10*len(str(score))),436))
    if squished:
        screen.blit(unchanged,(220,100))
        screen.blit(squished_img,(200,-100))
    else:
        screen.blit(time_over,(300,30))
    #Button 1
    pygame.draw.rect(screen,(68, 121, 53),(270,500,200,70),border_radius=10)
    pygame.draw.rect(screen,(15, 51, 31),(270,500,200,70),4,10)
    pygame.draw.rect(screen,(139,69,19),(274,504,192,62),4,5)
    screen.blit(menu_return1,((284,518)))
    #Button 2
    pygame.draw.rect(screen,(68, 121, 53),(530,500,200,70),border_radius=10)
    pygame.draw.rect(screen,(15, 51, 31),(530,500,200,70),4,10)
    pygame.draw.rect(screen,(139,69,19),(534,504,192,62),4,5)
    screen.blit(menu_return2,((574,518)))
    pygame.display.update()

def volume_redraw():
    pygame.draw.rect(screen,(169,122,87),(sound_rect1[0]-5,sound_rect1[1],sound_rect1[2]+10,sound_rect1[3]),border_radius=5)
    pygame.draw.rect(screen,(79,32,15),(sound_rect1[0]-5,sound_rect1[1],sound_rect1[2]+10,sound_rect1[3]),5,5)
    if SOUND:
        screen.blit(volume,sound_rect1)
    else:
        screen.blit(mute,mute_rect1)
    pygame.display.update()

def volume_redraw_alter():
    pygame.draw.rect(screen,(169,122,87),(sound_rect1_alter[0]-5,sound_rect1_alter[1],sound_rect1_alter[2]+135,sound_rect1_alter[3]),border_radius=5)
    pygame.draw.rect(screen,(79,32,15),(sound_rect1_alter[0]-5,sound_rect1_alter[1],sound_rect1_alter[2]+135,sound_rect1_alter[3]),5,5)
    pygame.draw.rect(screen,(79,32,15),(sound_rect1_alter[0]+65,sound_rect1_alter[1]+20,100,sound_rect1_alter[3]-40),2,border_radius=5)
    pygame.draw.circle(screen,(79,32,15),(sound_rect1_alter[0]+65+SOUND_VOLUME, sound_rect1_alter[1]+25),10,10)
    if SOUND:
        screen.blit(volume,sound_rect1_alter)
    else:
        screen.blit(mute,mute_rect1_alter)
    pygame.display.update()
    
def volume_redraw2():
    if SOUND:
        pygame.draw.rect(screen,(169,122,87),(sound_rect2[0]-5,sound_rect2[1],sound_rect2[2]+10,sound_rect2[3]),border_radius=5)
        pygame.draw.rect(screen,(79,32,15),(sound_rect2[0]-5,sound_rect2[1],sound_rect2[2]+10,sound_rect2[3]),5,5)
        screen.blit(volume,sound_rect2)
    else:
        pygame.draw.rect(screen,(169,122,87),(sound_rect2[0]-5,sound_rect2[1],sound_rect2[2]+10,sound_rect2[3]),border_radius=5)
        pygame.draw.rect(screen,(79,32,15),(sound_rect2[0]-5,sound_rect2[1],sound_rect2[2]+10,sound_rect2[3]),5,5)
        screen.blit(mute,mute_rect2)
    pygame.display.update()
    
def volume_redraw_alter2():
    pygame.draw.rect(screen,(169,122,87),(sound_rect2_alter[0]-5,sound_rect2_alter[1],sound_rect2_alter[2]+10,sound_rect2_alter[3]+125),border_radius=5)
    pygame.draw.rect(screen,(79,32,15),(sound_rect2_alter[0]-5,sound_rect2_alter[1],sound_rect2_alter[2]+10,sound_rect2_alter[3]+125),5,5)
    pygame.draw.rect(screen,(79,32,15),(sound_rect2_alter[0]+20,sound_rect2_alter[1]+58,sound_rect2_alter[2]-40,100),2,border_radius=5)
    pygame.draw.circle(screen,(79,32,15),(sound_rect2_alter[0]+25, sound_rect2_alter[1]+158-SOUND_VOLUME),10,10)
    if SOUND:
        screen.blit(volume,sound_rect2_alter)
    else:
        screen.blit(mute,mute_rect2_alter)
    pygame.display.update()
    
def volume_redraw3():
    if SOUND:
        pygame.draw.rect(screen,(169,122,87),(sound_rect3[0]-5,sound_rect3[1],sound_rect3[2]+10,sound_rect3[3]),border_radius=5)
        pygame.draw.rect(screen,(79,32,15),(sound_rect3[0]-5,sound_rect3[1],sound_rect3[2]+10,sound_rect3[3]),5,5)
        screen.blit(volume,sound_rect3)
    else:
        pygame.draw.rect(screen,(169,122,87),(sound_rect3[0]-5,sound_rect3[1],sound_rect3[2]+10,sound_rect3[3]),border_radius=5)
        pygame.draw.rect(screen,(79,32,15),(sound_rect3[0]-5,sound_rect3[1],sound_rect3[2]+10,sound_rect3[3]),5,5)
        screen.blit(mute,mute_rect3)
    pygame.display.update()


def main():
    global hscore_thread, thread_for_hscore
    screen.blit(main_menu_bg,(0,0))
    screen.blit(board,(386,-20))
    screen.blit(smiling_man,(70,300))
    if USER_NAME is not None:
        screen.blit(cloud,(0,80))
        # screen.blit(wood2,(180,135))
        hello = font.render("Hello !",True,(0,0,0))
        screen.blit(wave, (200,160))
        name = font.render(USER_NAME,True,(0,0,0))
        screen.blit(hello,(90,170))
        if len(USER_NAME)<8:
            screen.blit(name,(160,220))
        else:
            screen.blit(name,(110,220))
    
    # screen.blit(button,(480,100))
    pygame.draw.rect(screen,(169,122,87),(info_icon_rect[0]-5,info_icon_rect[1]-5,info_icon_rect[2]+10,info_icon_rect[3]+10),border_radius=5)
    pygame.draw.rect(screen,(79,32,15),(info_icon_rect[0]-5,info_icon_rect[1]-5,info_icon_rect[2]+10,info_icon_rect[3]+10),5,5)
    screen.blit(info_icon,info_icon_rect)
    pygame.draw.rect(screen,(169,122,87),(527,220,220,50),border_radius=5)
    pygame.draw.rect(screen,(79,32,15),(527,220,220,50),5,5)
    screen.blit(play,(597,228))
    pygame.draw.rect(screen,(169,122,87),(507,310,260,50),border_radius=5)
    pygame.draw.rect(screen,(79,32,15),(507,310,260,50),5,5)
    screen.blit(leader,(522,318))
    credits = font.render("Credits", True, (255,255,255))
    pygame.draw.rect(screen, (169,122,87), (550,400,170,50), border_radius=12)
    pygame.draw.rect(screen, (79,32,15), (550,400,170,50), 5, border_radius=12)
    screen.blit(credits, (578,409))
    
    if SOUND:
        # (568, 519)
        pygame.draw.rect(screen,(169,122,87),(sound_rect1[0]-5,sound_rect1[1],sound_rect1[2]+10,sound_rect1[3]),border_radius=5)
        pygame.draw.rect(screen,(79,32,15),(sound_rect1[0]-5,sound_rect1[1],sound_rect1[2]+10,sound_rect1[3]),5,5)
        screen.blit(volume,sound_rect1)
    else:
        pygame.draw.rect(screen,(169,122,87),(sound_rect1[0]-5,sound_rect1[1],sound_rect1[2]+10,sound_rect1[3]),border_radius=5)
        pygame.draw.rect(screen,(79,32,15),(sound_rect1[0]-5,sound_rect1[1],sound_rect1[2]+10,sound_rect1[3]),5,5)
        screen.blit(mute,mute_rect1)
    
    if not online_game:
        pygame.draw.rect(screen,(169,122,87),(10,10,260,60),border_radius=30)
        pygame.draw.rect(screen,(79,32,15),(10,10,260,60),8,30)
        screen.blit(offline,(37,22))
        
    if online_game and not hscore_thread:
        thread_for_hscore = threading.Thread(target=hscore)
        thread_for_hscore.start()
    
    pygame.display.update()


def loading():
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    screen.blit(main_menu_bg,(0,0))
    screen.blit(loading_man,(325,71))
    pygame.display.update()
    
def display_info():
    pygame.draw.rect(screen,(169,122,87),(202,500,600,50),border_radius=30)
    pygame.draw.rect(screen,(79,32,15),(202,500,600,50),5,30)
    if instruction_num==0:
        textji = font2.render("Press       to save urself from the branch above !",True,(0,0,0))
        screen.blit(textji,(222,510))
        screen.blit(aright2,(290,512))
    elif instruction_num==1:
        textji = font2.render("Press       now, chopping the log while moving !",True,(0,0,0))
        screen.blit(textji,(222,510))
        screen.blit(aleft2,(290,512))
        # screen.blit(aright2,(280,512))
    elif instruction_num==2:
        textji = font2.render("You can stay left or cut branch on the right",True,(0,0,0))
        screen.blit(textji,(222,510))
        screen.blit(aright2,(740,512))
    elif instruction_num==3:
        textji = font2.render("Hurray !! You did it my boi",True,(0,0,0))
        screen.blit(textji,(362,510))
    pygame.display.update()
    
def information():
    screen.blit(main_menu_bg,(0,0))
    pygame.draw.rect(screen,(169,122,87),(20,20,70,50),border_radius=10)
    pygame.draw.rect(screen,(79,32,15),(20,20,70,50),2,10)
    screen.blit(aleft,(40,30))
    screen.blit(info_panel,(-20,0))
    
    how = font4.render("HOW TO PLAY ?",True,(255,255,255))
    screen.blit(how,(343,75))
    
    if on_page==1:
        pygame.draw.rect(screen,(169,122,87),(202,500,600,50),border_radius=30)
        pygame.draw.rect(screen,(79,32,15),(202,500,600,50),5,30)

        textji = font2.render("Press       or       for chopping woods & moving !",True,(0,0,0))
        screen.blit(textji,(222,510))
        screen.blit(aleft2,(290,512))
        screen.blit(aright2,(360,512))
        draw_playable1()
    elif on_page==2:
        draw_playable2()
    elif on_page==3:
        pygame.draw.rect(screen,(169,122,87),(202,200,600,50),border_radius=30)
        pygame.draw.rect(screen,(79,32,15),(202,200,600,50),5,30)
        textji = font2.render("Take care of this deadly timer. It runs out fast !!",True,(0,0,0))
        screen.blit(textji,(222,210))
        
        pygame.draw.rect(screen,(55,55,55),(370,270,250,50),border_radius=5)
        pygame.draw.rect(screen,(255,255,255),(370,270,250,50),2,5)
        pygame.draw.rect(screen,(255, 234, 0),(375,275,150,40),border_radius=5)
        pygame.display.update()
        
        pygame.draw.rect(screen,(169,122,87),(202,340,600,190),border_radius=30)
        pygame.draw.rect(screen,(79,32,15),(202,340,600,190),5,30)
        textji = font2.render("Move fast with the keys !",True,(0,0,0))
        screen.blit(textji,(222,350))
        textji2 = font2.render("Every move increases time in the bar !",True,(0,0,0))
        screen.blit(textji2,(222,380))
        textji3 = font2.render("Note: You can press 'm' on your keyboard",True,(0,0,0))
        screen.blit(textji3,(222,460))
        textji4 = font2.render("            for mute/unmute shortcut",True,(0,0,0))
        screen.blit(textji4,(222,490))
        
    # textji2 = font10.render("To stay on the same side and chop, ",True,(0,0,0))
    # screen.blit(textji2,(212,425))
    # textji3 = font10.render("   press the arrow key to that direction !!",True,(0,0,0))
    # screen.blit(textji3,(212,450))
    # textji4 = font10.render("If branch is above your head,",True,(0,0,0))
    # screen.blit(textji4,(212,475))
    # textji5 = font10.render("   Move to the opposite side to prevent getting squished",True,(0,0,0))
    # screen.blit(textji5,(212,500))
    # textji6 = font10.render("Also, Branch on the same level as you on the opposite side can be cut",True,(0,0,0))
    # screen.blit(textji6,(212,525))
    
    if SOUND:
        pygame.draw.rect(screen,(169,122,87),(sound_rect2[0]-5,sound_rect2[1],sound_rect2[2]+10,sound_rect2[3]),border_radius=5)
        pygame.draw.rect(screen,(79,32,15),(sound_rect2[0]-5,sound_rect2[1],sound_rect2[2]+10,sound_rect2[3]),5,5)
        screen.blit(volume,sound_rect2)
    else:
        pygame.draw.rect(screen,(169,122,87),(sound_rect2[0]-5,sound_rect2[1],sound_rect2[2]+10,sound_rect2[3]),border_radius=5)
        pygame.draw.rect(screen,(79,32,15),(sound_rect2[0]-5,sound_rect2[1],sound_rect2[2]+10,sound_rect2[3]),5,5)
        screen.blit(mute,mute_rect2)
    
    if on_page!=3:
        pygame.draw.rect(screen,(169,122,87),(752,560,70,50),border_radius=10)
        pygame.draw.rect(screen,(79,32,15),(752,560,70,50),2,10)
        screen.blit(aright,(770,570))
    
    if on_page!=1:
        pygame.draw.rect(screen,(169,122,87),(202,560,70,50),border_radius=10)
        pygame.draw.rect(screen,(79,32,15),(202,560,70,50),2,10)
        screen.blit(aleft,(220,570))
        
    if on_page==3:
        pygame.draw.rect(screen,(0, 128, 0),(722,560,100,50),border_radius=10)
        pygame.draw.rect(screen,(0,0,0),(722,560,100,50),4,10)
        textji = font3.render("PLAY !",True,(0,0,0))
        screen.blit(textji,(745,568))
        
    pygame.display.update()
    

def draw_playable1():
    screen.blit(bg2, (255,155))
    pygame.draw.rect(screen,(0,0,0),(255,155,500,333.5),5)
    screen.blit(tree2, (455,155))
    if not still_man2:
        if left2:
            screen.blit(man_down_left2,(370,340))
        else:
            screen.blit(man_down_right2,(540,340))
    screen.blit(tree2, (455,155))
    # screen.blit(bamboo, (300,230))
    if still_man2:
        if left2:
            screen.blit(man_up_left2,(370,335))
        else:
            screen.blit(man_up_right2,(540,335))    
    
    pygame.display.update()
    
def draw_playable2():
    display_info()
    screen.blit(bg2, (255,155))
    pygame.draw.rect(screen,(0,0,0),(255,155,500,333.5),5)
    screen.blit(tree2, (455,155))
    if not still_man2:
        if left2:
            screen.blit(man_down_left2,(370,340))
        else:
            screen.blit(man_down_right2,(540,340))
    screen.blit(tree2, (455,155))
    # screen.blit(bamboo, (300,230))
    if still_man2:
        if left2:
            screen.blit(man_up_left2,(370,335))
        else:
            screen.blit(man_up_right2,(540,335))
            
    for i in branch_locs2:
        if i[0]=='left':
            screen.blit(branch_flipped2,i[1])
        elif i[0]=='right':
            screen.blit(branch2,i[1])
    pygame.display.update()

def leaderboard():
    global leaderboard_thread, thread_for_leaderboard
    screen.blit(main_menu_bg,(0,0))
    pygame.draw.rect(screen,(169,122,87),(20,20,70,50),border_radius=10)
    pygame.draw.rect(screen,(79,32,15),(20,20,70,50),2,10)
    screen.blit(aleft,(40,30))
    screen.blit(leaderboard_img,(0,20))
    lead = font4.render("LEADERBOARD",True,(255,255,255))
    screen.blit(lead,(350,90))
    couldnt = font.render("Retrieving ...", True, (0,0,0))
    screen.blit(couldnt,(412,350))
    
    if SOUND:
        pygame.draw.rect(screen,(169,122,87),(sound_rect2[0]-5,sound_rect2[1],sound_rect2[2]+10,sound_rect2[3]),border_radius=5)
        pygame.draw.rect(screen,(79,32,15),(sound_rect2[0]-5,sound_rect2[1],sound_rect2[2]+10,sound_rect2[3]),5,5)
        screen.blit(volume,sound_rect2)
    else:
        pygame.draw.rect(screen,(169,122,87),(sound_rect2[0]-5,sound_rect2[1],sound_rect2[2]+10,sound_rect2[3]),border_radius=5)
        pygame.draw.rect(screen,(79,32,15),(sound_rect2[0]-5,sound_rect2[1],sound_rect2[2]+10,sound_rect2[3]),5,5)
        screen.blit(mute,mute_rect2)
    
    pygame.display.update()
    
    if not leaderboard_thread:
        thread_for_leaderboard = threading.Thread(target=leading)
        thread_for_leaderboard.start()



def name_input():
    screen.blit(landing_bg,(0,0))
    
    pygame.draw.rect(screen,(169,122,87),(140,270,730,207),border_radius=30)
    pygame.draw.rect(screen,(79,32,15),(140,270,730,207),15,30)
    
    screen.blit(watching_man,(140,0))
    
    screen.blit(user_name1,(200,300))
    pygame.draw.rect(screen,(169,122,87),(180,360,550,87),border_radius=30)
    pygame.draw.rect(screen,(79,32,15),(180,360,550,87),6,30)
    pygame.display.update()
allow_textinput = False
if show_name_input:
    name_input()
else:
    main_menu = True
    SOUND_PLAYING = True
    pygame.mixer.music.play(-1)
    generate_branch_locs()
    main()
while True:
    events = pygame.event.get()
    if game_running:
        pos = pygame.mouse.get_pos()
        if (alter_over and sound_rect2.collidepoint(pos[0],pos[1])) or (alter_over and mute_rect2.collidepoint(pos[0],pos[1])) or (not alter_over and sound_rect2_alter.collidepoint(pos[0],pos[1])) or (not alter_over and SOUND_RECT2.collidepoint(pos[0],pos[1])) or (not alter_over and pos[0]>(sound_rect2_alter[0]+20) and pos[0]<(sound_rect2_alter[0]+40) and pos[1]>(sound_rect2_alter[1]+153-SOUND_VOLUME) and pos[1]<(sound_rect2_alter[1]+173-SOUND_VOLUME)):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and still_man:
                    if not timer_started:
                        timer_started = True
                    still_man = False
                    left = True
                    do_action = True
                    score += 1
                    val = 0
                    pygame.time.set_timer(ANIMATE_MAN,50,1)
                    pygame.time.set_timer(ANIMATE_LOG,1,10)
                    if time_left<=240-4 and time_left!=0:
                        time_left+=4
                    generate_branch_locs()
                    if SOUND:
                        chop_sound.play()
                    load_game()
                elif event.key == pygame.K_RIGHT and still_man:
                    if not timer_started:
                        timer_started = True
                    still_man = False
                    left = False
                    do_action = True
                    score += 1
                    val = 0
                    if time_left<=240-4 and time_left!=0:
                        time_left+=4
                    pygame.time.set_timer(ANIMATE_MAN,50,1)
                    pygame.time.set_timer(ANIMATE_LOG,1,10)
                    generate_branch_locs()
                    if SOUND:
                        chop_sound.play()
                    load_game()
                elif event.key == pygame.K_ESCAPE:
                    game_running = False
                    just_game_over = True
                    show_name_input = False
                    leaderboard_screen = False
                    game_done = True
                    main_menu = True
                    loading()
                    if hscore_thread:
                        try:
                            thread_for_hscore.join()
                        except:
                            pass
                        hscore_thread = False
                    if SOUND:
                        SOUND_PLAYING = True
                        pygame.mixer.music.play(-1)
                    main()
                elif event.key == pygame.K_m:
                    SOUND = not SOUND
                    if SOUND and not SOUND_PLAYING:
                        SOUND_PLAYING = True
                        if SOUND_VOLUME==0:
                            SOUND_VOLUME = PREV_SOUND_VOLUME
                        pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    elif not SOUND and SOUND_PLAYING:
                        SOUND_PLAYING = False
                        PREV_SOUND_VOLUME = SOUND_VOLUME
                        SOUND_VOLUME = 0
                        pygame.mixer.music.set_volume(0)
                    if alter_over:
                        volume_redraw2()
                    else:
                        volume_redraw_alter2()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not alter_over and event.pos[0]>(sound_rect2_alter[0]+20) and event.pos[0]<(sound_rect2_alter[0]+40) and event.pos[1]>(sound_rect2_alter[1]+153-SOUND_VOLUME) and event.pos[1]<(sound_rect2_alter[1]+173-SOUND_VOLUME):
                    DRAG_ALLOWED = True
                elif alter_over and (sound_rect2.collidepoint(event.pos[0],event.pos[1]) or mute_rect2.collidepoint(event.pos[0],event.pos[1])):
                    SOUND = not SOUND
                    if SOUND and not SOUND_PLAYING:
                        SOUND_PLAYING = True
                        if SOUND_VOLUME==0:
                            SOUND_VOLUME = PREV_SOUND_VOLUME
                        pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    elif not SOUND and SOUND_PLAYING:
                        SOUND_PLAYING = False
                        PREV_SOUND_VOLUME = SOUND_VOLUME
                        SOUND_VOLUME = 0
                        pygame.mixer.music.set_volume(0)
                    volume_redraw2()
                elif (not alter_over and sound_rect2_alter.collidepoint(event.pos[0],event.pos[1])) or (not alter_over and mute_rect2_alter.collidepoint(event.pos[0],event.pos[1])):
                    SOUND = not SOUND
                    if SOUND and not SOUND_PLAYING:
                        SOUND_PLAYING = True
                        if SOUND_VOLUME==0:
                            SOUND_VOLUME = PREV_SOUND_VOLUME
                        pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    elif not SOUND and SOUND_PLAYING:
                        SOUND_PLAYING = False
                        PREV_SOUND_VOLUME = SOUND_VOLUME
                        SOUND_VOLUME = 0
                        pygame.mixer.music.set_volume(0)
                    volume_redraw_alter2()
                elif not alter_over and SOUND_RECT2.collidepoint(event.pos[0], event.pos[1]):
                    SOUND_VOLUME = (SOUND_RECT2[1]+SOUND_RECT2[3]) - event.pos[1]
                    if SOUND_VOLUME==0:
                        SOUND = not SOUND
                        SOUND_PLAYING = False
                    else:
                        SOUND = True
                        SOUND_PLAYING = True
                    pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    volume_redraw_alter2()
            elif event.type == pygame.MOUSEBUTTONUP:
                DRAG_ALLOWED = False
            elif not alter_over and event.type == pygame.MOUSEMOTION and DRAG_ALLOWED:
                mouse_x, mouse_y = event.pos
                SOUND_VOLUME = (SOUND_RECT2[1]+SOUND_RECT2[3]) - mouse_y
                if SOUND_VOLUME!=PREV_SOUND_VOLUME:
                    if SOUND_VOLUME<0:
                        SOUND_VOLUME=0
                    if SOUND_VOLUME>100:
                        SOUND_VOLUME=100
                    if SOUND_VOLUME==0:
                        SOUND = False
                        SOUND_PLAYING = False
                    else:
                        SOUND = True
                        SOUND_PLAYING = True
                    PREV_SOUND_VOLUME = SOUND_VOLUME
                    pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    volume_redraw_alter2()
            else:
                if (sound_rect2.collidepoint(pos[0],pos[1])) or (mute_rect2.collidepoint(pos[0],pos[1])) and altered_allowed:
                    altered_allowed = False
                    alter_over = False
                    volume_redraw_alter2()
                elif not sound_alter_rect2.collidepoint(pos[0],pos[1]) and not alter_over:
                    altered_allowed = True
                    alter_over = True
                    screen.blit(bg,sound_alter_rect2,sound_alter_rect2)
                    volume_redraw2()
            if event.type == ANIMATE_MAN:
                still_man = True
                load_game()
            if event.type == ANIMATE_LOG:
                val+=1
                if val==10:
                    log_location = [400,520]
                    val = 0
                else:
                    if left:
                        log_location = [log_location[0]+10,log_location[1]+30]
                    else:
                        log_location = [log_location[0]-10,log_location[1]+30]
        if time_left!=0 and timer_started:
            time_left-=1
            if game_running:
                update_timer()
        elif time_left==0:
            game_running = False
            just_game_over = True
            main_menu = False
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            show_name_input = False
            leaderboard_screen = False
            loading()
            if SOUND:
                time_up_sound.play()
            game_over_page()
            game_over_screen = True
    if game_over_screen:
        if online_game:
            if score>HIGH_SCORE:
                some_text = font7.render("HIGH SCORE !!",True,(0,0,0))
                some_text = pygame.transform.rotate(some_text,30)
                screen.blit(some_text,(130,-10))
                pygame.display.update()
                doit = True
                score_updated = False
                HIGH_SCORE = score
                with open(os.path.join(data_dir,'user.env'),'w') as file:
                    file.write(str({'ID': USER_ID, 'NAME': USER_NAME, 'HIGH SCORE': HIGH_SCORE}))
            if doit:
                doit = False
                try:
                    # print(f'updated with {HIGH_SCORE}')
                    t = requests.post("https://yogya.pythonanywhere.com/update_score",data={'id': USER_ID, 'score': HIGH_SCORE})
                    if t.content == "":
                        is_there_a_problem = True
                        something = font2.render("Couldn't update score !",True,(0,0,0))
                        screen.blit(something,(320,580))
                        pygame.draw.rect(screen,(255,255,255),(600,580,80,35),border_radius=10)
                        pygame.draw.rect(screen,(0,0,0),(600,580,80,35),3,10)
                        retry = font2.render("Retry",True,(0,0,0))
                        screen.blit(retry,(610,582))
                        pygame.display.update()
                except:
                    # print("Couldn't update score")
                    is_there_a_problem = True
                    something = font2.render("Couldn't update score !",True,(0,0,0))
                    screen.blit(something,(320,580))
                    pygame.draw.rect(screen,(255,255,255),(600,580,80,35),border_radius=10)
                    pygame.draw.rect(screen,(0,0,0),(600,580,80,35),3,10)
                    retry = font2.render("Retry",True,(0,0,0))
                    screen.blit(retry,(610,582))
                    pygame.display.update()
        else:
            if score>HIGH_SCORE:
                some_text = font7.render("HIGH SCORE !!",True,(0,0,0))
                some_text = pygame.transform.rotate(some_text,40)
                screen.blit(some_text,(130,-10))
                pygame.display.update()
                HIGH_SCORE = score
                something = font2.render("No score updated | Offline_Mode |",True,(0,0,0))
                screen.blit(something,(310,580))
                pygame.display.update()
            
        pos = pygame.mouse.get_pos()
        if (pos[0]>270 and pos[0]<470 and pos[1]>500 and pos[1]<570) or (pos[0]>530 and pos[0]<730 and pos[1]>500 and pos[1]<570) or (is_there_a_problem and pos[0]>600 and pos[0]<680 and pos[1]>580 and pos[1]<615):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.pos[0]>270 and event.pos[0]<470 and event.pos[1]>500 and event.pos[1]<570):
                    main_menu = True
                    loading()
                    if SOUND and not SOUND_PLAYING:
                        SOUND_PLAYING = True
                        pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    elif not SOUND and SOUND_PLAYING:
                        SOUND_PLAYING = False
                        pygame.mixer.music.set_volume(0)
                    game_over_screen = False
                    if hscore_thread:
                        try:
                            thread_for_hscore.join()
                        except:
                            pass
                        hscore_thread = False
                    main()
                elif (event.pos[0]>530 and event.pos[0]<730 and event.pos[1]>500 and event.pos[1]<570):
                    game_running=True
                    game_over_screen = False
                    loading()
                    reset()
                    load_game()
                elif (is_there_a_problem and event.pos[0]>600 and event.pos[0]<680 and event.pos[1]>580 and event.pos[1]<615):
                    try:
                        pygame.draw.rect(screen,(169,122,87),(320,580,360,35))
                        something = font2.render("Retrying ...",True,(0,0,0))
                        screen.blit(something,(450,580))
                        pygame.display.update()
                        t = requests.post("https://yogya.pythonanywhere.com/update_score",data={'id': USER_ID, 'score': HIGH_SCORE})
                        if t.content == "":
                            is_there_a_problem = True
                            pygame.draw.rect(screen,(169,122,87),(320,580,360,35))
                            something = font2.render("Couldn't update score !",True,(0,0,0))
                            screen.blit(something,(320,580))
                            pygame.draw.rect(screen,(255,255,255),(600,580,80,35),border_radius=10)
                            pygame.draw.rect(screen,(0,0,0),(600,580,80,35),3,10)
                            retry = font2.render("Retry",True,(0,0,0))
                            screen.blit(retry,(610,582))
                        else:
                            is_there_a_problem = False
                            pygame.draw.rect(screen,(169,122,87),(320,580,360,35))
                        pygame.display.update()
                    except:
                        is_there_a_problem = True
                        pygame.draw.rect(screen,(169,122,87),(320,580,360,35))
                        something = font2.render("Couldn't update score !",True,(0,0,0))
                        screen.blit(something,(320,580))
                        pygame.draw.rect(screen,(255,255,255),(600,580,80,35),border_radius=10)
                        pygame.draw.rect(screen,(0,0,0),(600,580,80,35),3,10)
                        retry = font2.render("Retry",True,(0,0,0))
                        screen.blit(retry,(610,582))
                        pygame.display.update()
    elif not main_menu and show_name_input and not leaderboard_screen and not info and not on_credits_page:
        pos = pygame.mouse.get_pos()
        if allow_textinput:
            textinput.update(events)
            pygame.draw.rect(screen,(169,122,87),(180,360,550,87),border_radius=30)
            pygame.draw.rect(screen,(79,32,15),(180,360,550,87),6,30)
            screen.blit(textinput.surface,(210,383))
            
            if textinput.value!="":
                pygame.draw.rect(screen,(0, 128, 0),(745,360,100,87),border_radius=30)
                pygame.draw.rect(screen,(79,32,15),(745,360,100,87),6,30)
                screen.blit(tick,(755,368))
            else:
                pygame.draw.rect(screen,(169,122,87),(745,360,100,87),border_radius=30)
                pygame.draw.rect(screen,(169,122,87),(745,360,100,87),6,30)
            if (pos[0]>180 and pos[0]<730 and pos[1]>360 and pos[1]<447):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
            elif (textinput.value!="" and pos[0]>745 and pos[0]<845 and pos[1]>360 and pos[1]<447):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        else:
            if (pos[0]>180 and pos[0]<730 and pos[1]>360 and pos[1]<447):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)
        
        pygame.display.update()
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.pos[0]>180 and event.pos[0]<730 and event.pos[1]>360 and event.pos[1]<447):
                    allow_textinput = True
                elif (textinput.value!="" and event.pos[0]>745 and event.pos[0]<845 and event.pos[1]>360 and event.pos[1]<447):
                    allow_textinput = False
                    show_name_input = False
                    answer = str(textinput.value).lower().title()
                    try:
                        requests.post("https://yogya.pythonanywhere.com/register_user",data={'id': USER_ID,'name': answer})
                        with open(os.path.join(data_dir,"user.env"),'w') as file:
                            file.write(str({'ID': USER_ID, 'NAME': answer, 'HIGH SCORE': HIGH_SCORE}))
                        USER_NAME = answer
                    except:
                        count = 5
                        i = 0
                        while True:
                            screen.blit(main_menu_bg,(0,0))
                            pygame.draw.rect(screen,(169,122,87),(30,200,930,207),border_radius=30)
                            pygame.draw.rect(screen,(79,32,15),(30,200,930,207),15,30)
                            if i%30==0:
                                count-=1
                            text2 = font.render(f"Restart for online !! Offline Mode Initiating ... {count}",True,(0,0,0))
                            screen.blit(note,(430,230))
                            screen.blit(text,(70,280))
                            screen.blit(text2,(70,330))
                            pygame.display.update()
                            i+=1
                            if i==150:
                                break
                            events = pygame.event.get()
                            for event in events:
                                if event.type ==  pygame.QUIT:
                                    sys.exit()
                            clock.tick(30)
                    info = True
                    if SOUND and not SOUND_PLAYING:
                        SOUND_PLAYING = True
                        pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    elif not SOUND and SOUND_PLAYING:
                        SOUND_PLAYING = False
                        pygame.mixer.music.set_volume(0)
                    reset()
                    pygame.mixer.music.play(-1)
                    loading()
                    information()
                else:
                    allow_textinput = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and textinput.value!="" and allow_textinput:
                    allow_textinput = False
                    show_name_input = False
                    answer = str(textinput.value).lower().title()
                    try:
                        requests.post("https://yogya.pythonanywhere.com/register_user",data={'id': USER_ID,'name': answer})
                        with open(os.path.join(data_dir,"user.env"),'w') as file:
                            file.write(str({'ID': USER_ID, 'NAME': answer, 'HIGH SCORE': HIGH_SCORE}))
                        USER_NAME = answer
                    except:
                        count = 5
                        i = 0
                        while True:
                            screen.blit(main_menu_bg,(0,0))
                            pygame.draw.rect(screen,(169,122,87),(30,200,930,207),border_radius=30)
                            pygame.draw.rect(screen,(79,32,15),(30,200,930,207),15,30)
                            if i%30==0:
                                count-=1
                            text2 = font.render(f"Restart for online !! Offline Mode Initiating ... {count}",True,(0,0,0))
                            screen.blit(note,(430,230))
                            screen.blit(text,(70,280))
                            screen.blit(text2,(70,330))
                            pygame.display.update()
                            i+=1
                            if i==150:
                                break
                            events = pygame.event.get()
                            for event in events:
                                if event.type ==  pygame.QUIT:
                                    sys.exit()
                            clock.tick(30)
                    info = True
                    if SOUND and not SOUND_PLAYING:
                        SOUND_PLAYING = True
                        pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    elif not SOUND and SOUND_PLAYING:
                        SOUND_PLAYING = False
                        pygame.mixer.music.set_volume(0)
                    reset()
                    pygame.mixer.music.play(-1)
                    loading()
                    information()
    if on_credits_page:
        
        screen.blit(frames[frame_num], (50, 80))
        pygame.display.update()
        frame_num8 = (frame_num + 1) % len(frames)
        
        
        rects = [(450, 260, 150,50), (610, 260, 150,50), (120, 550, 180, 50),(20,20,70,50)]
        pos = pygame.mouse.get_pos()
        in_oneji = False
        for r in rects:
            if (pos[0]>r[0] and pos[0]<r[0]+r[2] and pos[1]>r[1] and pos[1]<r[1]+r[3]):
                in_oneji = True
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        if email_rect.collidepoint(pos[0],pos[1]) or (alter_over and sound_rect2.collidepoint(pos[0],pos[1])) or (alter_over and mute_rect2.collidepoint(pos[0],pos[1])) or (not alter_over and sound_rect2_alter.collidepoint(pos[0],pos[1])) or (not alter_over and SOUND_RECT2.collidepoint(pos[0],pos[1])) or (not alter_over and pos[0]>(sound_rect2_alter[0]+20) and pos[0]<(sound_rect2_alter[0]+40) and pos[1]>(sound_rect2_alter[1]+153-SOUND_VOLUME) and pos[1]<(sound_rect2_alter[1]+173-SOUND_VOLUME)):
            in_oneji = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        if not in_oneji:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not alter_over and event.pos[0]>(sound_rect2_alter[0]+20) and event.pos[0]<(sound_rect2_alter[0]+40) and event.pos[1]>(sound_rect2_alter[1]+153-SOUND_VOLUME) and event.pos[1]<(sound_rect2_alter[1]+173-SOUND_VOLUME):
                    DRAG_ALLOWED = True
                if (event.pos[0]>450 and event.pos[0]<600 and event.pos[1]>260 and event.pos[1]<310):
                    webbrowser.open("https://github.com/YogyaChugh/Timberly.git")
                elif (event.pos[0]>610 and event.pos[0]<760 and event.pos[1]>260 and event.pos[1]<310):
                    webbrowser.open("https://hackclub.slack.com/team/U09218J0E94")
                elif (event.pos[0]>120 and event.pos[0]<300 and event.pos[1]>550 and event.pos[1]<600):
                    webbrowser.open("https://timber-credits.onrender.com")
                elif (email_rect.collidepoint(event.pos[0],event.pos[1])):
                    webbrowser.open("https://mailto:yogya.developer@gmail.com")
                elif (event.pos[0]>20 and event.pos[0]<90 and event.pos[1]>20 and event.pos[1]<70):
                    main_menu = True
                    leaderboard_screen = False
                    game_running = False
                    on_credits_page = False
                    loading()
                    if hscore_thread:
                        try:
                            thread_for_hscore.join()
                        except:
                            pass
                        hscore_thread = False
                    main()
                elif alter_over and (sound_rect2.collidepoint(event.pos[0],event.pos[1]) or mute_rect2.collidepoint(event.pos[0],event.pos[1])):
                    SOUND = not SOUND
                    if SOUND and not SOUND_PLAYING:
                        SOUND_PLAYING = True
                        if SOUND_VOLUME==0:
                            SOUND_VOLUME = PREV_SOUND_VOLUME
                        pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    elif not SOUND and SOUND_PLAYING:
                        SOUND_PLAYING = False
                        PREV_SOUND_VOLUME = SOUND_VOLUME
                        SOUND_VOLUME = 0
                        pygame.mixer.music.set_volume(0)
                    volume_redraw2()
                elif (not alter_over and sound_rect2_alter.collidepoint(event.pos[0],event.pos[1])) or (not alter_over and mute_rect2_alter.collidepoint(event.pos[0],event.pos[1])):
                    SOUND = not SOUND
                    if SOUND and not SOUND_PLAYING:
                        SOUND_PLAYING = True
                        if SOUND_VOLUME==0:
                            SOUND_VOLUME = PREV_SOUND_VOLUME
                        pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    elif not SOUND and SOUND_PLAYING:
                        SOUND_PLAYING = False
                        PREV_SOUND_VOLUME = SOUND_VOLUME
                        SOUND_VOLUME = 0
                        pygame.mixer.music.set_volume(0)
                    volume_redraw_alter2()
                elif not alter_over and SOUND_RECT2.collidepoint(event.pos[0], event.pos[1]):
                    SOUND_VOLUME = (SOUND_RECT2[1]+SOUND_RECT2[3]) - event.pos[1]
                    if SOUND_VOLUME==0:
                        SOUND = not SOUND
                        SOUND_PLAYING = False
                    else:
                        SOUND = True
                        SOUND_PLAYING = True
                    pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    volume_redraw_alter2()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    SOUND = not SOUND
                    if SOUND and not SOUND_PLAYING:
                        SOUND_PLAYING = True
                        if SOUND_VOLUME==0:
                            SOUND_VOLUME = PREV_SOUND_VOLUME
                        pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    elif not SOUND and SOUND_PLAYING:
                        SOUND_PLAYING = False
                        PREV_SOUND_VOLUME = SOUND_VOLUME
                        SOUND_VOLUME = 0
                        pygame.mixer.music.set_volume(0)
                    if alter_over:
                        volume_redraw2()
                    else:
                        volume_redraw_alter2()
            elif event.type == pygame.MOUSEBUTTONUP:
                DRAG_ALLOWED = False
            elif not alter_over and event.type == pygame.MOUSEMOTION and DRAG_ALLOWED:
                mouse_x, mouse_y = event.pos
                SOUND_VOLUME = (SOUND_RECT2[1]+SOUND_RECT2[3]) - mouse_y
                if SOUND_VOLUME!=PREV_SOUND_VOLUME:
                    if SOUND_VOLUME<0:
                        SOUND_VOLUME=0
                    if SOUND_VOLUME>100:
                        SOUND_VOLUME=100
                    if SOUND_VOLUME==0:
                        SOUND = False
                        SOUND_PLAYING = False
                    else:
                        SOUND = True
                        SOUND_PLAYING = True
                    PREV_SOUND_VOLUME = SOUND_VOLUME
                    pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    volume_redraw_alter2()
            else:
                if (sound_rect2.collidepoint(pos[0],pos[1])) or (mute_rect2.collidepoint(pos[0],pos[1])) and altered_allowed:
                    altered_allowed = False
                    alter_over = False
                    volume_redraw_alter2()
                elif not sound_alter_rect2.collidepoint(pos[0],pos[1]) and not alter_over:
                    altered_allowed = True
                    alter_over = True
                    screen.blit(landing_bg,sound_alter_rect2,sound_alter_rect2)
                    volume_redraw2()

    if main_menu:
        if hscore_thread:
            try:
                thread_for_hscore.join()
            except:
                pass
            hscore_thread = False
        rects = [(527,220,220,50), (507,310,260,50), (550,400,170,50)]
        pos = pygame.mouse.get_pos()
        in_one = False
        for r in rects:
            if (pos[0]>r[0] and pos[0]<r[0]+r[2] and pos[1]>r[1] and pos[1]<r[1]+r[3]):
                in_one = True
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        if info_icon_rect.collidepoint(pos[0],pos[1]) or (alter_over and sound_rect1.collidepoint(pos[0],pos[1])) or (alter_over and mute_rect1.collidepoint(pos[0],pos[1])) or (not alter_over and sound_rect1_alter.collidepoint(pos[0],pos[1])) or (not alter_over and SOUND_RECT.collidepoint(pos[0],pos[1])) or (not alter_over and pos[0]>(sound_rect1_alter[0]+55+SOUND_VOLUME) and pos[0]<(sound_rect1_alter[0]+75+SOUND_VOLUME) and pos[1]>(sound_rect1_alter[1]+15) and pos[1]<(sound_rect1_alter[1]+35)):
            in_one = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        if not in_one:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and not DRAG_ALLOWED:
                if not alter_over and event.pos[0]>(sound_rect1_alter[0]+55+SOUND_VOLUME) and event.pos[0]<(sound_rect1_alter[0]+75+SOUND_VOLUME) and event.pos[1]>(sound_rect1_alter[1]+15) and event.pos[1]<(sound_rect1_alter[1]+35):
                    DRAG_ALLOWED = True
                if (event.pos[0]>527 and event.pos[0]<750 and event.pos[1]>220 and event.pos[1]<270):
                    game_running=True
                    main_menu=False
                    loading()
                    reset()
                    if SOUND_PLAYING:
                        pygame.mixer.music.stop()
                        SOUND_PLAYING = False
                    load_game()
                elif (event.pos[0]>507 and event.pos[0]<720 and event.pos[1]>400 and event.pos[1]<450):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    credits_page()
                    main_menu = False
                    leaderboard_screen = False
                    on_credits_page = True
                elif (event.pos[0]>550 and event.pos[0]<770 and event.pos[1]>310 and event.pos[1]<360):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    leaderboard()
                    main_menu = False
                    leaderboard_screen = True
                elif (info_icon_rect.collidepoint(event.pos[0],event.pos[1])):
                    info = True
                    on_page = 1
                    reset()
                    loading()
                    information()
                elif (alter_over and sound_rect1.collidepoint(event.pos[0],event.pos[1])) or (alter_over and mute_rect1.collidepoint(event.pos[0],event.pos[1])):
                    SOUND = not SOUND
                    if SOUND and not SOUND_PLAYING:
                        SOUND_PLAYING = True
                        if SOUND_VOLUME==0:
                            SOUND_VOLUME = PREV_SOUND_VOLUME
                        pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    elif not SOUND and SOUND_PLAYING:
                        SOUND_PLAYING = False
                        PREV_SOUND_VOLUME = SOUND_VOLUME
                        SOUND_VOLUME = 0
                        pygame.mixer.music.set_volume(0)
                    volume_redraw()
                elif (not alter_over and sound_rect1_alter.collidepoint(event.pos[0],event.pos[1])) or (not alter_over and mute_rect1_alter.collidepoint(event.pos[0],event.pos[1])):
                    SOUND = not SOUND
                    if SOUND and not SOUND_PLAYING:
                        SOUND_PLAYING = True
                        if SOUND_VOLUME==0:
                            SOUND_VOLUME = PREV_SOUND_VOLUME
                        pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    elif not SOUND and SOUND_PLAYING:
                        SOUND_PLAYING = False
                        PREV_SOUND_VOLUME = SOUND_VOLUME
                        SOUND_VOLUME = 0
                        pygame.mixer.music.set_volume(0)
                    volume_redraw_alter()
                elif not alter_over and SOUND_RECT.collidepoint(event.pos[0], event.pos[1]):
                    SOUND_VOLUME = event.pos[0] - SOUND_RECT[0]
                    if SOUND_VOLUME==0:
                        SOUND = not SOUND
                        SOUND_PLAYING = False
                    pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    volume_redraw_alter()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    SOUND = not SOUND
                    if SOUND and not SOUND_PLAYING:
                        SOUND_PLAYING = True
                        if SOUND_VOLUME==0:
                            SOUND_VOLUME = PREV_SOUND_VOLUME
                        pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    elif not SOUND and SOUND_PLAYING:
                        SOUND_PLAYING = False
                        PREV_SOUND_VOLUME = SOUND_VOLUME
                        SOUND_VOLUME = 0
                        pygame.mixer.music.set_volume(0)
                    if alter_over:
                        volume_redraw()
                    else:
                        volume_redraw_alter()
            elif event.type == pygame.MOUSEBUTTONUP:
                DRAG_ALLOWED = False
            elif not alter_over and event.type == pygame.MOUSEMOTION and DRAG_ALLOWED:
                mouse_x, mouse_y = event.pos
                SOUND_VOLUME = mouse_x - SOUND_RECT[0]
                if SOUND_VOLUME!=PREV_SOUND_VOLUME:
                    if SOUND_VOLUME<0:
                        SOUND_VOLUME=0
                    if SOUND_VOLUME>100:
                        SOUND_VOLUME=100
                    if SOUND_VOLUME==0:
                        SOUND = False
                        SOUND_PLAYING = False
                    else:
                        SOUND = True
                        SOUND_PLAYING = True
                    PREV_SOUND_VOLUME = SOUND_VOLUME
                    pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    volume_redraw_alter()
            else:
                if (sound_rect1.collidepoint(pos[0],pos[1])) or (mute_rect1.collidepoint(pos[0],pos[1])) and altered_allowed:
                    altered_allowed = False
                    alter_over = False
                    volume_redraw_alter()
                elif not sound_alter_rect.collidepoint(pos[0],pos[1]) and not alter_over:
                    altered_allowed = True
                    alter_over = True
                    screen.blit(board,sound_alter_rect,(sound_alter_rect[0]-386,sound_alter_rect[1]+20, sound_alter_rect[2],sound_alter_rect[3]))
                    volume_redraw()
    if leaderboard_screen:
        if leaderboard_thread:
            try:
                thread_for_leaderboard.join()
            except:
                pass
            leaderboard_thread = False
        pos = pygame.mouse.get_pos()
        if (pos[0]>20 and pos[0]<90 and pos[1]>20 and pos[1]<70) or (alter_over and sound_rect2.collidepoint(pos[0],pos[1])) or (alter_over and mute_rect2.collidepoint(pos[0],pos[1])) or (not alter_over and sound_rect2_alter.collidepoint(pos[0],pos[1])) or (not alter_over and SOUND_RECT2.collidepoint(pos[0],pos[1])) or (not alter_over and pos[0]>(sound_rect2_alter[0]+20) and pos[0]<(sound_rect2_alter[0]+40) and pos[1]>(sound_rect2_alter[1]+153-SOUND_VOLUME) and pos[1]<(sound_rect2_alter[1]+173-SOUND_VOLUME)):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not alter_over and event.pos[0]>(sound_rect2_alter[0]+20) and event.pos[0]<(sound_rect2_alter[0]+40) and event.pos[1]>(sound_rect2_alter[1]+153-SOUND_VOLUME) and event.pos[1]<(sound_rect2_alter[1]+173-SOUND_VOLUME):
                    DRAG_ALLOWED = True
                if event.pos[0]>20 and event.pos[0]<90 and event.pos[1]>20 and event.pos[1]<70:
                    main_menu = True
                    leaderboard_screen = False
                    game_running = False
                    loading()
                    if hscore_thread:
                        try:
                            thread_for_hscore.join()
                        except:
                            pass
                        hscore_thread = False
                    if hscore_thread:
                        try:
                            thread_for_hscore.join()
                        except:
                            pass
                        hscore_thread = False
                    main()
                elif alter_over and (sound_rect2.collidepoint(event.pos[0],event.pos[1]) or mute_rect2.collidepoint(event.pos[0],event.pos[1])):
                    SOUND = not SOUND
                    if SOUND and not SOUND_PLAYING:
                        SOUND_PLAYING = True
                        if SOUND_VOLUME==0:
                            SOUND_VOLUME = PREV_SOUND_VOLUME
                        pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    elif not SOUND and SOUND_PLAYING:
                        SOUND_PLAYING = False
                        PREV_SOUND_VOLUME = SOUND_VOLUME
                        SOUND_VOLUME = 0
                        pygame.mixer.music.set_volume(0)
                    volume_redraw2()
                elif (not alter_over and sound_rect2_alter.collidepoint(event.pos[0],event.pos[1])) or (not alter_over and mute_rect2_alter.collidepoint(event.pos[0],event.pos[1])):
                    SOUND = not SOUND
                    if SOUND and not SOUND_PLAYING:
                        SOUND_PLAYING = True
                        if SOUND_VOLUME==0:
                            SOUND_VOLUME = PREV_SOUND_VOLUME
                        pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    elif not SOUND and SOUND_PLAYING:
                        SOUND_PLAYING = False
                        PREV_SOUND_VOLUME = SOUND_VOLUME
                        SOUND_VOLUME = 0
                        pygame.mixer.music.set_volume(0)
                    volume_redraw_alter2()
                elif not alter_over and SOUND_RECT2.collidepoint(event.pos[0], event.pos[1]):
                    SOUND_VOLUME = (SOUND_RECT2[1]+SOUND_RECT2[3]) - event.pos[1]
                    if SOUND_VOLUME==0:
                        SOUND = not SOUND
                        SOUND_PLAYING = False
                    else:
                        SOUND = True
                        SOUND_PLAYING = True
                    pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    volume_redraw_alter2()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    SOUND = not SOUND
                    if SOUND and not SOUND_PLAYING:
                        SOUND_PLAYING = True
                        if SOUND_VOLUME==0:
                            SOUND_VOLUME = PREV_SOUND_VOLUME
                        pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    elif not SOUND and SOUND_PLAYING:
                        SOUND_PLAYING = False
                        PREV_SOUND_VOLUME = SOUND_VOLUME
                        SOUND_VOLUME = 0
                        pygame.mixer.music.set_volume(0)
                    if alter_over:
                        volume_redraw2()
                    else:
                        volume_redraw_alter2()
            elif event.type == pygame.MOUSEBUTTONUP:
                DRAG_ALLOWED = False
            elif not alter_over and event.type == pygame.MOUSEMOTION and DRAG_ALLOWED:
                mouse_x, mouse_y = event.pos
                SOUND_VOLUME = (SOUND_RECT2[1]+SOUND_RECT2[3]) - mouse_y
                if SOUND_VOLUME!=PREV_SOUND_VOLUME:
                    if SOUND_VOLUME<0:
                        SOUND_VOLUME=0
                    if SOUND_VOLUME>100:
                        SOUND_VOLUME=100
                    if SOUND_VOLUME==0:
                        SOUND = False
                        SOUND_PLAYING = False
                    else:
                        SOUND = True
                        SOUND_PLAYING = True
                    PREV_SOUND_VOLUME = SOUND_VOLUME
                    pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    volume_redraw_alter2()
            else:
                if (sound_rect2.collidepoint(pos[0],pos[1])) or (mute_rect2.collidepoint(pos[0],pos[1])) and altered_allowed:
                    altered_allowed = False
                    alter_over = False
                    volume_redraw_alter2()
                elif not sound_alter_rect2.collidepoint(pos[0],pos[1]) and not alter_over:
                    altered_allowed = True
                    alter_over = True
                    screen.blit(main_menu_bg,sound_alter_rect2,sound_alter_rect2)
                    volume_redraw2()
                    
    if info:
        pos = pygame.mouse.get_pos()
        if pos[0]>20 and pos[0]<90 and pos[1]>20 and pos[1]<70 or (pos[0]>202 and pos[0]<272 and pos[1]>560 and pos[1]<610 and on_page!=1) or (pos[0]>752 and pos[0]<822 and pos[1]>560 and pos[1]<610 and on_page!=3) or (pos[0]>722 and pos[0]<822 and pos[1]>560 and pos[1]<610 and on_page==3) or (alter_over and sound_rect2.collidepoint(pos[0],pos[1])) or (alter_over and mute_rect2.collidepoint(pos[0],pos[1])) or (not alter_over and sound_rect2_alter.collidepoint(pos[0],pos[1])) or (not alter_over and SOUND_RECT2.collidepoint(pos[0],pos[1])) or (not alter_over and pos[0]>(sound_rect2_alter[0]+20) and pos[0]<(sound_rect2_alter[0]+40) and pos[1]>(sound_rect2_alter[1]+153-SOUND_VOLUME) and pos[1]<(sound_rect2_alter[1]+173-SOUND_VOLUME)):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)


        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not alter_over and event.pos[0]>(sound_rect2_alter[0]+20) and event.pos[0]<(sound_rect2_alter[0]+40) and event.pos[1]>(sound_rect2_alter[1]+153-SOUND_VOLUME) and event.pos[1]<(sound_rect2_alter[1]+173-SOUND_VOLUME):
                    DRAG_ALLOWED = True
                if event.pos[0]>20 and event.pos[0]<90 and event.pos[1]>20 and event.pos[1]<70:
                    main_menu = True
                    leaderboard_screen = False
                    game_running = False
                    info = False
                    loading()
                    if hscore_thread:
                        try:
                            thread_for_hscore.join()
                        except:
                            pass
                        hscore_thread = False
                    main()
                elif (event.pos[0]>202 and event.pos[0]<272 and event.pos[1]>560 and event.pos[1]<610 and on_page!=1):
                    on_page-=1
                    if on_page==2:
                        reset2()
                        instruction_num = 0
                        right_allowed = True
                        branch_locs2 = [['None',(305,410)], ['left',(305,310)],['right',(555,210)],['None',(305,110)]]
                    loading()
                    information()
                elif (event.pos[0]>752 and event.pos[0]<822 and event.pos[1]>560 and event.pos[1]<610 and on_page!=3):
                    on_page+=1
                    if on_page==2:
                        reset2()
                        instruction_num = 0
                        right_allowed = True
                        branch_locs2 = [['None',(305,410)],['left',(305,310)],['right',(555,210)],['None',(305,110)]]
                    loading()
                    information()
                elif (event.pos[0]>722 and event.pos[0]<822 and event.pos[1]>560 and event.pos[1]<610 and on_page==3):
                    game_running=True
                    main_menu=False
                    info = False
                    loading()
                    reset()
                    if SOUND_PLAYING:
                        pygame.mixer.music.stop()
                        SOUND_PLAYING = False
                    load_game()
                elif alter_over and (sound_rect2.collidepoint(event.pos[0],event.pos[1]) or mute_rect2.collidepoint(event.pos[0],event.pos[1])):
                    SOUND = not SOUND
                    if SOUND and not SOUND_PLAYING:
                        SOUND_PLAYING = True
                        if SOUND_VOLUME==0:
                            SOUND_VOLUME = PREV_SOUND_VOLUME
                        pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    elif not SOUND and SOUND_PLAYING:
                        SOUND_PLAYING = False
                        PREV_SOUND_VOLUME = SOUND_VOLUME
                        SOUND_VOLUME = 0
                        pygame.mixer.music.set_volume(0)
                    volume_redraw2()
                elif (not alter_over and sound_rect2_alter.collidepoint(event.pos[0],event.pos[1])) or (not alter_over and mute_rect2_alter.collidepoint(event.pos[0],event.pos[1])):
                    SOUND = not SOUND
                    if SOUND and not SOUND_PLAYING:
                        SOUND_PLAYING = True
                        if SOUND_VOLUME==0:
                            SOUND_VOLUME = PREV_SOUND_VOLUME
                        pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    elif not SOUND and SOUND_PLAYING:
                        SOUND_PLAYING = False
                        PREV_SOUND_VOLUME = SOUND_VOLUME
                        SOUND_VOLUME = 0
                        pygame.mixer.music.set_volume(0)
                    volume_redraw_alter2()
                elif not alter_over and SOUND_RECT2.collidepoint(event.pos[0], event.pos[1]):
                    SOUND_VOLUME = (SOUND_RECT2[1]+SOUND_RECT2[3]) - event.pos[1]
                    if SOUND_VOLUME==0:
                        SOUND = not SOUND
                        SOUND_PLAYING = False
                    else:
                        SOUND = True
                        SOUND_PLAYING = True
                    pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    volume_redraw_alter2()
            elif event.type == pygame.MOUSEBUTTONUP:
                DRAG_ALLOWED = False
            elif not alter_over and event.type == pygame.MOUSEMOTION and DRAG_ALLOWED:
                mouse_x, mouse_y = event.pos
                SOUND_VOLUME = (SOUND_RECT2[1]+SOUND_RECT2[3]) - mouse_y
                if SOUND_VOLUME!=PREV_SOUND_VOLUME:
                    if SOUND_VOLUME<0:
                        SOUND_VOLUME=0
                    if SOUND_VOLUME>100:
                        SOUND_VOLUME=100
                    if SOUND_VOLUME==0:
                        SOUND = False
                        SOUND_PLAYING = False
                    else:
                        SOUND = True
                        SOUND_PLAYING = True
                    PREV_SOUND_VOLUME = SOUND_VOLUME
                    pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    volume_redraw_alter2()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    SOUND = not SOUND
                    if SOUND and not SOUND_PLAYING:
                        SOUND_PLAYING = True
                        if SOUND_VOLUME==0:
                            SOUND_VOLUME = PREV_SOUND_VOLUME
                        pygame.mixer.music.set_volume(SOUND_VOLUME/100)
                    elif not SOUND and SOUND_PLAYING:
                        SOUND_PLAYING = False
                        PREV_SOUND_VOLUME = SOUND_VOLUME
                        SOUND_VOLUME = 0
                        pygame.mixer.music.set_volume(0)
                    if alter_over:
                        volume_redraw2()
                    else:
                        volume_redraw_alter2()
                elif (event.key == pygame.K_LEFT and still_man2 and on_page==1) or (event.key == pygame.K_LEFT and still_man2 and on_page==2 and left_allowed):
                    still_man2 = False
                    left2 = True
                    pygame.time.set_timer(ANIMATE_MAN,50,1)
                    if SOUND:
                        chop_sound.play()
                    
                    if on_page==2 and instruction_num==1:
                        instruction_num=2
                        left_allowed = True
                        right_allowed = True
                        branch_locs2 = [['right',(555,410)],['None',(305,310)],['left',(305,210)]]
                    elif on_page==2:
                        branch_locs2 = [['None',(305,410)],['left',(305,310)]]
                        left_allowed = False
                        right_allowed = False
                        instruction_num = 3
                    
                    if on_page==1:
                        draw_playable1()
                    elif on_page==2:
                        draw_playable2()
                elif (event.key == pygame.K_RIGHT and still_man2 and on_page==1) or (event.key == pygame.K_RIGHT and still_man2 and on_page==2 and right_allowed):
                    still_man2 = False
                    left2 = False
                    pygame.time.set_timer(ANIMATE_MAN,50,1)
                    if SOUND:
                        chop_sound.play()
                    if on_page==2 and instruction_num==0:
                        instruction_num=1
                        left_allowed = True
                        right_allowed = False
                        branch_locs2 = [['left',(305,410)],['right',(555,310)],['None',(305,210)],['None',(305,110)]]
                    elif on_page==2:
                        branch_locs2 = [['None',(305,410)],['left',(305,310)]]
                        left_allowed = False
                        right_allowed = False
                        instruction_num = 3
                    if on_page==1:
                        draw_playable1()
                    elif on_page==2:
                        draw_playable2()
            elif event.type == ANIMATE_MAN:
                still_man2 = True
                if on_page==1:
                    draw_playable1()
                elif on_page==2:
                    draw_playable2()
            else:
                if (sound_rect2.collidepoint(pos[0],pos[1])) or (mute_rect2.collidepoint(pos[0],pos[1])) and altered_allowed:
                    altered_allowed = False
                    alter_over = False
                    volume_redraw_alter2()
                elif not sound_alter_rect2.collidepoint(pos[0],pos[1]) and not alter_over:
                    altered_allowed = True
                    alter_over = True
                    screen.blit(main_menu_bg,sound_alter_rect2,sound_alter_rect2)
                    volume_redraw2()
            
                    
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
            
    clock.tick(30)
