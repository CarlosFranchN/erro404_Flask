import os

class Config:
    # Outras configurações
    USE_CDN = os.environ.get('USE_CDN', 'True') == 'True'
    FONT_AWESOME_CDN = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"
    FONT_AWESOME_LOCAL = "static/css/all.min.css"

    @staticmethod
    def get_font_awesome_url():
        return Config.FONT_AWESOME_CDN if Config.USE_CDN else Config.FONT_AWESOME_LOCAL
