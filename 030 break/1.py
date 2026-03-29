# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# ┃                                                            ┃
# ┃  break - sındırmaq deməkdir, while ilə yaranan döngünü     ┃
# ┃  sonlandırır.                                              ┃
# ┃  Heç nə daxil etmədikdə döngü davam edir, bir şey yazdıqda ┃
# ┃  dayanır.                                                  ┃
# ┃                                                            ┃
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

while True:

    ad = input('Adinizi daxil edin: ')

    if ad != '':

        break

# Output:
# ──> (İstifadəçi heç nə yazmazsa döngü davam edir)
# ──> (İstifadəçi bir şey yazdıqda döngü dayanır)