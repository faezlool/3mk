import requests
import json
from datetime import datetime
from colorama import Fore

r = requests.session ()
text = """

  ██████  ███▄    █  ▄▄▄       ██▓███    █████▒██▀███   ██▓▓█████  ███▄    █ ▓█████▄   ██████ 
▒██    ▒  ██ ▀█   █ ▒████▄    ▓██░  ██▒▓██   ▒▓██ ▒ ██▒▓██▒▓█   ▀  ██ ▀█   █ ▒██▀ ██▌▒██    ▒ 
░ ▓██▄   ▓██  ▀█ ██▒▒██  ▀█▄  ▓██░ ██▓▒▒████ ░▓██ ░▄█ ▒▒██▒▒███   ▓██  ▀█ ██▒░██   █▌░ ▓██▄   
  ▒   ██▒▓██▒  ▐▌██▒░██▄▄▄▄██ ▒██▄█▓▒ ▒░▓█▒  ░▒██▀▀█▄  ░██░▒▓█  ▄ ▓██▒  ▐▌██▒░▓█▄   ▌  ▒   ██▒
▒██████▒▒▒██░   ▓██░ ▓█   ▓██▒▒██▒ ░  ░░▒█░   ░██▓ ▒██▒░██░░▒████▒▒██░   ▓██░░▒████▓ ▒██████▒▒
▒ ▒▓▒ ▒ ░░ ▒░   ▒ ▒  ▒▒   ▓▒█░▒▓▒░ ░  ░ ▒ ░   ░ ▒▓ ░▒▓░░▓  ░░ ▒░ ░░ ▒░   ▒ ▒  ▒▒▓  ▒ ▒ ▒▓▒ ▒ ░
░ ░▒  ░ ░░ ░░   ░ ▒░  ▒   ▒▒ ░░▒ ░      ░       ░▒ ░ ▒░ ▒ ░ ░ ░  ░░ ░░   ░ ▒░ ░ ▒  ▒ ░ ░▒  ░ ░
░  ░  ░     ░   ░ ░   ░   ▒   ░░        ░ ░     ░░   ░  ▒ ░   ░      ░   ░ ░  ░ ░  ░ ░  ░  ░  
      ░           ░       ░  ░                   ░      ░     ░  ░         ░    ░          ░  
                                                                              ░               
"""
print(Fore.YELLOW + text ,Fore.WHITE)
print(f"Join{Fore.YELLOW} Telegram | https://t.me/xfff0800 {Fore.WHITE}for exclusive FREE tools")
print(f"{Fore.WHITE}By {Fore.YELLOW}0xfff0800 1.2\n")

