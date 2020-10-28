str = "28/10/2020"
print("Вот дата по русски - ", str)

date = str.split("/")
en_date = date[2] + '-' + date[1] + '-' + date[0]

print("Вот что получилось - ", en_date)
