# backup_to_zip
## Description
Copies an entire folder and its contains into a zip file whose filename increments. 
## How to use
Open the program by terminal. 
Write as frist argument the folder to bacup to zip.
The second optional parameter is the folder destination. If you dont write folder destination, the program will use the parent folder.
## Use example
**$ python3 main.py "user/myfoldertobackup" "user/folderdestination"** #Specify folder to backup

**python3 main.py "user/myfoldertobackup"** #Use parent folder as destination

# backup_to_zip (ESPAÑOL)
## Descripción
COpia un folder completo y su contenido, a un archivo zip con un nombre que incrementa.
## Cómo usar
Ejecutar el programa desde terminal. 
Escribe como primer argumento el folder a comprimir. 
El segundo parámetro opcional es el folder de destino. Si no especificas un folder de destino el programa usará el directorio padre.
## Ejemplo de uso
**python3 main.py "user/myfoldertobackup" "user/folderdestination"** # Especificar folder para respaldar.

**python3 main.py "user/myfoldertobackup"** # Usar el directorio padre como destino
