// Conseguir modal
var modal = document.getElementById('mModal');

// Conseguir imagen y caption del modal
var modalImg = document.getElementById("img-modal");
var captionText = document.getElementById("caption-modal");

// Mostrar el modal
function displayModal(ctx){
    modal.style.display = "block";
    modalImg.src = ctx.src; //conseguir 'src' de la imagen
    captionText.innerHTML = "<h3>"+ctx.alt+"</h3>";   //conseguir texto del elemento 'alt'
    document.body.style.overflow = 'hidden';//evitar mostrar dos scrolls
}
// Conseguir elemento <span> para cerrar el modal
var span = document.getElementsByClassName("close-modal")[0];
span.onclick = function() {
    modal.style.display = "none";
    document.body.style.overflow = '';
}