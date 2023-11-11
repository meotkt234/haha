import sys
import pygame
from pygame.locals import QUIT
from math import *
import random
import button
import asyncio
async def main():
    pygame.font.init()
    width = 1500
    height = 775
    sc = pygame.display.set_mode((width, height))
    pygame.display.set_caption('game')
    sc_wait=pygame.image.load('wall.png')
    wait=False
    sc_wait=pygame.transform.scale(sc_wait,(65,65))
    wall=pygame.image.load('wall.png')
    wall=pygame.transform.scale(wall,(65,65))
    wall2=pygame.image.load('wall2.png')
    wall2=pygame.transform.scale(wall2,(65,65))
    wall3=pygame.image.load('wall3.png')
    wall3=pygame.transform.scale(wall3,(65,65))
    wall3_1=pygame.image.load('wall3.1.png')
    wall3_1=pygame.transform.scale(wall3_1,(65,65))
    wall4=pygame.image.load('wall4.png')
    wall4=pygame.transform.scale(wall4,(65,65))
    door=pygame.image.load('wall1.png')
    door=pygame.transform.scale(door,(65,65))
    nv=pygame.image.load('bird.png')
    nv=pygame.transform.scale(nv,(65,65))
    nv_rect = pygame.Rect(65*11,65*11,65,65)
    nv_pin=pygame.image.load('pin.png')
    nv_pin=pygame.transform.scale(nv_pin,(65,65))
    nv_chai=pygame.image.load('chai.png')
    nv_chai=pygame.transform.scale(nv_chai,(65,65))
    rac_voco=pygame.image.load('rac_voco.png')
    rac_voco=pygame.transform.scale(rac_voco,(65,65))
    rac_huuco=pygame.image.load('rac_huuco.png')
    nv_lon=pygame.image.load('lon.png')
    nv_lon=pygame.transform.scale(nv_lon,(65,65))
    nv_baonilong=pygame.image.load('baonilong.png')
    nv_baonilong=pygame.transform.scale(nv_baonilong,(65,65))
    rac_huuco=pygame.transform.scale(rac_huuco,(65,65))
    myfont = pygame.font.SysFont('Source Sans Pro', 30)
    sline=0
    direct = 90
    luom=False
    phai=False
    trai=False
    len=False
    xuong=False
    hh=0
    x_pin=random.randrange(65,1365,65)
    y_pin=random.randrange(65,715,65)
    x_chai=random.randrange(65,1365,65)
    y_chai=random.randrange(65,715,65)
    x_lon=random.randrange(65,1365,65)
    y_lon=random.randrange(65,715,65)
    x_pin1=random.randrange(65,1365,65)
    y_pin1=random.randrange(65,715,65)
    x_chai1=random.randrange(65,1365,65)
    y_chai1=random.randrange(65,715,65)
    x_lon1=random.randrange(65,1365,65)
    y_lon1=random.randrange(65,715,65)
    x_pin2=random.randrange(65,1365,65)
    y_pin2=random.randrange(65,715,65)
    x_chai2=random.randrange(65,1365,65)
    y_chai2=random.randrange(65,715,65)
    x_lon2=random.randrange(65,1365,65)
    y_lon2=random.randrange(65,715,65)
    x_pin3=random.randrange(65,1365,65)
    y_pin3=random.randrange(65,715,65)
    x_chai3=random.randrange(65,1365,65)
    y_chai3=random.randrange(65,715,65)
    x_lon3=random.randrange(65,1365,65)
    y_lon3=random.randrange(65,715,65)
    start_img = pygame.image.load('start_btn.png').convert_alpha()
    exit_img = pygame.image.load('exit_btn.png').convert_alpha()
    resume_img = pygame.image.load('resume_btn.png').convert_alpha()
    resume_img=pygame.transform.scale(resume_img,(260,130))
    resume_button = button.Button(650, 200, resume_img, 0.8)
    start_img=pygame.transform.scale(start_img,(260,130))
    exit_img=pygame.transform.scale(exit_img,(260,130))
    start_button = button.Button(650, 200, start_img, 0.8)
    exit_button = button.Button(650, 400, exit_img, 0.8)
    print(x_pin,y_pin)
    print(x_chai,y_chai)
    print(x_lon,y_lon)
    print(x_pin1,y_pin1)
    print(x_chai1,y_chai1)
    print(x_lon1,y_lon1)
    print(x_pin2,y_pin2)
    print(x_chai2,y_chai2)
    print(x_lon2,y_lon2)
    print(x_pin3,y_pin3)
    print(x_chai3,y_chai3)
    print(x_lon3,y_lon3)
    bienmat=False
    x=65*11
    y=65*11
    map=1
    cnt=0
    ditheo=False
    ditheo1=False
    ditheo2=False
    ditheo3=False
    ditheo4=False
    ditheo5=False
    ditheo6=False
    ditheo7=False
    ditheo8=False
    ditheo9=False
    ditheo10=False
    ditheo11=False
    batdau=False
    run = True
    b=[]
    ditheo=False
    map1=[[0,0,0,0,0,0,0,0,1,2,2,2,2,1,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,1,2,2,2,2,1,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,1,2,2,2,2,1,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,1,2,2,2,2,1,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,1,2,2,2,2,1,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,1,2,2,2,2,1,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,1,2,2,2,2,1,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,1,2,2,2,2,1,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,1,2,2,2,2,1,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,1,2,2,2,2,1,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,1,2,2,2,2,1,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,1,2,3,4,2,1,0,0,0,0,0,0,0,0,0]]
    
    map2=[[7,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6],
          [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
          [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
          [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
          [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
          [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
          [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
          [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
          [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
          [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
          [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1],
          [1,1,1,1,1,1,1,1,8,2,2,2,2,8,1,1,1,1,1,1,1,1,1]]
    
    def draw_map(map,player_rect,x,y,direction):
        tilex=tiley=0
        for line in map:
            for pixel in line:
                if pixel == 1:
                    sc.blit(wall,(tilex,tiley))
                    rect = pygame.Rect(tilex,tiley,65,65)
                    if rect.colliderect(player_rect):
                        if direction == 90:
                            x -= 65/2
                        elif direction == -90:
                            x += 65/2
                        elif direction == 180:
                            y -= 65/2
                        elif direction == 0:
                            y += 65/2
                if pixel == 2:
                    sc.blit(door,(tilex,tiley))
                if pixel==3:
                      sc.blit(door,(tilex,tiley))
                      sc.blit(rac_voco,(tilex,tiley))
                if pixel==4:
                      sc.blit(door,(tilex,tiley))
                      sc.blit(rac_huuco,(tilex,tiley))
                if pixel==5:
                      rect = pygame.Rect(tilex,tiley,65,65)
                      if rect.colliderect(player_rect):
                        if direction == 90:
                            x -= 65/2
                        elif direction == -90:
                            x += 65/2
                        elif direction == 180:
                            y -= 65/2
                        elif direction == 0:
                            y += 65/2
                      sc.blit(door,(tilex,tiley))
                      sc.blit(wall2,(tilex,tiley))
                if pixel==6:
                      rect = pygame.Rect(tilex,tiley,65,65)
                      if rect.colliderect(player_rect):
                        if direction == 90:
                            x -= 65/2
                        elif direction == -90:
                            x += 65/2
                        elif direction == 180:
                            y -= 65/2
                        elif direction == 0:
                            y += 65/2
                      sc.blit(door,(tilex,tiley))
                      sc.blit(wall3,(tilex,tiley))
                if pixel==7:
                      rect = pygame.Rect(tilex,tiley,65,65)
                      if rect.colliderect(player_rect):
                        if direction == 90:
                            x -= 65/2
                        elif direction == -90:
                            x += 65/2
                        elif direction == 180:
                            y -= 65/2
                        elif direction == 0:
                            y += 65/2
                      sc.blit(door,(tilex,tiley))
                      sc.blit(wall3_1,(tilex,tiley))
                if pixel==8:
                      rect = pygame.Rect(tilex,tiley,65,65)
                      if rect.colliderect(player_rect):
                        if direction == 90:
                            x -= 65/2
                        elif direction == -90:
                            x += 65/2
                        elif direction == 180:
                            y -= 65/2
                        elif direction == 0:
                            y += 65/2
                      sc.blit(door,(tilex,tiley))
                      sc.blit(wall4,(tilex,tiley))
                tilex+=65
            tiley+=65
            tilex=0
        return x,y
    def drawmapphiphai(playerrect,x,y,direct):
          sc.fill((0, 0, 0))
          if map==1:
                px,py = draw_map(map1,playerrect,x,y,direct)
          elif map==2:
                px,py = draw_map(map2,playerrect,x,y,direct)
          return px,py
    while run:
          if map==1:
               luom=False
          else:
               luom=True
          if phai:
                x+=1
          if trai:
                x-=1
          if len:
                y-=1
          if xuong:
                y+=1
          if x==x_pin and y==y_pin and luom==True:
                ditheo=True
          if (x_pin==11*65 and y_pin==11*65 or x_pin==10*65 and y_pin==11*65) and map==1:
               cnt+=1
               x_pin=-65
               y_pin=-65
               ditheo=False
          if x==x_chai and y==y_chai and luom==True:
                ditheo1=True
          if (x_chai==11*65 and y_chai==11*65 or x_chai==10*65 and y_chai==11*65) and map==1:
               cnt+=1
               x_chai=-65
               y_chai=-65
               ditheo1=False
          if x==x_lon and y==y_lon and luom==True:
                ditheo2=True
          if (x_lon==11*65 and y_lon==11*65 or x_lon==10*65 and y_lon==11*65) and map==1:
               cnt+=1
               x_lon=-65
               y_lon=-65
               ditheo2=False
          if x==x_pin1 and y==y_pin1 and luom==True:
                ditheo3=True
          if (x_pin1==11*65 and y_pin1==11*65 or x_pin1==10*65 and y_pin1==11*65) and map==1:
               cnt+=1
               x_pin1=-65
               y_pin1=-65
               ditheo3=False
          if x==x_chai1 and y==y_chai1 and luom==True:
                ditheo4=True
          if (x_chai1==11*65 and y_chai1==11*65 or x_chai1==10*65 and y_chai1==11*65) and map==1:
               cnt+=1
               x_chai1=-65
               y_chai1=-65
               ditheo4=False
          if x==x_lon1 and y==y_lon1 and luom==True:
                ditheo5=True
          if (x_lon1==11*65 and y_lon1==11*65 or x_lon1==10*65 and y_lon1==11*65) and map==1:
               cnt+=1
               x_lon1=-65
               y_lon1=-65
               ditheo5=False
          if x==x_pin2 and y==y_pin2 and luom==True:
                ditheo6=True
          if (x_pin2==11*65 and y_pin2==11*65 or x_pin2==10*65 and y_pin2==11*65) and map==1:
               cnt+=1
               x_pin2=-65
               y_pin2=-65
               ditheo6=False
          if x==x_chai2 and y==y_chai2 and luom==True:
                ditheo7=True
          if (x_chai2==11*65 and y_chai2==11*65 or x_chai2==10*65 and y_chai2==11*65) and map==1:
               cnt+=1
               x_chai2=-65
               y_chai2=-65
               ditheo7=False
          if x==x_lon2 and y==y_lon2 and luom==True:
                ditheo8=True
          if (x_lon2==11*65 and y_lon2==11*65 or x_lon2==10*65 and y_lon2==11*65) and map==1:
               cnt+=1
               x_lon2=-65
               y_lon2=-65
               ditheo8=False
          if x==x_pin3 and y==y_pin3 and luom==True:
                ditheo9=True
          if (x_pin3==11*65 and y_pin3==11*65 or x_pin3==10*65 and y_pin3==11*65) and map==1:
               cnt+=1
               x_pin3=-65
               y_pin3=-65
               ditheo9=False
          if x==x_chai3 and y==y_chai3 and luom==True:
                ditheo10=True
          if (x_chai3==11*65 and y_chai3==11*65 or x_chai3==10*65 and y_chai3==11*65) and map==1:
               cnt+=1
               x_chai3=-65
               y_chai3=-65
               ditheo10=False
          if x==x_lon3 and y==y_lon3 and luom==True:
                ditheo11=True
          if (x_lon3==11*65 and y_lon3==11*65 or x_lon3==10*65 and y_lon3==11*65) and map==1:
               cnt+=1
               x_lon3=-65
               y_lon3=-65
               ditheo11=False
          for event in pygame.event.get():
                if event.type == QUIT:
                      pygame.quit()
                      sys.exit()
                if ditheo:
                      y_pin=y
                      x_pin=x
                if ditheo1:
                      y_chai=y
                      x_chai=x
                if ditheo2:
                      y_lon=y
                      x_lon=x
                if ditheo3:
                      y_pin1=y
                      x_pin1=x
                if ditheo4:
                      y_chai1=y
                      x_chai1=x
                if ditheo5:
                      y_lon1=y
                      x_lon1=x
                if ditheo6:
                      y_pin2=y
                      x_pin2=x
                if ditheo7:
                      y_chai2=y
                      x_chai2=x
                if ditheo8:
                      y_lon2=y
                      x_lon2=x
                if ditheo9:
                      y_pin3=y
                      x_pin3=x
                if ditheo10:
                      y_chai3=y
                      x_chai3=x
                if ditheo11:
                      y_lon3=y
                      x_lon3=x
                if event.type==pygame.KEYDOWN :
                      if event.key==pygame.K_d and (trai==False and len==False and xuong==False)and batdau :
                            #phai=True
                            x+=65
                            direct = 90
                            print('x=',x)
                      if event.key==pygame.K_a and (phai==False and len==False and xuong==False)and batdau:
                            #trai=True
                            x-=65
                            direct = -90
                            print('x=',x)
                      if event.key==pygame.K_w and (phai==False and trai==False and xuong==False) and batdau:
                            #len=True
                            y-=65
                            direct = 0
                            print('y=',y)
                      if event.key==pygame.K_s and (phai==False and trai==False and len==False)and batdau:
                            #xuong=True
                            y+=65
                            direct = 180
                            print('y=',y)
                      if event.key==pygame.K_ESCAPE:
                            batdau=False
          nv_rect = pygame.Rect(x,y,65,65)
          if y < 0 and map == 1:
                map = 2
                y = 715
                x = 715
          if y>=780 and map==2:
               map=1
               y=0
               x=715
          if batdau:
                x,y = drawmapphiphai(nv_rect,x,y,direct)
                sc.blit(nv,(x,y))
                textsurface = myfont.render('Điểm '+ str(cnt), False, (255, 0, 0))
                sc.blit(textsurface,(0,0))
                if map!=1 or ditheo :
                      sc.blit(nv_baonilong,(x_pin,y_pin))
                if map!=1 or ditheo1 :
                      sc.blit(nv_baonilong,(x_chai,y_chai))
                if map!=1 or ditheo2 :
                      sc.blit(nv_baonilong,(x_lon,y_lon))
                if map!=1 or ditheo3 :
                      sc.blit(nv_pin,(x_pin1,y_pin1))
                if map!=1 or ditheo4 :
                      sc.blit(nv_chai,(x_chai1,y_chai1))
                if map!=1 or ditheo5 :
                      sc.blit(nv_lon,(x_lon1,y_lon1))
                if map!=1 or ditheo6 :
                      sc.blit(nv_pin,(x_pin2,y_pin2))
                if map!=1 or ditheo7 :
                      sc.blit(nv_chai,(x_chai2,y_chai2))
                if map!=1 or ditheo8 :
                      sc.blit(nv_lon,(x_lon2,y_lon2))
                if map!=1 or ditheo9 :
                      sc.blit(nv_pin,(x_pin3,y_pin3))
                if map!=1 or ditheo10 :
                      sc.blit(nv_chai,(x_chai3,y_chai3))
                if map!=1 or ditheo11 :
                      sc.blit(nv_lon,(x_lon3,y_lon3))
          else:
                if hh<1:
                      if start_button.draw(sc):
                            batdau=True
                            hh+=1
                else:
                      pygame.draw.rect(sc, (85, 85, 85,0.5), (0, 0, 1500, 775))
                      if resume_button.draw(sc):
                            batdau=True
                            hh+=1
                if exit_button.draw(sc):
                      pygame.quit()
                      sys.exit()
          await asyncio.sleep(0)
          pygame.display.update()
asyncio.run(main())