user = input (f"{Fore.WHITE}Username --> ")
flo = input (f"{Fore.WHITE}Password --> ")
url = "https://gcp.api.snapchat.com/scauth/login"
payload = "device_check_token=AgAAAPT%2BXCouCrlJodXkIuWSN3EEUNk0%2Bme89vLfv5ZingpyOOkgXXXyjPzYTzWmWSu%2BBYqcD47byirLZ%2B%2B3dJccpF99hWppT7G5xAuU%2By56WpSYsAQp%2FiLfcTV3fxO1erU2rCCKkAzakDkotrg5BCL0VAeAVdO953xMLVslL2kMd5QLeUs5Giqx%2B%2Fc%2BxMvdv%2FvdStazbAgAAPqKUP9J88R9IAKl%2FcUwu5wDt6JlAtS4Qh46ytGUT45gITIY5RlT8Udxr%2BFDx%2BbyrkEWq%2FpOeno0nf7jZriLp9qOa%2BxtRXB%2BWGLBAvmYzglEkQasf0ekDJPBqGixkZOaKHSf%2FBTmGYPEWnfuoy5QbY9BZ3lieMxOXcEqvFmhW1vV62Y0u%2BipvfoiPR2N1v3R3rmjiIwJJ9zNu%2FTqfU3TmNK8NHyi4LM880zCUiyLf9XMiIVzk19Qq465TaydDlkv46SpioZTGro%2Bc3j6OpGeOmmR0qRscQhqL3MCi8tNgSurHZ%2FGdhOG3PRpVAtuONsU3WXQFUJWMOYlBnQScvoiL9JK0k%2BrAnIYVMipuPv53FXqE7jD7mWCCTqM8FJo8g5Nb2J1CWSBmixKidAhyTbVxqBlZvuYz2BOoSIj1X32aZR5A5UUvVGOkJSFFE0sCsyK7qE4xNWjMh%2BibvJccQWLee4dIR0QjgIXlls6xfr8jSwKHCsah%2BF1YWoN0Qu4p2bRxHBccLUv9cFRLfGYvNqfHOBymp9OuVIIzBNQ8B9N4hKrvVAlbNPSK8FmPlq2V60yjGP7N%2BJ23MXoXydS6q1CAumpWQXpNaUVAzp6GgyzjeAAHDftvDMaLvxvKcL%2FwNA4IOM0o2dDogSEnHANqvYDN6MxHK1fD1DZIH8VeP6mjVdt0Ln1AClf7u%2FYEAm%2FsX6MVkF8s10qrAAT%2B3%2BpdIWPex8pX8fzjIpSrvEi24ZFj2pk1FxcXU4GS1qxFg3V38M9APkW72kDweJ8QkzrvBDPJzOTao7xGvBmbVlJw14aV7iaN7%2FAYCOjnFEZhoT4ezfoDREKGTnMdgxcsG%2FQ2lbh9Bq8guDBSjlifxXw9ltgjXANUGUuN9Jp5TwDEumL5yEU6cJ9VniQOso3ef9jNhlHZuorPaxXUyG3FHbC3mz1hBOPY%2BwtZ6HxVFssLb1BeQISOgRdW4FLK2%2BVjd85ZZLJSEeoJS2%2Fqumi90Z50mA4PvmmqjysdzmHxMpkNugTenyi3uGJK9kOWGgxMVBc7lXnvLUzr9FlTsZF6Qfvd8RiiLC7qE%2BzVGbOarxFggTY6wwX%2BRailhjULSLhEAjtFtWcdk%2Bh1h%2B04YnvkFAO7TCZD3cY0fjOBliMHMx1nyOBqtznNhAmTel7szr2w3nzDPmEwBwy3SGp2Sx8Rk2rWhvJtAue0MSQ%2FO3y%2Fdw3EygvkYOU2xGCG%2F2VdTsuUwnG5rlhfOOLwrICaV%2FHZH7wv4f4eN6Z6tYtiDsB1GkCT7%2F0Ouno0Zwemar4z7bWeuqEg7ubDMCmxathJtQlN7EQgvH59Ztm29arw7%2F%2BAFtVpB%2FfaK9hGbk2y6JCZTU5iPR2aqqSeA3tSH5L1w5ld9RHv%2BoGrDVpjETaUClZ7CrwfQQ6%2FjCU1IiLGlmyfHVB4j0RLGeVKvYXyldu48Mi1dcdv97tm0ghOU6mAus%2BnMmRu%2Fw7Ihg0X%2BHOi8fojpRK1r%2B6tWGwjdEJc8GKOGEd0feWjatjvt6KLnWLfV4UGlDAeWE%2BYiDQAy7FAj0WGgoloPpsPp5cCpjRyEa3tAte4l5uXfePgxu9uiIqgXk0ck4OGVb2LWLpll5xRkRK9r8pOLdf02siClXkr2FAtQz9JyDxlfzMfhZuxJzNs0hOmhK%2Bs77PzoezRhBaRDwFIdWfbs86CkvYAXxRHPjgZk%2FgSivIZyCnYvo5dbydWXo2DBN%2BqkWQe5X8okWaj3tGTGI80tDVahMXtXMJSJr01GRvy1m2dgXmLX0Ilncw3sepEvHBergg6ErXP11RUi%2BbfdHmk5abMX5XotQXoYUoEYQUC8REr%2BDeUWeoWr8ldCQtv%2FwnK9zGzMDzdY2naTD18zvgV5U3adVEGc0QiIF5e%2FuS8dzW5vzngUMUMHtvGb4DgzNsB%2BO%2BD0wKc49cFoQrkEDhYGSd8p3q3pe4rDaUuBa4x6nISt4yDmwh8oTfotJD4Y4Upi61kvcx0y61yn62dOn2ssOPuqzO2Q7E0EvCRbaBGctuG7WcZQ8kkIbfcYpaO2dJ5pdEVtyUN4yfQC0fHXOZdJVPVqc2Liq39KmC0pQ3RTZqlmEipqocRiEaqDBRU%2BwXYB%2ByyyEoatPxwuvnRhzYVV1rbHN1sVnz629zfTtLvPuk91fQwdarcoJRe6L64ra6HQrxFbLURg68RQ5HsG2%2B93wwk0IO3Q3zhqbDyagsWrcYRF%2F74qa%2BE%2BecDgGURyV6XIFgcsojLjl7mkbPAmkRLq%2BxR8f%2FviPkpZfSoVZyREDeK3v3sKjEL7kp8KeR%2B9AJ39fR6CGiFEvb6BqxC0T3p09zMEjO5FgWnSH4qpR6NzeSlR2E1wcE3%2FhwADKn42AY1hsp9Uxa%2FUpMGqHgBGREQXbquPOBUttmEsb9cSX3JZxwunTOqjCbEB0wUx4j8M46wx0OyAgIvDCA9yTP%2FEMMiBiM61vpA8Z1FLjSQLAj3tvMt2OmpL5tlkaWjzbUMnqte59gU78tekeG7tBhCBYhxpJQsB3HmdW%2BK2PwmzePbXraqVg9tm1jISAHQ3O7o8U8Jkure0Ywm1gxtGz763CcOXbCcBi41Vcp0rkIyaytIYKEl1%2FlHucc1mxrOpHO3PpP5IbsUcOgweKcuSruqcsbF%2FdlP5y3fKV1TlGgzwIgAaK%2Ff1ElC8PrJ6MwFeYzxgGa%2B7l2gykrYPCvgqHY%2BsbaZk8c%2BlypWDAAkiYJyJJFJ7zkUSNqHXKYOOfH4VE0XBWtf342jXu4rHmXSOPRT6Op%2Fis2TMJLfpa%2B8aUieCWJwJIEWXIaQ8fxfr%2FiOpdeevhEm35yxadmXLT6Tot2GcsR657GEo6UMYjzj6fkSU%2FEHqXzVpZHFi38rNBeZv1%2FnDHM%2B%2BGF&device_id=331942&fidelius_client_init=%7B%22new_fidelius_version%22%3A9%2C%22hashed_out_betas%22%3A[%220oduqrFHUCWrIbZS0m9NXlOgGH91KFwtzMP37CfbAQY%3D%22%2C%22QCWtWFftU%2BhFPn5iFHdyd3JWBdZWt2Uwm8xvAjNli5g%3D%22]%2C%22new_hashed_out_beta%22%3A%220oduqrFHUCWrIbZS0m9NXlOgGH91KFwtzMP37CfbAQY%3D%22%2C%22new_iwek%22%3A%22dLw4NA0BpDxqDK0dxNgERCbSDTiw19neE0zcy33qVps%3D%22%2C%22new_out_beta%22%3A%22MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAES%2FbINcgIJxyB8sZyg9YMfr2qnTGHKPe3VnRfH8J9gNezsLxs4tmPUHRfmpo3xEM8EuMtGqnizpBSGOjPEePKlQ%3D%3D%22%7D&from_deeplink=false&height=1334&nt=1&odlv_pre_auth_token=&password="+ flo +"&pre_auth_token=&ptoken=%7Blength%20%3D%2032%2C%20bytes%20%3D%200xeb81879c%206ed5e60d%20c7ee56be%201e0272ce%20...%2058450616%2057ee7e04%20%7D&reactivation_confirmed=false&remember_device=true&req_token=93052650fa41a0286ecad6e9f4af2b6454ed4d8d19f3da8539b4f314dac5136b&screen_height_in=0&screen_height_px=667&screen_width_in=0&screen_width_px=375&timestamp=1675366128923&username="+ user +"&width=750"
headers = {
        "X-Snapchat-Uuid": "D348BDC9-2FA4-4BB9-A7CC-5595250FB823",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        "User-Agent": "Snapchat/11.79.0.31 (iPhone9,3; iOS 15.7.5; gzip)",
        "X-Snapchat-Att": "CgsYACAAFQwxDa8IChLYAkweKwxW4Yz7NoHAVk59z4BRtp5N88IYTAQaZYGGVlGN0B8ArUw9E4f0dpoFqA1TnLoRro8c7jI6VfUunOvKKXICY00VnPIf3NgYXu2EmGmc2snkdJuBNb9qkvc75_SsiWmgPKTO3w0A9xTJP91sJJgDZ2ZI4LoSHWUuT0T7jJSbsHiDtFA2RGC5vBuMsRUqfPcxWm2vzAhAzhygdCTSzE_g8W1937dqkDKEJHlmX6nyJqGcD8D-aLBvpsoDm5LpgWd6_cxWGNHtZhRZuRJcHmnjQJcHuF9aVU6gfYvn9x6gISH8TYaTeWOauL-REcyKBMUorfid5a8s6Jt7AE4dgIX1ofnxewqEB34WwCYnSJkgI6bTrTuitrW3Tt9_sEjk0rO7kg_FAEdzN4Y0pxqJ1CjHz-APpfI_mxA-gyZx2a3xKxZA6Sav3CDZG0IMjn4QXIALe37w0mrs",
        "Host": "gcp.api.snapchat.com"
    }
