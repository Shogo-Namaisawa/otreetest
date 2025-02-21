from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'PublicGoods_trial'
    PLAYERS_PER_GROUP = 3   #3人プレイヤー
    NUM_ROUNDS = 10  #一気飲み章末問題で10にする箇所
    ENDOWMENT = cu(100)  #初期保有額20pを設定
    MULTIPLAYER = 2   #全員の貢献額を1.6倍する


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    
    #各グループの貢献額の合計をいれるオブジェクト
    total_contribution = models.CurrencyField()

    #各プレイヤーの個別の分配額をいれるオブジェクト
    individual_share = models.CurrencyField()
    


class Player(BasePlayer):
    #プレイヤーの貢献額をぶち込むオブジェクト
    contribution = models.CurrencyField(

        # 0p ~ 保有額pまで 1p刻みで選択肢を表示する。
        choices = currency_range(cu(0), cu(C.ENDOWMENT), cu(10)),

        # 貢献学の選択肢の前に設問文を表示
        label = "あなたはいくら貢献しますか？",

    )



def compute(group: Group):

    #groupクラスに所属するプレイヤー情報を取得
    players = group.get_players()

    #プレイヤー貢献額をリストにまとめる
    contributions = [p.contribution for p in players]

    #グループの総合貢献額を計算
    group.total_contribution = sum(contributions)

    #各プレイヤーへの分配額を計算
    group.individual_share = (
        group.total_contribution * C.MULTIPLAYER / C.PLAYERS_PER_GROUP
    )

    #各プレイヤーの獲得額を計算
    #保有額 - 貢献額 + 分配額
    for p in players:
        p.payoff = C.ENDOWMENT - p.contribution + group.individual_share


#パートナーマッチング（ずっと同じ相手とゲームする）
def creating_session(subsession: Subsession):
    if subsession.round_number == 1:
        # 第1期ならランダム割当
        subsession.group_randomly()
    else:
        # 第2期以降なら第1期であたった相手とマッチング
        subsession.group_like_round(1)


#ストレンジャーマッチング（毎期ランダムマッチング）
#def creating_session(subsession: Subsession):
        #subsession.group_randomly()

#パーフェクト・ストレンジャーマッチング（一回マッチングしたやつとはマッチングしない）
#otreeでは未実装
#海外の研究者が実装しているからググってやるのもあり


# PAGES
class Page1(Page):
    form_model = 'player'
    #プレイヤーが貢献額を入力する。
    form_fields = ['contribution']


class Page2(WaitPage):
    after_all_players_arrive = compute


class Page3(Page):
    pass


page_sequence = [Page1, Page2, Page3]
