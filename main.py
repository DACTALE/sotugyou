#すますとそれぞれのマッチカードフレームを継承からインスタンスにする

#標準ライブラリインポート
import tkinter as tk
from tkinter import ttk
import ctypes

#サードパーティーライブラリインポート
from ttkthemes import ThemedTk

#自作ライブラリインポート
#from utils.toggle_decoration_subwindow import toggle_decoration
from utils.add_image import add_image_obj
from matchcard_frame import MatchCard_window
from data import Data


#メインウィンドウ
class App(ThemedTk):
    def __init__(self):
        super().__init__(theme="adapta")
        self.title("レクアプリ")
        self.geometry("960x540")

        # フレームを作成して配置
        #ウィンドウいっぱいのフレーム
        main_frame = ttk.Frame(self)
        main_frame.pack(fill="both", expand=True)
        
        center_frame = ttk.Frame(main_frame)
        center_frame.place(relx=0.5, rely=0.5, anchor="c")

        # ページを作成
        self.pages = {}
        for F in (StartPage, 
                  SmashTournament, 
                  Suto6Tournament,
                  MaricaRank, 
                  Page2):
            page = F(center_frame, self)
            self.pages[F] = page
            page.grid(row=0, column=0, sticky="nsew")
            
        # 初期ページを表示
        self.show_page(StartPage)

    def show_page(self, page_class):
        page = self.pages[page_class]
        page.tkraise()
        
    
    ##
    def show_match_card(self, team1_class, team2_class):
        # SmashMatchCardのインスタンスを作成し、別ウィンドウとして表示
        match_card = MatchCard_window(self, team1class=team1_class, team2class=team2_class)


class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = ttk.Label(self, text="スタートページ")
        label.pack(pady=10)

        button1 = ttk.Button(self, text="スマブラ", command=lambda: controller.show_page(SmashTournament))
        button1.pack()
        
        goto_suto6_btn = ttk.Button(self, text="スト６", command=lambda: controller.show_page(Suto6Tournament))
        goto_suto6_btn.pack()
        
        goto_marica_btn = ttk.Button(self, text="マリオカート", command=lambda: controller.show_page(MaricaRank))
        goto_marica_btn.pack()
        
        button2 = ttk.Button(self, text="ページ2へ", command=lambda: controller.show_page(Page2))
        button2.pack()












#############################################################################
#スマブラトーナメント画面
class SmashTournament(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)


        #セル間の距離を設定
        self.grid_columnconfigure(0, pad=30)
        self.grid_columnconfigure(2, pad=30)
        self.grid_rowconfigure(0, pad=50)


        title_label = ttk.Label(self, text="スマブラページ")
        title_label.grid(row=0, column=0)

        startpage_button = ttk.Button(self, text="スタートページへ",
                           command=lambda: controller.show_page(StartPage))
        startpage_button.grid(row=0, column=1)


        #インスタンス変数定義
        # self.teamA_name = data.teamA_name
        # self.teamB_name = data.teamB_name
        # self.teamC_name = data.teamC_name
        # self.teamD_name = data.teamD_name
        

        #マッチカード各所へ
        def add_frame_in_goto_matchcard_btn(row, column, team1name, team2name):
            
            ##
            def name_obj_return(team_name):

                team_info_class = None
                
                if team_name == data.team_a_class.team_name:
                    team_info_class = data.team_a_class
                    print("akura")
                if team_name == data.team_b_class.team_name:
                    team_info_class = data.team_b_class
                    print("bkura")
                if team_name == data.team_c_class.team_name:
                    team_info_class = data.team_c_class
                if team_name == data.team_d_class.team_name:
                    team_info_class = data.team_d_class
                
                return team_info_class
            
            ##
            team1class = name_obj_return(team1name)
            team2class = name_obj_return(team2name)
            
            match_frame = ttk.Frame(self)
            match_frame.grid(row=row, column=column, padx=0, pady=0)
            match_team_button1 = ttk.Button(match_frame, text=team1name, command=lambda: controller.show_match_card(team1_class=team1class, team2_class=team2class))
            match_team_button2 = ttk.Button(match_frame, text=team2name, command=lambda: controller.show_match_card(team1_class=team1class, team2_class=team2class))
            match_team_button1.pack(side=tk.TOP)
            match_team_button2.pack(side=tk.TOP)
            

                
                
        ##1回戦
        add_frame_in_goto_matchcard_btn(row=1, column=0, team1name=data.suma_class.suma_match1_team_name_1, team2name=data.suma_class.suma_match1_team_name_2)
        
        add_frame_in_goto_matchcard_btn(row=3, column=0, team1name=data.suma_class.suma_match2_team_name_1, team2name=data.suma_class.suma_match1_team_name_2)
        
        ##決勝3決
        add_frame_in_goto_matchcard_btn(row=2, column=2, team1name="", team2name="")
        
        add_frame_in_goto_matchcard_btn(row=3, column=2, team1name="", team2name="")


        #画像オブジェクトを作成
        go_to_kessyou_img_obj = add_image_obj(image_name="gotokessyou.png", width=120, height=120)
        # ラベルを作成し、画像を設定
        go_to_kessyou_img = tk.Label(self, image=go_to_kessyou_img_obj)
        go_to_kessyou_img.image = go_to_kessyou_img_obj # ガベージコレクションを防ぐ
        # ラベルをgridで配置
        go_to_kessyou_img.grid(row=2, column=1)
        
        #画像オブジェクトを作成
        top_img_obj = add_image_obj(image_name="top.png", width=120, height=120)
        # ラベルを作成し、画像を設定
        top_image = tk.Label(self, image=top_img_obj)
        top_image.image = top_img_obj # ガベージコレクションを防ぐ
        # ラベルをgridで配置
        top_image.grid(row=1, column=1)
        
        #画像オブジェクトを作成
        bottom_img_obj = add_image_obj(image_name="bottom.png", width=120, height=120)
        # ラベルを作成し、画像を設定
        bottom_img = tk.Label(self, image=bottom_img_obj)
        bottom_img.image = bottom_img_obj # ガベージコレクションを防ぐ
        # ラベルをgridで配置
        bottom_img.grid(row=3, column=1)
