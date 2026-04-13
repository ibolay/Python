# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  mövcud deyeri deyişmek üçün açar sözden istifadə          ┃
# ┃  edirik. get() metodundan istifade etmek olmaz             ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


telebe = {
    "ad"    : "Mehman",
    "yas"   : 20,
    "seher" : "Gəncə"
}

telebe["yas"] = 21 

deyer = telebe["yas"]

print( deyer )

# Output:
# 21