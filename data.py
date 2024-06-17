import openpyxl


class Data():
    def __init__(self, use_workbook):
        
        
        ##エクセルファイルを開く
        self.workbook = openpyxl.load_workbook(use_workbook)
        
        ###シートを選択,定義
        self.sheet_teaminfo = self.workbook["team_info"]
        self.sheet_teamA_member = self.workbook["teamA_member"]
        self.sheet_teamB_member = self.workbook["teamB_member"]
        self.sheet_teamC_member = self.workbook["teamC_member"]
        self.sheet_teamD_member = self.workbook["teamD_member"]
        self.sheet_suma = self.workbook["スマブラ"]
        self.sheet_suto6 = self.workbook["スト6"]
        
        
        ###各チーム情報インスタンス定義
        self.team_a_class = self.TeamA(self)
        self.team_b_class = self.TeamB(self)
        self.team_c_class = self.TeamC(self)
        self.team_d_class = self.TeamD(self)
        
        ###各ゲーム情報インスタンス定義
        self.suma_class = self.Suma(self)
        
        
        ###インスタンス変数の定義（ここにエクセルからすべてのデータを持ってくる）

        
        ##スト６トーナメント対戦相手
        #マッチ１
        self.suto6_match1_1 = ""
        self.suto6_match1_2 = ""
        #マッチ２
        self.suto6_match2_1 = ""
        self.suto6_match2_2 = ""
        #マッチ３（決勝）
        self.suto6_match3_1 = ""
        self.suto6_match3_2 = ""
        #マッチ４（３決）
        self.suto6_match4_1 = ""
        self.suto6_match4_2 = ""
        
        
        
        ###アプリ起動時にインスタンス変数にセットする
        #self.initial_acquisition()
        
        
        
        
        
        
        
        
        
        
############################################################################################################
    ###チームのベースクラス
    class TeamInfo:
        def __init__(self, outer): #内部クラスのインスタンスから、外側のクラスのインスタンスにアクセスしないため、外側クラスのインスタンスは受け取らない
            
            ##各チームクラスで変更しない固定の変数
            #外側クラスのインスタンスを保持
            self.outer = outer
            
            ##各チームクラスで変更する変数
            #継承先で使うチームのシートをそれぞれ再定義する。将来的にポイント管理のシートも同じことするかも
            self.team_sheet = None
            
            #チーム名があるセル
            self.my_team_name_where = ""
            
            self.team_name = ""
            self.team_member_name_list = []
            
            self.suma_senpo_name = ""
            self.suma_jiho_name = ""
            self.suma_taisyo_name = ""
            
            self.suto6_senpo_name = ""
            self.suto6_jiho_name = ""
            self.suto6_taisyo_name = ""
            
            
        #最初関数
        def set_team_info_initial(self, my_team_name_where, team_sheet):
            #チーム名
            self.team_name = self.outer.sheet_teaminfo[my_team_name_where].value
            #チームメンバー一覧リスト（使う予定ないから後回し）
            
            #スマブラ出場者
            member_list = self.outer.search_member(sheet=self.team_sheet, suma_or_suto6="suma")
            self.suma_senpo_name = member_list[0]
            self.suma_jiho_name = member_list[1]
            self.suma_taisyo_name = member_list[2]
            
            #スト6出場者
            member_list = self.outer.search_member(sheet=self.team_sheet, suma_or_suto6="suto6")
            self.suto6_senpo_name = member_list[0]
            self.suto6_jiho_name = member_list[1]
            self.suto6_taisyo_name = member_list[2]
            
            
    class TeamA(TeamInfo):
        def __init__(self, outer):
            super().__init__(outer)
            ##
            #チーム名セットで使うセル
            self.my_team_name_where = "B2"
            #チームメンバーシートをそれぞれ指定
            self.team_sheet = self.outer.sheet_teamA_member
            
            ##最初セット関数
            self.set_team_info_initial(my_team_name_where=self.my_team_name_where,
                                       team_sheet=self.team_sheet)

    class TeamB(TeamInfo):
        def __init__(self, outer):
            super().__init__(outer)
            ##
            #チーム名セットで使うセル
            self.my_team_name_where = "B3"
            #チームメンバーシートをそれぞれ指定
            self.team_sheet = self.outer.sheet_teamB_member
            
            ##最初セット関数
            self.set_team_info_initial(my_team_name_where=self.my_team_name_where,
                                       team_sheet=self.team_sheet)
            
    class TeamC(TeamInfo):
        def __init__(self, outer):
            super().__init__(outer)
            
            self.my_team_name_where = "B4"
            #チームメンバーシートをそれぞれ指定
            self.team_sheet = self.outer.sheet_teamC_member
            
            ##
            self.set_team_info_initial(my_team_name_where=self.my_team_name_where,
                                       team_sheet=self.team_sheet)
            
    class TeamD(TeamInfo):
        def __init__(self, outer):
            super().__init__(outer)
            
            self.my_team_name_where = "B5"
            #チームメンバーシートをそれぞれ指定
            self.team_sheet = self.outer.sheet_teamD_member
            ##
            self.set_team_info_initial(my_team_name_where=self.my_team_name_where,
                                       team_sheet=self.team_sheet)
