
        
def start_prog (user_id,namebot,message_in,status,message_id,name_file_picture,telefon_nome):
    import iz_func
    import iz_telegram 
    print ('-----------------------------------------------------')
    if message_in == 'Начать тест':
        status = ''
        iz_telegram.save_variable (user_id,namebot,"status",'')

    if status == 'Ввод капчи':
        message_out,menu = iz_telegram.get_message (user_id,'Ввод капчи',namebot)
        markup = ''
        answer = iz_telegram.bot_send (user_id,namebot,message_out,markup,message_id)
        db,cursor = iz_func.connect ()
        id_save   = iz_telegram.load_variable (user_id,namebot,'id capcha')
        sql = "UPDATE vk_capcha SET capcha = '"+str(message_in) + "',status = 'get' where id = "+str(id_save)+""
        print ('[+] sql:',sql)
        cursor.execute(sql)
        db.commit()