########################################################
########################################################
#スマブラマッチカード画面４つ
'''
class SmashMatchCard1(SmashMatchCard):
        def __init__(self, parent, controller):
            super().__init__(parent, controller)
            
            #トーナメント画面に戻るボタン
            tournament_button = ttk.Button(self, text="トーナメントへ", command=lambda: controller.show_page(SmashTournament))
            tournament_button.grid(row=5, column=4)
            
            #なんのページがわかるラベル
            this_page_name_label = ttk.Label(self, text="SmashMatchCard1")
            this_page_name_label.grid(row=5, column=0)
            
class SmashMatchCard2(SmashMatchCard):
        def __init__(self, parent, controller):
            super().__init__(parent, controller)
            
            #トーナメント画面に戻るボタン
            tournament_button = ttk.Button(self, text="トーナメントへ", command=lambda: controller.show_page(SmashTournament))
            tournament_button.grid(row=5, column=4)
            
            #なんのページがわかるラベル
            this_page_name_label = ttk.Label(self, text="SmashMatchCard2")
            this_page_name_label.grid(row=5, column=0)
            
class SmashMatchCard3(SmashMatchCard):
        def __init__(self, parent, controller):
            super().__init__(parent, controller)
            
            #トーナメント画面に戻るボタン
            tournament_button = ttk.Button(self, text="トーナメントへ", command=lambda: controller.show_page(SmashTournament))
            tournament_button.grid(row=5, column=4)
            
            #なんのページがわかるラベル
            this_page_name_label = ttk.Label(self, text="SmashMatchCard3")
            this_page_name_label.grid(row=5, column=0)
            
class SmashMatchCard4(SmashMatchCard):
        def __init__(self, parent, controller):
            super().__init__(parent, controller)
            
            #トーナメント画面に戻るボタン
            tournament_button = ttk.Button(self, text="トーナメントへ", command=lambda: controller.show_page(SmashTournament))
            tournament_button.grid(row=5, column=4)
            
            #なんのページがわかるラベル
            this_page_name_label = ttk.Label(self, text="SmashMatchCard4")
            this_page_name_label.grid(row=5, column=0)
'''
############################################################################












