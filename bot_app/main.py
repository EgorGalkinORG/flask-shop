import telebot
import sqlite3
import os

bot = telebot.TeleBot(token= "7423716714:AAFXsmLt8SICOR1mKAbqclKpm9CyhO_11cs")
button = telebot.types.InlineKeyboardButton(text="GET USERS", callback_data = "get")
keyboard = telebot.types.InlineKeyboardMarkup(
    keyboard= [
        [button]
    ]
)
button1 = telebot.types.InlineKeyboardButton(text="CHECK", callback_data = "check")
keyboard1 = telebot.types.InlineKeyboardMarkup(
    keyboard= [
        [button1]
    ]
)
button_products_1 = telebot.types.InlineKeyboardButton(text="GET PRODUCTS", callback_data= "get_products")
button_products_2 = telebot.types.InlineKeyboardButton(text="ADD PRODUCT", callback_data= "add_product")
keyboard_products = telebot.types.InlineKeyboardMarkup(
    keyboard= [
        [button_products_1, button_products_2]
    ]
)



USERS_ID = "5"
PRODUCTS_ID = "7"
step1 = "start"

product = {
    "name":"",
    "price":"",
    "discount":"",
    "description":"",
    "count":""
}
def name(message):
    global step1,product
    product['name'] = message.text
    step1 = "image"
def image(message):
    global step1,product
    with open(os.path.abspath(__file__ + f"/../../shop_page/static/imgs/{product['name']}.png"), "wb") as file:
        file.write(bot.download_file(bot.get_file(message.photo[-1].file_id).file_path))
    step1 = "price"

def price(message):
    global step1,product
    product['price'] = message.text
    step1 = "discount"
def discount(message):
    global step1,product
    product['discount'] = message.text
    step1 = "description"
def description(message):
    global step1,product
    product['description'] = message.text
    step1 = "count"
def count(message):
    global step1,product
    product['count'] = message.text
    step1 = "final"
adding_new_product = False
@bot.message_handler(commands=['start'])
def start(message):
    if str(message.reply_to_message.id) == USERS_ID:
        bot.send_message(message.chat.id, 'Get all users' , reply_markup=keyboard)
    elif str(message.reply_to_message.id) == PRODUCTS_ID:
        bot.send_message(message.chat.id, 'Manual edit products' , reply_markup=keyboard_products)
    print(message.reply_to_message.id)

@bot.callback_query_handler(lambda callback: True)
def get_users(callback):
    global step1, product, adding_new_product, keyboard1
    adding_new_product = True
    database = sqlite3.connect(os.path.abspath(__file__ + '/../../project/data.db'))
    cursor = database.cursor()
    if callback.data == 'get':
        cursor.execute('SELECT * FROM user')
        list_users = cursor.fetchall()
        for user in list_users:
            if int(user[4]):
                is_admin = "True"
            else:
                is_admin = "False"
            delete_user = telebot.types.InlineKeyboardButton(text= "DELETE USER", callback_data= f"delete-{user[0]}")
            if user[4]:
                remove_user = telebot.types.InlineKeyboardButton(text= "REMOVE ADMIN", callback_data= f"change_admin-{user[0]}-{user[4]}")
            else:
                remove_user = telebot.types.InlineKeyboardButton(text= "ADD ADMIN", callback_data= f"change_admin-{user[0]}-{user[4]}")

            keyboard1 = telebot.types.InlineKeyboardMarkup(
                keyboard= [
                    [delete_user, remove_user]
                ]
            )
            bot.send_message(callback.message.chat.id, f'ID: {user[0]}\nNAME: {user[1]}\nPASSWORD: {user[3]}\nADMIN: {is_admin}', reply_markup= keyboard1)
    elif callback.data.split('-')[0] == "delete":
        cursor.execute(f"DELETE FROM user WHERE id = {callback.data.split('-')[1]}")
    elif callback.data.split("-")[0] == "change_admin":
        if int(callback.data.split("-")[2]):
            cursor.execute(f"UPDATE user SET is_admin = 0 where id = {callback.data.split('-')[1]}")
        else:
            cursor.execute(f"UPDATE user SET is_admin = 1 where id = {callback.data.split('-')[1]}")
    elif callback.data == "get_products":
        cursor.execute('SELECT * FROM product')
        list_users = cursor.fetchall()
        for product in list_users:
            bot.send_message(callback.message.chat.id, f"ID: {product[0]}\nNAME: {product[1]}\nPRICE: {product[2]}\nDISCOUNT: {product[3]}")
    elif callback.data == "add_product" or adding_new_product:
        adding_new_product = True
        if step1 == "start":
            bot.send_message(callback.message.chat.id, f"Enter name of new product", reply_markup=keyboard1)
            bot.register_next_step_handler(callback.message,name)
        elif step1 == "image" and callback.data == "check":
            bot.send_message(callback.message.chat.id, f"Upload image of new product", reply_markup=keyboard1)
            bot.register_next_step_handler(callback.message,image)
            
        elif step1 == "price" and callback.data == "check":
            # print(callback)
            # print(callback.message)
            # print(callback.message.photo)
            
            bot.send_message(callback.message.chat.id, f"Enter price of new product", reply_markup=keyboard1)
            bot.register_next_step_handler(callback.message,price)
            
        elif step1 == "discount" and callback.data == "check":
            # product['price'] = callback.message.text
            bot.send_message(callback.message.chat.id, f"Enter discount of new product", reply_markup=keyboard1)
            bot.register_next_step_handler(callback.message,discount)
        elif step1 == "description" and callback.data == "check":
            # product['discount'] = callback.message.text
            bot.send_message(callback.message.chat.id, f"Enter description of new product", reply_markup=keyboard1)
            bot.register_next_step_handler(callback.message,description)
        elif step1 == "count" and callback.data == "check":
            # product['description'] = callback.message.text
            bot.send_message(callback.message.chat.id, f"Enter count of new product", reply_markup=keyboard1)
            # step1 = "final"
            bot.register_next_step_handler(callback.message,count)
        elif step1 == "final" and callback.data == "check":
            product['count'] = callback.message.text
            bot.send_message(callback.message.chat.id, f"Writing...")
            cursor.execute('INSERT INTO product (name, price, discount, capacity1, capacity2, capacity3) Values (?,?,?,?,?,?)', (product["name"],product["price"],product["discount"], "64", "128", "256")) 
            database.commit()
            product = {
                "name":"",
                "price":"",
                "discount":"",
                "description":"",
                "count":""
            }
            step1 = "start"
            adding_new_product = False
            bot.send_message(callback.message.chat.id, f"congratulations! Your product was created!\nYou can see your product on website!")



    database.commit()
    database.close()
    adding_new_product = False
bot.infinity_polling()