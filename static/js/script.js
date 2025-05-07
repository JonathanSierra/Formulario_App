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
        }else{
            document.getElementById("emergentWrapper").classList.add("show");
            document.body.style.overflow = "hidden";
        }

        const aceptar = document.getElementById("btnAccept").addEventListener("click", () => {
            document.getElementById("emergentWrapper").classList.remove("show");
            document.body.style.overflow = "visible";

            document.getElementById("txtFirstNames").value = ""
            document.getElementById("txtLastNames").value = ""
            document.getElementById("txtEmail").value = ""
            document.getElementById("txtPhoneNumber").value = ""
            document.getElementById("txtBirthDate").value = ""
        })

        const respuesta = await response.json();
        console.log("Respuesta del backend", respuesta);

    } catch (error) {
        console.error("Error al enviar los datos:", error);
        alert("Ocurrio un error al enviar el formulario");
    }

});

document.getElementById("txtPhoneNumber").addEventListener("input", function(e) {
    this.value = this.value.replace(/[^0-9]/g, '');
});

document.addEventListener("DOMContentLoaded", function(){
    flatpickr("#txtBirthDate", {
        dateFormat: "d-m-Y",
        locale: "es",
        allowInput: true,
        disableMobile: true
    });
});
