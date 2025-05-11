
import pandas as pd

clicks = pd.read_csv("click_logs.csv", header=None, names=["Waktu", "ID", "IP", "Negara", "UserAgent"])
wa = pd.read_csv("wa_users.csv", header=None, names=["NoWA", "Pesan"])

# Cari ID unik dari pesan (format: /id XXXXX)
wa["ID"] = wa["Pesan"].str.extract(r"/id\s*(\w+)")

# Gabung berdasarkan ID
result = pd.merge(clicks, wa, on="ID", how="left")
result.to_csv("hasil_gabungan.csv", index=False)

print("✅ Data berhasil digabung. Cek file hasil_gabungan.csv")
