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
