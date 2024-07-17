function validar() {
    var retorno_email = validar_correo();
    var retorno_fono = validar_fono();
    var retorno_informacion = validar_informacion();

    return retorno_email && retorno_fono && retorno_informacion;
}



function validar_correo() {
    var input_email = document.getElementById("input-email");
    var div_error_email = document.getElementById("emailError");
    var correo = input_email.value.trim();
    var pos_arroba = correo.indexOf("@");
    var pos_punto = correo.lastIndexOf(".");
    var arr_correo = correo.split(".");
    var extension = arr_correo[arr_correo.length - 1];

    if (pos_arroba > 0 && pos_punto > pos_arroba && (extension.length > 1 && extension.length <= 3)) {
        div_error_email.innerHTML = "";
        return true;
    } else {
        div_error_email.innerHTML = "El correo electrónico no tiene el formato correcto";
        div_error_email.className = "text-danger small mt-1";
        return false;
    }
}


function validar_fono() {
    var input_fono = document.getElementById("input-fono");
    var div_error_fono = document.getElementById("phoneError");
    var fono = input_fono.value;
    var phonePattern = /^\+?[0-9\s-]{7,15}$/;

    if (phonePattern.test(fono)) {
        div_error_fono.innerHTML = "";
        return true;
    } else {
        div_error_fono.innerHTML = "El número de teléfono no tiene el formato correcto";
        div_error_fono.className = "text-danger small mt-1";
        return false;
    }
}

function validar_informacion() {
    var div_info = document.getElementById("informacionAdicional");
    var div_error_info = document.getElementById("infoError");
    var informacion = div_info.innerText.trim();

    if (informacion.length > 500) {
        div_error_info.innerHTML = "La información adicional no debe exceder los 500 caracteres";
        div_error_info.className = "text-danger small mt-1";
        return false;
    } else {
        div_error_info.innerHTML = "";
        return true;
    }
}

function eliminarProducto(id) {
    if (confirm("¿Estás seguro de eliminar este producto?")) {
        location.href = "/eliminar_producto/" + id + "/";
    }
}