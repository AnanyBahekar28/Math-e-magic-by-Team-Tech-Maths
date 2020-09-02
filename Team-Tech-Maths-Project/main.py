import pygame
pygame.init()
import sys
from time import sleep

green = (0,255,0)
dark_green = (50,150,50)
red = (255,0,0)
dark_red = (150,50,50)
blue = (0,0,255)
dark_blue = (50,50,150)

font = pygame.font.SysFont("Courier", 40)

def writeOnTheWindow(text = ""):
    global font
    
    textToUpdate = font.render(text, True, (0,0,0), None)
    win.blit(textToUpdate, (20, 500))

def User_Interface():
    Width = 600
    Height = 540

    screen_template = pygame.image.load("images/template.png")
    icon = pygame.image.load("images/icon.png")
    
    pygame.display.set_icon(icon)
    pygame.display.set_caption("Math-e-magic")
    
    screen = pygame.display.set_mode((Width, Height))
    
    screen.blit(screen_template, (0, 0))
    return screen

win = User_Interface()

#%%

def turnToNextPageForNotes(list_of_pages):
    global page, current_index
    
    pages_turned = 0
    for i in list_of_pages:
        pages_turned += 1
        if page == i:
            current_index = pages_turned - 1
            page = list_of_pages[pages_turned]
            break


#%%

def turnToLastPageForNotes(list_of_pages):
    global page, current_index
    
    pages_turned = 0
    for i in list_of_pages:
        pages_turned += 1
        if page == i:
            current_index = pages_turned - 1
            page = list_of_pages[pages_turned - 2]


#%% Lists for tests of chapters

QuesInt = ['-3+7=','4+-9=','-9+8=','-24*6=','5*-8=','-40/10=','-36/4=','45--10=','34-+6=','67-56=']
AnsInt  = ['4','-5','-1','-144','-40','-4','-9','55','28','11']

QuesRatio = ['If 12:7::24:x, then find the value of 2x',
        'Are 6:4 and 3:7 in proportion?(y/n)',
        'Two numbers are in a ratio 5:6. Their difference is equal to 10. What is the first number?',
        'Are 9:13 and 14:3 in proportion?(y/n)',
        'If 53:12::212:x, then find the value of 2x+1',
        'Two numbers are in a ratio 7:8. Their sum is equal to 135. What is the second number?',
        'Are 2:9 and 6:27 in proportion(y/n)',
        'Two numbers are in a ratio 5:9. Their difference is equal to 20. What is the first number?',
        'If 13:5::169:x, then find the value of x',
        'Two numbers are in a ratio 7:4. Their sum is equal to 44. What is the second number?']
AnsRatio = ['28','n','50','n','97','72','y','25','65','16']


QuesSq = ['√36','√441','√121','√81','√169','15²','18²','12²','19²','7²']
AnsSq = ['6','21','11','9','13','225','324','144','361','49']

QuesCube = ['9³','5³','13³','16³','7³','∛9621','∛1331','∛64','∛6859','∛1000']
AnsCube  = ['729','125','2197','4096','343','21','11','4','19','10']


#%% Tests

def conductTest(ques, ans):
    print("Here you go the test")
    
    score = 0
    
    for i in range(len(ques)):
        user_ans = input(ques[i])
        if user_ans == ans[i]:
            print("Correct!!")
            score += 1
        else:
            print("Wrong")
    
    print(f"These are the number of right questions you scored: {score}")


#%% Button Configuration
class button:
    def __init__(self, color, x, y, width, height, text = ''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self._enable = False
        
    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))
        self._enable = True
        
    def isOver(self, pos): #pos[0] = x
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if self._enable == True:
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True
        return False
    
    def setEnable(self, status=False):
        self._enable = status
        return self._enable

    def getEnable(self):
        return (self._enable)
    


#%% Page initialization

backList = [["StartPage"],
            ["StudyPage", "AboutUsPage"],
            ["5thStdPage", "6thStdPage", "7thStdPage", "8thStdPage"],
            ["Integers5thStdPage1", "Integers5thStdPage2", "Integers5thStdPage3", "Integers5thStdPage4", "Integers5thStdPage5", "Integers5thStdPage6", "Integers5thStdPage7"],
            ["Fractions5thStdPage1", "Fractions5thStdPage2", "Fractions5thStdPage3", "Fractions5thStdPage4", "Fractions5thStdPage5", "Fractions5thStdPage6", "Fractions5thStdPage7", "Fractions5thStdPage8", "Fractions5thStdPage9", "Fractions5thStdPage10", "Fractions5thStdPage11", "Fractions5thStdPage12", "Fractions5thStdPage13"],
            ["Mensuration6thPage1", "Mensuration6thPage2", "Mensuration6thPage2", "Mensuration6thPage3", "Mensuration6thPage4", "Mensuration6thPage5", "Mensuration6thPage6", "Mensuration6thPage7", "Mensuration6thPage9", "Mensuration6thPage10", "Mensuration6thPage11", "Mensuration6thPage12"],
            ["Algebra6thPage1", "Algebra6thPage2", "Algebra6thPage3", "Algebra6thPage4", "Algebra6thPage5", "Algebra6thPage6", "Algebra6thPage7", "Algebra6thPage8", "Algebra6thPage9", "Algebra6thPage10"],
            ["Exponents7thPage1", "Exponents7thPage2", "Exponents7thPage3", "Exponents7thPage4", "Exponents7thPage5", "Exponents7thPage6", "Exponents7thPage7", "Exponents7thPage8", "Exponents7thPage9", "Exponents7thPage10"],
            ["Ratio7thPage1", "Ratio7thPage2", "Ratio7thPage3", "Ratio7thPage4", "Ratio7thPage5", "Ratio7thPage6", "Ratio7thPage7", "Ratio7thPage8", "Ratio7thPage9", "Ratio7thPage10", "Ratio7thPage11", "Ratio7thPage12"],
            ["Squares8thPage1", "Squares8thPage2", "Squares8thPage3", "Squares8thPage4", "Squares8thPage5", "Squares8thPage6", "Squares8thPage7", "Squares8thPage8", "Squares8thPage9", "Squares8thPage10", "Squares8thPage11", "Squares8thPage12", "Squares8thPage13", "Squares8thPage14", "Squares8thPage15", "Squares8thPage16", "Squares8thPage17", "Squares8thPage18", "Squares8thPage19", "Squares8thPage20", "SquareSquare8thPage21", "Squares8thPage22", "Squares8thPage23", "Squares8thPage24", "Squares8thPage25", "Squares8thPage26"],
            ["Cube8thPage1", "Cube8thPage2", "Cube8thPage4", "Cube8thPage5", "Cube8thPage6", "Cube8thPage7", "Cube8thPage8", "Cube8thPage9", "Cube8thPage10", "Cube8thPage11", "Cube8thPage12", "Cube8thPage13", "Cube8thPage14", "Cube8thPage15", "Cube8thPage16", "Cube8thPage17", "Cube8thPage18"]]

