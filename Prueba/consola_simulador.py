import modulo_simulador as sim
import time
def correr_tiempo(intervalo,t_total,resolucion):
    t_transcurrido=0
    while t_transcurrido<t_total:
        print(sim.dibujar_pantalla(resolucion))
        print("tiempo transcurrido:",t_transcurrido)
        sim.actualizar_gravedad(intervalo)
        time.sleep(intervalo)
        t_transcurrido+=intervalo
def iniciar_aplicación():
    print("Simular el movimiento de un planeta")
    ejecucion=True
    while ejecucion:
        total=float(input("¿Por cuantos segundos deseas simular el movimiento? (más de 25 es aburrido): "))
        res=int(input("¿Que tanta resolución deseas usar? (se recomienda 50): "))
        inter=float(input("¿Cuál quieres que sea la duración de los intervalos de simulación? (se recomienda entre 0.02 y 0.005): "))
        correr_tiempo(inter, total, res)
        if(input("si desea continuar la simulación presione 1")!="1"):
            ejecucion=False
    print("Adios, nos vemos la próxima vez")
iniciar_aplicación()