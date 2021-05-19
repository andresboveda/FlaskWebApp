#!/usr/bin/python3.8

from flask import Flask, request

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET", "POST"])
def adder_page():
    errors = ""
    if request.method == "POST":
        d = None
        e = None
        f = None
        g = None
        b = None
        h = None
        i = None
        c = None
        j = None
        a = None
        try:
            d = int(request.form["d"])
        except:
            errors += "<p>{!r} no es un número válido.</p>\n".format(request.form["d"])
        try:
            e = int(request.form["e"])
        except:
            errors += "<p>{!r} no es un número válido.</p>\n".format(request.form["e"])
        try:
            f = str(request.form["f"])
        except:
            errors += "<p>{!r} is not a valid string input.</p>\n".format(request.form["f"])
        try:
            g = str(request.form["g"])
        except:
            errors += "<p>{!r} is not a valid string input.</p>\n".format(request.form["g"])
        try:
            b = str(request.form["b"])
        except:
            errors += "<p>{!r} is not a valid string input.</p>\n".format(request.form["b"])
        try:
            h = str(request.form["h"])
        except:
            errors += "<p>{!r} is not a valid string input.</p>\n".format(request.form["h"])
        try:
            i = int(request.form["i"])
        except:
            errors += "<p>{!r} no es un número válido.</p>\n".format(request.form["i"])
        try:
            c = int(request.form["c"])
        except:
            errors += "<p>{!r} no es un número válido.</p>\n".format(request.form["c"])
        try:
            j = str(request.form["j"])
        except:
            errors += "<p>{!r} is not a valid string input.</p>\n".format(request.form["j"])
        try:
            a = str(request.form["a"])
        except:
            errors += "<p>{!r} is not a valid string input.</p>\n".format(request.form["a"])
        if d is not None and e is not None and f is not None and g is not None and b is not None and h is not None and i is not None and c is not None and j is not None and a is not None:
            total = 170
            if f == "Familia directa": 
                total = (260 + (250 * d) + (130 * e))
            elif f == "Familia no directa":
                total = (210 + (200 * d) + (110 * e))
            elif f == "Amistad muy cercana":
                total = (260 + (230 * d) + (115 * e))
            elif f == "Amistad":
                total = (162 + (150 * d) + (100 * e))
            elif f == "Se casa el/la hij@ de un/a amig@":
                total = (180 + (180 * d) + (115 * e))   
            if g == "Boda entera":
                total += 0
            elif g == "Solo a la ceremonia inicial":
                total = total - 80 - (80 * d) - (100 * e)
            elif g == "Solo a la fiesta posterior":
                total = total - 80 - (80 * d) - (100 * e)

            #tipo de ceremonia
            if b == "Religiosa":
                total *= 1.07
            elif b == "Civil":
                total += 0
            elif b == "Otra":
                total += 0

            #alojamiento?
            if h == "Sí":
                total = total + 90 + (90 * d) + (60 * e)
            elif h == "No":
                total += 0

            #gasto en desplazamiento y alojamiento
            total = total - (0.11 * i)

            #despedida soltero
            total = total - (0.12 * c)

            #situacion financiera
            if j == "Buena":
                total *= 1.10
            elif j == "Media":
                total *= 1
            elif j == "Mala":
                total *= 0.75

            #comunidad autonoma
            if a == "País Vasco":
                total *= 1.19
            elif a == "La Rioja":
                total *= 1.17
            elif a == "Aragón":
                total *= 1.15
            elif a == "Asturias":
                total *= 1.13
            elif a == "Cantabria":
                total *= 1.1
            elif a == "Navarra":
                total *= 1.08
            elif a == "Melilla":
                total *= 1.06
            elif a == "Madrid":
                total *= 1.04
            elif a == "Castilla y León":
                total *= 1.01
            elif a == "Galicia":
                total *= 0.99
            elif a == "Comunidad Valenciana":
                total *= 0.97
            elif a == "Castilla La Mancha":
                total *= 0.95
            elif a == "Cataluña":
                total *= 0.92
            elif a == "Ceuta":
                total *= 0.9
            elif a == "Andalucía":
                total *= 0.89
            elif a == "Islas Baleares":
                total *= 0.88
            elif a == "Extremadura":
                total *= 0.87
            elif a == "Canarias":
                total *= 0.84
            elif a == "Murcia":
                total *= 0.79

            if total < 125:
                total = 125




            result = int(total)
            return '''
                <!DOCTYPE html>
                <html>
                    <head>
                        <title>Calculadora del regalo de boda</title>
                    </head>
                    <body style="background-color: white; background-image: url('https://i.ibb.co/bBbhv58/euro4.jpg'); background-repeat: no-repeat; background-position: center; background-size: cover; background-attachment: fixed;">
                        <p style="text-align: center;">&nbsp;</p>
                        <p style="text-align: center;">&nbsp;</p>
                        <p style="text-align: center;">&nbsp;</p>
                        <p style="text-align: center;">&nbsp;</p>
                        <p style="text-align: center; font-family: Helvetica; font-size: 2em;">En total deberías regalar a la pareja</p>
                        <p style="text-align: center; font-family: Helvetica; font-size:5em; font-weight: bold;">€{result}</p>
                        <p style="text-align: center;">&nbsp;</p>
                        <p style="text-align: center; font-family: Helvetica; font-size: 1.75em;"><a href="/">Calcular otra vez</a>
                        <p style="text-align: center;">&nbsp;</p>
                        <p style="text-align: center; font-family: Helvetica; font-size: 1.5em;">===============================================================</p>
                        <p style="text-align: center;">&nbsp;</p>
                        <p style="text-align: center;">&nbsp;</p>
                        <p style="text-align: center;">&nbsp;</p>
                        <p style="text-align: center;">&nbsp;</p>
                        <p style="text-align: center;">&nbsp;</p>
                        <p style="text-align: center;">&nbsp;</p>
                        <p style="text-align: center; font-family: Helvetica; font-size: 2em;">En total deberías regalar a la pareja</p>
                        <p style="text-align: center; font-family: Helvetica; font-size:5em; font-weight: bold;">€{result}</p>
                        <p style="text-align: center;">&nbsp;</p>
                        <p style="text-align: center; font-family: Helvetica; font-size: 1.75em;"><a href="/">Calcular otra vez</a>

                    </body>
                <p style="text-align: center;">&nbsp;</p>
                <p style="text-align: center;">&nbsp;</p>
                <p style="text-align: center;">&nbsp;</p>
                <p style="text-align: center;">&nbsp;</p>


                </html>
            '''.format(result=result)
    return '''
        <!DOCTYPE html>
        <html lang="es">
            <head>
                <meta charset="utf-8">
                <title>Calculadora del regalo de boda</title>
                <meta name="robots" content="index,follow">
                <meta name="description" content="Calcula cuánto dinero hay que regalar a los novios por su boda. Utiliza esta calculadora para averiguarlo y haz el regalo que toca.">

                <!-- Global site tag (gtag.js) - Google Analytics -->
                <script async src="https://www.googletagmanager.com/gtag/js?id=INSERT YOUR GOOGLE ANALYTICS ID"></script>
                <script>
                  window.dataLayer = window.dataLayer || [];
                  function gtag(){{dataLayer.push(arguments);}}
                  gtag('js', new Date());

                  gtag('config', 'INSERT YOUR GOOGLE ANALYTICS ID');
                </script>

            </head>
            <body style="background-color: white; background-image: url('https://i.ibb.co/bBbhv58/euro4.jpg'); background-repeat: no-repeat; background-position: center center; background-size: cover; background-attachment: fixed;">

                {errors}
                <p style="text-align: center;">&nbsp;</p>
                <p style="text-align: center;">&nbsp;</p>
                <h1 style="text-align: center; font-family: Arial; font-size: 2.5em;"><strong><u>Calculadora del regalo de boda</u></strong></h1>
                <h2 style="text-align: center; font-family: Helvetica; font-size: 1.5em;">Lo típico. Te han invitado a una boda y no sabes cuánto dinero regalar a los novios.</h2>
                <h2 style="text-align: center; font-family: Helvetica; font-size: 1.5em;">Utiliza esta calculadora para averiguarlo y evita un disgusto con tu regalo de boda ;) </h2>


                <form method="post" action="." style="margin-left:20%; margin-right:20%; width:60%;">
                    <p style="text-align: center;">&nbsp;</p>
                    <p style="text-align: center; font-family: Helvetica; font-size: 1.5em;">Además de ti, ¿con cuántos acompañantes adultos asistirás a la boda? <label for="d"></label></p>
                    <p style="text-align: center; font-size: 1.5em;"><select name="d" id="d" style= "height: 40px; font-size: 1em;">
                      <option value="0">Voy solo/a</option>
                      <option value="1">1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="4">4</option>
                      <option value="5">5</option>
                      <option value="6">6</option>
                      <option value="7">7</option>
                      <option value="8">8</option>
                      <option value="9">9</option>
                      <option value="10">10</option>
                    </select></p>

                    <p style="text-align: center; font-family: Helvetica; font-size: 1.5em;">¿Con cuántos acompañantes menores asistirás a la boda? <label for="e"></label></p>
                    <p style="text-align: center; font-size: 1.5em;"><select name="e" id="e" style= "height: 40px; font-size: 1em;">
                      <option value="0">Voy sin menores</option>
                      <option value="1">1</option>
                      <option value="2">2</option>
                      <option value="3">3</option>
                      <option value="4">4</option>
                      <option value="5">5</option>
                      <option value="6">6</option>
                      <option value="7">7</option>
                      <option value="8">8</option>
                      <option value="9">9</option>
                      <option value="10">10</option>
                    </select></p>

                    <p style="text-align: center; font-family: Helvetica; font-size: 1.5em;">¿Qué relación tienes con quien se casa? <label for="f"></label></p>
                    <p style="text-align: center; font-size: 1.5em;"><select name="f" id="f" style= "height: 40px; font-size: 1em;">
                      <option value="Familia directa">Familia cercana</option>
                      <option value="Familia no directa">Familia lejana</option>
                      <option value="Amistad muy cercana">Amistad muy cercana</option>
                      <option value="Amistad">Amistad</option>
                      <option value="Se casa el/la hij@ de un/a amig@">Se casa el/la hij@ de un/a amig@</option>
                      <option value="Amistad">Otra</option>
                    </select></p>

                    <p style="text-align: center; font-family: Helvetica; font-size: 1.5em;">¿A qué parte de la boda asistirás? <label for="g"></label></p>
                    <p style="text-align: center; font-size: 1.5em;"><select name="g" id="g" style= "height: 40px; font-size: 1em;">
                      <option value="Boda entera">Boda entera</option>
                      <option value="Solo a la ceremonia inicial">Solo a la ceremonia inicial</option>
                      <option value="Solo a la fiesta posterior">Solo a la fiesta posterior</option>
                    </select></p>

                    <p style="text-align: center; font-family: Helvetica; font-size: 1.5em;">¿Qué tipo de ceremonia es? <label for="b"></label></p>

                    <p style="text-align: center; font-size: 1.5em;"><select name="b" id="b" style= "height: 40px; font-size: 1em;">
                      <option value="Religiosa">Religiosa</option>
                      <option value="Civil">Civil</option>
                      <option value="Otra">Otra</option>
                    </select></p>

                    <p style="text-align: center; font-family: Helvetica; font-size: 1.5em;">¿La invitación cubre alojamiento? <label for="h"></label></p>

                    <p style="text-align: center; font-size: 1.5em;"><select name="h" id="h" style= "height: 40px; font-size: 1em;">
                      <option value="No">No</option>
                      <option value="Sí">Sí</option>
                    </select></p>

                    <p style="text-align: center; font-family: Helvetica; font-size: 1.5em;">¿Cuánto dinero gastarás en desplazamiento y/o alojamiento? Pon 0 si no tendrás estos gastos.</p>
                    <p style="text-align: center; font-size: 1.5em;"><input name="i" style= "height: 40px; font-size: 1em;"/></p>

                    <p style="text-align: center; font-family: Helvetica; font-size: 1.5em;">¿Cuánto dinero gastaste en la despedida de soltero/a? Pon 0 si no hubo o no fuiste.</p>
                    <p style="text-align: center; font-size: 1.5em;"><input name="c" style= "height: 40px; font-size: 1em;"/></p>

                    <p style="text-align: center; font-family: Helvetica; font-size: 1.5em;">¿Cuál es tu situación financiera actual? <label for="j"></label></p>

                    <p style="text-align: center; font-size: 1.5em;"><select name="j" id="j" style= "height: 40px; font-size: 1em;">
                      <option value="Buena">Buena</option>
                      <option value="Media">Media</option>
                      <option value="Mala">Mala</option>
                    </select></p>

                    <p style="text-align: center; font-family: Helvetica; font-size: 1.5em;">Indica la Comunidad Autónoma donde se celebra la boda. <label for="a"></label></p>

                    <p style="text-align: center; font-size: 1.5em;"><select name="a" id="a" style= "height: 40px; font-size: 1em;">
                      <option value="Andalucía">Andalucía</option>
                      <option value="Aragón">Aragón</option>
                      <option value="Asturias">Asturias</option>
                      <option value="Canarias">Canarias</option>
                      <option value="Cantabria">Cantabria</option>
                      <option value="Castilla La Mancha">Castilla La Mancha</option>
                      <option value="Castilla y León">Castilla y León</option>
                      <option value="Cataluña">Cataluña</option>
                      <option value="Ceuta">Ceuta</option>
                      <option value="Comunidad Valenciana">Comunidad Valenciana</option>
                      <option value="Extremadura">Extremadura</option>
                      <option value="Galicia">Galicia</option>
                      <option value="Islas Baleares">Islas Baleares</option>
                      <option value="La Rioja">La Rioja</option>
                      <option value="Madrid">Madrid</option>
                      <option value="Melilla">Melilla</option>
                      <option value="Murcia">Murcia</option>
                      <option value="Navarra">Navarra</option>
                      <option value="País Vasco">País Vasco</option>
                    </select></p>

                    <p style="text-align: center;">&nbsp;</p>
                    <p style="text-align: center;"><input type="submit" style ="cursor: pointer; width: 160px; height: 50px; font-family:Helvetica; font-size: 1.5em; background-color:DodgerBlue; border-radius:20px; color:white" value="Calcular" /></p>
                    <p style="text-align: center;">&nbsp;</p>
                </form>
                <p style="text-align: center;">&nbsp;</p>
                <p style="text-align: center;">&nbsp;</p>
                <p style="text-align: center;">&nbsp;</p>
                <p style="text-align: center;">&nbsp;</p>
                <p style="text-align: center;">&nbsp;</p>
            </body>
        </html>
    '''.format(errors=errors)

