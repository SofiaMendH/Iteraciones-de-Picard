import numpy as np
import spicy as sp
from sympy import *
from sympy import Eq, simplify, exp, cos, sin, integrate, log
from sympy.abc import t, s, y
from sympy.plotting import plot
t, s = symbols('t s', real=True)
#y=Function("y")(t)
#ed=Eq(y.diff(t)-6*y,0)
#dsolve(y.diff(t)-6*y,ics={y.subs(t,0):1})
#print(dsolve(y.diff(t)-6*y,ics={y.subs(t,0):1}))
#dsolve(y.diff(t)-6*y)
#print(dsolve(y.diff(t)-6*y))
A=True
msj='\n Si desea ejecutar el programa presione enter, si quiere finalizar ingrese "salir": '
while A:
    sms = input(msj)
    sms = sms.upper()
    if sms == "SALIR":
        A = False
    else:
        act=True
        while act:
            Coef=list(map(int, input("\n Ingrese los coeficientes de y,ty,t y del termino constante, en ese orden, separados por coma (considere estos valores igualados a la prima de y): ").split(",")))
            Ci=list(map(int, input('\n ingrese la condición inicial como: "valor inicial de t, valor inicial de y": ').split(",")))
            f=Coef[0]*y+Coef[1]*t*y+Coef[2]*t+Coef[3]
            print("\n El problema ingresado es: y(t)'=",f," con y(",Ci[0],")=",Ci[1])
            indicador=input('\n Si  desea continuar presione enter, en caso contrario escriba "no": ')
            indicador = indicador.upper()
            if indicador == "NO":
                act = False
            else:
                n=int(input("\n Ingrese  la cantidad de iteraciones a realizar: "))
                print("Es momento de registrar la iterada cero:")
                Coef_y0 = list(map(int, input('\n Ingrese los coeficientes de t de sus potencias en orden ascendente (0,1,2,...), separados por coma: ').split(",")))
                ban=0
                y0=0
                Iteracion1=[]
                while ban <= len(Coef_y0) -1:
                    y0= y0 + Coef_y0[ban]*(t**ban)
                    ban = ban + 1
                p0=plot(y0,(t,-3,3),show=False, label = "Iteración 1",title="Iteraciones de Picard", xlabel="t", ylabel="y")
                print(y0)
                y1=0
                m=1
                while m<=n:
                    Iteracion=[]
                    y0=y0.subs(t,s)
                    f = Coef[0] * y + Coef[1] * t * y + Coef[2] * t + Coef[3]
                    y1= Ci[1] + integrate(f.subs(t,s).subs(y,y0),(s,Ci[0],t))
                    pi = plot(y1,(t,-3,3),show=False, label=("Iteración ",m))
                    p0.extend(pi)
                    if y0 != y1:
                        y0=y1
                        y1=0
                        m=m+1
                    else:
                        exit
            #y = Function("y")(t)
            # ed=Eq(y.diff(t)-6*y,0)
            # dsolve(y.diff(t)-6*y,ics={y.subs(t,0):1})
            # print(dsolve(y.diff(t)-6*y,ics={y.subs(t,0):1}))
            # dsolve(y.diff(t)-6*y)
            # print(dsolve(y.diff(t)-6*y))
            #sol=dsolve(y.diff(t) + Coef[0] * y + Coef[1] * t * y + Coef[2] * t + Coef[3], ics={y.subs(t, 0): 2})
            ##print("\n La solución del PVI es: ",sol)
            #Valsolx=[]
            #for i in Listax:
             #   Valsolx.append(sol.subs(t,i))
            #for i in range(len(Valsolx)):
             #   plt.plot(Listax,Valsolx[i][2], label="Solución")
            solucion=1+exp(-t**2)
            sol=plot(solucion,(t,-3,3),show=False)
            p0.extend(sol)
            p0.show()
            Final=input('\n Si desea resolver otra EDO presione enter, en caso contrario escriba "no": ')
            Final=Final.upper()
            if Final == "NO":
                act=False
                A=False




