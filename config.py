"""Configuration Class for Flask"""
import os
import secrets


class Config:
    """Default Config Settings"""
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', "TRUE")
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', "sqlite:///app.db")
    SECRET_KEY = secrets.token_urlsafe(16)
    HOST = 'us-east.connect.psdb.cloud'
    USERNAME = 'f49g9a0xaxsdqh45i6m6'
    PASSWORD = 'pscale_pw_gUnuTFqy1temlcCWcNasRblkvYnuYTLZpLaGhz6WPEs'
    DATABASE = 'shedflow'
