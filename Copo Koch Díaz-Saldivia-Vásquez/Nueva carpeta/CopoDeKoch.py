#####################################################################################################################################
#CopoKoch.py
#Copo de Nieve de Koch
#Integrantes: Daniel Díaz, Nicolás Saldivia y Sebastián Vásquez.
import turtle as t
#####################################################################################################################################
def main():
  iterac = leeIteraciones()
  segmento = leeLongitudSegmento()
  inicializaTortuga(segmento,iterac)
  CopoNieveKoch(iterac,segmento)
  t.done()
#####################################################################################################################################
def valida(men):
  class Error(Exception):
    pass
  class vacio(Error):
    pass
  class espacios(Error):
    pass
  class rango(Error):
    pass
  men1 = ("Ingrese cantidad de iteraciones(0 a 5): ")
  men2 = ("Ingrese longitud del segmento(1 a 600)\npara una mejor visualización prefiera medida mayor a 200: ")
  men3 = ("""Ingrese algún numero para escojer el color del fondo...
Las opciones son las siguientes:
  1 = Plateado
  2 = Rojo Navideño
  3 = Verde Navideño
  4 = Azul
  5 = Violeta Oscuro
  6 = Teal
Ingrese N° de opción: """)
  if(men == 1):
    men = men1
  elif(men == 2):
    men = men2
  elif(men == 3):
    men = men3
  sigue = True
  while(sigue):
    try:
      x = input(men)
      if(len(x) == 0):
        raise vacio
      if(len(x.strip()) == 0):
        raise espacios
      if(men == men1):
        if((int(x) < 0) or (int(x) > 10)):
          raise rango
      if(men == men2):
        if((int(x)>6000) or (int(x)<1)):
          raise rango
      if(men == men3):
        if((int(x)<1) or (int(x)>6)):
          raise rango
      sigue = False
      return(int(x))
    except(ValueError):
      print("Error!! Ingresó texto: '{0}'\n".format(x))
    except(vacio):
      print("Error!! No ha ingresado nada.\n")
    except(espacios):
      print("Error!! Ingresó solo espacios.\n")
    except(rango):
      print("Error!! Ingresó número equivocado: '{0}'\n".format(x))
######################################################################################################################################
def leeIteraciones():
  ite = valida(1)
  return(ite)
######################################################################################################################################    
def leeLongitudSegmento():
  long = valida(2)
  return(long)
######################################################################################################################################
def inicializaTortuga(seg,ite):
  Op = valida(3)
  t.title("Copo de Nieve")
  t.setup(seg + 110, seg + 110)
  t.shape("turtle")
  t.speed(0)
  fondo(Op,seg)
  t.penup()
  t.goto(-seg / 2, seg * 19 / 64)#distancia desde la mitad de la pantalla
  t.pendown()
  t.begin_fill()
  if(seg < 200):
      t.pensize(3)
  t.pensize(4)
  t.color("white","#D4AF37")
######################################################################################################################################
def fondo(op,seg):
  if(op == 1):
    t.fillcolor("#A19595")
  if(op == 2):
    t.fillcolor("#EE0808")
  if(op == 3):
    t.fillcolor("#2E7D32")
  if(op == 4):
    t.fillcolor("#0277BD")
  if(op == 5):
    t.fillcolor("#8E24AA")
  if(op == 6):
    t.fillcolor("#00897B")
  t.begin_fill()
  t.penup()
  t.goto(-800, -800)
  t.pendown()
  t.goto(800, -800)
  t.goto(800, 800)
  t.goto(-800, 800)
  t.goto(-800, -800)
  t.end_fill()
  nieves = (110 * (float(("1.") + str(seg))))
  print(nieves)
  for i in range(nieves):
    t.penup()
    nieve("white",seg)
    t.pendown()
######################################################################################################################################
def nieve(wh,seg):
  import random
  p = (random.randint((int(-seg / 2) - 50),(int(seg / 2) + 50)),random.randint((int(-seg / 2) - 50),(int(seg / 2) + 50)))
  t.goto(p)
  t.pensize(seg/100)
  t.dot(wh)
  t.pensize(0.1)
######################################################################################################################################   
def CopoNieveKoch(ite,seg):
  linea(ite,seg)
  t.right(120)
  linea(ite,seg)
  t.right(120)
  linea(ite,seg)
  t.goto(-seg / 2, seg * 19 / 64)
  t.end_fill()
  t.penup()
  felizNavidad(ite,seg)
######################################################################################################################################  
def linea(ite,seg):
  if(ite == 0):
      t.forward(seg)
  else:
      linea(ite-1, seg / 3)
      t.left(60)
      linea(ite-1, seg / 3)
      t.right(120)
      linea(ite-1, seg / 3)
      t.left(60)
      linea(ite-1, seg / 3)
######################################################################################################################################
def felizNavidad(ite,seg):
  t.pencolor("white")
  if((seg >= 180) and (seg<300)):
    t.goto(5, 20)
    t.write("Feliz  Navidad",True,"center",("arial",16))
    if(ite == 0):
        t.goto(5, -20)
    else:
        t.goto(5, -40)
    t.write("Profesora!",True,"center",("arial",18,))
  elif((seg >= 300) and (seg < 380)):
    t.goto(5, 40)
    t.write("Feliz Navidad",True,"center",("arial",30))
    if(ite == 0):
        t.goto(5, -20)
    else:
        t.goto(5, -60)
    t.write("Profesora!",True,"center",("arial",30))
  elif((seg >= 380) and (seg <= 400)):
    t.goto(5, 50)
    t.write("Feliz Navidad",True,"center",("arial",37))
    if(ite == 0):
        t.goto(5, -20)
    else:
        t.goto(5, -70)
    t.write("Profesora!",True,"center",("arial",40))
  elif((seg > 400) and (seg <= 500)):
    t.goto(5, 55)
    t.write("Feliz Navidad",True,"center",("arial",40))
    if(ite == 0):
        t.goto(5, -20)
    else:
        t.goto(5, -100)
    t.write("Profesora!",True,"center",("arial",45))
  elif(seg > 500):
    t.goto(5, 65)
    t.write("Feliz Navidad",True,"center",("arial",50))
    if(ite == 0):
        t.goto(5, -20)
    else:
        t.goto(5, -130)
    t.write("Profesora!",True,"center",("arial",50))
  bailaTurtle(seg)
######################################################################################################################################
def bailaTurtle(seg):
  col = [("#607D8B"),("#EE0808"),("#2E7D32"),("#0277BD"),("#8E24AA"),("#00897B")]
  if(seg < 180):
    t.speed(0)
    t.hideturtle()
    t.goto(0,0)
    t.showturtle()
  t.speed(2)
  for i in range(50):
    for j in(col):
      t.color(j)
      for k in range(1):
        t.setheading(60)
        t.setheading(120)
######################################################################################################################################        
main()
######################################################################################################################################    
