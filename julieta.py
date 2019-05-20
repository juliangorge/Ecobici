def cuentas_bloqueadas (usuarios_bloqueados, suarios):
    claves_usuarios = usuarios.keys()
    clave_de_desbloqueo = hola
    for i in usuarios_bloqueados:
        print ((i+1), usuarios_bloqueados[i])
    usuario_a_desbloquear = validar_dni ()
    if usuario in usuarios_bloqueados :
            palabra_secreta = input ("Ingrese la palabra secreta: ")
            if palabra_secreta == clave_de_desbloqueo: 
                print ("Su usuario ha sido desbloqueado.")
                usuarios_bloqueados.remove (usuario)
            else: 
                palabra_secreta = input ("La clave ha sido incorrecta. Ingresela nuevamente: ")
    else:
        print ("Su usuario no esta bloqueado.")