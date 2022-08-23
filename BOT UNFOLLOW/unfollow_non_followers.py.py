#Importamos las librerias
from instabot import Bot
from time import sleep
from random import randint
import my_config

#Instanciamos los objetos del bot
"""Aqui se cambia el tiempo"""
bot = Bot(unfollow_delay=35)
unfollow_delay=28
#Ingresa en la cuenta de instagram
bot.login(username = my_config.USERNAME,password =my_config.PASSWORD)
#Va a la lista de seguidos en la cuenta de instagram
non_followers = set(bot.following) - set(bot.followers)
#Hace un bucle sobre todos los usuarios
for non_follower in non_followers:
    try:
        bot.unfollow(non_follower)
    except Exception as e:
        print(e)
      

