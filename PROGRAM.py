import in_out as io

try:
    io.param()
except ValueError:
    print('proszę wprowadzić dane do pliku tekstowego i uruchomić program ponownie')
else:
    io.output()
    io.preview()
    import wykresy
    import animacja
    wykresy.wykresy()
    animacja.animacja()
