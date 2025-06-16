from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'questionnaire'
    PLAYERS_PER_GROUP = None
    # 1人のときは"None"と記述する。
    NUM_ROUNDS = 1
    # 質問は1度だけ

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    q_gender = models.CharField(initial = None,
                                choices  = ['男性', '女性', '回答しない'],
                                verbose_name = 'あなたの名前を入れてください。',
                                widget = widgets.RadioSelect)
    # ラジオボタンを使うときは　widget = widgets.RadioSelectを記述する。

    q_age = models.IntegerField(initial = None,
                                verbose_name = 'あなたの年齢を教えてください。',
                                choices  = range(0, 125)
                                )
    # 数字の場合はchoicesを使うことで範囲を指定できる
    # ０<= q_age < 125になるので、最小値は0,最大値は124となる 

    q_area = models.CharField(initial = None,
                                choices  = ['北海道', '東北地方', '関東地方',
                                            '中部地方', '近畿地方', '中国地方', 
                                            '四国地方', '九州地方'], 
                                            verbose_name = 'あなたの年齢を教えてください。'
                                            )
    
    q_tanmatsu = models.CharField(initial = None,
                                choices = ['パソコン',
                                            'タブレット', 
                                            'スマートフォン', 
                                            'それ以外'], 
                                            verbose_name = '回答端末を教えてください', 
                                            widget = widgets.RadioSelect
                                            # widget = widgets.RadioSelectHorizontalはラジオボタンを水平に並べる。
                                            )
    
    q_LivingAlone =  models.CharField(initial = None,
                                choices = ['はい',
                                            'いいえ'] ,
                                            verbose_name = '一人暮らしですか？', 
                                            widget = widgets.RadioSelect
                                            # widget = widgets.RadioSelectHorizontalはラジオボタンを水平に並べる。
                                            )
    
    q_student = models.BooleanField(initial = None,
                                verbose_name = 'あなたは学生ですか？(0:はい 1:いいえ)',
                                choices  = range(0,2)
                                )




# PAGES
class Page1(Page):
    #質問項目は4つ
    form_model = 'player'

    form_fields = [
        'q_gender', 'q_age', 'q_area','q_tanmatsu', 'q_LivingAlone', 'q_student'
        ]
    
    template_name = 'questionnaire/Page1.html'



class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Page1]