page = backList[0][0]
oldPage = ""
current_index = 0

#%% Pages

aboutUs_Img = pygame.image.load("images/about_us.png")

# 5th std images ch1
p1_chapter1_std5 = pygame.image.load("images/Std 5 chapter 1/page_1.png")
p2_chapter1_std5 = pygame.image.load("images/Std 5 chapter 1/page_2.png")
p3_chapter1_std5 = pygame.image.load("images/Std 5 chapter 1/page_3.png")
p4_chapter1_std5 = pygame.image.load("images/Std 5 chapter 1/page_4.png")
p5_chapter1_std5 = pygame.image.load("images/Std 5 chapter 1/page_5.png")
p6_chapter1_std5 = pygame.image.load("images/Std 5 chapter 1/page_6.png")
p7_chapter1_std5 = pygame.image.load("images/Std 5 chapter 1/page_7.png")

# 5th std images ch2
p1_chapter2_std5 = pygame.image.load("images/Std 5 chapter 2/page_1.png")
p2_chapter2_std5 = pygame.image.load("images/Std 5 chapter 2/page_2.png")
p3_chapter2_std5 = pygame.image.load("images/Std 5 chapter 2/page_3.png")
p4_chapter2_std5 = pygame.image.load("images/Std 5 chapter 2/page_4.png")
p5_chapter2_std5 = pygame.image.load("images/Std 5 chapter 2/page_5.png")
p6_chapter2_std5 = pygame.image.load("images/Std 5 chapter 2/page_6.png")
p7_chapter2_std5 = pygame.image.load("images/Std 5 chapter 2/page_7.png")
p8_chapter2_std5 = pygame.image.load("images/Std 5 chapter 2/page_8.png")
p9_chapter2_std5 = pygame.image.load("images/Std 5 chapter 2/page_9.png")
p10_chapter2_std5 = pygame.image.load("images/Std 5 chapter 2/page_10.png")
p11_chapter2_std5 = pygame.image.load("images/Std 5 chapter 2/page_11.png")
p12_chapter2_std5 = pygame.image.load("images/Std 5 chapter 2/page_12.png")
p13_chapter2_std5 = pygame.image.load("images/Std 5 chapter 2/page_13.png")

# 6th std images ch1
p1_chapter1_std6 = pygame.image.load("images/Std 6 chapter 1/page_1.png")
p2_chapter1_std6 = pygame.image.load("images/Std 6 chapter 1/page_2.png")
p3_chapter1_std6 = pygame.image.load("images/Std 6 chapter 1/page_3.png")
p4_chapter1_std6 = pygame.image.load("images/Std 6 chapter 1/page_4.png")
p5_chapter1_std6 = pygame.image.load("images/Std 6 chapter 1/page_5.png")
p6_chapter1_std6 = pygame.image.load("images/Std 6 chapter 1/page_6.png")
p7_chapter1_std6 = pygame.image.load("images/Std 6 chapter 1/page_7.png")
p8_chapter1_std6 = pygame.image.load("images/Std 6 chapter 1/page_8.png")
p9_chapter1_std6 = pygame.image.load("images/Std 6 chapter 1/page_9.png")
p10_chapter1_std6 = pygame.image.load("images/Std 6 chapter 1/page_10.png")
p11_chapter1_std6 = pygame.image.load("images/Std 6 chapter 1/page_11.png")
p12_chapter1_std6 = pygame.image.load("images/Std 6 chapter 1/page_12.png")

# 6th std images ch2
p1_chapter2_std6 = pygame.image.load("images/Std 6 chapter 2/page_1.png")
p2_chapter2_std6 = pygame.image.load("images/Std 6 chapter 2/page_2.png")
p3_chapter2_std6 = pygame.image.load("images/Std 6 chapter 2/page_3.png")
p4_chapter2_std6 = pygame.image.load("images/Std 6 chapter 2/page_4.png")
p5_chapter2_std6 = pygame.image.load("images/Std 6 chapter 2/page_5.png")
p6_chapter2_std6 = pygame.image.load("images/Std 6 chapter 2/page_6.png")
p7_chapter2_std6 = pygame.image.load("images/Std 6 chapter 2/page_7.png")
p8_chapter2_std6 = pygame.image.load("images/Std 6 chapter 2/page_8.png")
p9_chapter2_std6 = pygame.image.load("images/Std 6 chapter 2/page_9.png")
p10_chapter2_std6 = pygame.image.load("images/Std 6 chapter 2/page_10.png")

