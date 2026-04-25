from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-8z8v(&tjk_zq8ik6e+-0c=$5whma&ry01cp%f4c%wtc%o&g$6i'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'maquinas',
    'transacao',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'app' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'app' / 'static',
]

MEDIA_ROOT = BASE_DIR / 'media'

MEDIA_URL = '/media/'


JAZZMIN_SETTINGS = {
    "site_title": "Frango Moisés Admin",
    "site_header": "Frango do Moisés",
    "site_brand": "Frango Moisés",
    "site_logo": "app/img/logo_admin.png",
    "welcome_sign": "Administrador da aplicação Frango do Moisés",
    "copyright": "Moisés Ltda",
    "show_sidebar": True,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "navigation_expanded": True,
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "maquinas.maquinas_model": "fas fa-credit-card",
        "transacao.vendas_model": "fas fa-shopping-cart",
    },
    "topmenu_links": [
        # Link para Voltar (ou outra página específica)
        {"name": "Sair do Admin", "url": "/"},
    ],
    # A configuração específica para esconder o log de ações da home:
    "hide_models": ["auth.Group"],

    "custom_css": "app/css/custom_admin.css",

    "usermenu_links": [
        {"name": "Sair do Admin", "url": "/", "icon": "fas fa-sign-out-alt"},
    ],

    "sidebar_nav_child_indent": True,
    "custom_links": {
        "app": [
            {
                "name": "Sair do Admin",
                "url": "/",
                "icon": "fas fa-sign-out-alt",
                "permissions": ["auth.view_user"]
            },
        ],
    },
    
}