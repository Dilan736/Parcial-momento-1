compra=int(input("Ingrese aqui su compra"))
if(compra<50):
    print("DESCUENTO APLICADO: ",f"${0}")
    print("TOTAL A PAGAR:",f"${compra}")
elif(50<compra<=100):
    print("DESCUENTO APLICADO:",f"${(compra*0.05)}")
    print("TOTAL A PAGAR:",f"${compra-(compra*0.05)}")
else:
    print("DESCUENTO APLICADO: ",f"${(compra*0.10)}")
    print("TOTAL A PAGAR: ",f"${compra-(compra*0.10)}")