############################################################################
#スト６トーナメント画面
class Suto6Tournament(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        
        #セル間の距離を設定
        self.grid_columnconfigure(0, pad=30)
        self.grid_columnconfigure(2, pad=30)
        self.grid_rowconfigure(0, pad=50)
        

        title_label = ttk.Label(self, text="スト６ページ")
        title_label.grid(row=0, column=0)

        startpage_button = ttk.Button(self, text="スタートページへ",
                           command=lambda: controller.show_page(StartPage))
        startpage_button.grid(row=0, column=1)
        
        
        #インスタンス変数定義
        # self.teamA_name = data.team_a_class.team_name
        # self.teamB_name = data.team_b_class.team_name
        # self.teamC_name = data.team_c_class.team_name
        # self.teamD_name = data.team_d_class.team_name
        

        #マッチカード各所へ
        def add_frame_in_goto_matchcard_btn(row, column, team1name, team2name, jump_page):
            match_frame = ttk.Frame(self)
            match_frame.grid(row=row, column=column)
            match_team_button1 = ttk.Button(match_frame, text=team1name, command=lambda: controller.show_page(jump_page))
            match_team_button2 = ttk.Button(match_frame, text=team2name, command=lambda: controller.show_page(jump_page))
            match_team_button1.pack(side=tk.TOP)
            match_team_button2.pack(side=tk.TOP)
        
        #add_frame_in_goto_matchcard_btn(row=1, column=0, team1name=self.teamA_name, team2name=self.teamB_name)
        
        #add_frame_in_goto_matchcard_btn(row=3, column=0, team1name=self.teamC_name, team2name=self.teamD_name)
        
        #add_frame_in_goto_matchcard_btn(row=2, column=2, team1name="", team2name="")
        
        #add_frame_in_goto_matchcard_btn(row=3, column=2, team1name="", team2name="")


        #画像オブジェクトを作成
        go_to_kessyou_img_obj = add_image_obj(image_name="gotokessyou.png", width=120, height=120)
        # ラベルを作成し、画像を設定
        go_to_kessyou_img = tk.Label(self, image=go_to_kessyou_img_obj)
        go_to_kessyou_img.image = go_to_kessyou_img_obj # ガベージコレクションを防ぐ
        # ラベルをgridで配置
        go_to_kessyou_img.grid(row=2, column=1)
        
        #画像オブジェクトを作成
        top_img_obj = add_image_obj(image_name="top.png", width=120, height=120)
        # ラベルを作成し、画像を設定
        top_image = tk.Label(self, image=top_img_obj)
        top_image.image = top_img_obj # ガベージコレクションを防ぐ
        # ラベルをgridで配置
        top_image.grid(row=1, column=1)
        
        #画像オブジェクトを作成
        bottom_img_obj = add_image_obj(image_name="bottom.png", width=120, height=120)
        # ラベルを作成し、画像を設定
        bottom_img = tk.Label(self, image=bottom_img_obj)
        bottom_img.image = bottom_img_obj # ガベージコレクションを防ぐ
        # ラベルをgridで配置
        bottom_img.grid(row=3, column=1)
########################################################
########################################################
#スト6マッチカード画面４つ
'''
class Suto6MatchCard1(Suto6MatchCard):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
        #なんのページがわかるラベル
        this_page_name_label = ttk.Label(self, text="Suto6MatchCard1")
        this_page_name_label.grid(row=5, column=0)
        
        goto_suto6_btn = ttk.Button(self, text="トーナメントへ", command=lambda: controller.show_page(Suto6Tournament))
        goto_suto6_btn.grid(row=5, column=4)
        
class Suto6MatchCard2(Suto6MatchCard):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
        #なんのページがわかるラベル
        this_page_name_label = ttk.Label(self, text="Suto6MatchCard2")
        this_page_name_label.grid(row=5, column=0)
        
        goto_suto6_btn = ttk.Button(self, text="トーナメントへ", command=lambda: controller.show_page(Suto6Tournament))
        goto_suto6_btn.grid(row=5, column=4)
        
class Suto6MatchCard3(Suto6MatchCard):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
        #なんのページがわかるラベル
        this_page_name_label = ttk.Label(self, text="Suto6MatchCard3")
        this_page_name_label.grid(row=5, column=0)
        
        goto_suto6_btn = ttk.Button(self, text="トーナメントへ", command=lambda: controller.show_page(Suto6Tournament))
        goto_suto6_btn.grid(row=5, column=4)

class Suto6MatchCard4(Suto6MatchCard):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
        #なんのページがわかるラベル
        this_page_name_label = ttk.Label(self, text="Suto6MatchCard4")
        this_page_name_label.grid(row=5, column=0)
        
        goto_suto6_btn = ttk.Button(self, text="トーナメントへ", command=lambda: controller.show_page(Suto6Tournament))
        goto_suto6_btn.grid(row=5, column=4)
'''
##################################################################












##################################################################
#マリカ順位入力フレーム

class MaricaRank(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        
        startpage_button = ttk.Button(self, text="スタートページへ", command=lambda: controller.show_page(StartPage))
        startpage_button.grid(row=2, column=5)
        
        
         #セル間の距離を設定
        self.grid_columnconfigure(0, minsize=100)
        self.grid_columnconfigure(1, minsize=100)
        self.grid_columnconfigure(2, minsize=100)
        self.grid_columnconfigure(3, minsize=100)
        self.grid_columnconfigure(4, minsize=100)
        self.grid_columnconfigure(5, minsize=250)
        self.grid_rowconfigure(0, pad=25)
        self.grid_rowconfigure(2, pad=300)
        
        
        ##チーム名ラベル
        self.teamA_name = data.team_a_class.team_name
        self.teamB_name = data.team_b_class.team_name
        self.teamC_name = data.team_c_class.team_name
        self.teamD_name = data.team_d_class.team_name
        
        self.teamA_name_lbl = ttk.Label(self, text=self.teamA_name)
        self.teamB_name_lbl = ttk.Label(self, text=self.teamB_name)
        self.teamC_name_lbl = ttk.Label(self, text=self.teamC_name)
        self.teamD_name_lbl = ttk.Label(self, text=self.teamD_name)
        
        self.teamA_name_lbl.grid(row=0, column=1)
        self.teamB_name_lbl.grid(row=0, column=2)
        self.teamC_name_lbl.grid(row=0, column=3)
        self.teamD_name_lbl.grid(row=0, column=4)
        
        
        ##カウンターボタン
        
        self.counterA = tk.IntVar(value=0)
        self.counterB = tk.IntVar(value=0)
        self.counterC = tk.IntVar(value=0)
        self.counterD = tk.IntVar(value=0)
        
        self.rank_counter = 0
        
        def rank_btn_click(click_btn):
            if click_btn == "teamA_rank":
                if not self.rank_counter == 4 and self.counterA.get() == 0:
                    self.rank_counter += 1
                    self.counterA.set(self.rank_counter)
            elif click_btn == "teamB_rank":
                if not self.rank_counter == 4 and self.counterB.get() == 0:
                    self.rank_counter += 1
                    self.counterB.set(self.rank_counter)
            elif click_btn == "teamC_rank":
                if not self.rank_counter == 4 and self.counterC.get() == 0:
                    self.rank_counter += 1
                    self.counterC.set(self.rank_counter)
            elif click_btn == "teamD_rank":
                if not self.rank_counter == 4 and self.counterD.get() == 0:
                    self.rank_counter += 1
                    self.counterD.set(self.rank_counter)
        
        self.teamA_rank = ttk.Button(self, textvariable=self.counterA, command=lambda: rank_btn_click("teamA_rank"))
        self.teamB_rank = ttk.Button(self, textvariable=self.counterB, command=lambda: rank_btn_click("teamB_rank"))
        self.teamC_rank = ttk.Button(self, textvariable=self.counterC, command=lambda: rank_btn_click("teamC_rank"))
        self.teamD_rank = ttk.Button(self, textvariable=self.counterD, command=lambda: rank_btn_click("teamD_rank"))
        
        self.teamA_rank.grid(row=1, column=1)
        self.teamB_rank.grid(row=1, column=2)
        self.teamC_rank.grid(row=1, column=3)
        self.teamD_rank.grid(row=1, column=4)
        
        # def baka():
        #     print(str(self.counterA.get()) + " : " + str(self.counterB.get()) + " : " + str(self.counterC.get()) + " : " + str(self.counterD.get()))
        # self.tamesi = ttk.Button(self, command=baka)
        # self.tamesi.grid(row=1, column=5)
        
        ##カウンターリセットボタン
         #リセットボタンで入力した順位をリセットする関数
        def rank_reset_click():
            #カウンターリセット
            self.rank_counter = 0
            #各チームカウンターリセット
            self.counterA.set(0)
            self.counterB.set(0)
            self.counterC.set(0)
            self.counterD.set(0)
        self.counter_reset_btn = ttk.Button(self, text="リセット", command=rank_reset_click)
        self.counter_reset_btn.grid(row=1, column=5)
        

##################################################################










class Page2(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = ttk.Label(self, text="ページ2")
        label.pack()

        button = ttk.Button(self, text="スタートページへ",
                           command=lambda: controller.show_page(StartPage))
        button.pack()


if __name__ == "__main__":
    
    #set the system's DPI to app.
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    
    data = Data("data.xlsx")
    app = App()
    app.mainloop()