import pygame
import pygame_textinput
import random
import time
import webbrowser
import appdirs
import os
import requests

app_name = "Timber"

data_dir = appdirs.user_data_dir(app_name)
os.makedirs(data_dir, exist_ok=True)

application_allowed = True
pygame.init()
screen = pygame.display.set_mode((1000,667))
pygame.display.set_caption(app_name)
clock = pygame.time.Clock()

font = pygame.font.Font("assets/fonts/VarelaRound-Regular.ttf",30)
loading_man = pygame.image.load("assets/loading.png")
timberly = pygame.image.load("assets/timberly.png")
# timberly = pygame.transform.scale(timberly,(350,525))


main_menu_bg = pygame.image.load("assets/bgg.png")
landing_bg = pygame.image.load("assets/landing_bg.png")
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
                    exit()
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
pygame.mixer.music.load("assets/audio/magic_forest.wav")
pygame.mixer.music.play(-1)
dead_sound = pygame.mixer.Sound("assets/audio/dead.wav")
time_up_sound = pygame.mixer.Sound("assets/audio/time_up.wav")
chop_sound = pygame.mixer.Sound("assets/audio/chop.wav")


# Image loads
bg = pygame.image.load("assets/bg.png")
tree = pygame.image.load("assets/tree.png")
tree_log = pygame.image.load("assets/log.png")
man_up_left = pygame.image.load("assets/man_up_left.png")
man_down_left = pygame.image.load("assets/man_down_left.png")
man_up_right = pygame.image.load("assets/man_up_right.png")
man_down_right = pygame.image.load("assets/man_down_right.png")
branch = pygame.image.load("assets/branch.png")
branch_flipped = pygame.image.load("assets/branch_flipped.png")

dead_man = pygame.image.load("assets/dead.png")
unchanged = pygame.image.load("assets/dead.png")
unchanged = pygame.transform.scale(unchanged,(500,333))
unchanged = pygame.transform.rotate(unchanged,10)
dead_man = pygame.transform.scale(dead_man,(300,200))
dead_man = pygame.transform.rotate(dead_man,10)
dead_man_flipped = pygame.image.load("assets/dead_flipped.png")
dead_man_flipped = pygame.transform.scale(dead_man_flipped,(300,200))
dead_man_flipped = pygame.transform.rotate(dead_man_flipped,-10)

squished_img = pygame.image.load("assets/squished.png")
time_over = pygame.image.load("assets/time_over.png")

wood = pygame.image.load("assets/wood.png")
wood2 = pygame.transform.scale(wood,(60,60))
wood = pygame.transform.scale(wood,(50,50))

board = pygame.image.load("assets/menu.png")
smiling_man = pygame.image.load("assets/smiling_man.png")
github = pygame.image.load('assets/github.png')
slack = pygame.image.load('assets/slack.png')
watching_man = pygame.image.load("assets/watching_man.png")
tick = pygame.image.load("assets/tick.png")
cloud = pygame.image.load("assets/cloud.png")
cloud = pygame.transform.rotate(cloud,347)
leaderboard_img = pygame.image.load("assets/leaderboard.png")
info_panel = pygame.image.load("assets/info_panel2.png")
aleft = pygame.image.load("assets/leftji.png")
aright = pygame.transform.rotate(aleft,180)
wave = pygame.image.load("assets/wave.png")
info_icon = pygame.image.load("assets/info.png")
info_icon_rect = info_icon.get_rect()
info_icon_rect.topleft = (730, 130)

volume = pygame.image.load("assets/volume.png")

#fonts
font2 = pygame.font.Font("assets/fonts/VarelaRound-Regular.ttf",24)
font3 = pygame.font.Font("assets/fonts/BebasNeue-Regular.ttf",30)
font4 = pygame.font.Font("assets/fonts/VarelaRound-Regular.ttf",40)
font5 = pygame.font.Font("assets/fonts/VarelaRound-Regular.ttf",28)

#renders
score_ = font.render("Logs:", True, (0,0,0))
menu_return1 = font5.render("Main Menu",True,(255,255,255))
menu_return2 = font5.render("Replay",True,(255,255,255))
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
left = True
do_action = False
branch_locs = []
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

