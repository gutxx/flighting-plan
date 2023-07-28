import pygame
from pygame.locals import *
'''
1、实现飞机的显示 并可以控制飞机的移动【面向对象】
'''
class heroplan(object):
    def __init__(self,screen):
        '''

        :param screen: 主窗体对象
        '''
        #飞机默认位置
        self.x=250
        self.y=390
        #设置要显示内容的窗口
        self.screen=screen
        #生成飞机的图片对象
        self.imagepath='./feiji/hero.jpg'
        self.image1=pygame.image.load(self.imagepath)
        #用来存放子弹的列表
        self.bulletlist=[]
        pass
    def moveleft(self):
        if self.x>=20:
            self.x-=20

        pass
    def moveright(self):
        if self.x<=480:
            self.x+=20
        pass
    def moverup(self):
        if self.y>=20:
            self.y-=20
        pass
    def movedown(self):
        if self.y<=370:
            self.y+=20
        pass
    def display(self):
        self.screen.blit(self.image1,(self.x,self.y))
        pass
        #完善子弹的展示逻辑
        needdeletelist=[]
        for item in self.bulletlist:
            if item.judge():
                needdeletelist.append(item)
        #重新遍历一下
        for i in needdeletelist:
            self.bulletlist.remove(i)
            pass
        for bullet in self.bulletlist:
            bullet.display()#显示子弹的位置
            bullet.move()#让这个子弹进行移动
    #发射子弹
    def shoot(self):
        #创建一个新的子弹对象
        newbullet=bullet(self.x,self.y,self.screen)
        self.bulletlist.append(newbullet)
        pass

    pass
def key_control(heroplan):
    eventlist = pygame.event.get()
    for event in eventlist:
        if event.type == QUIT:
            print("退出")
            exit()
            pass
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print("left")
                heroplan.moveleft()#调用函数实现
            elif event.key == K_d or event.key == K_RIGHT:
                print("right")
                heroplan.moveright()
            elif event.key == K_w or event.key == K_UP:
                print("UP")
                heroplan.moverup()
            elif event.key == K_s or event.key == K_DOWN:
                print("DOWN")
                heroplan.movedown()
            elif event.key == K_SPACE:
                print("K_SPACE")
                heroplan.shoot() #空格  发射子弹

class bullet(object):
    def __init__(self,x,y,screen):
        self.x=x+10
        self.y=y-30
        self.screen=screen
        self.image=pygame.image.load('./feiji/bullet.jpg')

        pass
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
        pass
    def move(self):
        self.y-=0.1
        pass
    def judge(self):
        '''判断子弹是否越界'''
        if self.y<0:
            return  True
        else:
            return  False


def main():
    #首先创建一个窗口 用来显示内容
    screen = pygame.display.set_mode((500,421))
    #设置一个背景图片
    background = pygame.image.load('./feiji/background.jpg')
    #设置一个标题
    pygame.display.set_caption("飞机大战",'plan')
    #添加背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load('./feiji/backgroundmusic.mp3')
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)#循环次数 -1为无限循环

    #载入玩家的飞机图片
    hero=heroplan(screen)
    #初始化玩家的位置：
    x,y=250,390
    #设定要显示的内容
    while True:
        #显示背景图
        screen.blit(background,(0,0))
        #显示玩家飞机模型
        hero.display()
        #获取键盘事件
        key_control(hero)
        eventlist=pygame.event.get()
        for event in eventlist:
            if event.type==QUIT:
                print("退出")
                exit()
                pass
            elif event.type==KEYDOWN:
                if event.key==K_a or event.key==K_LEFT:
                    print("left")
                    if x>=20:
                        x-=20
                elif event.key==K_d or event.key==K_RIGHT:
                    print("right")
                    if x<=480:
                        x+=20
                elif event.key==K_w or  event.key==K_UP:
                    print("UP")
                    if y>=20:
                        y-=20
                elif event.key==K_s or event.key==K_DOWN:
                    print("DOWN")
                    if y<=380:
                        y+=20
                elif event.key==K_SPACE:
                    print("K_SPACE")
        pygame.display.update()
if __name__ == '__main__':
    main()