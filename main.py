import vk_api
import keep_alive
import os
from user import *
import vk_api
from groups import *
from threading import Thread
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
import requests, time, datetime



def message_vk():
  vk.messages.send(user_id=user, random_id=get_random_id(), message="Капча")


def captcha_handler(captcha):
  message_vk()
  key = input("Капча {0}: ".format(captcha.get_url())).strip()
  return captcha.try_again(key)
 
keep_alive.keep_alive()
global vk_session, vk
vk_session = vk_api.VkApi(token=os.environ['token'], captcha_handler=captcha_handler)
print('Авторизовался')
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

namebot = vk.users.get(fields='screen_name')
name = '✔ ' + namebot[0]['first_name'] + ' ' + namebot[0][
    'last_name'] + ' запустился'
print(name)

count_post = 9
def cool_time():
  time.sleep(7200)
def sleep_like():
  time.sleep(20)


# 0 = https://vk.com/ioanyt
def ioan():
    vk.account.setOnline()
    print('📲 В онлайне на 5 минут')
    name = vk.groups.getById(group_id=group_name_ioan, fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_ioan, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post', item_id=postItem, owner_id=group_ioan)
        if like['liked'] == 0:
            vk.likes.add(type='post', item_id=postItem, owner_id=group_ioan)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
            
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1


# 1 = https://vk.com/freeskin_ru
def free_skins():
    name = vk.groups.getById(group_id=group_name_free_skins,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_free_skins, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_free_skins)
        if like['liked'] == 0:
            vk.likes.add(type='post', item_id=postItem, owner_id=group_free_skins)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1


# https://vk.com/freeskins
def free_skins_csgo():
    name = vk.groups.getById(group_id=group_name_free_skins_csgo,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_free_skins_csgo, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_free_skins_csgo)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_free_skins_csgo)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1


# # https://vk.com/gratis_csgo
# def gratis():
#     name = vk.groups.getById(group_id=group_name_gratis, fields='screen_name')
#     sumname = '--- ' + name[0]['name'] + ' ---'
#     print(sumname)
#     print('---------------------------------------------------')
#     posts = vk.wall.get(owner_id=group_gratis, count=count_post)
#     sumpost = len(posts['items'])
#     print(f'всего постов : {sumpost}')
#     job = 0
#     while job < count_post:
#         postItem = posts['items'][job]['id']
#         like = vk.likes.isLiked(type='post',
#                                 item_id=postItem,
#                                 owner_id=group_gratis)
#         if like['liked'] == 0:
#             vk.likes.add(type='post', item_id=postItem, owner_id=group_gratis)
#             print(
#                 f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
#             )
#             sleep_like()
#             vk.likes.delete(type='post', item_id=postItem, owner_id=group_gratis)
#             print(
#                 f'❌  {job + 1} |    {namebot[0]["first_name"]}: Удалил лайк с публикации! (Публикация №{postItem})'
#             )
#             sleep_like()
#         elif like['liked'] == 1:
#             print(
#                 f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
#             )
#             vk.likes.delete(type='post', item_id=postItem, owner_id=group_gratis)
#             print(
#                 f'❌  {job + 1} |    {namebot[0]["first_name"]}: Удалил лайк с публикации! (Публикация №{postItem})'
#             )
#         job = job + 1


# https://vk.com/blacks_csgo
def black_moon():
    name = vk.groups.getById(group_id=group_name_black_moon,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_black_moon, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_black_moon)
        if like['liked'] == 0:
            vk.likes.add(type='post', item_id=postItem, owner_id=group_black_moon)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1


# https://vk.com/zlaypchela
def zlaypchela():
    name = vk.groups.getById(group_id=group_name_zlaypchela,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_zlaypchela, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_zlaypchela)
        if like['liked'] == 0:
            vk.likes.add(type='post', item_id=postItem, owner_id=group_zlaypchela)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1


# https://vk.com/ggdrop_win
def ggdrop():
    name = vk.groups.getById(group_id=group_name_ggdrop, fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_ggdrop, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_ggdrop)
        if like['liked'] == 0:
            vk.likes.add(type='post', item_id=postItem, owner_id=group_ggdrop)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1


