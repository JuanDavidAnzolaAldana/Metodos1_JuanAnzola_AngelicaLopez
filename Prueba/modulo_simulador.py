constgrav=0.0000000000667
vpx=0#velocidad planeta en x
vpy=106#velocidad planeta en y
ppx=25#posición planeta
ppy=50
mp=200000000000000#masa del planeta
rp=1.6#radio del planeta
ve1x=-0#variables de estrella 1
ve1y=-5
pe1x=50
pe1y=50
me1=400000e10
re1=4.5
def calcular_fuerza_gravedad(masa_1: float, masa_2: float, distancia: float)->float:
    return (constgrav*masa_1*masa_2)*distancia**-2
def actualizar_fisicas(apx,apy,ae1x,ae1y,tiempo):
    global ppx#actualiza posiciones
    global vpx
    ppx+=vpx*tiempo+apx*tiempo**2/2
    global ppy
    global vpy
    ppy+=vpy*tiempo+apy*tiempo**2/2
    global pe1x
    global ve1x
    pe1x+=ve1x*tiempo+ae1x*tiempo**2/2
    global pe1y
    global ve1y
    pe1y+=ve1y*tiempo+ae1y*tiempo**2/2
    vpx+=apx*tiempo#actualiza velocidades
    vpy+=apy*tiempo
    ve1x+=ae1x*tiempo
    ve1y+=ae1y*tiempo
def calc_dist(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
def actualizar_gravedad(tiempo):
    distpe1=calc_dist(ppx, ppy, pe1x, pe1y)#calcula la distancia entre el planeta p y la estrella e1
    fpe1=calcular_fuerza_gravedad(mp, me1, distpe1)#calcula la fuerza gravitacional entre p y e1
    actualizar_fisicas((fpe1*(pe1x-ppx)/distpe1)/mp, (fpe1*(pe1y-ppy)/distpe1)/mp,\
                       (fpe1*(ppx-pe1x)/distpe1)/me1, (fpe1*(ppy-pe1y)/distpe1)/me1,\
                       tiempo)
def dibujar_pixel(x,y):
    if calc_dist(x, y, pe1x, pe1y)<=re1:
        return "#"
    elif calc_dist(x, y, ppx, ppy)<=rp:
        return "8"
    else:
        return " "
def dibujar_pantalla(resolucion):
    x=0
    texto=""
    while x<(resolucion*2):
        y=0
        while y<(resolucion*2):
            texto+=dibujar_pixel(x*50/resolucion, y*50/resolucion)
            y+=1
        texto+="\n"
        x+=2
    return texto