// Script Carrusel

var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("presentacion");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace("active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}

//Script formulario

function validacion(){
    var nombre = document.getElementById("nombre").value;
    var asunto = document.getElementById("asunto").value;
    var telefono = document.getElementById("telefono").value;
    var correo = document.getElementById("correo").value;
    var mensaje = document.getElementById("mensaje").value;
    var mensaje_error = document.getElementById("mensaje_error");
    var text;
    
    mensaje_error.style.padding = "10px";
    
    //Validaciones
    
    if(nombre.length < 1){
        text = "Por favor ingrese un nombre válido";
        mensaje_error.innerHTML = text;
        return false;
    }
    
    if(asunto.length < 4){
        text = "Por favor ingrese un asunto de al menos a 4 caracteres";
        mensaje_error.innerHTML = text;
        return false;
    }
    
    if(isNaN(telefono) || telefono.length != 9){
        text = "Por favor ingrese un número teléfonico válido de 9 digitos";
        mensaje_error.innerHTML = text;
        return false;
    }    
    
    if(correo.indexOf("@") == -1 || correo.length < 6){
        text = "Por favor ingrese un correo válido";
        mensaje_error.innerHTML = text;
        return false;
    }
    
    if(mensaje.length <= 30){
        text = "Por favor ingrese un mensaje de más de 30 caracteres";
        mensaje_error.innerHTML = text;
        return false;
    }
    alert("Formulario enviado exitosamente!")
    return true;
}