# # https://vk.com/free.ekopgisecu
# def free_ekopgisecu():
#     name = vk.groups.getById(group_id=group_name_free_ekopgisecu,
#                              fields='screen_name')
#     sumname = '--- ' + name[0]['name'] + ' ---'
#     print(sumname)
#     print('---------------------------------------------------')
#     posts = vk.wall.get(owner_id=group_free_ekopgisecu, count=count_post)
#     sumpost = len(posts['items'])
#     print(f'всего постов : {sumpost}')
#     job = 0
#     while job < count_post:
#         postItem = posts['items'][job]['id']
#         like = vk.likes.isLiked(type='post',
#                                 item_id=postItem,
#                                 owner_id=group_free_ekopgisecu)
#         if like['liked'] == 0:
#             vk.likes.add(type='post',
#                          item_id=postItem,
#                          owner_id=group_free_ekopgisecu)
#             print(
#                 f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
#             )
#             sleep_like()
#         elif like['liked'] == 1:
#             print(
#                 f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
#             )
#         job = job + 1


# https://vk.com/csgoblink
def csgoblink():
    name = vk.groups.getById(group_id=group_name_csgoblink,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_csgoblink, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_csgoblink)
        if like['liked'] == 0:
            vk.likes.add(type='post', item_id=postItem, owner_id=group_csgoblink)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1


# https://vk.com/halava_ananas
def halava_ananas():
    name = vk.groups.getById(group_id=group_name_halava_ananas,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_halava_ananas, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_halava_ananas)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_halava_ananas)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1


# https://vk.com/freealter
def freealter():
    name = vk.groups.getById(group_id=group_name_freealter,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_freealter, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_freealter)
        if like['liked'] == 0:
            vk.likes.add(type='post', item_id=postItem, owner_id=group_freealter)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1

# https://vk.com/fail_promokod
def fail_promokod():
    name = vk.groups.getById(group_id=group_name_fail_promokod,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_fail_promokod, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_fail_promokod)
        if like['liked'] == 0:
            vk.likes.add(type='post', item_id=postItem, owner_id=group_fail_promokod)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# https://vk.com/xaluavniykimi
def xaluavniykimi():
    name = vk.groups.getById(group_id=group_name_xaluavniykimi,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_xaluavniykimi, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_xaluavniykimi)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_xaluavniykimi)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1




    



# https://vk.com/csgoaffk
def csgoaffk():
    name = vk.groups.getById(group_id=group_name_csgoaffk,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_csgoaffk, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_csgoaffk)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_csgoaffk)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1

# https://vk.com/ekopgisecu.csgo
def ekopgisecu_csgo():
    name = vk.groups.getById(group_id=group_name_ekopgisecu_csgo,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_ekopgisecu_csgo, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_ekopgisecu_csgo)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_ekopgisecu_csgo)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# https://vk.com/rubachannel
def rubachannel():
    name = vk.groups.getById(group_id=group_name_rubachannel,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_rubachannel, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_rubachannel)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_rubachannel)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# # https://vk.com/promo666code
# def promo666code():
#     name = vk.groups.getById(group_id=group_name_promo666code,
#                              fields='screen_name')
#     sumname = '--- ' + name[0]['name'] + ' ---'
#     print(sumname)
#     print('---------------------------------------------------')
#     posts = vk.wall.get(owner_id=group_promo666code, count=count_post)
#     sumpost = len(posts['items'])
#     print(f'всего постов : {sumpost}')
#     job = 0
#     while job < count_post:
#         postItem = posts['items'][job]['id']
#         like = vk.likes.isLiked(type='post',
#                                 item_id=postItem,
#                                 owner_id=group_promo666code)
#         if like['liked'] == 0:
#             vk.likes.add(type='post',
#                          item_id=postItem,
#                          owner_id=group_promo666code)
#             print(
#                 f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
#             )
#             sleep_like()
#         elif like['liked'] == 1:
#             print(
#                 f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
#             )
#         job = job + 1



# # https://vk.com/lezriland
# def lezriland():
#     name = vk.groups.getById(group_id=group_name_lezriland,
#                              fields='screen_name')
#     sumname = '--- ' + name[0]['name'] + ' ---'
#     print(sumname)
#     print('---------------------------------------------------')
#     posts = vk.wall.get(owner_id=group_lezriland, count=count_post)
#     sumpost = len(posts['items'])
#     print(f'всего постов : {sumpost}')
#     job = 0
#     while job < count_post:
#         postItem = posts['items'][job]['id']
#         like = vk.likes.isLiked(type='post',
#                                 item_id=postItem,
#                                 owner_id=group_lezriland)
#         if like['liked'] == 0:
#             vk.likes.add(type='post',
#                          item_id=postItem,
#                          owner_id=group_lezriland)
#             print(
#                 f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
#             )
#             sleep_like()
#         elif like['liked'] == 1:
#             print(
#                 f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
#             )
#         job = job + 1



