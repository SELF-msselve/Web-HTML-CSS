<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="estilos.css" rel="stylesheet"/>
</head>
<body>
    <section>
        <div class="menu-opciones">
            <p>Esta es la pagina de los pagos de los alquileres</p>
            <table>
                <tr>
                    <td>Cochera -3 12</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Cochera -3 57</td>
                    <td>Nosotros</td>
                </tr>
                <tr>
                    <td>Cochera -2 105</td>
                    <td></td>
                </tr>
                <tr>
                    <td>211 7B 271</td>
                    <td></td>
                </tr>
                <tr>
                    <td>211 8I 277</td>
                    <td></td>
                </tr>
                <tr>
                    <td>644 PBD 3</td>
                    <td></td>
                </tr>
                <tr>
                    <td>644 4C 18</td>
                    <td></td>
                </tr>
                <tr>
                    <td>644 5D 21</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Gringo</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Local</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Depto</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Esquina</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Peluqueria</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Flow</td>
                    <td>Pago dep</td>
                </tr>
                <tr>
                    <td>Rada Tilly</td>
                    <td>Pago</td>
                </tr>      
            </table>
        </div>  
    </section>
    <section>
        <br>
        <br>
        <div class="menu-opciones">
            <a href="index.html">Back</a>
        </div>
        
    </section>

    <section>
        <?php

            // Ruta

            $rutaArchivo = "pagos.csv";

            if (($archivo = fopen($rutaArchivo, "r")) ==! false) {
                echo "<table>";
                while (($datos = fgetcsv($archivo, 1000, ";")) !== false) {
                    echo "<tr>";
                    foreach ($datos as $key => $dato) {
                    echo "<td>$dato</td>";
                }
                echo "</tr>";
            }
            fclose($archivo);
            echo "</table>";
            } else {
            echo "No hay tabla";
            }

        ?>
    </section>
    
</body>
</html>