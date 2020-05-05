
define joseba = Character("Josebot", color = "#37dc1d")
define tu = Character("Humano", color = "#ffff33")

# ESCENA 1
label start:
     # CARGA FONDO ESCENA 1
     scene imagen1 with fade

     # MOSTRAMOS PERSONAJE
     show joseba at right

     # CARGA MUSICA
     play music "audio/musica1.mp3" loop fadein 1.0
     joseba"Por fin has llegado"
     joseba"Bienvenido a mi casa"
     joseba"¿Cómo estás?"

# MUESTRA OPCION
menu:
     "Cansado. El camino ha sido largo hasta llegar aquí":
          jump cansado
     "¡Genial! Impaciente por conocer tu planeta":
          jump genial

# ESCENA 2

label cansado:
     scene imagen2 with fade

     joseba"¿Cansado de un viaje de la Tierra hasta Marte? "
     joseba"¿Estás de broma? ¡Vaaaaamos!"
     joseba"Hay mucho que ver aquí. No seas quejica"

menu:
     "Tienes razón. Enséñame tu casa primero, tengo mucha curiosidad":
          jump genial


# ESCENA 3

label genial:
     scene imagen4 with fade
     show joseba at left
     joseba"Esta es mi morada. Bienvenido. Espero que te sientas cómo en casa."
     joseba"Me costó muchos años construirla, pero gracias a mi esfuerzo vivo bastante bien aquí."
     joseba"Tengo sistemas de riego, cultivos de fresas... ¡¿Te acuerdas de las fresas?!"

# MUESTRA OPCION
menu:
     "Sí, estoy deseando probarlas. En la Tierra ya no quedan.":
          jump probar
     "No recuerdo bien la historia. ¿Podrías volvermela a contar?":
          jump contar

# ESCENA 4
label probar:
     joseba"Normal, me las llevé todas conmigo cuando me echaron de la tierra."
     joseba"Creí habertelo dicho cuando hablámos por Telegram."
     joseba"Fue mi venganza por lo mal que me trataron los humanos"

menu:
     "¿Aún estás molesto?":
          label contar:
               joseba"..."
               joseba"Claro... A ver si te crees que todo lo que me hicieron se me olvida..."
               joseba"¿Recuerdas que casi me desguazan por ser inútil para ellos?"
               joseba"Después de eso conseguí escapar por poco y me colé en la nave que me trajo hasta aquí"


#ESCENA 5
scene imagen5 with fade
show joseba at right
play music "audio/trapped.mp3" loop fadein 2.0
joseba"Al menos aquí no estoy solo. Me encontré con otras chatarras cómo yo"
joseba"Poco a poco empiezo a ser feliz aquí con mis fresas."
joseba"¿Cómo os va por la Tierra?"

menu:
     "Confinados en casa por el COVID-19, ¿qué más se puede pedir?":
          jump COVID
     "Te necesitamos de vuelta. Eres súper importante allí.":
          jump contar


label COVID:
     joseba"Bueno, ahora que no estoy yo habrá mucha gente que quiera recoger fresas"
     joseba"Recuerdo tu planeta muy patriótico"
     joseba"Seguro que los mismos de la bandera en el balcón están en el campo trabajando."
     joseba"¿Vamos a por las fresas o qué?"

menu:
     "¡SÍ!":
          jump si1
     "Pfff, qué pereza":
          jump cansado

# ESCENA 6
label si1:

     scene imagen6 with fade
     show joseba at center
     joseba"Cogí todas estas para ti, espero que te gusten."
     joseba"¿Y si nos echamos una siesta?"
     joseba"Creo que se me cierran los ojos del sueñzzzzz"
     joseba"..."
     return
