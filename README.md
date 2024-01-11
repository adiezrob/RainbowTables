# Este repositorio contiene recursos que he creado para el trabajo opcional de SGSSI.

## Ejercicio 1
El fichero [ejercicio1.py](ejercicio1.py) es la solución al primer ejercicio que propongo en el informe.

## Ejercicio 3
[pt2hash.py](pt2hash.py) es el fichero con el que transformo [este](https://github.com/DavidWittman/wpxmlrpcbrute/blob/master/wordlists/1000-most-common-passwords.txt) fichero de passwords en otro de hashes NTLM de ellas.

[NTLM-1000-most-common-passwords.txt](NTLM-1000-most-common-passwords.txt) es el fichero que consigo al ejecutar [pt2hash.py](pt2hash.py), y el que hay que crackear el tercer ejercicio.

[cracked_passwords.csv](cracked_passwords.csv) es el fichero de las contraseñas crackeadas que he conseguido en el ejercicio 3.

## Ejercicio 4
[pt2salthash.py](pt2salthash.py) es el fichero con el que transformo [este](https://github.com/DavidWittman/wpxmlrpcbrute/blob/master/wordlists/1000-most-common-passwords.txt) fichero de passwords en otro de hashes NTLM salteados de ellas.

[NTLM-SALTED-1000-most-common-passwords.txt](NTLM-SALTED-1000-most-common-passwords.txt) es la versión salteada de [NTLM-1000-most-common-passwords.txt](NTLM-1000-most-common-passwords.txt), que se usa en el ejercicio 4.
