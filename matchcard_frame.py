from tkinter import ttk
import tkinter as tk


class MatchCard():
    
    def __init__(self, team_num):
        
        #プロパティ
        self.team_num = team_num
        
        self.team_name = "teamname"
        
        self.senpo = "senpo"
        self.jiho = "jiho"
        self.taisyo = "taisyo"
        
        self.senpo_point = 0
        self.jiho_point = 0
        self.taisyo_point = 0
        
        self.team_point = 0
        self.team_winlose = ""
        
        self.win_label_senpo = None
        self.win_label_jiho = None
        self.win_label_taisyo = None
        

    
    #メソッド
    def add_team_name_card(self, parent, row, column):
        label = ttk.Label(parent, text=self.team_name)
        label.grid(row=row, column=column)


    def add_player_name_card(self, parent, row, column):
        
        #ボタンを押すと色ラベル表示トグル、senpojihotaisyoそれぞれのポイントトグル、チームポイント足し引き
        def win_button_clicked(num):
            
            #左側チームボタンが押された場合
            if self.team_num == 1:
                if num == 0:
                    if self.senpo_point == 0:
                        #senpo_point + 1
                        self.senpo_point = 1
                        #winラベル出現
                        self.win_label_senpo = ttk.Label(parent, text="win", foreground="white", background="blue")
                        self.win_label_senpo.grid(row=row+num, column=column+1)
                        #チームポイント + 1
                        self.team_point += 1
                    else:
                        #senpo_point = 0
                        self.senpo_point = 0
                        self.win_label_senpo.destroy()
                        self.team_point -= 1
                
                elif num == 1:
                    if self.jiho_point == 0:
                        self.jiho_point = 1
                        self.win_label_jiho = ttk.Label(parent, text="win", foreground="white", background="blue")
                        self.win_label_jiho.grid(row=row+num, column=column+1)
                        self.team_point += 1
                    else:
                        self.jiho_point = 0
                        self.win_label_jiho.destroy()
                        self.team_point -= 1
                        
                elif num == 2:
                    if self.taisyo_point == 0:
                        self.taisyo_point = 1
                        self.win_label_taisyo = ttk.Label(parent, text="win", foreground="white", background="blue")
                        self.win_label_taisyo.grid(row=row+num, column=column+1)
                        self.team_point += 1
                    else:
                        self.taisyo_point = 0
                        self.win_label_taisyo.destroy()
                        self.team_point -= 1


            #右側チームボタンが押された場合
            if self.team_num == 2:
                if num == 0:
                    if self.senpo_point == 0:
                        self.senpo_point = 1
                        self.win_label_senpo = ttk.Label(parent, text="win", foreground="white", background="red")
                        self.win_label_senpo.grid(row=row+num, column=column-1)
                        self.team_point += 1
                    else:
                        self.senpo_point = 0
                        self.win_label_senpo.destroy()
                        self.team_point -= 1
                
                elif num == 1:
                    if self.jiho_point == 0:
                        self.jiho_point = 1
                        self.win_label_jiho = ttk.Label(parent, text="win", foreground="white", background="red")
                        self.win_label_jiho.grid(row=row+num, column=column-1)
                        self.team_point += 1
                    else:
                        self.jiho_point = 0
                        self.win_label_jiho.destroy()
                        self.team_point -= 1
                        
                elif num == 2:
                    if self.taisyo_point == 0:
                        self.taisyo_point = 1
                        self.win_label_taisyo = ttk.Label(parent, text="win", foreground="white", background="red")
                        self.win_label_taisyo.grid(row=row+num, column=column-1)
                        self.team_point += 1
                    else:
                        self.taisyo_point = 0
                        self.win_label_taisyo.destroy()
                        self.team_point -= 1

        button_senpo = ttk.Button(parent, text=self.senpo, command=lambda: win_button_clicked(num=0))
        button_jiho = ttk.Button(parent, text=self.jiho, command=lambda: win_button_clicked(num=1))
        button_taisyo = ttk.Button(parent, text=self.taisyo, command=lambda: win_button_clicked(num=2))
        button_senpo.grid(row=row, column=column)
        button_jiho.grid(row=row+1, column=column)
        button_taisyo.grid(row=row+2, column=column)


    def add_spinbox(self, parent, row, column):
        spin1 = ttk.Spinbox(parent, increment=1, from_=0, to=500, width=5)
        spin2 = ttk.Spinbox(parent, increment=1, from_=0, to=500, width=5)
        spin3 = ttk.Spinbox(parent, increment=1, from_=0, to=500, width=5)
        spin1.grid(row=row, column=column)
        spin2.grid(row=row+1, column=column)
        spin3.grid(row=row+2, column=column)
        
    
    #自身のプロパティにセットする関数
    def set_property(self, team_name, senpo, jiho, taisyo):
        self.team_name = team_name
        self.senpo = senpo
        self.jiho = jiho
        self.taisyo = taisyo



