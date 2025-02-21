from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'dicator_trial'
    PLAYERS_PER_GROUP = 2   #２人でやる
    NUM_ROUNDS = 1  #１ラウンド
    ENDOWMENT = cu(10)  #初期保有額10


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    proposal = models.CurrencyField(
        choices = currency_range(cu(0), C.ENDOWMENT, cu(1)),
        label = 'Player2にいくら渡しますか',
    )   #Player1は分配額を決定する


class Player(BasePlayer):
    pass

def compute(group: Group):
    #Player情報の取得
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)

    #p1は 初期保有額 - 分配額
    p1.payoff = C.ENDOWMENT - group.proposal
    #p2は 分配額
    p2.payoff = group.proposal

# PAGES
class MyPage(Page):
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage, ResultsWaitPage, Results]
