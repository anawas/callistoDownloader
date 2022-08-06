from callistoDownloader import callistoDownloader as cd

instruments = cd.instrument_codes(2022, 8, 5)
instruments = sorted(instruments)
for i in instruments:
    print(i)