def get_random_branch_status():
    global score
    allowed = [1,2,3,4,5,6,7]
    if score<30:
        allowed = [1,2,3,4,5,6,7]
    elif score<100:
        allowed = [1,2,3,4,5,6,7,8]
    elif score<200:
        allowed = [1,2,3,4,5,6,7,8,9]
    else:
        allowed = [1,2,3,4,5,6,7,8,9,10]
    rr = random.randint(1,10)
    if rr in allowed:
        if rr <= len(allowed)//2:
            return 'left'
        else:
            return 'right'
    else:
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
    global score, branch_locs,left,game_running, time_left,screen, just_game_over, squished, main_menu, show_name_input, leaderboard_screen
    screen.blit(bg, (0,0))
    game_done = False
    if (branch_locs[0][0]=='left' and left==False) or (branch_locs[0][0]=='right' and left==True):
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
    pygame.draw.rect(screen,(55,55,55),(720,20,250,50),border_radius=5)
    pygame.draw.rect(screen,(255,255,255),(720,20,250,50),2,5)
    pygame.draw.rect(screen,(255, 234, 0),(725,25,time_left,40),border_radius=5)
    if not timer_started:
        textji = font.render("Press      or      to start !",True,(0,0,0))
        screen.blit(textji,(650,580))
        screen.blit(aleft,(737,585))
        screen.blit(aright,(812,585))
    textji2 = font2.render("Press 'Esc' to exit !",True,(0,0,0))
    screen.blit(textji2,(20,630))
    
    pygame.display.update()
    if game_done:
        loading()
        game_over_page()
    
    
def update_timer():
    pygame.draw.rect(screen,(55,55,55),(720,20,250,50),border_radius=5)
    pygame.draw.rect(screen,(255,255,255),(720,20,250,50),2,5)
    pygame.draw.rect(screen,(255, 234, 0),(725,25,time_left,40),border_radius=5)
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
    screen.blit(menu_return1,((296,520)))
    #Button 2
    pygame.draw.rect(screen,(68, 121, 53),(530,500,200,70),border_radius=10)
    pygame.draw.rect(screen,(15, 51, 31),(530,500,200,70),4,10)
    pygame.draw.rect(screen,(139,69,19),(534,504,192,62),4,5)
    screen.blit(menu_return2,((586,520)))
    pygame.display.update()
    
    
def main():
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
    screen.blit(info_icon,info_icon_rect)
    pygame.draw.rect(screen,(169,122,87),(530,220,220,50),border_radius=5)
    pygame.draw.rect(screen,(79,32,15),(530,220,220,50),5,5)
    screen.blit(play,(600,228))
    pygame.draw.rect(screen,(169,122,87),(510,310,260,50),border_radius=5)
    pygame.draw.rect(screen,(79,32,15),(510,310,260,50),5,5)
    screen.blit(leader,(525,318))
    #github button
    pygame.draw.rect(screen, (0,0,0),(550, 420, 170,50),border_radius=20)
    pygame.draw.rect(screen, (0,0,0),(550, 420, 170,50),4,border_radius=20)
    pygame.draw.rect(screen, (44, 42, 49), (562, 420, 45, 45),border_radius=10)
    screen.blit(github, (561,420))
    screen.blit(agi, (606,429))
    # pygame.draw.rect(screen, (255,255,255),(550, 420, 170,50),2,border_radius=20)
    #slack button
    pygame.draw.rect(screen, (255,250,250),(560, 483, 150,50),border_radius=20)
    pygame.draw.rect(screen, (0,0,0),(560, 483, 150,50),4,border_radius=20)
    screen.blit(slack, (580, 485))
    
    if not online_game:
        pygame.draw.rect(screen,(169,122,87),(10,10,260,60),border_radius=30)
        pygame.draw.rect(screen,(79,32,15),(10,10,260,60),8,30)
        screen.blit(offline,(37,22))
        
    try:
        if online_game:
            bb = requests.get("https://yogya.pythonanywhere.com/get_score",data={'id': USER_ID})
            if eval(bb.content) != "":
                pygame.draw.rect(screen,(169,122,87),(20,10,300,60),border_radius=30)
                pygame.draw.rect(screen,(79,32,15),(20,10,300,60),8,30)
                offline = font.render(f"High Score: {eval(bb.content)}",True,(0,0,0))
                if len(str(eval(bb.content)))==1:
                    screen.blit(offline,(67,22))
                elif len(str(eval(bb.content)))==2:
                    screen.blit(offline,(57,22))
                else:
                    screen.blit(offline,(47,22))
                pygame.display.update()
    except:
        pass
    
    screen.blit(credit,credit_rect)
    pygame.draw.line(screen,(0,0,0),(credit_rect.x,credit_rect.y+32),(credit_rect.x+102,credit_rect.y+32),3)
    pygame.display.update()


