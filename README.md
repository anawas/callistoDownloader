# callistoDownloader
Hello World! 

calliistoDownloader is a python package for downloading spectrograms sourced from the [e-Callisto](http://www.e-callisto.org), which is an international network of solar radio spectrometers.

This package allows for bulk downloads of spectrograms for a given set of days in a given month and year, for a list of given instruments (visit [link](http://soleil.i4ds.ch/solarradio/data/readme.txt) for a list of all instruments from which the data is sourced).

The downloads are structured within a <code>e-Callisto</code> directory inside the working directory. The same is illustrated below:


```
working directory/
└───e-Callisto/
    └───yyyy/
        └───mm/
            └───dd/
                └───file1..
                    file2..
```

## Functions of this package:
<code>which_years()</code>

<code>which_months(select_year)</code>

<code>which_days(select_year, select_month)</code>

<code>download(select_year, select_month, select_days, instruments)</code>

<code></code>

<code></code>

<code></code>

