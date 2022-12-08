var button = document.querySelector("#btn-slog");

function foo(event)
{
    element = event.target;

    if ( element.classList.contains('btn-primary') )
    {
        var new_class = 'btn-danger';
        var old_class = 'btn-info';
    }
    else {
        var new_class = 'btn-info';
        var old_class = 'btn-danger';
    }

    element.classList.remove(old_class);
    element.classList.add(new_class);
}

button.addEventListener('click', foo, false);