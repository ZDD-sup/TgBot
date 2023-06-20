import sqlite3 as sq

def sql_baseid_start():
    global basei, curi
    basei = sq.connect('id_phone.db')
    curi = basei.cursor()
    if basei:
        print('База id_phone подключина!')
    basei.execute('CREATE TABLE IF NOT EXISTS {}(id TEXT, PHnumber TEXT)'.format('dataID'))

async def sql_add_i_command(state):
    async with state.proxy() as data:
        curi.execute('INSERT INTO dataID VALUES(?, ?)', tuple(data.values()))
        basei.commit()

'''******************************************'''

def sql_photo_start():
    global basep, curp
    basep = sq.connect('phone_photo.db')
    curp = basep.cursor()
    if basep:
        print('База phone_photo подключина!')
    basep.execute('CREATE TABLE IF NOT EXISTS {}(PHnumber TEXT,  phote TEXT)'.format('dataPH'))

async def sql_add_p_command(state):
    async with state.proxy() as data:
        curp.execute('INSERT INTO dataPH VALUES(?, ?)', tuple(data.values()))
        basep.commit()

def sql_read(num):
    return curp.execute('SELECT photo FROM dataPH WHERE PHnumber ==?', (num,)).fetchone()


    # for ret in curp.execute('SELECT PHnumber FROM dataPH').fetchall():

    #  await bot.send_photo(message.from_user.id,'Фотографии', ret[1])