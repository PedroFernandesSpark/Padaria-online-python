#!/usr/bin/env python3
import database
import sys

database.add_admin("12345678900", "Admin", "admin@mail.com", "6140028922", "senha123")
database.add_client("24446666660", "Joao", "user@mail.com", "6134354040", "senha456")

img_file = open(sys.argv[1])
img = img_file.read()
img_file.close()
database.add_product("Pao Frances", 3.5, img, 100, "Pao Frances quentinho, perf"
                     "eito para acompanhar um cafe com leite.")

img_file = open(sys.argv[2])
img = img_file.read()
img_file.close()
database.add_product("Refrigerante", 7, img, 20, "Refrigerante bem gelado, para"
                     " comer durante um almoço ou janta.")

img_file = open(sys.argv[3])
img = img_file.read()
img_file.close()
database.add_product("Pao de Queijo", 4.9, img, 200, "Pao de Queijo feito com"
                     " queijo de verdade, perfeito para um lanche da tarde.")
