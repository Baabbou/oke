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

## Basic char

```bash
oke A
+---------------+-----------+
|    Format     |   Value   |
+---------------+-----------+
|    decimal    |    65     |
|  hexadecimal  |   0x41    |
|     byte      | 01000001  |
|      URL      |    %41    |
|   HTML name   |   None    |
|   HTML dec    |   &#41;   |
| HTML URL(dec) | %26%2341; |
|   HTML hex    |  &#x41;   |
| HTML URL(hex) | %26%2341; |
|  Js unicode   |  \u0041   |
|   URL 2ble    |   %2541   |
+---------------+-----------+
```

## Decimal value

```bash
oke -d 123
+-------------+----------+
|   Format    |  Value   |
+-------------+----------+
|   decimal   |   123    |
| hexadecimal |   0x7b   |
|    byte     | 01111011 |
+-------------+----------+
```

## Hex value

```bash
oke -h 0x10
+-------------+----------+
|   Format    |  Value   |
+-------------+----------+
|   decimal   |    10    |
| hexadecimal |   0x0a   |
|    byte     | 00001010 |
+-------------+----------+
```

## Binary value

```bash
oke -b 1011
+-------------+----------+
|   Format    |  Value   |
+-------------+----------+
|   decimal   |    11    |
| hexadecimal |   0x0b   |
|    byte     | 00001011 |
+-------------+----------+
```

# Contact

Real hackers have no contact with anyone.
