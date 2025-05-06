const form = document.getElementById("form");

form.addEventListener("submit", async function (event) {
    event.preventDefault();
    const data = {
        firstNames: form.firstNames.value,
        lastNames: form.lastNames.value,
        email: form.email.value,
        phoneNumber: form.phone.value,
        date: form.birthDate.value,
    };

    console.log("Enviando datos:", data);

    try {

        const response = await fetch("https://formulario-app.onrender.com/guardar", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data)
        });

        if (!response.ok) {
            throw new Error("Error del servidor: " + response.status);
        }

        const respuesta = await response.json();
        console.log("Respuesta del backend", respuesta);
        alert("formulario enviado correctamente");

    } catch (error) {
        console.error("Error al enviar los datos:", error);
        alert("Ocurrio un error al enviar el formulario");
    }

});