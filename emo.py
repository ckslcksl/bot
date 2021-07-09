weather_i = {'맑음':'☀️','흐림':'☁️','소나기':'🌧️'}
fortune_i = {'쥐띠':'🐀','소띠':'🐂','호랑이띠':'🐅','토끼띠':'🐇','용띠':'🐉'
            ,'뱀띠':'🐍','말띠':'🐎','양띠':'🐏','원숭이띠':'🐒','닭띠':'🐔'
            ,'개띠':'🐕','돼지띠':'🐖'}



def weather_icon(wStr):
    wKey = ''
    ##
    if '맑음' in wStr:
        wKey = '맑음'
    elif '흐림' in wStr:
        wKey = '흐림'
    elif '소나기' in wStr:
        wKey = '소나기'       
    ##
    if wKey in weather_i:
        w_icon = weather_i[wKey]
    return w_icon

def fortune_icon(fStr):      
    ##
    if fStr in fortune_i:
        f_icon = fortune_i[fStr]
    return f_icon