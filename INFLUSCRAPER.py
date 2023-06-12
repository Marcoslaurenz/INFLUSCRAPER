import json
from traceback import print_tb
from instagrapi import Client
import json
from bs4 import BeautifulSoup
import requests
while True: 
    print("""
    _____                                
    /  ___|                               
    \ `--.  ___ _ __ __ _ _ __   ___ _ __ 
    `--. \/ __| '__/ _` | '_ \ / _ \ '__|
    /\__/ / (__| | | (_| | |_) |  __/ |   
    \____/ \___|_|  \__,_| .__/ \___|_|   
                        | |              
                        |_|         
        
        """)
    print("1 = INSTAGRAM \n2 = TIKTOK \n3 = YOUTUBE")
    opt = input("INGRESE LA OPCION DESEADA: ")
    print("======================================")


    if opt == "1":
        tg = input("Enter Instagram target: ")
        cl = Client()
        ACCOUNT_USERNAME="pruebascraper2.0"
        ACCOUNT_PASSWORD="Marsa0330"
        cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

        user_id = cl.user_id_from_username(tg)
        medias = cl.user_clips(user_id, 20)



        l = str(medias)
        l = l.split(",")
        total = 0
        for e in l:
            if "play_count" in e:
                e = e.replace(" play_count=","")
                print("=====================")
                print(e)
                total += int(e)
            else:
                pass
        print("============================")
        print("Views Total: "+str(total))
        print("============================")
        with open("InstagramResults.txt","a+") as f:
            f.write(tg+","+str(total)+"\n")
    elif opt == "2":
        
        user = input("Enter Tiktok Username: ")
        h={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"}

        r = requests.get("https://www.tiktok.com/@"+user, headers=h)

        soup = BeautifulSoup(r.text, "html.parser")
        name = soup.find_all(class_="video-count")
        total = 0
        for element in name:
            resultado = element.text
            print(resultado)
            print("sin alterar")
            if not "K" in resultado:
               
                print(resultado)
                views = int(resultado)
                total += views
                
            elif ".1K" in resultado:
                resultado = resultado.replace("K","00")
                resultado = resultado.replace(".","")
                print(resultado)
                views = int(resultado)
                total += views
            elif ".2K" in resultado:
                resultado = resultado.replace("K","00")
                resultado = resultado.replace(".","")
                print(resultado)
                views = int(resultado)
                total += views
            elif ".3K" in resultado:
                resultado = resultado.replace("K","00")
                resultado = resultado.replace(".","")
                print(resultado)
                
                views = int(resultado)
                total += views
            elif ".4K" in resultado:
                resultado = resultado.replace("K","00")
                resultado = resultado.replace(".","")
                print(resultado)
                views = int(resultado)
                total += views
            elif ".5K" in resultado:
                resultado = resultado.replace("K","00")
                resultado = resultado.replace(".","")
                print(resultado)
                print(resultado)
                views = int(resultado)
                total += views

            elif ".6K" in resultado:
                resultado = resultado.replace("K","00")
                resultado = resultado.replace(".","")
                print(resultado)
                print(resultado)
                views = int(resultado)
                total += views
            elif ".7K" in resultado:
                resultado = resultado.replace("K","00")
                resultado = resultado.replace(".","")
                print(resultado)
                print(resultado)
                views = int(resultado)
                total += views
            elif ".8K" in resultado:
                resultado = resultado.replace("K","00")
                resultado = resultado.replace(".","")
                print(resultado)
                views = int(resultado)
                total += views
            elif ".9K" in resultado:
                resultado = resultado.replace("K","00")
                resultado = resultado.replace(".","")
                print(resultado)
                print(resultado)
                views = int(resultado)
                total += views
            elif "K" in resultado:
               
                resultado = resultado.replace("K","000")
                resultado = resultado.replace(".","")
                print(resultado)
                views = int(resultado)
                total += views
            else:
                pass
            
           
        print("===========================================================")
        print(user+" Tiene un total de: "+str(total)+" Vizualizaciones")
        with open("TiktokResults.txt","a+") as f:
            f.write(user+","+str(total)+"\n")
           
    elif opt == "3":
        url = input("Ingrese USER CHANNEL: ")

        h={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0"}
        r = requests.get("https://www.youtube.com/@{url}/videos", headers=h)




        name = r.text.split('"')

        total = 0 
        for e in name:
            try:
                if 'vistas'  in e:
                    
                    print("==================")
                
                    view1 = e.replace(" vistas","")
                    view2 = view1.replace(",","")
                    view = int(view2)
                    print(view)
            
                    total += view
                else:
                    pass
            except:
                pass
        print("Vistas totales: "+str(total))
        with open("YoutubeResults.txt", "a+") as f:
            f.write(str(total)+","+url+"\n")