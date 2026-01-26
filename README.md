# lightgun-controllers

SVG images of lightgun controllers showing controls for **Batocera Linux**.

## Color codes for each lightgun

### AE lightgun
| Color name | RGBA |
|-----------|------|
| Black    | `#333333FF` |
| Grey     | `#C8B7B7FF` |

### Aimtrack
| Color name | RGBA |
|-----------|------|
| Grey    | `#CCCCCCFF` |
| Red     | `#D35F5FFF` |

### GunCon 2
| Color name | RGBA |
|-----------|------|
| Blue      | `#7785CCFF` |
| White     | `#FFFFFFFF` |

### GunCon 3
| Color name   | RGBA |
|-------------|------|
| Orange      | `#FF9955FF` |
| Dark orange | `#BA6B33FF` |
| Light grey  | `#E3DBDBFF` |
| Grey        | `#AC9393FF` |

### Sinden
| Color name | RGBA |
|-----------|------|
| Red       | `#ED5555FF` |
| Cream    | `#FFF6D5FF` |

### XGunner
| Color name   | RGBA |
|-------------|------|
| Khaki green | `#7A857AFF` |
| Light khaki | `#B3B9B3FF` |
| Orange      | `#FF9600FF` |
| Dark orange | `#CD7900FF` |

# Command to generate png from svg
for i in $(ls svg | sed -e s+'\.svg'++); do convert -background none svg/$i.svg -resize 1000x1000 png/$i.png ; done

# Contributors
Initial work by Antoine Rochat
