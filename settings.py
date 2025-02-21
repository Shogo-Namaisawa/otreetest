from os import environ

SESSION_CONFIGS = [
    dict(
        # この構成の名前を設定します
        name = 'questionnaire',

        # oTreeのデモ画面で表示される名前を設定します
        display_name = '初めてのアンケート',

        # デモ画面で参加人数を設定しておく必要があります
        num_demo_participants = 1,

        # この構成で使用するアプリケーションを設定します
        app_sequence = ['questionnaire']
    ),

    dict(
        name = 'pg3',
        display_name = '初めての公共財ゲーム',
        num_demo_participants = 3,
        app_sequence = ['PublicGoods_trial']
    ),

    dict(
        name = 'DG',
        display_name = '初めての独裁者ゲーム',
        num_demo_participants = 2,
        app_sequence = ['dictator_trial']
    )
    
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ja'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '6654196676519'

ROOMS = [
    dict(
        name = 'label',
        display_name = '実験参加者 label',
        participant_label_file = '_rooms/label.txt',
    ),
]