# https://vk.com/nezoxcsgo
def nezoxcsgo():
    name = vk.groups.getById(group_id=group_name_nezoxcsgo,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_nezoxcsgo, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_nezoxcsgo)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_nezoxcsgo)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# # https://vk.com/qwerskins
# def qwerskins():
#     name = vk.groups.getById(group_id=group_name_qwerskins,
#                              fields='screen_name')
#     sumname = '--- ' + name[0]['name'] + ' ---'
#     print(sumname)
#     print('---------------------------------------------------')
#     posts = vk.wall.get(owner_id=group_qwerskins, count=count_post)
#     sumpost = len(posts['items'])
#     print(f'всего постов : {sumpost}')
#     job = 0
#     while job < count_post:
#         postItem = posts['items'][job]['id']
#         like = vk.likes.isLiked(type='post',
#                                 item_id=postItem,
#                                 owner_id=group_qwerskins)
#         if like['liked'] == 0:
#             vk.likes.add(type='post',
#                          item_id=postItem,
#                          owner_id=group_qwerskins)
#             print(
#                 f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
#             )
#             sleep_like()
#         elif like['liked'] == 1:
#             print(
#                 f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
#             )
#         job = job + 1



# # https://vk.com/promorunn
# def promorunn():
#     name = vk.groups.getById(group_id=group_name_promorunn,
#                              fields='screen_name')
#     sumname = '--- ' + name[0]['name'] + ' ---'
#     print(sumname)
#     print('---------------------------------------------------')
#     posts = vk.wall.get(owner_id=group_promorunn, count=count_post)
#     sumpost = len(posts['items'])
#     print(f'всего постов : {sumpost}')
#     job = 0
#     while job < count_post:
#         postItem = posts['items'][job]['id']
#         like = vk.likes.isLiked(type='post',
#                                 item_id=postItem,
#                                 owner_id=group_promorunn)
#         if like['liked'] == 0:
#             vk.likes.add(type='post',
#                          item_id=postItem,
#                          owner_id=group_promorunn)
#             print(
#                 f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
#             )
#             sleep_like()
#         elif like['liked'] == 1:
#             print(
#                 f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
#             )
#         job = job + 1



# https://vk.com/malyaft
def malyaft():
    name = vk.groups.getById(group_id=group_name_malyaft,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_malyaft, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_malyaft)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_malyaft)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# https://vk.com/gocs53
def gocs53():
    name = vk.groups.getById(group_id=group_name_gocs53,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_gocs53, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_gocs53)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_gocs53)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# # https://vk.com/xalyava.csgo1
# def xalyava_csgo1():
#     name = vk.groups.getById(group_id=group_name_xalyava_csgo1,
#                              fields='screen_name')
#     sumname = '--- ' + name[0]['name'] + ' ---'
#     print(sumname)
#     print('---------------------------------------------------')
#     posts = vk.wall.get(owner_id=group_xalyava_csgo1, count=count_post)
#     sumpost = len(posts['items'])
#     print(f'всего постов : {sumpost}')
#     job = 0
#     while job < count_post:
#         postItem = posts['items'][job]['id']
#         like = vk.likes.isLiked(type='post',
#                                 item_id=postItem,
#                                 owner_id=group_xalyava_csgo1)
#         if like['liked'] == 0:
#             vk.likes.add(type='post',
#                          item_id=postItem,
#                          owner_id=group_xalyava_csgo1)
#             print(
#                 f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
#             )
#             sleep_like()
#         elif like['liked'] == 1:
#             print(
#                 f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
#             )
#         job = job + 1



# https://vk.com/freedim4ik
def freedim4ik():
    name = vk.groups.getById(group_id=group_name_freedim4ik,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_freedim4ik, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_freedim4ik)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_freedim4ik)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# https://vk.com/promo_lime
def promo_lime():
    name = vk.groups.getById(group_id=group_name_promo_lime,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_promo_lime, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_promo_lime)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_promo_lime)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# https://vk.com/sweetfreecsgo
def sweetfreecsgo():
    name = vk.groups.getById(group_id=group_name_sweetfreecsgo,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_sweetfreecsgo, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_sweetfreecsgo)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_sweetfreecsgo)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1