class SmashMatchCard(ttk.Frame):
    def __init__(self, parent, team1_class, team2_class):
        super().__init__(parent)
        
        #セル間の距離を設定
        #self.grid_columnconfigure(0, minsize=100)
        self.grid_rowconfigure(1, pad=50)
        self.grid_rowconfigure(2, pad=30)
        self.grid_rowconfigure(3, pad=30)
        self.grid_rowconfigure(4, pad=30)
        self.grid_rowconfigure(5, pad=30)
        
        ##
        
        self.team1class = team1_class
        self.team2class = team2_class
        
        #
        team1_name = self.team1class.team_name
        team1_senpo = self.team1class.suma_senpo_name
        team1_jiho = self.team1class.suma_jiho_name
        team1_taisyo = self.team1class.suma_taisyo_name
        
        team2_name = self.team2class.team_name
        team2_senpo = self.team2class.suma_senpo_name
        team2_jiho = self.team2class.suma_jiho_name
        team2_taisyo = self.team2class.suma_taisyo_name

        
        match_card1 = MatchCard(team_num=1)
        match_card1.set_property(team_name=team1_name, senpo=team1_senpo, jiho=team1_jiho, taisyo=team1_taisyo)
        match_card1.add_team_name_card(self, row=1, column=1)
        match_card1.add_player_name_card(self, row=2, column=1)
        
        match_card2 = MatchCard(team_num=2)
        match_card2.set_property(team_name=team2_name, senpo=team2_senpo, jiho=team2_jiho, taisyo=team2_taisyo)
        match_card2.add_team_name_card(self, row=1, column=5)
        match_card2.add_player_name_card(self, row=2, column=5)
        
        label_winlose = ttk.Label(self, text=" vs ")
        label_winlose.grid(row=1, column=3)
        
        label_senpo = ttk.Label(self, text="先鋒戦")
        label_jiho = ttk.Label(self, text="次鋒戦")
        label_taisyo = ttk.Label(self, text="大将戦")
        label_senpo.grid(row=2, column=3)
        label_jiho.grid(row=3, column=3)
        label_taisyo.grid(row=4, column=3)
        
        #決着ボタン
        def tamesi():
            # 3マッチの結果を入れた場合のみ
            if match_card1.team_point + match_card2.team_point == 3:
                #左側が２または３ポイントとっていた場合
                if match_card1.team_point == 2 or match_card1.team_point == 3:
                    #マッチカードオブジェの結果にそれぞれ代入
                    match_card1.team_winlose = "win"
                    match_card2.team_winlose = "lose"
                    team1_win_label.grid(row=1, column=2)
                    team2_win_label.grid_forget()
                else:#右側が２または３ポイントとっていた場合
                    match_card1.team_winlose = "lose"
                    match_card2.team_winlose = "win"
                    team2_win_label.grid(row=1, column=4)
                    team1_win_label.grid_forget()
            else:#3マッチじゃないとき（操作のミス等）
                team2_win_label.grid_forget()
                team1_win_label.grid_forget()
                match_card1.team_winlose = ""
                match_card2.team_winlose = ""
        team1_win_label = ttk.Label(self, text="WIN", background="blue")
        team2_win_label = ttk.Label(self, text="WIN", background="red")
        kettyaku_btn = ttk.Button(self, text="決着", command=tamesi)
        kettyaku_btn.grid(row=5, column=2)
        
        #スピンボックス
        match_card1.add_spinbox(self, row=2, column=0)
        match_card2.add_spinbox(self, row=2, column=7)
        
        
        #仮ボタン
        kali_btn = ttk.Button(self, text="kali")
        kali_btn.grid(row=5, column=4)


'''
#スト６マッチカードフレーム
class Suto6MatchCard(SmashMatchCard):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        '''


class MatchCard_window(tk.Toplevel):
    def __init__(self, parent, team1class, team2class):
        super().__init__(parent)
        self.title("別ウィンドウ")
        self.geometry("960x540")
        
        # フレームを作成して配置
        #ウィンドウいっぱいのフレーム
        main_frame = ttk.Frame(self)
        main_frame.pack(fill="both", expand=True)
        
        center_frame = SmashMatchCard(main_frame, team1_class=team1class, team2_class=team2class)
        center_frame.place(relx=0.5, rely=0.5, anchor="c")