##########################################################################################################          
















########################################################################################
    class Suma:
        def __init__(self, outer):
            
            ###インスタンス変数定義
            ##
            #
            self.outer = outer

            ##スマブラトーナメント対戦相手
            #マッチ１
            self.suma_match1_team_name_1 = ""
            self.suma_match1_team_name_2 = ""
            #マッチ２
            self.suma_match2_team_name_1 = ""
            self.suma_match2_team_name_2 = ""
            #マッチ３（決勝）
            self.suma_match3_team_name_1 = ""
            self.suma_match3_team_name_2 = ""
            #マッチ４（３決）
            self.suma_match4_team_name_1 = ""
            self.suma_match4_team_name_2 = ""
            
            ##スマブラトーナメント結果
            #マッチ1
            self.suma_match1_team1_winlose = ""
            self.suma_match1_team2_winlose = ""
            #マッチ2
            self.suma_match2_team1_winlose = ""
            self.suma_match2_team2_winlose = ""
            #マッチ3
            self.suma_match3_team1_winlose = ""
            self.suma_match3_team2_winlose = ""
            #マッチ4
            self.suma_match4_team1_winlose = ""
            self.suma_match4_team2_winlose = ""
            
            #最初関数
            self.set_suma_info_initial()
            
            
        def set_suma_info_initial(self):
            
            ##スマブラトーナメント対戦相手
            #マッチ１
            self.suma_match1_team_name_1 = self.outer.sheet_suma["A8"].value
            self.suma_match1_team_name_2 = self.outer.sheet_suma["A9"].value
            #マッチ２
            self.suma_match2_team_name_1 = self.outer.sheet_suma["A12"].value
            self.suma_match2_team_name_2 = self.outer.sheet_suma["A13"].value
            #マッチ３（決勝）
            self.suma_match3_team_name_1 = self.outer.sheet_suma["A16"].value
            self.suma_match3_team_name_2 = self.outer.sheet_suma["A17"].value
            #マッチ４（３決）
            self.suma_match4_team_name_1 = self.outer.sheet_suma["A20"].value
            self.suma_match4_team_name_2 = self.outer.sheet_suma["A21"].value
################################################################################################
        
        
        
        
        
        
        
        
        
        
    #Dataクラスメソッド
###############################################################################################
    ###スマ、ストで出場者を検索する関数→インスタンス変数に入れるため###
    def search_member(self, sheet, suma_or_suto6):
        
        #スマブラならB2セルから出場者検索、スト６ならC2
        search_start_row = ""
        if suma_or_suto6 == "suma":
            search_start_row = "B"
        elif suma_or_suto6 == "suto6":
            search_start_row = "C"
            
        #戻り値のリスト
        senpo_jiho_taisyo_list = ["", "", ""]
        
        # サーチスタートセルから下の行を検索
        for i in range(2, 8):
            if sheet[search_start_row + f"{i}"].value == 1:
                senpo_jiho_taisyo_list[0] = sheet["A" + f"{i}"].value
            elif sheet[search_start_row + f"{i}"].value == 2:
                senpo_jiho_taisyo_list[1] = sheet["A" + f"{i}"].value
            elif sheet[search_start_row + f"{i}"].value == 3:
                senpo_jiho_taisyo_list[2] = sheet["A" + f"{i}"].value

        return senpo_jiho_taisyo_list
####################################################################################################


        


if __name__ == "__main__":
    
    data = Data(use_workbook="data.xlsx")
    
    print(data.suma_class.suma_match1_team_name_1)