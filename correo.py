UsuarioCorreo = str(input("Introduzca el nombre de usuario de su correo electrónico: \n"))
Dominio = str(input("Introduzca el dominio de su correo. Puede ser gmail, outlook, yahoo, etc... El primer caracter de lo que entre tiene que ser una arroba. \n"))
Extension = str(input("Introduzca la extensión de su correo. El primer caracter de esta parte debe de ser un punto. \n"))
Nombre = str(input("Introduzca su nombre. Debe de tener por lo menos 3 caracteres. \n"))
Edad = int(input("Introduzca su edad. Usted debe tener entre 18 y 65 años. \n"))

Correo = UsuarioCorreo+Dominio+Extension
print("Su correo es: ",Correo)

DominioArroba = Dominio[0] == "@"
ExtensionPunto = Extension[0] == "."
CorreoValidacion = bool(DominioArroba and ExtensionPunto)
EdadValidacion = bool(Edad >= 18 and Edad <= 65)
NombreValidacion = bool(len(Nombre)>3)
print("La validez de su correo es: ",CorreoValidacion)
print("La validez de su edad es: ",EdadValidacion)
print("La validez de su nombre es: ",NombreValidacion)