# 7th std images ch1
p1_chapter1_std7 = pygame.image.load("images/Std 7 chapter 1/page_1.png")
p2_chapter1_std7 = pygame.image.load("images/Std 7 chapter 1/page_2.png")
p3_chapter1_std7 = pygame.image.load("images/Std 7 chapter 1/page_3.png")
p4_chapter1_std7 = pygame.image.load("images/Std 7 chapter 1/page_4.png")
p5_chapter1_std7 = pygame.image.load("images/Std 7 chapter 1/page_5.png")
p6_chapter1_std7 = pygame.image.load("images/Std 7 chapter 1/page_6.png")
p7_chapter1_std7 = pygame.image.load("images/Std 7 chapter 1/page_7.png")

# 7th std images ch2
p1_chapter2_std7 = pygame.image.load("images/Std 7 chapter 2/page_1.png")
p2_chapter2_std7 = pygame.image.load("images/Std 7 chapter 2/page_2.png")
p3_chapter2_std7 = pygame.image.load("images/Std 7 chapter 2/page_3.png")
p4_chapter2_std7 = pygame.image.load("images/Std 7 chapter 2/page_4.png")
p5_chapter2_std7 = pygame.image.load("images/Std 7 chapter 2/page_5.png")
p6_chapter2_std7 = pygame.image.load("images/Std 7 chapter 2/page_6.png")
p7_chapter2_std7 = pygame.image.load("images/Std 7 chapter 2/page_7.png")
p8_chapter2_std7 = pygame.image.load("images/Std 7 chapter 2/page_8.png")
p9_chapter2_std7 = pygame.image.load("images/Std 7 chapter 2/page_9.png")
p10_chapter2_std7 = pygame.image.load("images/Std 7 chapter 2/page_10.png")
p11_chapter2_std7 = pygame.image.load("images/Std 7 chapter 2/page_11.png")
p12_chapter2_std7 = pygame.image.load("images/Std 7 chapter 2/page_12.png")

# 8th std images ch1
p1_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_1.png")
p2_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_2.png")
p3_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_3.png")
p4_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_4.png")
p5_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_5.png")
p6_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_6.png")
p7_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_7.png")
p8_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_8.png")
p9_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_9.png")
p10_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_10.png")
p11_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_11.png")
p12_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_12.png")
p13_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_13.png")
p14_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_14.png")
p15_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_15.png")
p16_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_16.png")
p17_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_17.png")
p18_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_18.png")
p19_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_19.png")
p20_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_20.png")
p21_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_21.png")
p22_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_22.png")
p23_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_23.png")
p24_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_24.png")
p25_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_25.png")
p26_chapter1_std8 = pygame.image.load("images/Std 8 chapter 1/page_26.png")

# 8th std images ch2
p1_chapter2_std8 = pygame.image.load("images/Std 8 chapter 2/page_1.png")
p2_chapter2_std8 = pygame.image.load("images/Std 8 chapter 2/page_2.png")
p3_chapter2_std8 = pygame.image.load("images/Std 8 chapter 2/page_3.png")
p4_chapter2_std8 = pygame.image.load("images/Std 8 chapter 2/page_4.png")
p5_chapter2_std8 = pygame.image.load("images/Std 8 chapter 2/page_5.png")
p6_chapter2_std8 = pygame.image.load("images/Std 8 chapter 2/page_6.png")
p7_chapter2_std8 = pygame.image.load("images/Std 8 chapter 2/page_7.png")
p8_chapter2_std8 = pygame.image.load("images/Std 8 chapter 2/page_8.png")
p9_chapter2_std8 = pygame.image.load("images/Std 8 chapter 2/page_9.png")
p10_chapter2_std8 = pygame.image.load("images/Std 8 chapter 2/page_10.png")
p11_chapter2_std8 = pygame.image.load("images/Std 8 chapter 2/page_11.png")
p12_chapter2_std8 = pygame.image.load("images/Std 8 chapter 2/page_12.png")
p13_chapter2_std8 = pygame.image.load("images/Std 8 chapter 2/page_13.png")
p14_chapter2_std8 = pygame.image.load("images/Std 8 chapter 2/page_14.png")
p15_chapter2_std8 = pygame.image.load("images/Std 8 chapter 2/page_15.png")
p16_chapter2_std8 = pygame.image.load("images/Std 8 chapter 2/page_16.png")
p17_chapter2_std8 = pygame.image.load("images/Std 8 chapter 2/page_17.png")
p18_chapter2_std8 = pygame.image.load("images/Std 8 chapter 2/page_18.png")


#%% Button initialization

