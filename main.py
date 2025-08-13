import pygame
import random
import time

pygame.init()
screen = pygame.display.set_mode((1000,667))
# screen = pygame.Surface((1000,667), pygame.SRCALPHA)
pygame.display.set_caption("Timber")

bg = pygame.image.load("assets/bg.png")
bg = pygame.transform.scale(bg, (1000,667))

# bamboo = pygame.image.load("assets/bamboo.png")
# bamboo = pygame.transform.scale(bamboo,(412,412))

tree = pygame.image.load("assets/tree.png")
tree = pygame.transform.scale(tree, (200,630))

man_1 = pygame.image.load("assets/man_1.png")
man_1 = pygame.transform.scale(man_1, (200, 300))
man_2 = pygame.image.load("assets/man_3.png")
man_2 = pygame.transform.scale(man_2, (200, 300))

man_3 = pygame.image.load("assets/man_4.png")
man_3 = pygame.transform.scale(man_3, (200, 300))
man_4 = pygame.image.load("assets/man_5.png")
man_4 = pygame.transform.scale(man_4, (200, 300))

branch = pygame.image.load("assets/branch.png")
branch = pygame.transform.scale(branch, (300,60))
branch_flipped = pygame.image.load("assets/branch_flipped.png")
branch_flipped = pygame.transform.scale(branch_flipped, (300,60))

dead_man = pygame.image.load("assets/dead.png")
unchanged = pygame.image.load("assets/dead.png")
unchanged = pygame.transform.scale(unchanged,(500,333))
unchanged = pygame.transform.rotate(unchanged,10)
dead_man = pygame.transform.scale(dead_man,(300,200))
dead_man = pygame.transform.rotate(dead_man,10)
dead_man_flipped = pygame.image.load("assets/dead_flipped.png")
dead_man_flipped = pygame.transform.scale(dead_man_flipped,(300,200))
dead_man_flipped = pygame.transform.rotate(dead_man_flipped,-10)

squished_img = pygame.image.load("assets/squished_3.png")
squished_img = pygame.transform.scale(squished_img,(600,600))
time_over = pygame.image.load("assets/time_over.png")
time_over = pygame.transform.scale(time_over,(400,400))

wood = pygame.image.load("assets/wood.png")
wood = pygame.transform.scale(wood,(50,50))

main_menu_bg = pygame.image.load("assets/bgg.png")
main_menu_bg = pygame.transform.scale(main_menu_bg,(1000,667))
board = pygame.image.load("assets/menu.png")
board = pygame.transform.scale(board,(500,750))
smiling_man = pygame.image.load("assets/smiling_man.png")
smiling_man = pygame.transform.scale(smiling_man,(240,360))

# button = pygame.image.load("assets/button.png")
# button = pygame.transform.scale(button,(300,200))
font = pygame.font.Font("assets/fonts/VarelaRound-Regular.ttf",30)
font2 = pygame.font.Font("assets/fonts/VarelaRound-Regular.ttf",24)

clock = pygame.time.Clock()

animate_man = pygame.USEREVENT

still_man = True
left = True
branch_locs = []
game_running = False
score = 0
BASE_BRANCH_LOC = 510
TOTAL_BRANCHES = 6
time_left = 240
transparency = 255
just_game_over = False
main_menu = True
squished = False

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

generate_branch_locs()
def load_game():
    global score, branch_locs,left,game_running, time_left,screen, just_game_over, squished
    screen.blit(bg, (0,0))
        
    if (branch_locs[0][0]=='left' and left==False) or (branch_locs[0][0]=='right' and left==True):
        game_running = False
        just_game_over = True
        squished = True
        score-=1
    
    for i in branch_locs:
        if i[0]=='left':
            screen.blit(branch,i[1])
        elif i[0]=='right':
            screen.blit(branch_flipped,i[1])
            
    if game_running:
        if not still_man:
            if left:
                screen.blit(man_2,(230,370))
            else:
                screen.blit(man_4,(570,370))

        screen.blit(tree, (400,0))

        # screen.blit(bamboo, (300,230))
        if still_man:
            if left:
                screen.blit(man_1,(230,360))
            else:
                screen.blit(man_3,(570,360))
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
    score_ = font.render("Logs:", True, (255,255,255))
    score_text = font.render(f"{score}", True, (255,255,255))
    screen.blit(score_,(92,28))
    screen.blit(score_text,(172,28))
    
    pygame.draw.rect(screen,(55,55,55),(720,20,250,50),border_radius=5)
    pygame.draw.rect(screen,(255,255,255),(720,20,250,50),2,5)
    pygame.draw.rect(screen,(255, 234, 0),(725,25,time_left,40),border_radius=5)
    pygame.display.update()