def loading():
    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
    screen.blit(main_menu_bg,(0,0))
    screen.blit(loading_man,(325,71))
    pygame.display.update()
    
def information():
    screen.blit(main_menu_bg,(0,0))
    pygame.draw.rect(screen,(169,122,87),(20,20,70,50),border_radius=10)
    pygame.draw.rect(screen,(79,32,15),(20,20,70,50),2,10)
    screen.blit(aleft,(40,30))
    screen.blit(info_panel,(-20,0))
    pygame.display.update()

def leaderboard():
    screen.blit(main_menu_bg,(0,0))
    pygame.draw.rect(screen,(169,122,87),(20,20,70,50),border_radius=10)
    pygame.draw.rect(screen,(79,32,15),(20,20,70,50),2,10)
    screen.blit(aleft,(40,30))
    screen.blit(leaderboard_img,(0,20))
    lead = font4.render("LEADERBOARD",True,(255,255,255))
    screen.blit(lead,(350,90))
    couldnt = font.render("Retrieving ...", True, (0,0,0))
    screen.blit(couldnt,(412,350))
    pygame.display.update()
    fetched = True
    try:
        content = eval(requests.get("https://yogya.pythonanywhere.com/get_leaderboard",data={'id': USER_ID,'name': USER_NAME}).content)
        screen.blit(leaderboard_img,(0,20))
        lead = font4.render("LEADERBOARD",True,(255,255,255))
        screen.blit(lead,(350,90))
        pygame.display.update()
        if content == "" or type(content)!=list                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 :
            fetched = False
            couldnt = font.render("Couldn't Fetch details ! Try Again Later !!", True, (0,0,0))
            screen.blit(couldnt,(212,350))
    except:
        screen.blit(leaderboard_img,(0,20))
        lead = font4.render("LEADERBOARD",True,(255,255,255))
        screen.blit(lead,(350,90))
        pygame.display.update()
        fetched = False
        if online_game:
            couldnt = font.render("Couldn't Fetch details ! Try Again Later !!", True, (0,0,0))
            screen.blit(couldnt,(212,350))
        else:
            couldnt2 = font.render("| Offline Mode | ", True, (0,0,0))
            couldnt3 = font.render("Re-start application with Internet to exit mode !!",True,(0,0,0))
            screen.blit(couldnt2,(212,350))
            screen.blit(couldnt3,(212,380))
    if fetched:
        if len(content)<=4:
            for i in range(len(content)):
                pygame.draw.rect(screen,(169,122,87),(202,220+(i*80),600,60),border_radius=30)
                pygame.draw.rect(screen,(79,32,15),(202,220+(i*80),600,60),5,30)
                temp_id = font.render(str(content[i][0]),True,(255,255,255))
                temp_name = font.render(str(content[i][1]),True,(255,255,255))
                temp_score = font.render(str(content[i][2]),True,(255,255,255))
                screen.blit(temp_id,(225,233+(i*80)))
                screen.blit(temp_name,(300,233+(i*80)))
                screen.blit(wood,(646,227+(i*80)))
                screen.blit(temp_score,(705,233+(i*80)))
        else:
            for i in range(3):
                pygame.draw.rect(screen,(169,122,87),(202,220+(i*80),600,60),border_radius=30)
                pygame.draw.rect(screen,(79,32,15),(202,220+(i*80),600,60),5,30)
                temp_id = font.render(str(content[i][0]),True,(255,255,255))
                temp_name = font.render(str(content[i][1]),True,(255,255,255))
                temp_score = font.render(str(content[i][2]),True,(255,255,255))
                screen.blit(temp_id,(225,233+(i*80)))
                screen.blit(temp_name,(300,233+(i*80)))
                screen.blit(wood,(646,227+(i*80)))
                screen.blit(temp_score,(705,233+(i*80)))
            pygame.draw.rect(screen,(169,122,87),(202,490,600,60),border_radius=30)
            pygame.draw.rect(screen,(79,32,15),(202,490,600,60),5,30)
            temp_id = font.render(str(content[-1][0]),True,(255,255,255))
            temp_name = font.render(str(content[-1][1]),True,(255,255,255))
            temp_score = font.render(str(content[-1][2]),True,(255,255,255))
            screen.blit(temp_id,(225,233+(4*80)))
            screen.blit(temp_name,(300,233+(4*80)))
            screen.blit(wood,(646,227+(4*80)))
            screen.blit(temp_score,(705,233+(4*80)))
    pygame.display.update()





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
    generate_branch_locs()
    main()