# # https://vk.com/evreyxalava
# def evreyxalava():
#     name = vk.groups.getById(group_id=group_name_evreyxalava,
#                              fields='screen_name')
#     sumname = '--- ' + name[0]['name'] + ' ---'
#     print(sumname)
#     print('---------------------------------------------------')
#     posts = vk.wall.get(owner_id=group_evreyxalava, count=count_post)
#     sumpost = len(posts['items'])
#     print(f'всего постов : {sumpost}')
#     job = 0
#     while job < count_post:
#         postItem = posts['items'][job]['id']
#         like = vk.likes.isLiked(type='post',
#                                 item_id=postItem,
#                                 owner_id=group_evreyxalava)
#         if like['liked'] == 0:
#             vk.likes.add(type='post',
#                          item_id=postItem,
#                          owner_id=group_evreyxalava)
#             print(
#                 f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
#             )
#             sleep_like()
#         elif like['liked'] == 1:
#             print(
#                 f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
#             )
#         job = job + 1



# # https://vk.com/cs_typicai
# def cs_typicai():
#     name = vk.groups.getById(group_id=group_name_cs_typicai,
#                              fields='screen_name')
#     sumname = '--- ' + name[0]['name'] + ' ---'
#     print(sumname)
#     print('---------------------------------------------------')
#     posts = vk.wall.get(owner_id=group_cs_typicai, count=count_post)
#     sumpost = len(posts['items'])
#     print(f'всего постов : {sumpost}')
#     job = 0
#     while job < count_post:
#         postItem = posts['items'][job]['id']
#         like = vk.likes.isLiked(type='post',
#                                 item_id=postItem,
#                                 owner_id=group_cs_typicai)
#         if like['liked'] == 0:
#             vk.likes.add(type='post',
#                          item_id=postItem,
#                          owner_id=group_cs_typicai)
#             print(
#                 f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
#             )
#             sleep_like()
#         elif like['liked'] == 1:
#             print(
#                 f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
#             )
#         job = job + 1


# https://vk.com/csgo_up
# def csgo_up():
#     name = vk.groups.getById(group_id=group_name_csgo_up,
#                              fields='screen_name')
#     sumname = '--- ' + name[0]['name'] + ' ---'
#     print(sumname)
#     print('---------------------------------------------------')
#     posts = vk.wall.get(owner_id=group_csgo_up, count=count_post)
#     sumpost = len(posts['items'])
#     print(f'всего постов : {sumpost}')
#     job = 0
#     while job < count_post:
#         postItem = posts['items'][job]['id']
#         like = vk.likes.isLiked(type='post',
#                                 item_id=postItem,
#                                 owner_id=group_csgo_up)
#         if like['liked'] == 0:
#             vk.likes.add(type='post',
#                          item_id=postItem,
#                          owner_id=group_csgo_up)
#             print(
#                 f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
#             )
#             sleep_like()
#         elif like['liked'] == 1:
#             print(
#                 f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
#             )
#         job = job + 1



# # https://vk.com/blank_labb
# def blank_labb():
#     name = vk.groups.getById(group_id=group_name_blank_labb,
#                              fields='screen_name')
#     sumname = '--- ' + name[0]['name'] + ' ---'
#     print(sumname)
#     print('---------------------------------------------------')
#     posts = vk.wall.get(owner_id=group_blank_labb, count=count_post)
#     sumpost = len(posts['items'])
#     print(f'всего постов : {sumpost}')
#     job = 0
#     while job < count_post:
#         postItem = posts['items'][job]['id']
#         like = vk.likes.isLiked(type='post',
#                                 item_id=postItem,
#                                 owner_id=group_blank_labb)
#         if like['liked'] == 0:
#             vk.likes.add(type='post',
#                          item_id=postItem,
#                          owner_id=group_blank_labb)
#             print(
#                 f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
#             )
#             sleep_like()
#         elif like['liked'] == 1:
#             print(
#                 f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
#             )
#         job = job + 1



# https://vk.com/freefilka
def freefilka():
    name = vk.groups.getById(group_id=group_name_freefilka,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_freefilka, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_freefilka)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_freefilka)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1


      
