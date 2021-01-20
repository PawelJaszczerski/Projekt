import in_out as io

try:
    io.param()
except ValueError:
    print('Proszę wprowadzić poprawne dane do pliku i uruchomić program ponownie')
else:
    try:
        io.output()
        io.preview()
    except TypeError:
        print('Proszę wprowadzić dodatnie przyspieszenie grawitacyjne')
    except NameError:
        print('Proszę wprowadzić dane do pliku i uruchomić program ponownie')
    else:
        import wykresy
        import animacja
        wykresy.wykresy()
