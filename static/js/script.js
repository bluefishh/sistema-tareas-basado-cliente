// Seleccionar todos los botones de edición
const btnEditar = document.querySelectorAll('.btn-editar');
// Seleccionar todos los botones de cancelación de edición
const btnCancelarEdicion = document.querySelectorAll('.btn-cancelar-edicion'); 

// Iterar sobre los botones y añadir un evento de clic a cada uno
btnEditar.forEach(function(button, index) {
    button.addEventListener('click', function(e) {
        e.preventDefault(); // Evitar el comportamiento por defecto del enlace

        // Se traen los elementos que contienen el texto y los botones, también el formulario de actualización
        const textTarea = document.querySelectorAll('.text-tarea')[index];
        const btnsTarea = document.querySelectorAll('.btns-tarea')[index];
        const formActualizar = document.querySelectorAll('.form-actualizar-tarea')[index];
        const textArea = formActualizar.querySelector('textarea');

        textArea.value = textTarea.textContent.trim();
        
        // Ocultar el texto y los botones, mostrar el formulario
        textTarea.classList.add('d-none');
        btnsTarea.classList.add('d-none');
        formActualizar.classList.remove('d-none');
    });
});

// Iterar sobre los botones y añadir un evento de clic a cada uno
btnCancelarEdicion.forEach(function(button, index) {
    button.addEventListener('click', function(e) {
        e.preventDefault(); // Evitar el comportamiento por defecto del enlace

        // Se traen los elementos que contienen el texto y los botones, también el formulario de actualización
        const textTarea = document.querySelectorAll('.text-tarea')[index];
        const btnsTarea = document.querySelectorAll('.btns-tarea')[index];
        const formActualizar = document.querySelectorAll('.form-actualizar-tarea')[index];
        
        // Mostrar el texto y los botones, ocultar el formulario de actualización
        textTarea.classList.remove('d-none');
        btnsTarea.classList.remove('d-none');
        formActualizar.classList.add('d-none');
    });
});