# # https://vk.com/metadon321
# def metadon321():
#     name = vk.groups.getById(group_id=group_name_metadon321,
#                              fields='screen_name')
#     sumname = '--- ' + name[0]['name'] + ' ---'
#     print(sumname)
#     print('---------------------------------------------------')
#     posts = vk.wall.get(owner_id=group_metadon321, count=count_post)
#     sumpost = len(posts['items'])
#     print(f'всего постов : {sumpost}')
#     job = 0
#     while job < count_post:
#         postItem = posts['items'][job]['id']
#         like = vk.likes.isLiked(type='post',
#                                 item_id=postItem,
#                                 owner_id=group_metadon321)
#         if like['liked'] == 0:
#             vk.likes.add(type='post',
#                          item_id=postItem,
#                          owner_id=group_metadon321)
#             print(
#                 f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
#             )
#             sleep_like()
#         elif like['liked'] == 1:
#             print(
#                 f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
#             )
#         job = job + 1



# https://vk.com/gamehuntnet
def gamehuntnet():
    name = vk.groups.getById(group_id=group_name_gamehuntnet,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_gamehuntnet, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_gamehuntnet)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_gamehuntnet)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1


      
# https://vk.com/penis.csgo
def peniscsgo():
    name = vk.groups.getById(group_id=group_name_peniscsgo,
                             fields='screen_name')
    sumname = '--- ' + name[0]['name'] + ' ---'
    print(sumname)
    print('---------------------------------------------------')
    posts = vk.wall.get(owner_id=group_peniscgo, count=count_post)
    sumpost = len(posts['items'])
    print(f'всего постов : {sumpost}')
    job = 0
    while job < count_post:
        postItem = posts['items'][job]['id']
        like = vk.likes.isLiked(type='post',
                                item_id=postItem,
                                owner_id=group_peniscgo)
        if like['liked'] == 0:
            vk.likes.add(type='post',
                         item_id=postItem,
                         owner_id=group_peniscgo)
            print(
                f'✅  {job + 1} |    {namebot[0]["first_name"]}: Поставил лайк на публикацию! (Публикация №{postItem})'
            )
            sleep_like()
        elif like['liked'] == 1:
            print(
                f'❗   {job + 1} |    {namebot[0]["first_name"]}: Уже ставил лайк на публикацию! (Публикация №{postItem})'
            )
        job = job + 1
      
while True:
    # csgo_up()
    # print('--------------------------------------------------')

    ioan()
    print('---------------------------------------------------')

    free_skins()
    print('---------------------------------------------------')

    free_skins_csgo()
    print('---------------------------------------------------')

    # gratis()
    # print('---------------------------------------------------')

    gamehuntnet()
    print('---------------------------------------------------')
  
    black_moon()
    print('---------------------------------------------------')

    peniscsgo()
    print('---------------------------------------------------')
  
    zlaypchela()
    print('---------------------------------------------------')

    ggdrop()
    print('---------------------------------------------------')

    # metadon321()
    # print('---------------------------------------------------')
  
    # free_ekopgisecu()
    # print('---------------------------------------------------')

    csgoblink()
    print('---------------------------------------------------')

    halava_ananas()
    print('---------------------------------------------------')

    freealter()
    print('---------------------------------------------------')

    fail_promokod()
    print('---------------------------------------------------')
    
    # ggpromodrop()
    # print('---------------------------------------------------')

    xaluavniykimi()
    print('---------------------------------------------------')

    freefilka()
    print('---------------------------------------------------')


    csgoaffk()
    print('---------------------------------------------------')

    ekopgisecu_csgo()
    print('---------------------------------------------------')

    rubachannel()
    print('---------------------------------------------------')

    # promo666code()
    # print('---------------------------------------------------')

    # lezriland()
    # print('---------------------------------------------------')

    nezoxcsgo()
    print('---------------------------------------------------')

    # qwerskins()
    # print('---------------------------------------------------')

    # promorunn()
    # print('---------------------------------------------------')

    malyaft()
    print('---------------------------------------------------')

    gocs53()
    print('---------------------------------------------------')

    # xalyava_csgo1()
    # print('--------------------------------------------------')

    freedim4ik()
    print('--------------------------------------------------')

    promo_lime()
    print('--------------------------------------------------')
    
    sweetfreecsgo()
    print('--------------------------------------------------')

    # evreyxalava()
    # print('--------------------------------------------------')

    # cs_typicai()
    # print('--------------------------------------------------')

    # blank_labb()
    # print('--------------------------------------------------')
    
    os.system('clear')
    today = datetime.datetime.today()
    print(today.strftime("%Y-%m-%d %H:%M:%S") + '| Не работаю 2 часа 🙂......')
    vk.messages.send(user_id=user, message='Не работаю 2 часа🙂... ', random_id=get_random_id())
    cool_time()
    