response = r.post (url, data=payload, headers=headers).text
info = json.loads (response)
nb = 0
if 'updates_response' in response:
    try:
        print (f'{Fore.GREEN}Good login [👍]{Fore.RESET}','username : ' + user + ' | password : ' + flo )
    except:
        print ("There may be an error in verification. There is no email or phone number for the account")

elif 'logged' in response:
        print(f'{Fore.RED}Error login [🚨]{Fore.WHITE}',"Oops! We could not find matching credentials")
        exit()

if 'data' in response:
    for i in range (3000):
        nb+=1
        try:
              ff = info["friends_response"]["friends"][i]["ts"]
              operationTwo = int(str(ff)[:-3])
              datetime_obj=datetime.fromtimestamp(operationTwo)
              print (f'{Fore.YELLOW}',nb,f' | {Fore.RED}Your followers [🫠]{Fore.RESET}',"--> Username : " + str (info["friends_response"]["friends"][i]["name"]) , f'{Fore.CYAN}' ," --> Name : " + str (info["friends_response"]["friends"][i]["display"]),f'{Fore.MAGENTA}',' --> add friend time : ' f'{Fore.WHITE}',f'{Fore.WHITE}New username [🚨]{Fore.WHITE}','--> ',f'{Fore.RED}' , str (info["friends_response"]["friends"][i]["mutable_username"]),f'{Fore.WHITE}',' | ',datetime_obj)
        except:
              pass
if 'two_fa_needed' in response:
    try:
        print (f'{Fore.RESET}Good login -> [🛡️]{Fore.RED} Oops 2FA [🔐]')
        print (f'{Fore.RESET}sms 2FA [🛡️]{Fore.CYAN}' , " --> " + str (info["is_sms_two_fa_enabled"]))
        print (f'{Fore.RESET}token 2FA  [🛡️]{Fore.CYAN}' , " --> " + str (info["pre_auth_token"]))
        print (f'{Fore.RESET}number 2FA  [🛡️]{Fore.CYAN}' , " --> " + str (info["phone_number"]))
    except:
        exit ()
