# Oke

Github for **OKE**: Over Kill Encoder (pronounced oké). The tool reference some forms of encodings or representations of the given value. Output is colored :)

Enjoy !

# Install

```bash
chmod +x scripts/install.sh
sudo scripts/install.sh
```

# Uninstall

```bash
chmod +x scripts/uninstall.sh
sudo scripts/uninstall.sh
```

# Use

```bash
usage: oke [-h] [-c] [-d] [-x] [-b] [-f FULL_TYPE] value [value ...]

OKÉ: A tool to convert anything into anything.

positional arguments:
  value                 The value you need to encode (as a char by default).

options:
  -h, --help            show this help message and exit
  -c, --char            The given input is a char.
  -d, --dec             The given input is a decimal.
  -x, --hex             The given input is a hex.
  -b, --byte            The given input is a byte.
  -f FULL_TYPE, --full-type FULL_TYPE
                        Convert a whole text and precise the type.
```

## Basics char

You will get all the forms of encoding in once for a single char :

```
oke 'A'
+------+-----------------+--------------+
| Type |     Format      |    Value     |
+------+-----------------+--------------+
|  0   |      given      |      A       |
|  1   |     decimal     |      65      |
|  2   |   hexadecimal   |     0x41     |
|  3   |      byte       |   01000001   |
|  4   |       URL       |     %41      |
|  5   |   HTML named    |     None     |
|  6   |    HTML num     |    &#65;     |
|  7   |    HTML hex     |    &#x41;    |
|  8   | URL(HTML named) |     None     |
|  9   |  URL(HTML num)  | %26%2365%3b  |
|  10  |  URL(HTML hex)  | %26%23x41%3b |
|  11  |     unicode     |    \u0041    |
|  12  |      URL2       |    %2541     |
+------+-----------------+--------------+
```

You can also precise another form of encoding as input (here in decimal) :

```bash
oke -d 65
+------+-------------+----------+
| Type |   Format    |  Value   |
+------+-------------+----------+
|  1   |    ASCII    |    A     |
|  2   |   decimal   |    65    |
|  3   | hexadecimal |   0x41   |
|  4   |    byte     | 01000001 |
+------+-------------+----------+
```
> Also avaliable in hex or in binary

## Encode a string

```
oke '<img src=1 onerror=alert(1)>' --full-type 6
&#60;&#105;&#109;&#103;&#32;&#115;&#114;&#99;&#61;&#49;&#32;&#111;&#110;&#101;&#114;&#114;&#111;&#114;&#61;&#97;&#108;&#101;&#114;&#116;&#40;&#49;&#41;&#62;
```
> Precise the type using the left column when `oke A` (here type 6 is for `HTML num`).

```bash
oke 'salut les nazes' -f 4
%73%61%6c%75%74%20%6c%65%73%20%6e%61%7a%65%73
```
> Here full-type 4 is for URL encode.

# Contact

Real hackers have no contact with anyone.
