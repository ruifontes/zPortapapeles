# Manual de zPortapapeles

Este complemento tiene la base del complemento Fake Clipboard Announcement.

Con zPortapapeles tendremos el anuncio de las pulsaciones de copiar, pegar, deshacer, cortar y seleccionar todo.

Se incluyo al complemento la posibilidad de activar y desactivar sonidos que refuercen los mensajes al igual que un historial con el que podremos copiar al foco.

## Gestos de entrada...

En el apartado de Gestos de entrada... de NVDA si buscamos la categoría zPortapapeles podremos añadir una combinación de teclas que no viene asignada por defecto al historial para mostrar el dialogo.

También tendremos un apartado donde poder modificar las teclas disparadoras referidas al portapapeles, este apartado solo modificarlo si nuestro lenguaje o sistema tiene otras teclas asignadas por defecto al portapapeles.

## Opciones del complemento

En las opciones del NVDA en la categoría Opciones de zPortapapeles podremos activar y desactivar a través de casillas de verificación tanto si deseamos sonidos como si deseamos tener el historial activado, también se podrá elegir si se desean recibir mensajes hablados.

Si la casilla del historial esta activada tendremos un cuadro combinado en el cual elegir el tiempo de monitoreo del portapapeles y una casilla para activar o desactivar si queremos un sonido cuando se agregue algo al historial.

Si la casilla esta desactivada tanto el cuadro combinado como el poder elegir si queremos sonidos en el historial no aparecerán.

Advertir que si empezamos a recibir errores del portapapeles es conveniente aumentar el tiempo de monitoreo del portapapeles.

## Dialogo del Historial

Este dialogo tendremos que asignarle en gestos de entrada una combinación de teclas por defecto no viene asignada.

El dialogo solo se abrirá cuando tenga una entrada guardada, mientras no tenga entradas no podremos abrirlo.

Todo se nos informara con mensajes informativos al igual si ya tenemos el dialogo abierto.

Una vez abierto el dialogo consta de la lista de entradas que tenga y 4 botones que son los siguientes:

* Borrar o Alt+B: Si pulsamos este botón borrara la entrada que la lista tenga el foco.

* Borrar todo o Alt+T: Borrara todas las entradas del historial.

* Refrescar o Alt+R: Refrescara el historial con las nuevas entradas agregadas, esto va bien por si agregamos al historial mientras el dialogo esta abierto.

* Cerrar o Alt+C, Escape o Alt+F4: Cerrara el dialogo del historial.

Cuando estamos en la lista si pulsamos INTRO la entrada que tenga el foco se copiara a la aplicación que este detrás del dialogo de historial.

Por ejemplo si tenemos abierto el bloc de notas y abrimos el historial y pulsamos INTRO en la primera entrada copiara al bloc de notas el item que tengamos seleccionado.

## Limitaciones de zPortapapeles

zPortapapeles no es compatible con otros complementos que estén instalados y que hagan lo mismo, como Fake Clipboard Announcement o Clipspeak. Puede haber otros, y en este caso tendrá que desactivarlos si desea usar zPortapapeles.

Apuntar que las entradas en el historial se borrarán cuando reiniciemos NVDA.

El historial de portapapeles de Windows puede tener entradas duplicadas si usamos el historial de zPortapapeles. Tendremos que elegir cual deseamos usar.

## Agradecimientos

* Javi Domínguez: Por su ayuda desinteresada y por contribuir con la función de monitoreo del portapapeles.
* Portugués Brasil: pedro-hdias
* Ruso: Valentin Kupriyanov
* Turco: Umut KORKMAZ
* Italiano: Alessio Lenzi
* Francés: Rémy Ruiz
* Árabe: Wafiq Taher

# Registro de cambios.
## Versión 0.4.

* Agregado modo juego.

Para activar dicho modo tendremos que asignarle un gesto en el gestor de entradas.

Este modo ira bien para aquellos juegos que copian al portapapeles y necesitan de traducción.

En opciones del complemento tendremos la posibilidad de aumentar el refresco de actualización del portapapeles y la posibilidad de elegir el idioma destino de la traducción.

El idioma origen en este caso del juego se detectara automáticamente y se traducirá lo copiado al portapapeles al idioma que hayamos elegido.

Mientras el modo juego esta activado todas las ordenes del resto de complemento quedan deshabilitadas incluido el historial del portapapeles.

## Versión 0.3.1.

* Se reescribió la función de impedir la ejecución del complemento en pantallas seguras.

* Agregado idioma Árabe.

## Versión 0.3.

* Agregado detección si hay texto seleccionado al copiar.

Ahora el complemento cuando demos a copiar si no detecta texto nos informara con un mensaje.

* Agregado el poder desactivar y activar rápidamente las funciones del complemento respecto al portapapeles.

En gestos de entrada podremos configurar una combinación para activar y desactivar rápidamente lo referido al portapapeles.

Cuando lo desactivemos el portapapeles y los mensajes serán los nativos de Windows junto a los mensajes que NVDA tenga predefinidos para el portapapeles.

Esto no afectara al historial que si esta activo seguirá activo.

* Agregado compatibilidad con teclados que usen caracteres cirílicos.

Se soluciono un problema en distribuciones de teclado que usan caracteres cirílicos.

* Agregados idiomas Ruso, Turco, Italiano y Portugués Brasil.

## Versión 0.2.

* Cambiadas todas las funciones del portapapeles a cTypes

Ahora el portapapeles se manejara directamente con funciones del sistema evitando usar las funciones de NVDA y wxpython.

* Preparado el complemento para ser traducido.

## Versión 0.1.5.

* Hablar lo copiado al portapapeles y agregado al Historial.

Si tenemos activada la opción Activar o desactivar el historial del portapapeles en las opciones del complemento ahora tendremos esta nueva opción.

Con esta opción lo copiado al historial o si ya se encuentra en el historial lo ultimo copiado al portapapeles se leerá con NVDA.

Solo se mencionara lo ultimo copiado y una única vez para no saturar hasta que no vuelva a decir otra cadena copiada no se volverá a repetir la anterior.

* Se borrara el portapapeles cuando inicie el complemento por primera vez.

Ahora ya no se copiara lo que tuviéramos en el portapapeles cuando iniciábamos NVDA, ahora el portapapeles empezara limpio.

Esto no afecta al historial de portapapeles de Windows.

*** Advertencia: esto tenemos que tenerlo en cuenta ya que se puede borrar algo importante que tuviéramos en el portapapeles. ***

## Versión 0.1.4.

* Cambiada la forma de obtener los datos del portapapeles.

## Versión 0.1.3.

* Se subió el requisito del complemento a NVDA 2021.2 como versión mínima para poder ser usado.

* Se agregaron opciones para el historial.

Ahora podremos elegir el tiempo de monitoreo como si deseamos un sonido cuando algo se copie al historial.

* Se agrego compatibilidad con Word y Excel para que no anuncie las teclas del portapapeles.

* Ahora se monitorea el portapapeles por lo que cualquier complemento que copie al portapapeles ya es compatible, incluso el copiado de NVDA al foco

## Versión 0.1.2.

* Se agrego Activar o desactivar anuncios hablados del portapapeles en opciones

En las aplicaciones permitidas nos omitirá los mensajes correspondientes a las teclas del portapapeles.

## Versión 0.1.1.

* Se cambio la forma de gestionar las capturas del portapapeles y su gestión.

* Se arreglo el error que dejaba abierto el portapapeles.

## Versión 0.1.

* Versión inicial.