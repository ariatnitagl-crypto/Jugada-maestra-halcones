const API_URL = "http://127.0.0.1:8000";

async function cargarDashboard() {
    try {
        // 1. Cargar Finanzas
        const resFinanzas = await fetch(API_URL + "/finanzas/comparativa");
        const dataFinanzas = await resFinanzas.json();
        
        document.getElementById('ingreso-actual').innerText = "$" + dataFinanzas.mes_actual.toLocaleString();
        document.getElementById('comparativa-finanzas').innerText = dataFinanzas.diferencia + " vs mes anterior";

        // 2. Cargar Asistencia
        const resAsistencia = await fetch(API_URL + "/asistencia/promedio");
        const dataAsis = await resAsistencia.json();
        let htmlAsis = "";
        for (const [cat, porc] of Object.entries(dataAsis)) {
            htmlAsis += "<p>" + cat + ": <span class='text-blue-600 font-bold'>" + porc + "</span></p>";
        }
        document.getElementById('asistencia-lista').innerHTML = htmlAsis;

        // 3. Cargar Tabla de Pagos
        const resPagos = await fetch(API_URL + "/pagos/estado");
        const dataPagos = await resPagos.json();
        let htmlPagos = "";
        
        dataPagos.forEach(p => {
            const colorEstado = p.estado === 'Pagado' ? 'bg-green-100 text-green-700' : 'bg-red-100 text-red-700';
            htmlPagos += "<tr class='border-b'>";
            htmlPagos += "<td class='p-4'>" + p.nombre + "</td>";
            htmlPagos += "<td class='p-4 text-gray-500'>" + p.categoria + "</td>";
            htmlPagos += "<td class='p-4'><span class='px-3 py-1 rounded-full text-xs font-bold " + colorEstado + "'>" + p.estado + "</span></td>";
            htmlPagos += "</tr>";
        });
        
        document.getElementById('tabla-pagos').innerHTML = htmlPagos;

    } catch (error) {
        console.error("Error cargando datos:", error);
        alert("No se pudo conectar con el servidor. Revisa que el backend esté encendido.");
    }
}

// Ejecutar la función
cargarDashboard();