def update_timer():
    pygame.draw.rect(screen,(55,55,55),(720,20,250,50),border_radius=5)
    pygame.draw.rect(screen,(255,255,255),(720,20,250,50),2,5)
    pygame.draw.rect(screen,(255, 234, 0),(725,25,time_left,40),border_radius=5)
    pygame.display.update()
    
def reset():
    global still_man, left, branch_locs, score, BASE_BRANCH_LOC, TOTAL_BRANCHES, time_left,transparency,just_game_over,main_menu,squished
    still_man = True
    left = True
    branch_locs = []
    score = 0
    BASE_BRANCH_LOC = 510
    TOTAL_BRANCHES = 6
    time_left = 240
    transparency = 255
    just_game_over = False
    main_menu = False
    squished = False
    generate_branch_locs()
    
    
def game_over_page():
    screen.blit(bg,(0,0))
    
    pygame.draw.rect(screen,(169,122,87),(200,30,600,607),border_radius=30)
    pygame.draw.rect(screen,(79,32,15),(200,30,600,607),15,30)
    
    
    # pygame.draw.rect(screen,(55,55,55),(410,480,180,50),border_radius=5)
    # pygame.draw.rect(screen,(255,255,255),(410,480,190,50),2,5)
    # score_ = font.render("Score:", True, (255,255,255))
    screen.blit(wood,(460,470))
    score_text = font.render(f"{score}", True, (0,0,0))
    # screen.blit(score_,(410,480))
    screen.blit(score_text,(520,475))
    if squished:
        screen.blit(unchanged,(220,100))
        screen.blit(squished_img,(200,-100))
    else:
        screen.blit(time_over,(300,30))

    #Button 1
    pygame.draw.rect(screen,(68, 121, 53),(280,550,180,50),border_radius=10)
    pygame.draw.rect(screen,(15, 51, 31),(280,550,180,50),4,10)
    pygame.draw.rect(screen,(139,69,19),(284,554,172,42),4,5)
    menu_return = font2.render("Main Menu",True,(255,255,255))
    screen.blit(menu_return,((302,560)))

    #Button 2
    pygame.draw.rect(screen,(68, 121, 53),(530,550,180,50),border_radius=10)
    pygame.draw.rect(screen,(15, 51, 31),(530,550,180,50),4,10)
    pygame.draw.rect(screen,(139,69,19),(534,554,172,42),4,5)
    menu_return = font2.render("Replay",True,(255,255,255))
    screen.blit(menu_return,((582,560)))
    
    pygame.display.update()
    
    
def main():
    screen.blit(main_menu_bg,(0,0))
    screen.blit(board,(386,-20))
    screen.blit(smiling_man,(70,300))
    # screen.blit(button,(480,100))
    pygame.draw.rect(screen,(169,122,87),(530,220,220,50),border_radius=5)
    pygame.draw.rect(screen,(79,32,15),(530,220,220,50),5,5)
    pygame.draw.rect(screen,(169,122,87),(530,320,220,50),border_radius=5)
    pygame.draw.rect(screen,(79,32,15),(530,320,220,50),5,5)
    pygame.display.update()

# load_game()
main()
while True:
    events = pygame.event.get()
    
    if game_running:
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and still_man:
                    still_man = False
                    left = True
                    score += 1
                    pygame.time.set_timer(animate_man,50,1)
                    if time_left<=240-4 and time_left!=0:
                        time_left+=4
                    generate_branch_locs()
                    load_game()
                elif event.key == pygame.K_RIGHT and still_man:
                    still_man = False
                    left = False
                    score += 1
                    if time_left<=240-4 and time_left!=0:
                        time_left+=4
                    pygame.time.set_timer(animate_man,50,1)
                    generate_branch_locs()
                    load_game()

            if event.type == animate_man:
                still_man = True
                load_game()
        if time_left!=0:
            time_left-=1
        else:
            game_running = False
            just_game_over = True
        update_timer()
    elif not main_menu:
        game_over_page()
        pos = pygame.mouse.get_pos()
        if (pos[0]>280 and pos[0]<460 and pos[1]>550 and pos[1]<600) or (pos[0]>530 and pos[0]<710 and pos[1]>550 and pos[1]<600):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (event.pos[0]>280 and event.pos[0]<460 and event.pos[1]>550 and event.pos[1]<600):
                    main_menu = True
                elif (event.pos[0]>530 and event.pos[0]<710 and event.pos[1]>550 and event.pos[1]<600):
                    game_running=True
                    reset()
                    load_game()
    
    
    for event in events:
        if event.type == pygame.QUIT:
            exit()
            
    clock.tick(30)