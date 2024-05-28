# Por la limitante de los computadores de la universidad al no tener acceso a algunos puertos para el host se utiliza como alternativa el entorno virtual esto se hace por medio del cmd y gracias a esto no se necesitara acceso de administrador en ningun momento sin enbargo se necesita installar las librerias como tensorflow, transformers, tf-keras.

# Para abir cualquier el entorno virtual dentro del proyecto se utilizan los siguientes comandos dentro del cmd:x

 cd C:\Users\usuario\Documents\Servicio-Anallisis-Sentimientos-Textos-Largos

# modificando dependiendo de donde se guarde el prototipo

# seguidamende se crea mediante

 python -m venv venv

# luego lo activamos

 venv\Scripts\activate

# instalamos las dependencias

 pip install flask transformers nltk
 
# instalamos tambien las librerias de PyTorch y tf-kera

pip install torch torchvision torchaudio
# De ser nesesario agregamos esta libreria
pip install tf-keras


# Iniciamos el servidor y podremos acceder mediante la URL que nos da el cmd

python modelo_entrenado.py

# En cualquier caso de necesitar cualquier libreria descargarla de la misma manera que las demas

# este Prototipo Analizara los sentimientos de el comentario o texto dependiendo de las palabras utilizadas y calculara un porcentaje de seguridad que se refiere a que tan seguro esta de que el sentimiento sea desde muy negativo hasta muy positivo dependiendo de lo largo que sea el texto y de las palabras utilizadas ya que analiza palabra por palabra.

# Mariana Ospina Perez y Angel Stiven Pinzon Sanchez prototipo Analisis de sentimientos de textos largos
