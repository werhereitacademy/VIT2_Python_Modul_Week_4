from datetime import datetime, timedelta

def tarih():
    su_an = datetime.now()
    # print(su_an.strftime("%Y-%m-%d-%H:%M:%S"))
    
    # 2 haftalık süre
    sure = timedelta(weeks=2)
    # print(sure)

    # Bitiş tarihi hesaplama
    bitis_tarihi = su_an + sure
    
    # print("Bitiş Tarihi:", bitis_tarihi.strftime("%Y-%m-%d"))
    return su_an.strftime("%Y-%m-%d-%H:%M:%S"),bitis_tarihi.strftime("%Y-%m-%d")