while True:
    events = pygame.event.get()
    if game_running:
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
                    load_game()
                elif event.key == pygame.K_ESCAPE:
                    game_running = False
                    just_game_over = True
                    show_name_input = False
                    leaderboard_screen = False
                    game_done = True
                    main_menu = True
                    loading()
                    main()
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
            game_over_page()
    elif not main_menu and not show_name_input and not leaderboard_screen:
        if online_game:
            if score>HIGH_SCORE:
                doit = True
                score_updated = False
                HIGH_SCORE = score
                with open(os.path.join(data_dir,'user.env'),'w') as file:
                    file.write(str({'ID': USER_ID, 'NAME': USER_NAME, 'HIGH SCORE': HIGH_SCORE}))
            if doit:
                doit = False
                try:
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
                    main()
                elif (event.pos[0]>530 and event.pos[0]<730 and event.pos[1]>500 and event.pos[1]<570):
                    game_running=True
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
    elif not main_menu and show_name_input and not leaderboard_screen:
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
                    try:
                        requests.post("https://yogya.pythonanywhere.com/register_user",data={'id': USER_ID,'name': textinput.value})
                        with open(os.path.join(data_dir,"user.env"),'w') as file:
                            file.write(str({'ID': USER_ID, 'NAME': textinput.value, 'HIGH SCORE': HIGH_SCORE}))
                        USER_NAME = textinput.value
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
                                    exit()
                            clock.tick(30)
                    main_menu = True
                    loading()
                    main()
                else:
                    allow_textinput = False
        
    if main_menu:
        rects = [(530,220,220,50), (510,310,260,50), (550, 420, 170,50), (560, 483, 150,50)]
        pos = pygame.mouse.get_pos()
        in_one = False
        for r in rects:
            if (pos[0]>r[0] and pos[0]<r[0]+r[2] and pos[1]>r[1] and pos[1]<r[1]+r[3]):
                in_one = True
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        if credit_rect.collidepoint(pos[0],pos[1]) or info_icon_rect.collidepoint(pos[0],pos[1]):
            in_one = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        if not in_one:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.pos[0]>530 and event.pos[0]<750 and event.pos[1]>220 and event.pos[1]<270):
                    game_running=True
                    main_menu=False
                    loading()
                    reset()
                    load_game()
                elif (event.pos[0]>510 and event.pos[0]<770 and event.pos[1]>310 and event.pos[1]<360):
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                    leaderboard()
                    main_menu = False
                    leaderboard_screen = True
                elif (event.pos[0]>550 and event.pos[0]<720 and event.pos[1]>420 and event.pos[1]<470):
                    webbrowser.open("https://github.com/YogyaChugh")
                elif (event.pos[0]>560 and event.pos[0]<710 and event.pos[1]>483 and event.pos[1]<533):
                    webbrowser.open('https://hackclub.slack.com/team/U09218J0E94')
                elif (credit_rect.collidepoint(event.pos[0],event.pos[1])):
                    webbrowser.open('https://timber-credits.onrender.com')
                elif (info_icon_rect.collidepoint(event.pos[0],event.pos[1])):
                    info = True
                    reset()
                    loading()
                    information()
    if leaderboard_screen:
        pos = pygame.mouse.get_pos()
        if pos[0]>20 and pos[0]<90 and pos[1]>20 and pos[1]<70:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0]>20 and event.pos[0]<90 and event.pos[1]>20 and event.pos[1]<70:
                    main_menu = True
                    leaderboard_screen = False
                    game_running = False
                    loading()
                    main()
    if info:
        pos = pygame.mouse.get_pos()
        if pos[0]>20 and pos[0]<90 and pos[1]>20 and pos[1]<70:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0]>20 and event.pos[0]<90 and event.pos[1]>20 and event.pos[1]<70:
                    main_menu = True
                    leaderboard_screen = False
                    game_running = False
                    info = False
                    loading()
                    main()
                    
    for event in events:
        if event.type == pygame.QUIT:
            exit()
            
    clock.tick(30)