def redrawWindow():
    global page
    
    if page == "StartPage":
        User_Interface()
        StudyButton.draw(win, (0,0,0))
        AboutUsButton.draw(win, (0,0,0))
    elif page == "StudyPage":
        User_Interface()
        BackButton.draw(win, (0,0,0))
        Std5Button.draw(win, (0,0,0))
        Std6Button.draw(win, (0,0,0))
        Std7Button.draw(win, (0,0,0))
        Std8Button.draw(win, (0,0,0))
    elif page == "AboutUsPage":
        User_Interface()
        win.blit(aboutUs_Img, (50, 26))
        BackButton.draw(win, (0,0,0))
    elif page == "5thStdPage":
        User_Interface()
        BackButton.draw(win, (0,0,0))
        Integer5thButton.draw(win, (0,0,0))
        Fractions5thButton.draw(win, (0,0,0))
    elif page == "6thStdPage":
        User_Interface()
        BackButton.draw(win, (0,0,0))
        Mensuration6thButton.draw(win, (0,0,0))
        Algebra6thButton.draw(win, (0,0,0))
    elif page == "7thStdPage":
        User_Interface()
        BackButton.draw(win, (0,0,0))
        Exponents7thButton.draw(win, (0,0,0))
        Ratio7thButton.draw(win, (0,0,0))
    elif page == "8thStdPage":
        User_Interface()
        BackButton.draw(win, (0,0,0))
        Square8thButton.draw(win, (0,0,0))
        Cube8thButton.draw(win, (0,0,0))
    elif page == "Integers5thStdPage1":
        User_Interface()
        win.blit(p1_chapter1_std5, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Integers5thStdPage2":
        User_Interface()
        win.blit(p2_chapter1_std5, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    elif page == "Integers5thStdPage3":
        User_Interface()
        win.blit(p3_chapter1_std5, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    elif page == "Integers5thStdPage4":
        User_Interface()
        win.blit(p4_chapter1_std5, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    elif page == "Integers5thStdPage5":
        User_Interface()
        win.blit(p5_chapter1_std5, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    elif page == "Integers5thStdPage6":
        User_Interface()
        win.blit(p6_chapter1_std5, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    elif page == "Integers5thStdPage7":
        User_Interface()
        win.blit(p7_chapter1_std5, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        writeOnTheWindow("Get ready for a test")
        
        pygame.display.update()
        sleep(2)
        
        conductTest(QuesInt, AnsInt)
        page = "5thStdPage"
    
    elif page == "Fractions5thStdPage1":
        User_Interface()
        win.blit(p1_chapter2_std5, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Fractions5thStdPage2":
        User_Interface()
        win.blit(p2_chapter2_std5, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Fractions5thStdPage3":
        User_Interface()
        win.blit(p3_chapter2_std5, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Fractions5thStdPage4":
        User_Interface()
        win.blit(p4_chapter2_std5, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Fractions5thStdPage5":
        User_Interface()
        win.blit(p5_chapter2_std5, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Fractions5thStdPage6":
        User_Interface()
        win.blit(p6_chapter2_std5, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Fractions5thStdPage7":
        User_Interface()
        win.blit(p7_chapter2_std5, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        
        writeOnTheWindow("Get ready for a test")
        pygame.display.update()
        sleep(2)
        
        conductTest(QuesInt, AnsInt)
        page = "5thStdPage"
    
    elif page == "Fractions5thStdPage8":
        User_Interface()
        win.blit(p8_chapter2_std5, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Fractions5thStdPage9":
        User_Interface()
        win.blit(p9_chapter2_std5, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Fractions5thStdPage10":
        User_Interface()
        win.blit(p10_chapter2_std5, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Fractions5thStdPage11":
        User_Interface()
        win.blit(p11_chapter2_std5, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Fractions5thStdPage12":
        User_Interface()
        win.blit(p12_chapter2_std5, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Fractions5thStdPage13":
        User_Interface()
        win.blit(p13_chapter2_std5, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Mensuration6thPage1":
        User_Interface()
        win.blit(p1_chapter1_std6, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Mensuration6thPage2":
        User_Interface()
        win.blit(p2_chapter1_std6, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Mensuration6thPage3":
        User_Interface()
        win.blit(p3_chapter1_std6, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Mensuration6thPage4":
        User_Interface()
        win.blit(p4_chapter1_std6, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Mensuration6thPage5":
        User_Interface()
        win.blit(p5_chapter1_std6, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Mensuration6thPage6":
        User_Interface()
        win.blit(p6_chapter1_std6, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Mensuration6thPage7":
        User_Interface()
        win.blit(p7_chapter1_std6, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Mensuration6thPage8":
        User_Interface()
        win.blit(p8_chapter1_std6, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Mensuration6thPage9":
        User_Interface()
        win.blit(p9_chapter1_std6, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Mensuration6thPage10":
        User_Interface()
        win.blit(p10_chapter1_std6, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Mensuration6thPage11":
        User_Interface()
        win.blit(p11_chapter1_std6, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Mensuration6thPage12":
        User_Interface()
        win.blit(p12_chapter1_std6, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Algebra6thPage1":
        User_Interface()
        win.blit(p1_chapter2_std6, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Algebra6thPage2":
        User_Interface()
        win.blit(p2_chapter2_std6, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Algebra6thPage3":
        User_Interface()
        win.blit(p3_chapter2_std6, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Algebra6thPage4":
        User_Interface()
        win.blit(p4_chapter2_std6, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Algebra6thPage5":
        User_Interface()
        win.blit(p5_chapter2_std6, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Algebra6thPage6":
        User_Interface()
        win.blit(p6_chapter2_std6, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Algebra6thPage7":
        User_Interface()
        win.blit(p7_chapter2_std6, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Algebra6thPage8":
        User_Interface()
        win.blit(p8_chapter2_std6, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Algebra6thPage9":
        User_Interface()
        win.blit(p9_chapter2_std6, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Algebra6thPage10":
        User_Interface()
        win.blit(p10_chapter2_std6, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Ratio7thPage1":
        User_Interface()
        win.blit(p1_chapter2_std7, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Ratio7thPage2":
        User_Interface()
        win.blit(p2_chapter2_std7, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Ratio7thPage3":
        User_Interface()
        win.blit(p3_chapter2_std7, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Ratio7thPage4":
        User_Interface()
        win.blit(p4_chapter2_std7, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Ratio7thPage5":
        User_Interface()
        win.blit(p5_chapter2_std7, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Ratio7thPage6":
        User_Interface()
        win.blit(p6_chapter2_std7, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Ratio7thPage7":
        User_Interface()
        win.blit(p7_chapter2_std7, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Ratio7thPage8":
        User_Interface()
        win.blit(p8_chapter2_std7, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Ratio7thPage9":
        User_Interface()
        win.blit(p9_chapter2_std7, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Ratio7thPage10":
        User_Interface()
        win.blit(p10_chapter2_std7, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Ratio7thPage11":
        User_Interface()
        win.blit(p11_chapter2_std7, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Ratio7thPage12":
        User_Interface()
        win.blit(p12_chapter2_std7, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        writeOnTheWindow("Get ready for a test")
        
        pygame.display.update()
        sleep(2)
        
        conductTest(QuesRatio, AnsRatio)
        page = "7thStdPage"
    
    elif page == "Exponents7thPage1":
        User_Interface()
        win.blit(p1_chapter1_std7, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Exponents7thPage2":
        User_Interface()
        win.blit(p2_chapter1_std7, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Exponents7thPage3":
        User_Interface()
        win.blit(p3_chapter1_std7, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Exponents7thPage4":
        User_Interface()
        win.blit(p4_chapter1_std7, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Exponents7thPage5":
        User_Interface()
        win.blit(p5_chapter1_std7, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Exponents7thPage6":
        User_Interface()
        win.blit(p6_chapter1_std7, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Exponents7thPage7":
        User_Interface()
        win.blit(p7_chapter1_std7, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage1":
        User_Interface()
        win.blit(p1_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage2":
        User_Interface()
        win.blit(p2_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage3":
        User_Interface()
        win.blit(p3_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage4":
        User_Interface()
        win.blit(p4_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage5":
        User_Interface()
        win.blit(p5_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage6":
        User_Interface()
        win.blit(p6_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage7":
        User_Interface()
        win.blit(p7_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage8":
        User_Interface()
        win.blit(p8_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage9":
        User_Interface()
        win.blit(p9_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage10":
        User_Interface()
        win.blit(p10_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage11":
        User_Interface()
        win.blit(p11_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage12":
        User_Interface()
        win.blit(p12_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage13":
        User_Interface()
        win.blit(p13_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage14":
        User_Interface()
        win.blit(p14_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage15":
        User_Interface()
        win.blit(p15_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage16":
        User_Interface()
        win.blit(p16_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage17":
        User_Interface()
        win.blit(p17_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage18":
        User_Interface()
        win.blit(p2_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage19":
        User_Interface()
        win.blit(p19_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage20":
        User_Interface()
        win.blit(p20_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage21":
        User_Interface()
        win.blit(p21_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage22":
        User_Interface()
        win.blit(p22_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage23":
        User_Interface()
        win.blit(p23_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage24":
        User_Interface()
        win.blit(p24_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage25":
        User_Interface()
        win.blit(p25_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
    
    elif page == "Squares8thPage26":
        User_Interface()
        win.blit(p26_chapter1_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        LastPageButton.draw(win, (0,0,0))
        
        writeOnTheWindow("Get ready for a test")
        
        pygame.display.update()
        sleep(2)
        
        conductTest(QuesSq, AnsSq)
        page = "8thStdPage"
    
    elif page == "Cubes8thPage1":
        User_Interface()
        win.blit(p1_chapter2_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Cubes8thPage2":
        User_Interface()
        win.blit(p2_chapter2_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Cubes8thPage3":
        User_Interface()
        win.blit(p3_chapter2_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Cubes8thPage4":
        User_Interface()
        win.blit(p4_chapter2_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Cubes8thPage5":
        User_Interface()
        win.blit(p1_chapter2_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Cubes8thPage1":
        User_Interface()
        win.blit(p5_chapter2_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Cubes8thPage6":
        User_Interface()
        win.blit(p6_chapter2_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Cubes8thPage7":
        User_Interface()
        win.blit(p7_chapter2_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Cubes8thPage8":
        User_Interface()
        win.blit(p8_chapter2_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Cubes8thPage9":
        User_Interface()
        win.blit(p9_chapter2_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Cubes8thPage10":
        User_Interface()
        win.blit(p10_chapter2_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Cubes8thPage11":
        User_Interface()
        win.blit(p11_chapter2_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Cubes8thPage12":
        User_Interface()
        win.blit(p12_chapter2_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Cubes8thPage13":
        User_Interface()
        win.blit(p13_chapter2_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Cubes8thPage14":
        User_Interface()
        win.blit(p14_chapter2_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Cubes8thPage15":
        User_Interface()
        win.blit(p15_chapter2_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Cubes8thPage16":
        User_Interface()
        win.blit(p16_chapter2_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Cubes8thPage17":
        User_Interface()
        win.blit(p17_chapter2_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
    
    elif page == "Cubes8thPage18":
        User_Interface()
        win.blit(p18_chapter2_std8, (50, 80))
        BackButton.draw(win, (0,0,0))
        NextPageButton.draw(win, (0,0,0))
        writeOnTheWindow("Get ready for a test")
        
        pygame.display.update()
        sleep(2)
        
        conductTest(QuesCube, AnsCube)
        page = "8thStdPage"


#%% Button Creation # (color, x, y, width, height, text)

# common button for every page(except main menu)
BackButton = button((255, 0, 0), 5, 10, 100, 50, text = "Back")

# page navigation buttons
LastPageButton = button((0, 0, 255), 245, 10, 50, 50, text = "<")
NextPageButton = button((0, 0, 255), 295, 10, 50, 50, text = ">")

# Main menu buttons
StudyButton = button((0, 255, 0), 200, 175, 175, 50, text = 'Study')
AboutUsButton = button((0, 255, 0), 190, 300, 200, 50, text = "About Us")

# Std button
Std5Button = button((0, 255, 0), 200, 150, 200, 50, text = "Std 5")
Std6Button = button((0, 255, 0), 200, 225, 200, 50, text = "Std 6")
Std7Button = button((0, 255, 0), 200, 300, 200, 50, text = "Std 7")
#Std7Button = button((0, 255, 0), 300, 400, 200, 50, text = "Std 7")
Std8Button = button((0, 255, 0), 200, 375, 200, 50, text = "Std 8")

# 5th std chapter buttons
Integer5thButton = button((0, 255, 0), 200, 175, 175, 50, text = "Integers")
Fractions5thButton = button((0, 255, 0), 50, 300, 480, 50, text = "Fractions and Decimals")

# 6th std chapter button
Mensuration6thButton = button((0, 255, 0), 150, 175, 275, 50, text = "Mensuration")
Algebra6thButton = button((0, 255, 0), 190, 300, 200, 50, text = "Algebra")

# 7th std chapter button
Exponents7thButton = button((0, 255, 0), 50, 170, 480, 50, text = "Exponents and Power")
Ratio7thButton = button((0, 255, 0), 50, 300, 480, 50, text = "Ratio and Proportion")

# 8th std chapter button
Square8thButton = button((0, 255, 0), 50, 175, 510, 50, text = "Squares and their Roots")
Cube8thButton = button((0, 255, 0), 60, 290, 480, 50, text = "Cubes and their Roots")


#%% Button disabling

buttonsOnAPage = {"StartPage": [StudyButton, AboutUsButton],
                  "StudyPage": [Std5Button, Std6Button, Std7Button, Std8Button],
                  "AboutUsPage": [None],
                  
                  # 5th std
                  "5thStdPage": [Integer5thButton, Fractions5thButton],
                  
                  "Integers5thStdPage1": [NextPageButton],
                  "Integers5thStdPage2": [NextPageButton, LastPageButton],
                  "Integers5thStdPage3": [NextPageButton, LastPageButton],
                  "Integers5thStdPage4": [NextPageButton, LastPageButton],
                  "Integers5thStdPage5": [NextPageButton, LastPageButton],
                  "Integers5thStdPage6": [NextPageButton, LastPageButton],
                  "Integers5thStdPage7": [LastPageButton],
                  
                  "Fractions5thStdPage1": [NextPageButton],
                  "Fractions5thStdPage2": [NextPageButton, LastPageButton],
                  "Fractions5thStdPage3": [NextPageButton, LastPageButton],
                  "Fractions5thStdPage4": [NextPageButton, LastPageButton],
                  "Fractions5thStdPage5": [NextPageButton, LastPageButton],
                  "Fractions5thStdPage6": [NextPageButton, LastPageButton],
                  "Fractions5thStdPage7": [NextPageButton, LastPageButton],
                  "Fractions5thStdPage8": [NextPageButton, LastPageButton],
                  "Fractions5thStdPage9": [NextPageButton, LastPageButton],
                  "Fractions5thStdPage10": [NextPageButton, LastPageButton],
                  "Fractions5thStdPage11": [LastPageButton],
                  
                  # 6th std
                  "6thStdPage": [Mensuration6thButton, Algebra6thButton],
                  
                  "Mensuration6thPage1": [NextPageButton],
                  "Mensuration6thPage2": [NextPageButton, LastPageButton],
                  "Mensuration6thPage3": [NextPageButton, LastPageButton],
                  "Mensuration6thPage4": [NextPageButton, LastPageButton],
                  "Mensuration6thPage5": [NextPageButton, LastPageButton],
                  "Mensuration6thPage6": [NextPageButton, LastPageButton],
                  "Mensuration6thPage7": [NextPageButton, LastPageButton],
                  "Mensuration6thPage8": [NextPageButton, LastPageButton],
                  "Mensuration6thPage9": [NextPageButton, LastPageButton],
                  "Mensuration6thPage10": [NextPageButton, LastPageButton],
                  "Mensuration6thPage11": [NextPageButton, LastPageButton],
                  "Mensuration6thPage12": [LastPageButton],
                  
                  "Algebra6thPage1": [NextPageButton],
                  "Algebra6thPage2": [NextPageButton, LastPageButton],
                  "Algebra6thPage3": [NextPageButton, LastPageButton],
                  "Algebra6thPage4": [NextPageButton, LastPageButton],
                  "Algebra6thPage5": [NextPageButton, LastPageButton],
                  "Algebra6thPage6": [NextPageButton, LastPageButton],
                  "Algebra6thPage7": [NextPageButton, LastPageButton],
                  "Algebra6thPage8": [NextPageButton, LastPageButton],
                  "Algebra6thPage9": [NextPageButton, LastPageButton],
                  "Algebra6thPage10": [LastPageButton],
                  
                  # 7th std
                  "7thStdPage": [Exponents7thButton, Ratio7thButton],
                  
                  "Exponents7thPage1": [NextPageButton],
                  "Exponents7thPage2": [NextPageButton, LastPageButton],
                  "Exponents7thPage3": [NextPageButton, LastPageButton],
                  "Exponents7thPage4": [NextPageButton, LastPageButton],
                  "Exponents7thPage5": [NextPageButton, LastPageButton],
                  "Exponents7thPage6": [NextPageButton, LastPageButton],
                  "Exponents7thPage7": [NextPageButton, LastPageButton],
                  "Exponents7thPage8": [NextPageButton, LastPageButton],
                  "Exponents7thPage9": [NextPageButton, LastPageButton],
                  "Exponents7thPage10": [LastPageButton],
                  
                  "Ratio7thPage1": [NextPageButton],
                  "Ratio7thPage2": [NextPageButton, LastPageButton],
                  "Ratio7thPage3": [NextPageButton, LastPageButton],
                  "Ratio7thPage4": [NextPageButton, LastPageButton],
                  "Ratio7thPage5": [NextPageButton, LastPageButton],
                  "Ratio7thPage6": [NextPageButton, LastPageButton],
                  "Ratio7thPage7": [NextPageButton, LastPageButton],
                  "Ratio7thPage8": [NextPageButton, LastPageButton],
                  "Ratio7thPage9": [NextPageButton, LastPageButton],
                  "Ratio7thPage10": [NextPageButton, LastPageButton],
                  "Ratio7thPage11": [NextPageButton, LastPageButton],
                  "Ratio7thPage12": [LastPageButton],
                  
                  # 8th std
                  "8thStdPage": [Square8thButton, Cube8thButton],
                  
                  "Squares8thPage1": [NextPageButton],
                  "Squares8thPage2": [NextPageButton, LastPageButton],
                  "Squares8thPage3": [NextPageButton, LastPageButton],
                  "Squares8thPage4": [NextPageButton, LastPageButton],
                  "Squares8thPage5": [NextPageButton, LastPageButton],
                  "Squares8thPage6": [NextPageButton, LastPageButton],
                  "Squares8thPage7": [NextPageButton, LastPageButton],
                  "Squares8thPage8": [NextPageButton, LastPageButton],
                  "Squares8thPage9": [NextPageButton, LastPageButton],
                  "Squares8thPage10": [NextPageButton, LastPageButton],
                  "Squares8thPage11": [NextPageButton, LastPageButton],
                  "Squares8thPage12": [NextPageButton, LastPageButton],
                  "Squares8thPage13": [NextPageButton, LastPageButton],
                  "Squares8thPage14": [NextPageButton, LastPageButton],
                  "Squares8thPage15": [NextPageButton, LastPageButton],
                  "Squares8thPage16": [NextPageButton, LastPageButton],
                  "Squares8thPage17": [NextPageButton, LastPageButton],
                  "Squares8thPage18": [NextPageButton, LastPageButton],
                  "Squares8thPage19": [NextPageButton, LastPageButton],
                  "Squares8thPage20": [NextPageButton, LastPageButton],
                  "Squares8thPage21": [NextPageButton, LastPageButton],
                  "Squares8thPage22": [NextPageButton, LastPageButton],
                  "Squares8thPage23": [NextPageButton, LastPageButton],
                  "Squares8thPage24": [NextPageButton, LastPageButton],
                  "Squares8thPage25": [NextPageButton, LastPageButton],
                  "Squares8thPage26": [LastPageButton],
                  
                  "Cube8thPage1": [NextPageButton],
                  "Cube8thPage2": [NextPageButton, LastPageButton],
                  "Cube8thPage3": [NextPageButton, LastPageButton],
                  "Cube8thPage4": [NextPageButton, LastPageButton],
                  "Cube8thPage5": [NextPageButton, LastPageButton],
                  "Cube8thPage6": [NextPageButton, LastPageButton],
                  "Cube8thPage7": [NextPageButton, LastPageButton],
                  "Cube8thPage8": [NextPageButton, LastPageButton],
                  "Cube8thPage9": [NextPageButton, LastPageButton],
                  "Cube8thPage10": [NextPageButton, LastPageButton],
                  "Cube8thPage11": [NextPageButton, LastPageButton],
                  "Cube8thPage12": [NextPageButton, LastPageButton],
                  "Cube8thPage13": [NextPageButton, LastPageButton],
                  "Cube8thPage14": [NextPageButton, LastPageButton],
                  "Cube8thPage15": [NextPageButton, LastPageButton],
                  "Cube8thPage16": [NextPageButton, LastPageButton],
                  "Cube8thPage17": [NextPageButton, LastPageButton],
                  "Cube8thPage18": [LastPageButton]}

def disableButtons(buttonsOnPage):
    for selectedButton in buttonsOnPage:
        if selectedButton is None:
            break
        else:
            selectedButton.setEnable(False)

#%% Implementation
run = True
while run:
    redrawWindow()
    pygame.display.update()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        # print(pos)
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if StudyButton.isOver(pos):
                oldPage = page
                page = "StudyPage"
                disableButtons(buttonsOnAPage[oldPage])
            
            elif BackButton.isOver(pos):
                #print ("back button pressed. Current page: ", page)
                if page in backList[1]:
                    oldPage = page
                    page = "StartPage"
                    disableButtons(buttonsOnAPage[oldPage])
                elif page in backList[2]:
                    oldPage = page
                    page = "StudyPage"
                    disableButtons(buttonsOnAPage[oldPage])
                elif page in backList[3]:
                    oldPage = page
                    page = "5thStdPage"
                    disableButtons(buttonsOnAPage[oldPage])
                elif page in backList[4]:
                    oldPage = page
                    page = "5thStdPage"
                    disableButtons(buttonsOnAPage[oldPage])
                elif page in backList[5]:
                    oldPage = page
                    page = "6thStdPage"
                    disableButtons(buttonsOnAPage[oldPage])
                elif page in backList[6]:
                    oldPage = page
                    page = "6thStdPage"
                    disableButtons(buttonsOnAPage[oldPage])
                elif page in backList[7]:
                    oldPage = page
                    page = "7thStdPage"
                    disableButtons(buttonsOnAPage[oldPage])
                elif page in backList[8]:
                    oldPage = page
                    page = "7thStdPage"
                    disableButtons(buttonsOnAPage[oldPage])
                elif page in backList[9]:
                    oldPage = page
                    page = "8thStdPage"
                    disableButtons(buttonsOnAPage[oldPage])
                elif page in backList[10]:
                    oldPage = page
                    page = "8thStdPage"
                    disableButtons(buttonsOnAPage[oldPage])
                #print ("New page: ", page)
            
            elif AboutUsButton.isOver(pos):
                oldPage = page
                page = "AboutUsPage"
                disableButtons(buttonsOnAPage[oldPage])
            
            elif Std5Button.isOver(pos):
                oldPage = page
                page = "5thStdPage"
                disableButtons(buttonsOnAPage[oldPage])
            
            elif Integer5thButton.isOver(pos):
                oldPage = page
                page = "Integers5thStdPage1"
                disableButtons(buttonsOnAPage[oldPage])
            
            elif Std6Button.isOver(pos):
                oldPage = page
                page = "6thStdPage"
                disableButtons(buttonsOnAPage[oldPage])
            
            elif Std7Button.isOver(pos):
                oldPage = page
                #print ("Std7 button pressed")
                page = "7thStdPage"
                disableButtons(buttonsOnAPage[oldPage])
            
            elif Std8Button.isOver(pos):
                oldPage = page
                page = "8thStdPage"
                disableButtons(buttonsOnAPage[oldPage])
            
            elif NextPageButton.isOver(pos):
                oldPage = page
                if page in backList[3]:
                    turnToNextPageForNotes(backList[3])
                elif page in backList[4]:
                    turnToNextPageForNotes(backList[4])
                elif page in backList[5]:
                    turnToNextPageForNotes(backList[5])
                elif page in backList[6]:
                    turnToNextPageForNotes(backList[6])
                elif page in backList[7]:
                    turnToNextPageForNotes(backList[7])
                elif page in backList[8]:
                    turnToNextPageForNotes(backList[8])
                elif page in backList[9]:
                    turnToNextPageForNotes(backList[9])
                elif page in backList[10]:
                    turnToNextPageForNotes(backList[10])
                disableButtons(buttonsOnAPage[oldPage])
            
            elif LastPageButton.isOver(pos):
                oldPage = page
                if page in backList[3]:
                    turnToLastPageForNotes(backList[3])
                elif page in backList[4]:
                    turnToLastPageForNotes(backList[4])
                elif page in backList[5]:
                    turnToLastPageForNotes(backList[5])
                elif page in backList[6]:
                    turnToLastPageForNotes(backList[6])
                elif page in backList[7]:
                    turnToLastPageForNotes(backList[7])
                elif page in backList[8]:
                    turnToLastPageForNotes(backList[8])
                elif page in backList[9]:
                    turnToLastPageForNotes(backList[9])
                elif page in backList[10]:
                    turnToLastPageForNotes(backList[10])
                disableButtons(buttonsOnAPage[oldPage])
            
            elif Fractions5thButton.isOver(pos):
                oldPage = page
                page = "Fractions5thStdPage1"
                disableButtons(buttonsOnAPage[oldPage])
            
            elif Mensuration6thButton.isOver(pos):
                oldPage = page
                page = "Mensuration6thStdPage1"
                disableButtons(buttonsOnAPage[oldPage])
            
            elif Algebra6thButton.isOver(pos):
                oldPage = page
                page = "Algebra6thStdPage1"
                disableButtons(buttonsOnAPage[oldPage])
            
            elif Ratio7thButton.isOver(pos):
                oldPage = page
                page = "Ratio7thStdPage1"
                disableButtons(buttonsOnAPage[oldPage])
            
            elif Exponents7thButton.isOver(pos):
                oldPage = page
                page = "Exponents7thPage1"
                disableButtons(buttonsOnAPage[oldPage])
            
            elif Square8thButton.isOver(pos):
                oldPage = page
                page = "Squares8thPage1"
                disableButtons(buttonsOnAPage[oldPage])
            
            elif Cube8thButton.isOver(pos):
                oldPage = page
                page = "Cube8thPage1"
                disableButtons(buttonsOnAPage[oldPage])
        
        elif event.type == pygame.MOUSEMOTION:
            # green Buttons
            if StudyButton.isOver(pos):
                StudyButton.color = dark_green
            else:
                StudyButton.color = green
            
            if AboutUsButton.isOver(pos):
                AboutUsButton.color = dark_green
            else:
                AboutUsButton.color = green
            
            # red Buttons
            if BackButton.isOver(pos):
                BackButton.color = dark_red
            else:
                BackButton.color = red
            
            if Std5Button.isOver(pos):
                Std5Button.color = dark_green
            else:
                Std5Button.color = green
            
            if Std6Button.isOver(pos):
                Std6Button.color = dark_green
            else:
                Std6Button.color = green
            
            if Std7Button.isOver(pos):
                Std7Button.color = dark_green
            else:
                Std7Button.color = green
            
            if Std8Button.isOver(pos):
                Std8Button.color = dark_green
            else:
                Std8Button.color = green
            
            if Integer5thButton.isOver(pos):
                Integer5thButton.color = dark_green
            else:
                Integer5thButton.color = green
            
            if Fractions5thButton.isOver(pos):
                Fractions5thButton.color = dark_green
            else:
                Fractions5thButton.color = green
            
            if Mensuration6thButton.isOver(pos):
                Mensuration6thButton.color = dark_green
            else:
                Mensuration6thButton.color = green
            
            if Algebra6thButton.isOver(pos):
                Algebra6thButton.color = dark_green
            else:
                Algebra6thButton.color = green
            
            if Exponents7thButton.isOver(pos):
                Exponents7thButton.color = dark_green
            else:
                Exponents7thButton.color = green
            
            if Ratio7thButton.isOver(pos):
                Ratio7thButton.color = dark_green
            else:
                Ratio7thButton.color = green
            
            if Square8thButton.isOver(pos):
                Square8thButton.color = dark_green
            else:
                Square8thButton.color = green
            
            if Cube8thButton.isOver(pos):
                Cube8thButton.color = dark_green
            else:
                Cube8thButton.color = green
            
            # blue Buttons
            if LastPageButton.isOver(pos):
                LastPageButton.color = dark_blue
            else:
                LastPageButton.color = blue
            
            if NextPageButton.isOver(pos):
                NextPageButton.color = dark_blue
            else:
                NextPageButton.color = blue
